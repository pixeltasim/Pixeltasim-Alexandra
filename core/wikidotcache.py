from time import sleep
import thread
import datetime
from whiffle import wikidotapi
import pickle

def cache_refresh(): #calls itself automatically once called for the first time
	api = wikidotapi.connection()

	#file reading
	localauthorlist = {}
	localtitlelist = {}
	localtaglist = {}
	localratinglist = {}
	scpcache = {}
	api.Site = "scp-wiki"
	pages = api.refresh_pages()
	__builtin__.scppages = api.refresh_pages()
	try:
		with open("cache.cache","rb") as f:
			scpcache = pickle.load(f)
	except EOFError:
		pass
	if len(scpcache) != 0:
		print "Reading cache"
		__builtin__.scppagecache = scpcache
		for page in pages:
			for item in scpcache:
				try:
					localauthorlist[page] = item[page]["created_by"]
					localtitlelist[page] = item[page]["title"]
					localtaglist[page] = item[page]["tags"]
					localratinglist[page] = item[page]["rating"]
				except KeyError:
				 pass
	__builtin__.authorlist = localauthorlist
	__builtin__.titlelist = localtitlelist
	__builtin__.taglist = localtaglist
	__builtin__.ratinglist = localratinglist

	#WL
	__builtin__.callsmade = 0
	api.Site = "wanderers-library"
	__builtin__.wlpages = api.refresh_pages()
	pages = api.refresh_pages()
	__builtin__.totalpagescurcache = len(pages)
	print "Refreshing WL cache"
	newpagecache = [] #the newpagecache is so that while it is updating you can still use the old one
	for page in pages:
		newpagecache.append(api.server.pages.get_meta({"site": api.Site, "pages": [page]}))
		time.sleep(0.4) #this keeps the api calls within an acceptable threshold
		__builtin__.callsmade+=1
	print "Cache refreshed!"
	__builtin__.pagecache= newpagecache #__builtin__ means that pagecache is global and can be used by plugins
	ts = time.time()
	__builtin__.lastcacherefresh = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

	#SCP
	#SCP
	__builtin__.callsmade = 0
	api.Site = "scp-wiki"
	pages = api.refresh_pages()
	__builtin__.totalpagescurcache = len(pages)
	print "Refreshing SCP cache"
	__builtin__.totalpagescurcache = len(pages)
	newpagecache = [] #the newpagecache is so that while it is updating you can still use the old one
	localauthorlist = {}
	localtitlelist = {}
	localtaglist = {}
	localratinglist = {}
	for page in pages:
		x = api.server.pages.get_meta({"site": api.Site, "pages": [page]})
		cache = {}
		cache[page] = x[page]
		localauthorlist[page] = cache[page]["created_by"]
		localtitlelist[page] = cache[page]["title"]
		localtaglist[page] = cache[page]["tags"]
		localratinglist[page] = cache[page]["rating"]
		newpagecache.append(x)
		time.sleep(0.3) #this keeps the api calls within an acceptable threshold
		__builtin__.callsmade +=1 
	__builtin__.authorlist = localauthorlist
	__builtin__.titlelist = localtitlelist
	__builtin__.taglist = localtaglist
	__builtin__.ratinglist = localratinglist
	print "Cache refreshed!"
	__builtin__.scppagecache= newpagecache #__builtin__ means that pagecache is global and can be used by plugins

	with open("cache.cache","wb") as f:
		pickle.dump(newpagecache,f)

	#end	
	ts = time.time()
	lastcacherefresh = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	time.sleep(3600) #one hour 
	cache_refresh() #calls itself again
	
	
def ban_refresh():
	#check bans
	unbanlist = []
	try:
		with open("bans.bans","r+b") as f:
			data = f.readlines()
			val = 0
			for line in data:
				parts = line.split()
				host = parts[0]
				m1time = parts[1]
				m2time = parts[2]
				m3time = m1time+' '+m2time
				mtime = datetime.datetime.strptime(m3time,"%Y-%m-%d %H:%M:%S.%f")
				if (datetime.datetime.now()-mtime)>datetime.timedelta(minutes=1): 
					#unbanlist.append(host)
					data.pop(val)
					#f.writelines(data)
				val +=1
	except EOFError:
		pass
	__builtin__.realunban = unbanlist
	api = wikidotapi.connection() #creates API connection
	#ban update 
	localbandict={}
	try:
		with open("ban.cache","rb") as f:
			localbanddict = pickle.load(f)
	except EOFError:
		pass
	__builtin__.bandict = localbandict
	localbandict = {}
	api.Site = "05command"
	pages = api.refresh_pages() #refresh page list provided by the API, is only a list of strings
	source = api.server.pages.get_one({"site":api.Site,"page":"alexandra-s-ban-page"})
	content = source["content"]
	fs = content.split("-----")
	banlist = fs[1]
	invbans = banlist.split("\n")
	for ban in invbans:
		parts = ban.split("||")
		val = 0
		banlist = []
		nick = ""
		for part in parts:
			val+=1
			if val ==2:
				#nicks
				nick = part
				banlist.append(part)
			if val ==3:
				#IPs
				banlist.append(part)
			if val ==4:
				#status
				if nick != "Nick":
					if part != "Perma":
						mtime = datetime.datetime.strptime(part,"%m/%d/%Y")
						if datetime.datetime.today() >= mtime:
							print datetime.datetime.today()
							print mtime
							banlist.append("Unbanned")
						else:
							banlist.append(part)
					else:
						banlist.append(part)
			if val ==5:
				#reason
				banlist.append(part)
				
		if nick != "Nick":
			localbandict[nick] = banlist
	print localbandict
	__builtin__.bandict = localbandict
	print "Ban update complete."
	
	with open("ban.cache","wb") as f:
		pickle.dump(localbandict,f)
	ts = time.time()
	__builtin__.lastbanrefresh = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	time.sleep(900) #15 minutes
	ban_refresh() #calls itself again

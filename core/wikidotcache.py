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
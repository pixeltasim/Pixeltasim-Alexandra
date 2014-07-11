from whiffle import wikidotapi
from util import hook
import re
import time,threading
import datetime
import __builtin__
@hook.command
def test(inp,input = None,chan =None,nick = None   ):
	#check bans
	try:
		with open("bans.bans","r+b") as f:
			data = f.readlines()
			val = 0
			for line in data:
				parts = line.split()
				host = parts[0]
				mtime = parts[1]
				if (datetime.datetime.now()-mtime)>datetime.timedelta(minutes=1): 
					data.pop(val)
					baninput.unban(host)
					print "Unbanning "+host 
				val +=1
	except EOFError:
		pass
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
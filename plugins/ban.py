from whiffle import wikidotapi
from util import hook
import re
import time,threading
import random 
import __builtin__
import datetime 

@hook.command
def updatebans(inp, conn= None,chan = None):
	if chan == "#site67":
		try:
			__builtin__.alertops = 0
			api = wikidotapi.connection()
			#overwrite update
			localbancache = {}
			__builtin__.bancache = {}
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
				_list = []
				nick = ""
				author = ""
				for part in parts:
					val+=1
					if val ==2:
						#Nick
						nick = part 
						_list.append(nick)
					if val ==3:
						#IP
						_list.append(part)
					if val ==4:
						#unban date
						if part != "Ban Status":
							if part != "Perma":
								date = datetime.datetime.strptime(part,"%m/%d/%Y")
								today =datetime.datetime.today()
								if date.date() <= today.date():
									part = "Unbanned"
								_list.append(part)
							else:
								_list.append(part)
					if val ==5:
						#Reason
						_list.append(part)
				if nick != "Nick(s)":
					localbancache[nick] = _list
			__builtin__.bancache = localbancache
			print "Ban update complete."
			__builtin__.hugs = 0
			ts = time.time()
			__builtin__.lastbanrefresh = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
			conn.msg(chan, "Ban List Updated")
		except Exception as e:
			conn.msg(chan, "Ban List Update Failed, please check ban list for errors. Error is: "+e.message)

@hook.event("*")
def banevent(func,nick = None, host = None, user = None, conn = None,chan = None ):
	if chan!="#site17":
		for bans in bancache:
			ban = bancache[bans]
			banz = 0
			val = 0
			nicks = []
			ips = []
			reason = ""
			for part in ban:
				val+=1
				if val == 1:
					nicks = part.split()
					for mnick in nicks:
						if "-generic" in mnick.lower():
							pass
						else:
							if mnick.lower() == nick.lower():
								banz = 1
				if val == 2:
					ips = part.split()
					hostmask = user+"@"+host
					for ip in ips:
						if hostmask.lower() == ip.lower() or host.lower() == ip.lower() or "@"+host.lower()==ip.lower():
							banz =1 
				if val == 3:
					if part == "Unbanned":
						banz = 0
				if val == 4:
					reason = part
			if banz ==1:
				message = "Your nick/ip matches one in Alexandra's Database, Reason for ban: "+reason+". If you wish to appeal please join channel #site17 "
				conn.cmd('KICK', [chan, nick,message ])
				conn.cmd('MODE', [chan, '+b', user+"@"+host])
				if "-generic" in nicks[0].lower():
					conn.msg(chan,"OP Alert: Autokicking "+nick+". They are "+nicks[0].lower().replace("-generic",""))
				else:
					conn.msg(chan, "OP Alert: Autokicking "+nick+". They are "+nicks[0])
				time.sleep(900)
				conn.cmd('MODE', [chan, '-b', user+"@"+host])
@hook.event("JOIN")
def joinevent(func,nick = None, conn = None,chan = None,user = None,host = None ):
	banned_words = ["bitch","fuck","asshole","penis","vagina","nigger","retard","faggot","chink","shit","hitler","douche"]
	for word in banned_words:
		if word in nick.lower():
			conn.cmd('KICK', [chan, nick, "Your nick contains inappropriate language, please use '/nick newnick' to change your name to something more appropriate. You may rejoin with a different nick after 10 seconds."])
			conn.cmd('MODE', [chan, '+b', user+"@"+host])
			conn.cmd('MODE', [chan, '+b', nick])
			if chan == "site19":
				conn.msg(chan, "OP Alert: Autokicking "+nick)
			else:
				conn.msg("#site67", "OP Alert: "+nick+" has joined "+chan)
			time.sleep(10)
			conn.cmd('MODE', [chan, '-b', user+"@"+host])
			time.sleep(890)
			conn.cmd('MODE', [chan, '-b', nick])
		
	
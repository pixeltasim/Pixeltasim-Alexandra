from whiffle import wikidotapi
from util import hook
import re
import time,threading
	
@hook.command
def unused(inp):
	api = wikidotapi.connection() 
	api.Site = "scp-wiki"
	pages = api.refresh_pages()
	scps = []
	for page in pages:
		try:
			if "scp" in taglist[page]:
				val = page 
				scps.append(val)
		except (KeyError,IndexError):
			pass
	for i in range(001,2999):
		x = str(i)
		if i<100:
			x="0"+str(i)
		if i<10:
			x="00"+str(i)
		if x in val:
			continue
		else:
			if api.page_exists("scp-"+x):
				continue 
			else:
				return "The first unused page found is SCP-"+x+" - http://www.scp-wiki.net/scp-"+x

@hook.regex("scp-")
def scpregex(match):
	if ' ' not in match.string:
		if match.string.lower().startswith("scp-") or match.string.lower().startswith("!scp-"):
			api = wikidotapi.connection() 
			api.Site = "scp-wiki"
			pages = api.refresh_pages() 
			page = re.sub("[!]",'',match.string.lower())
			if api.page_exists(page): 
				if "scp" in taglist[page]: 
					rating = ratinglist[page]
					if rating < 0:
						ratesign = "-"
					if rating >= 0:
						ratesign = "+" #adds + or minus sign in front of rating
					ratestring = "Rating:"+ratesign+str(rating)+"" 
					author = authorlist[page]
					if author == "":
						author = "unknown"
					authorstring = "Written by "+author
					if ":rewrite:" in author:
						bothauths = authorlist[page].split(":rewrite:")
						orgauth = bothauths[0]
						newauth = bothauths[1]
						authorstring = "Originally written by "+orgauth +", rewritten by "+newauth
						if ":override:" in newauth:
							author = newauth[10:]
							authorstring = "Written by "+ author
					title = titlelist[page]
					sepstring = ", "
					link = "http://scp-wiki.net/"+page.lower() 
					return ""+title+" ("+ratestring+sepstring+authorstring+") - "+link 
				else:
					return "Page exists but is either untagged or not an scp." 
			return "Page does not exist, but you can create it here: " + "http://scp-wiki.net/"+page
		
@hook.command
def untagged(inp):
	api = wikidotapi.connection() 
	api.Site = "scp-wiki"
	pages = api.refresh_pages() 
	final = "The following pages are untagged: "
	first = 1
	for page in pages:
		try:
			if taglist[page] == "":
				first =0
				final += titlelist[page] +"."
		except KeyError:
			pass 
	if first == 1:
		final = "No untagged pages found!"
	return final
	
@hook.regex("http://www.scp-wiki.net/")
def linkregex(inp):
	api = wikidotapi.connection() 
	api.Site = "scp-wiki"
	pages = api.refresh_pages() 
	substrings = inp.string.split()
	for ss in substrings:
		if "http://www.scp-wiki.net/"in ss :
			page = ss[24:]
			if page.startswith("com/"):
				page = ss[29:]
			if api.page_exists(page): 
				rating = ratinglist[page]
				if rating < 0:
					ratesign = "-"
				if rating >= 0:
					ratesign = "+" 
				ratestring = "Rating:"+ratesign+str(rating)+"" 
				author = authorlist[page]
				authorstring = "Written by "+author
				if ":rewrite:" in author:
						bothauths = authorlist[page].split(":rewrite:")
						orgauth = bothauths[0]
						newauth = bothauths[1]
						authorstring = "Originally written by "+orgauth +", rewritten by "+newauth
						if ":override:" in newauth:
							author = newauth[10:]
							authorstring = "Written by "+ author
				if author == "":
					author = "unknown"
				title = titlelist[page]
				sepstring = ", "
				return ""+title+" ("+ratestring+sepstring+authorstring+") - http://scp-wiki.net/"+page.lower() #returns the string, nonick:: means that the caller's nick isn't prefixed
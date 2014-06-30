from whiffle import wikidotapi
from util import hook
import re
import time,threading

@hook.command
def scp(inp): #this is for WL use, easily adaptable to SCP
	".scp <Article #> -- Will return exact match of 'SCP-Article#'"
	api = wikidotapi.connection() #creates API connection
	api.Site = "scp-wiki"
	pages = api.refresh_pages() #refresh page list provided by the API, is only a list of strings
	line = re.sub("[ ,']",'-',inp) #removes spaces and apostrophes and replaces them with dashes, per wikidot's standards
	page = "scp-"+inp.lower()
	if api.page_exists(page): #only api call in .tale, verification of page existence
		if "scp" in api.get_page_item(page,"tags"): #check for tag
			rating = api.get_page_item(page,"rating")
			if rating < 0:
				ratesign = "-"
			if rating >= 0:
				ratesign = "+" #adds + or minus sign in front of rating
			ratestring = "Rating:"+ratesign+str(rating)+"" 
			author = api.get_page_item(page,"created_by")
			authorstring = "Written by "+author
			title = api.get_page_item(page,"title")
			sepstring = ", "
			return ""+title+" ("+ratestring+sepstring+authorstring+") - http://scp-wiki.net/"+page.lower() #returns the string, nonick:: means that the caller's nick isn't prefixed
		else:
			return "Page exists but is either untagged or not an scp." 
	return "Page does not exist, but you can create it here: " + "http://scp-wiki.net/"+page
	
@hook.command
def unused(inp):
	api = wikidotapi.connection() #creates API connection
	api.Site = "scp-wiki"
	pages = api.refresh_pages() #refresh page list provided by the API, is only a list of strings
	scps = []
	for page in pages:
		try:
			if "scp" in taglist[page]:
				val = page[3]+page[4]+page[5]+page[6]
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

@hook.regex("SCP-")
def scpregex(match):
	if ' ' not in match.string:
		if match.string.startswith("SCP-") or match.string.startswith("!SCP-"):
			api = wikidotapi.connection() #creates API connection
			api.Site = "scp-wiki"
			pages = api.refresh_pages() #refresh page list provided by the API, is only a list of strings
			page = re.sub("[ ,']",'-',match.string.lower())
			if api.page_exists(page): #only api call in .tale, verification of page existence
				if "scp" in api.get_page_item(page,"tags"): #check for tag
					rating = api.get_page_item(page,"rating")
					if rating < 0:
						ratesign = "-"
					if rating >= 0:
						ratesign = "+" #adds + or minus sign in front of rating
					ratestring = "Rating:"+ratesign+str(rating)+"" 
					author = api.get_page_item(page,"created_by")
					if author == None:
						author = "unknown"
					authorstring = "Written by "+author
					title = api.get_page_item(page,"title")
					sepstring = ", "
					return ""+title+" ("+ratestring+sepstring+authorstring+") - http://scp-wiki.net/"+page.lower() #returns the string, nonick:: means that the caller's nick isn't prefixed
				else:
					return "Page exists but is either untagged or not an scp." 
			return "Page does not exist, but you can create it here: " + "http://scp-wiki.net/"+page
		
@hook.regex("scp-")
def scpregexlowercase(match):
	if ' ' not in match.string:
		if match.string.startswith("scp-") or match.string.startswith("!scp-"):
			api = wikidotapi.connection() #creates API connection
			api.Site = "scp-wiki"
			pages = api.refresh_pages() #refresh page list provided by the API, is only a list of strings
			page = re.sub("[!]",'',match.string.lower())
			if api.page_exists(page): #only api call in .tale, verification of page existence
				if "scp" in api.get_page_item(page,"tags"): #check for tag
					rating = api.get_page_item(page,"rating")
					if rating < 0:
						ratesign = "-"
					if rating >= 0:
						ratesign = "+" #adds + or minus sign in front of rating
					ratestring = "Rating:"+ratesign+str(rating)+"" 
					author = api.get_page_item(page,"created_by")
					if author == None:
						author = "unknown"
					authorstring = "Written by "+author
					title = api.get_page_item(page,"title")
					sepstring = ", "
					return ""+title+" ("+ratestring+sepstring+authorstring+") - http://scp-wiki.net/"+page.lower() #returns the string, nonick:: means that the caller's nick isn't prefixed
				else:
					return "Page exists but is either untagged or not an scp." 
			return "Page does not exist, but you can create it here: " + "http://scp-wiki.net/"+page

@hook.command
def untagged(inp):
	api = wikidotapi.connection() #creates API connection
	api.Site = "scp-wiki"
	pages = api.refresh_pages() #refresh page list provided by the API, is only a list of strings
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
	api = wikidotapi.connection() #creates API connection
	api.Site = "scp-wiki"
	pages = api.refresh_pages() #refresh page list provided by the API, is only a list of strings
	substrings = inp.string.split()
	for ss in substrings:
		if "http://www.scp-wiki.net/" in ss:
			page = ss[24:]
			if api.page_exists(page): #only api call in .tale, verification of page existence
				rating = api.get_page_item(page,"rating")
				if rating < 0:
					ratesign = "-"
				if rating >= 0:
					ratesign = "+" #adds + or minus sign in front of rating
				ratestring = "Rating:"+ratesign+str(rating)+"" 
				author = api.get_page_item(page,"created_by")
				authorstring = "Written by "+author
				title = api.get_page_item(page,"title")
				sepstring = ", "
				return ""+title+" ("+ratestring+sepstring+authorstring+") - http://scp-wiki.net/"+page.lower() #returns the string, nonick:: means that the caller's nick isn't prefixed
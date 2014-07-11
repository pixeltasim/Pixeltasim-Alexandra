from whiffle import wikidotapi
from util import hook
import re
import time,threading
import thread
import __builtin__

@hook.command()
def sea(inp): #this is for WL use, easily adaptable to SCP
	".sea <Article Name> -- Will return first three pages containing exact matches to Article Name, with number of other matches"
	api = wikidotapi.connection() #creates API connection
	api.Site = "scp-wiki"
	pages = api.refresh_pages() #refresh page list provided by the API, is only a list of strings
	line = re.sub("[ ,']",'-',inp) #removes spaces and apostrophes and replaces them with dashes, per wikidot's standards
	results = []
	for page in titlelist: 
		if line.lower() in page.lower(): #check for first match to input
			if api.page_exists(page.lower()): #only api call in .tale, verification of page existence
				if "tale" in api.get_page_item(page,"tags") or "scp" in api.get_page_item(page,"tags") or "essay" in api.get_page_item(page,"tags"): #check for tag
					results.append(page)
					continue 
			else:
				return "Match found but page does not exist, please consult pixeltasim for error."
		if inp.lower() in titlelist[page].lower():
			if api.page_exists(page.lower()): #only api call in .tale, verification of page existence
				if "tale" in api.get_page_item(page,"tags") or "scp" in api.get_page_item(page,"tags") or "essay" in api.get_page_item(page,"tags"): #check for tag
					results.append(page)
	if results == []:
		return "No matches found."
	final = ""
	third = 0
	for result in results:
		third+=1
		if third == 1:
			title = api.get_page_item(result,"title")
			rating = api.get_page_item(result,"rating")
			final+= ""+title+""+"(Rating:"+str(rating)+")"
		if third<=3 and third != 1:
			title = api.get_page_item(result,"title")
			rating = api.get_page_item(result,"rating")
			final+= ", "+title+""+"(Rating:"+str(rating)+")"
	if third>3:
		final += ", With " + str(third-3) + " more matches."
	if third==1:
		page = results[0]
		title = titlelist[page]
		rating = api.get_page_item(page,"rating")
		final = ""+title+""+"(Rating:"+str(rating)+") - http://www.scp-wiki.net/"+page
	__builtin__.seaiter = 1
	__builtin__.searesults = results
	return final

@hook.command("sm")
@hook.command("showmore")
def showmore(inp):
	global seaiter
	global searesults
	api = wikidotapi.connection() #creates API connection
	api.Site = "scp-wiki"
	pages = api.refresh_pages() #refresh page list provided by the API, is only a list of strings
	final = ""
	minval = seaiter*3+1
	maxval = seaiter*3+3
	__builtin__.seaiter +=1
	val= 0
	for result in searesults:
		val+=1
		if val == minval:
			title = api.get_page_item(result,"title")
			rating = api.get_page_item(result,"rating")
			final+= ""+title+""+"(Rating:"+str(rating)+")"
		if val<=maxval and val != minval and val>minval:
			title = api.get_page_item(result,"title")
			rating = api.get_page_item(result,"rating")
			final+= ", "+title+""+"(Rating:"+str(rating)+")"
	if val>maxval:
		final += ", With " + str(val-maxval) + " more matches."
	if final == "":
		return "There are no more matches to show."
	return final 
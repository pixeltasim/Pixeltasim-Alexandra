from whiffle import wikidotapi
from util import hook
import re
import time,threading

@hook.command
def test(inp):
	fstart = time.clock()
	api = wikidotapi.connection() #creates API connection
	api.Site = "scp-wiki"
	pages = api.Pages #refresh page list provided by the API, is only a list of strings
	line = re.sub("[ ,']",'-',inp) #removes spaces and apostrophes and replaces them with dashes, per wikidot's standards
	for page in pages: 
		if line.lower() in page.lower(): #check for first match to input
			if "tale" in taglist[page]: #check for tag
				rating = str(ratinglist[page])
				if rating < 0:
					ratesign = "-"
				if rating >= 0:
					ratesign = "+" #adds + or minus sign in front of rating
				ratestring = "Rating:"+ratesign+str(rating)+"" 
				ratestring = "Rating:"+ratesign+str(rating)+"" 
				author = authorlist[page]
				authorstring = "Written by "+author
				title = titlelist[page]
				sepstring = ", "
				#return ""+title+" ("+ratestring+sepstring+authorstring+") - http://scp-wiki.net/"+page.lower() #returns the string, nonick:: means that the caller's nick isn't prefixed
	fend = time.clock()
	return "First method took "+str(fend-fstart)+" seconds."
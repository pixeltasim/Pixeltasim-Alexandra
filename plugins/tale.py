from whiffle import wikidotapi
from util import hook
import re
import time,threading

@hook.command()
def tale(inp): #this is for WL use, easily adaptable to SCP
	".tale <Article Name> -- Will return first page containing exact match to Article Name"
	api = wikidotapi.connection() #creates API connection
	api.Site = "scp-wiki"
	pages = api.refresh_pages() #refresh page list provided by the API, is only a list of strings
	line = re.sub("[ ,']",'-',inp) #removes spaces and apostrophes and replaces them with dashes, per wikidot's standards
	for page in pages: 
		if line.lower() in page.lower(): #check for first match to input
			if api.page_exists(page.lower()): #only api call in .tale, verification of page existence
				if "tale" in taglist[page]: #check for tag
					rating = ratinglist[page] 
					if rating < 0:
						ratesign = "-"
					if rating >= 0:
						ratesign = "+" #adds + or minus sign in front of rating
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
					title = titlelist[page]
					sepstring = ", "
					return ""+title+" ("+ratestring+sepstring+authorstring+") - http://scp-wiki.net/"+page.lower() #returns the string, nonick:: means that the caller's nick isn't prefixed
				else:
					print page
					return "Page was found but it is either untagged or an administrative page."
			else:
				return "Match found but page does not exist, please consult pixeltasim for error."
	return "Page not found"
		
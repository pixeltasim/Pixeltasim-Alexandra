from whiffle import wikidotapi
from util import hook
import re
import time,threading

@hook.command("wl")
@hook.command("wandererslibrary")
def wandererslibrary(inp): #this is for WL use, easily adaptable to SCP
	".tale <Article Name> -- Will return first page containing exact match to Article Name"
	api = wikidotapi.connection() #creates API connection
	api.Site = "wanderers-library"
	pages = api.refresh_pages() #refresh page list provided by the API, is only a list of strings
	line = re.sub("[ ,']",'-',inp) #removes spaces and apostrophes and replaces them with dashes, per wikidot's standards
	for page in pages: 
		for item in pagecache: #iterates through ever attribute in the pagecache, similar to .author
			if line.lower() in page: #check for first match to input
				if api.page_exists(page.lower()): #only api call in .tale, verification of page existence
					try: #must do error handling as the key will be wrong for most of the items
						if "entry" in item[page]["tags"]: #check for tag
							rating = item[page]["rating"] 
							if rating < 0:
								ratesign = "-"
							if rating >= 0:
								ratesign = "+" #adds + or minus sign in front of rating
							ratestring = "Rating:"+ratesign+str(rating)+"" 
							author = item[page]["created_by"]
							authorstring = "Written by "+author
							title = item[page]["title"]
							sepstring = ", "
							return "nonick::"+title+" ("+ratestring+sepstring+authorstring+") - http://wanderers-library.wikidot.com/"+page.lower() #returns the string, nonick:: means that the caller's nick isn't prefixed
					except KeyError:
						pass 
				else:
					return "nonick::Match found but page does not exist, please consult pixeltasim for error."
	for page in pages: 
		for item in pagecache: #iterates through ever attribute in the pagecache, similar to .author
			try:
				if inp.lower() in item[page]["title"].lower(): #check for first match to input
					print item[page]["title"].lower()
					if api.page_exists(page.lower()): #only api call in .tale, verification of page existence
						#must do error handling as the key will be wrong for most of the items
							if "entry" in item[page]["tags"]: #check for tag
								rating = item[page]["rating"] 
								if rating < 0:
									ratesign = "-"
								if rating >= 0:
									ratesign = "+" #adds + or minus sign in front of rating
								ratestring = "Rating:"+ratesign+str(rating)+"" 
								author = item[page]["created_by"]
								authorstring = "Written by "+author
								title = item[page]["title"]
								sepstring = ", "
								return "nonick::"+title+" ("+ratestring+sepstring+authorstring+") - http://wanderers-library.wikidot.com/"+page.lower() #returns the string, nonick:: means that the caller's nick isn't prefixed
							else:
								return "nonick::Page was found but it is either untagged or an administrative page."
					else:
						return "nonick::Match found but page does not exist, please consult pixeltasim for error."
			except KeyError:
				pass 
	return "nonick::Page not found"
		


	
from whiffle import wikidotapi
from util import hook
import re
import time,threading

@hook.command()
def tale(inp): #this is for WL use, easily adaptable to SCP
	".tale <Article Name> -- Will return first page containing exact match to Article Name"
	line = re.sub("[ ,']",'-',inp) #removes spaces and apostrophes and replaces them with dashes, per wikidot's standards
	for page in scppages: 
		if line.lower() in page.lower(): #check for first match to input
			if "tale" in taglist[page] or "goi-format" in taglist[page]: #check for tag
				rating = ratinglist[page] 
				ratesign = ""
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
				title = titlelist[page]
				sepstring = ", "
				return ""+title+" ("+ratestring+sepstring+authorstring+") - http://scp-wiki.net/"+page.lower() 
			else:
				return "Match found but page does not exist, please consult pixeltasim for error."
		if inp.lower() in titlelist[page].lower(): #check for first match to input
			if "tale" in taglist[page] or "goi-format" in taglist[page]: #check for tag
				rating = ratinglist[page] 
				ratesign = ""
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
				title = titlelist[page]
				sepstring = ", "
				return ""+title+" ("+ratestring+sepstring+authorstring+") - http://scp-wiki.net/"+page.lower() 
			else:
				return "Match found but page does not exist, please consult pixeltasim for error."
	return "Page not found"
		
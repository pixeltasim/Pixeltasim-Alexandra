from whiffle import wikidotapi
from util import hook
import re
import time,threading

@hook.command("lc")
@hook.command("lastcreated")
def lastcreated(inp):
	api = wikidotapi.connection() #creates API connection
	api.Site = "scp-wiki"
	pages = api.Pages #refresh page list provided by the API, is only a list of strings
	final = ""
	final+=""+titlelist[pages[-1]]+"(Rating:"+str(ratinglist[pages[-1]])+") - http://www.scp-wiki.net/"+pages[-1]+" - "
	final+=""+titlelist[pages[-2]]+"(Rating:"+str(ratinglist[pages[-2]])+") - http://www.scp-wiki.net/"+pages[-2]+" - "
	final+=""+titlelist[pages[-3]]+"(Rating:"+str(ratinglist[pages[-3]])+") - http://www.scp-wiki.net/"+pages[-3]
	return  final
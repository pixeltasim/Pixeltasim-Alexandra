from whiffle import wikidotapi
from util import hook
import re
import time,threading

@hook.command("lc")
@hook.command("lastcreated")
def lastcreated(inp):
	api = wikidotapi.connection() #creates API connection
	api.Site = "scp-wiki"
	pages = api.refresh_pages() 
	final = ""
	final+=""+api.get_page_item(pages[-1],"title")+"(Rating:"+str(api.get_page_item(pages[-1],"rating"))+") - http://www.scp-wiki.net/"+pages[-1]+" - "
	final+=""+api.get_page_item(pages[-2],"title")+"(Rating:"+str(api.get_page_item(pages[-2],"rating"))+") - http://www.scp-wiki.net/"+pages[-2]+" - "
	final+=""+api.get_page_item(pages[-3],"title")+"(Rating:"+str(api.get_page_item(pages[-3],"rating"))+") - http://www.scp-wiki.net/"+pages[-3]
	return  final
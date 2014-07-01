from whiffle import wikidotapi
from util import hook
import re
import time,threading
import datetime
@hook.command
def test(inp):
	ts = time.time()
	lastcacherefresh = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	api = wikidotapi.connection() #creates API connection
	api.Site = "05command"
	pages = api.refresh_pages() #refresh page list provided by the API, is only a list of strings
	source = api.server.pages.get_one({"site":api.Site,"page":"alexandra-s-ban-page"})
	print source["content"]
	return str(ts)+"     "+lastcacherefresh
from whiffle import wikidotapi
from util import hook
import re
import time,threading

@hook.command
def ban(inp):
	api = wikidotapi.connection() #creates API connection
	api.Site = "scp-wiki"
	pages = api.refresh_pages() #refresh page list provided by the API, is only a list of strings
	source = api.server.pages.get_one({"site":api.Site,"page":"scp-2900"})
	return "This function is for testing purposes."
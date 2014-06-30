from time import sleep
import thread
from whiffle import wikidotapi

pagecache = [] 
def cache_refresh():
	global pagecache
	api = wikidotapi.connection()
	pages = api.refresh_pages()
	print "Refreshing cache"
	for page in pages:
		pagecache.append(api.server.pages.get_meta({"site": api.Site, "pages": [page]}))
		time.sleep(0.5)

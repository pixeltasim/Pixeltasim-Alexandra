from whiffle import wikidotapi

api = wikidotapi.connection()
pages = api.Pages
total = 0
for page in pages:
	total += 1
print total

@hook.command
def author(inp):
	".author <Author Name> -- Will return details regarding the author"
	authpages = []
	item for item in pagecache:
		if item["created_by"] == inp:
			authpages.append(item)
	total = 0
	pagetotal = 0
	for page in authpages:
		total += page["rating"]
		pagetotal += 1
	return inp +" has created " + pagetotal + " pages. With an average rating of "+ total/pagetotal+ ". Their most recently created page is " + authpages[-1]["title"]
	
	
	
pagecache = []

def refresh_cache():
	api = wikidotapi.connection()
	pages =  api.refresh_pages()
	for page in pages:
		 pagecache.append(api.server.pages.get_meta({"site": api.Site, "pages": [page]}))
	print "\n" + time.ctime()
	#threading.Timer(3600, refresh_cache).start()
	#refresh_cache()

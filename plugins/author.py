from whiffle import wikidotapi
from util import hook

@hook.command
def author(inp):
	".author <Author Name> -- Will return details regarding the author"
	api = wikidotapi.connection()
	api.Site = "scp-wiki"
	pages = api.refresh_pages()
	authpages = []
	totalrating = 0
	taletotal = 0
	scptotal = 0
	pagerating = 0
	author = "None"
	multimatch = []
	authorpage = ""
	try:
		for page in pages:
			if "scp" in taglist[page] or "tale" in taglist[page]: #makes sure only articles are counted
				if author == authorlist[page]:
					authpages.append(page)
					pagetitle = titlelist[page]
					pagerating = api.get_page_item(page,"rating")
					totalrating = totalrating + pagerating
					if "scp" in taglist[page]:
						scptotal +=1
					if  "tale" in taglist[page]:
						taletotal+=1
				try:
					if inp.lower() in authorlist[page].lower(): #this just matches the author with the first author match
						multimatch.append(authorlist[page])
						if author == "None":
							author = authorlist[page]
							authpages.append(page)
							pagetitle = titlelist[page]
							pagerating = api.get_page_item(page,"rating")
							totalrating = totalrating + pagerating
							if "scp" in taglist[page]:
								scptotal +=1
							if  "tale" in taglist[page]:
								taletotal+=1
				except AttributeError:
					pass
			else:
				if "author" in taglist[page]:
					if author == authorlist[page]:
						authorpage = "http://scp-wiki.net/"+page+" - "
						if author == "DrEverettMann": #hardcode because yes
							authorpage = "http://www.scp-wiki.net/dr-manns-personnel-file - "

	except KeyError:
		pass
	plusauth = []
	moreauthors = 1
	plusauth.append(author)
	for authors in multimatch: #checks to see if multiple authors found 
		z =0 
		for foundauthor in plusauth:
			if foundauthor ==authors:
				z =1
		if authors != author:
			if z == 0:
				moreauthors +=1
				plusauth.append(authors)

	if moreauthors>1:
		x = 0
		final = "Did you mean "
		for auth in plusauth:
			x+=1
			if x ==1:
				final+=auth+""
			if x ==2 and moreauthors ==2:
				final+=" or "+auth+"?"
			if x==2 and moreauthors >2:
				final+=", "+auth+""
			if x==3 and moreauthors ==3:
				final += ", or  "+auth+"?"
			if x==3 and moreauthors >3:
				final += ", or  "+auth+"? With " + str(moreauthors) + " more authors matching your query."
		return final
	avgrating = 0
	if taletotal+scptotal is not 0: #just so no division by zero
		avgrating = totalrating/(taletotal+scptotal)
	if not authpages: #if no author pages are added 
		return "Author not found."
	
	return authorpage+""+author +" has written " + str(scptotal) + " SCPs and "+str(taletotal)+" tales. They have " + str(totalrating)+ " net upvotes with an average rating of " + str(avgrating) + ". Their most recent article is " + pagetitle + "(Rating:" + str(pagerating) + ")"#+"- http://scp-wiki.net/" + authpages[-1].lower()
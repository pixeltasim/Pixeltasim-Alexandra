# -*- coding: utf-8 -*-

import math
import random
import re
import threading
import __builtin__

from util import hook
def return_final(page):
		title = titlelist[page]
		rating = ratinglist[page]
		is_title = 0
		try:
			if scptitles[page]:
				is_title = 1
		except Exception:
			pass 
		if is_title ==1:
			scptitle = scptitles[page]
			string = ""+scptitle+""+"("+title+", Rating:"+str(rating)+")"
			return string
		else:
			string = ""+title+""+"(Rating:"+str(rating)+")"
			return string 

@hook.command
def tags(inp):
    results =[]
	terms = inp.split()
	for page in scppages:
		failure = 0
		for term in terms:
			if term not in taglist[page]:
				failure = 1
		if failure != 0:
			results.append(page)
	if results == []:
		return "No matches found."
	final = ""
	third = 0
	for result in results:
		third+=1
		if third == 1:
			final+= return_final(result)
		if third<=3 and third != 1:
			final += ", "+return_final(result)
	if third>3:
		final += ", With " + str(third-3) + " more matches."
	if third==1:
		page = results[0]
		final = return_final(page)+" - http://www.scp-wiki.net/"+page
	__builtin__.seaiter = 1
	__builtin__.searesults = results
	return final




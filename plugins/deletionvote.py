from whiffle import wikidotapi
from util import hook
import re
import time,threading
import random 
import __builtin__
import datetime 

@hook.command
def deletionvotes(inp):
	final = ""
	for vote in deletion_votes:
		final += titlelist[vote]+" - www.scp-wiki.net/"+vote+" - Rating at "+ratinglist[vote]+". "
	return final 
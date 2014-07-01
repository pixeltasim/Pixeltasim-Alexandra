from whiffle import wikidotapi
from util import hook
from decimal import *
import re
import time,threading

@hook.command()
def cache(inp):
	return "The current cache has updated " +str(callsmade)+" out of "+ str(totalpagescurcache)+" total pages."#, or "+ str(Decimal(callsmade/totalpagescurcache)*100)+"%"
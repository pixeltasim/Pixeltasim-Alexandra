from util import hook
import __builtin__
@hook.command
def ignore(inp,chan = None):
	overrides = ["pixeltasim","thedeadlymoose"]
	if chan == "#site67":
		yes = 0
		for override in overrides:
			if inp.lower() == override:
				yes =1
		if yes ==0:
			__builtin__.blacklist_nicks.append(inp.lower())
			return inp +" has been added to blacklist."
		else:
			return "User cannot be ignored"
@hook.command
def removeignore(inp,chan = None):
	if chan == "#site67":
		try:
			__builtin__.blacklist_nicks.remove(inp.lower())
		except Exception:
			return "Error in removal, input is not in list"
		return "Removal of "+inp+" from blacklist is successful"
@hook.command
def listignores(inp,chan = None):
	if chan == "#site67":
		return str(blacklist_nicks)
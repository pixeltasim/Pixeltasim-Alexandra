from util import hook

@hook.command
def alexandra(inp):
	return "Alexandra is a SkyBot maintained with added functionality by Pixeltasim. Alexandra has updated its cache last at " + lastcacherefresh 
@hook.regex("hugs alexandra")
def hug(match):
	return "nonick::Thank you."
@hook.regex("alexandra sucks")
def insultpart(match):
	return "nonick::;("
@hook.regex("alexandra is awesome")
def awseomepart(match):
	return "nonick:::D"
@hook.regex("Anyone want to look at a draft?")
def draft(match, nick = None):
	return "nonick::"+nick+" has a draft guys!"
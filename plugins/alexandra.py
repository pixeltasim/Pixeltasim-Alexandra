from util import hook

@hook.command
def alexandra(inp):
	return "Alexandra is a version 1.0 SkyBot maintained with added functionality by Pixeltasim. Alexandra has updated its cache last at " + lastcacherefresh 
@hook.regex("hugs alexandra")
def hug(match):
	return "nonick::Aw shucks"
@hook.regex("alexandra sucks")
def insultpart(match):
	return "nonick::;("

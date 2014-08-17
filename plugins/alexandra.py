from util import hook
import random
import __builtin__

@hook.command
def alexandra(inp):
	return "Alexandra is a SkyBot maintained with added functionality by Pixeltasim. If you see any bugs, please post them here http://tinyurl.com/alex-bug-report . Alexandra has updated its cache last at " + lastcacherefresh 
@hook.regex("hugs alexandra")
def hug(match):
	__builtin__.hugs +=1
	if hugs > 5:
		return "That's enough hugs."
	if hugs > 10:
		return "That's enough hugs. Blacklisted."
	val = random.randint(0,2)
	if val == 0:
		return "nonick::Thank you."
	if val == 1:
		return "nonick::Aw shucks."
	if val == 2:
		return "nonick::Appreciate the hugs."
@hook.regex("alexandra sucks")
def insultpart(match):
	val = random.randint(0,3)
	if val == 0:
		return "nonick::I'm here you know!"
	if val == 1:
		return "nonick::>:|"
	if val == 2:
		return "nonick::Jerk"
@hook.regex("alexandra is awesome")
def awseomepart(match):
	return "nonick:::D"
@hook.regex("want to look at a draft")
def draft(match, nick = None):
	return "nonick::"+nick+" has a draft guys!"
@hook.regex("i have a draft")
def draft2(match, nick = None):
	return "nonick::"+nick+" has a draft guys!"
		
@hook.command()
def say00101010(inp,conn= None, nick = None, chan = None ):
	if nick =="Pixeltasim" and chan == nick:
		conn.msg("#site19", inp)

from util import hook
import random
import re
import __builtin__

@hook.command
def alexandra(inp):
	return "Alexandra is a SkyBot maintained with added functionality by Pixeltasim. If you see any bugs, please post them here http://tinyurl.com/alex-bug-report . Alexandra has updated its cache last at " + lastcacherefresh+". Her bans have been last updated at "+lastbanrefresh 
@hook.regex("hugs alexandra")
def hug(match):
	__builtin__.hugs +=1
	if hugs > 5:
		return "That's enough hugs."
	if hugs > 10:
		return "That's enough hugs. Blacklisted."
	val = random.randint(0,3)
	if val == 0:
		return "nonick::Thank you."
	if val == 1:
		return "nonick::Aw shucks."
	if val == 2:
		return "nonick::Appreciate the hugs."
	if val == 3:
		return "It's not like I /asked/ you to hug me or anything baka"
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
@hook.regex(re.compile("look at a draft|see a draft|!draft|i have a draft|look over a draft"))
def draft(match, nick = None,conn = None,chan = None):
	conn.msg("#site67", "Alert: "+nick+" has a draft in "+chan)
	return "nonick::"+nick+" has a draft guys!"
@hook.regex("i have a draft")
		
@hook.command()
def say00101010(inp,conn= None, nick = None, chan = None ):
	if nick =="Pixeltasim" and chan == nick:
		parts= inp.split()
		msg = ""
		for i in range(1,len(parts)):
			msg+=parts[i]+" "
		conn.msg(parts[0], msg)
@hook.command()
def ignore00101010(inp,conn= None, nick = None, chan = None ):
	if nick =="Pixeltasim" and chan == nick:
		conn.cmd('IGNORE', [chan,inp])

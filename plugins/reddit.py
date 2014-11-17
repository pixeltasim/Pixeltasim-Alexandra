import json
import urllib2
import time
from util import hook
import re

reddit_re = (r'.*((www\.)?reddit\.com/r[^ ]+)', re.I)

@hook.regex(*reddit_re)
def reddit_url(match):
	
    jsonlink = match.group(0) + '.json' # retrieve JSON-ified version of link
    req = urllib2.Request(jsonlink)
    req.add_header('User-agent', 'Python/Alexandra-1.0') # Reddit wants us to use unique user-agents. OK.
    response = urllib2.urlopen(req)

    data = json.load(response)
    submission = data[0]['data']['children'][0]['data'] # Dig down to the relevant bits.
    self = submission["is_self"]
    if self == True:
        url = 'http://redd.it/' + submission["id"]
    else:
        url = submission["url"]
    title = submission["title"]
    score = submission["score"]
    author = submission["author"]
    timeago = time.strftime("%b %d %Y %H:%M:%S", time.gmtime(submission["created_utc"]))
    comments = submission["num_comments"]
    return '%s - \x02%s\x02 - posted by \x02%s\x02 %s GMT - %s points and %s comments' % (
    url, title, author, timeago, score, comments) 

from util import hook, http
import re

reddit_re = (r'.*((www\.)?reddit\.com/r[^ ]+)', re.I)

@hook.regex(*reddit_re)
def reddit_url(match):

    thread = http.get_html(match.group(0))

    title = thread.xpath('//title/text()')[0]
    score = thread.xpath("//div[@class='score']/span[@class='number']/text()")[0]
    author = thread.xpath("//div[@id='siteTable']//a[contains(@class,'author')]/text()")[0]
    timeago = thread.xpath("//div[@id='siteTable']//p[@class='tagline']/time/text()")[0]
    comments = thread.xpath("//div[@id='siteTable']/div[1]/div[2]/ul/li[1]/a/text()")[0]

    return '%s - \x02%s\x02 - posted by \x02%s\x02 %s - %s net upvotes and %s' % (
            match.group(0), title, author, timeago, score, comments)
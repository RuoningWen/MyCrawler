__author__ = 'chenk_group1'
# -*- coding: utf-8 -*-
import socket
import urllib2
import re
import functools
import httplib
import urllib2
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
'''class BoundHTTPHandler(urllib2.HTTPHandler):
    def __init__(self, source_address=None, debuglevel=0):
        urllib2.HTTPHandler.__init__(self, debuglevel)
        self.http_class = functools.partial(httplib.HTTPConnection,
                source_address=source_address)
    def http_open(self, req):
        return self.do_open(self.http_class, req)
handler = BoundHTTPHandler(source_address=("172.1.4.17", 0))
opener = urllib2.build_opener(handler)
urllib2.install_opener(opener)'''
from bs4 import BeautifulSoup
# from BeautifulSoup import NavigableString, Tag
import requests
import csv
import unicodedata
import re
import urllib2
import random
import socket
import cookielib
waittime=time
#timeout=30
#socket.setdefaulttimeout(timeout)
urlnumber='start=0'   # Give the page number to start with
pa=1
def openurl(url):
        cookie_support= urllib2.HTTPCookieProcessor(cookielib.CookieJar())
        opener = urllib2.build_opener(cookie_support,urllib2.HTTPHandler)
        urllib2.install_opener(opener)
        user_agents = [
                    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
                    'Opera/9.25 (Windows NT 5.1; U; en)',
                    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
                    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
                    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
                    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
                    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
                    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 ",
                    ]
        agent = random.choice(user_agents)
        opener.addheaders = [("User-agent",agent),("Accept","*/*"),('Referer','http://www.google.com')]
        try:
            res = opener.open(url)
            print res
        except Exception,e:
            print e
        #else:
        return res





def gettext(souptext ,filename):
    entries = []
    entry = []
    for div in souptext.find_all('div'):
            if(div.get('class') != None and div.get('class')[0] == 'comment'): # A single post is referred to as a comment. Each comment is a block denoted in a div tag which has a class called comment.
                ps = div.find_all('p') #gets the message / body of the post
                aas = div.find_all('a') # gets the name of the person posting
                spans = div.find_all('span') #
                concat_str1 = ''
                for a in aas:
                    if (a.get('class') != None and a.get('class')[0] == ''):
                        for str in a.contents:
                            if str != "<br>" or str != "<br/>":
                                concat_str1 = (str.encode('utf-8')).strip()
                        #entry.append(concat_str)
                        rate = a.next_sibling.next_sibling
                        star = rate['class'][0]
                        concat_str2 = star.replace("allstar","")
                        #entry.append(star.replace("allstar",""))
                concat_str3 = ''
                for time in spans:
                    if (time.get('class') != None and time.get('class')[0] == ''):
                        for str in time.contents:
                            if str != "<br>" or str != "<br/>":
                                concat_str3 = (str.encode('utf-8')).strip()
                        #entry.append(concat_str)
                concat_str4 = ''
                usefulness = div.find_all("span", "votes pr5")[0]
                for str in usefulness.contents:
                    concat_str4 = (str.encode('utf-8')).strip()
                #entry.append(concat_str)
                concat_str5 = ''
                for str in ps:
                    concat_str5 = (str.get_text().encode('utf-8')).strip()
                if concat_str2=='':
                    concat_str2='Null'
                entry.append(concat_str1+'\t'+concat_str2+'\t'+concat_str3+'\t'+concat_str4+'\t'+concat_str5)
    entries.append(entry)
    with open(filename,'a') as output:
        writer = csv.writer(output, delimiter= '\n', lineterminator = '\n')
        writer.writerows(entries)


lines= open('D:\Comment&Review\\douban_nameandnumber2.txt').readlines()

for line in lines:
    whilerun=True
    urlnext='?start=0&limit=20&sort=new_score'
    a=line.split('\t')
    b= a[0]+'.txt'
    c=str(a[1]).replace("\n","")
    pa=1
    print b
    while whilerun: # Give the page number to end with
        url = 'http://movie.douban.com/subject/%s/comments%s'%(c,urlnext)
        print url
        try:
            response = urllib2.urlopen(url,timeout=100)
        except Exception,e:
            break
        data = response.read().decode('utf-8')
        soup1 = BeautifulSoup(data)
        for div in soup1.find_all('div'):
                if(div.get('id') == 'paginator'):
                    aas = div.find_all('a')
                    if (aas.__len__()==1 and pa == 1):
                        urlnext=aas[0].get('href')
                    elif (aas.__len__()==3):
                        urlnext=aas[2].get('href')
                    else:
                        whilerun=False
        gettext(soup1,b)

        pa=pa+1
        waittime.sleep(1)

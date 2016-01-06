__author__ = 'chenk_group1'
# -*- coding: utf-8 -*-
import socket
import urllib2
import re
import functools
import httplib
import urllib2
from bs4 import BeautifulSoup
#from BeautifulSoup import NavigableString, Tag
import requests
import csv
import unicodedata
import sys
import urllib2
import random
import socket
import cookielib
import time
entries = []
entry = []
pa=1
whilerun=True
moviename=''
movienumber=''
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
        if(div.get('class') != None and ( div.get('class')[0] == "main-hd")):
            spans = div.find_all('span') #
            concat_str = ''
            for time in spans:
                    for str in time.contents:
                        if str != "<br>" or str != "<br/>":
                            concat_str = (concat_str + ' '+ str.encode('utf-8')).strip()
            entry.append(concat_str)
    for div in souptext.find_all('div'):
        if(div.get('class') != None and div.get('class')[0] == "main-bd"):
            concat_str=(div.get_text().encode('utf-8').strip())
            entry.append(concat_str)
            entries.append(entry)
    with open(filename,'a') as output:
        writer = csv.writer(output, delimiter= ',', lineterminator = '\n')
        writer.writerows(entries)




lines= open('D:\Comment&Review\\movie_nameandnumber2.txt').readlines()
for line in lines:
    urlnext='?start=0&filter=&limit=20'
    a=line.split('\t')
    b= a[0]+'.txt'
    c=str(a[1]).replace("\n","")
    print c.__class__
    print b
    pa=1
    whilerun=True
    while whilerun: # Give the page number to end with
            print pa
            url = 'http://movie.douban.com/subject/%s/reviews%s' %(c,urlnext)
            print url
            try:
                response =  urllib2.urlopen(url,timeout=100)
            except Exception,e:
                break
            data = response.read().decode('utf-8')
            soup1=BeautifulSoup(data)
            reviewtext=[]
            for div in soup1.find_all('div'):
                aas = div.find_all('a')
                for aa in aas:# gets the name of the person posting
                    if(aa.get('href')=='#'):
                        reviewtext.append(aa.get('data-url'))
            new_list=[]
            for i in reviewtext:
                if i not in new_list:
                    new_list.append(i)
            for j in new_list:
                try:
                    response1 = openurl(j)
                    data1=response1.read()
                    souptext=BeautifulSoup(data1)
                    gettext(souptext,a[0])
                    time.sleep(1)
                except Exception,e1:
                    break
            for div in soup1.find_all('div'):
                if(div.get('id') == 'paginator'):
                    aas = div.find_all('a')
                    if (aas.__len__()==1):
                        urlnext=aas[0].get('href')
                    elif (aas.__len__()==3):
                        urlnext=aas[2].get('href')
                    else:
                        whilerun=False
            pa=pa+1




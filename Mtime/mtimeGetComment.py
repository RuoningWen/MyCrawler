__author__ = 'chenk_group1'
# -*- coding: utf-8 -*-
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
import socket
import time
concat_str=''
def gettext(souptext ,filename):
    entries = []
    entry = []
    concat_str = ''
    for ddd in souptext.find_all('dd'):
        if (ddd.get('class') != None and (ddd.get('class')[0] == '' or ddd.get('class')[0] == 'first')):
            nametimes=ddd.find_all('a')
            stars=ddd.find_all('span')
            comments=ddd.find_all('h3')
            concat_str4=""
            '''for name in nametimes:
                if(name.get('title')!=None and name.get('class')==None):
                    concat_str4=(name.get('title').encode('utf-8')).strip()'''
            concat_str4=(nametimes[0].get('title').encode('utf-8')).strip()
            concat_str2='Null'
            for star in stars:
                if(star.get('class') != None and star.get('entertime')==None):
                    concat_str2=(star.get_text().encode('utf-8')).strip()
            concat_str = ''
            for time in nametimes:
                if(time.get('entertime') != None):
                    concat_str1=(time.get('entertime').encode('utf-8')).strip()
            for comment in comments:
                concat_str3=(comment.get_text().encode('utf-8')).strip()
            concat_str = ''
            concat_str=((concat_str4+"\t")+(concat_str2+"\t")+(concat_str1+"\t")+concat_str3)
            entry.append(concat_str)
    entries.append(entry)
    with open(filename,'a') as output:
        writer = csv.writer(output, delimiter= '\n', lineterminator = '\n')
        writer.writerows(entries)
lines= open('D:\Comment&Review\\mtime_short2.txt').readlines()


for line in lines:
    whilerun=True
    a=line.split('\t')
    b= a[0]+'.txt'
    c=str(a[1]).replace("\n","")
    urlpre=c
    urlcurrent=c
    pa=1
    print a[0]
    while whilerun: # Give the page number to end with
        print urlcurrent
        time.sleep(1)
        try:
            response = urllib2.urlopen(urlcurrent,timeout=100)
        except Exception,e:
            break
        data = response.read().decode('utf-8')
        soup1 = BeautifulSoup(data)
        gettext(soup1,b)
        urlpre=urlcurrent
        for aa in soup1.find_all('a'):
            if (aa.get('id')=='key_nextpage'):
                urlcurrent=aa.get('href')
        if(urlcurrent==urlpre):
            whilerun=False


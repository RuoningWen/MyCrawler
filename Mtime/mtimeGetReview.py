__author__ = 'chenk_group1'
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
def gettext(souptext ,filename):
    entries = []
    entry = []
    time.sleep(1)
    concat_str3='Null'
    for dd in souptext.find_all('div'):
        if(dd.get('class') != None and ( dd.get('class')[0] == "db_mediacont")):
            concat_str1= (dd.get_text().encode('utf-8')).strip()
    for pp in souptext.find_all('p'):
        if(pp.get('class') != None and ( pp.get('class')[0] == "pt3")):
                concat_str2=(pp.get_text().encode('utf-8')).strip()
        if(pp.get('class') != None and ( pp.get('class')[0] == "mt9")):
            for span in pp.find_all('span'):
                concat_str3=(span.get_text().encode('utf-8')).strip()
        if(pp.get('class') != None and ( pp.get('class')[0] == "mt3")):
            concat_str4=(pp.get_text().encode('utf-8')).strip()
    entry.append(concat_str2+'\t'+concat_str3+'\t'+concat_str4+'\t'+concat_str1)
    entries.append(entry)
    with open(filename,'a') as output:
        writer = csv.writer(output, delimiter= '\n', lineterminator = '\n')
        writer.writerows(entries)
lines= open('D:\Comment&Review\\mtime_review.txt').readlines()
for line in lines:
    a=line.split('\t')
    b= a[0]+'.txt'
    c=str(a[1]).replace("\n","")
    urlpre=c
    urlcurrent=c
    print b
    pa=1
    whilerun=True
    while whilerun: # Give the page number to end with
            print pa
            print urlcurrent
            try:
                response =  urllib2.urlopen(urlcurrent,timeout=100)
            except Exception,e:
                break
            data = response.read().decode('utf-8')
            soup1=BeautifulSoup(data)
            reviewtext=[]
            for hh in soup1.find_all('h3'):
                for aa in hh.find_all('a'):
                    reviewtext.append(aa.get('href'))
                    print aa.get('href')
            for j in reviewtext:
                try:
                    response1 = urllib2.urlopen(j,timeout=100)
                    data1=response1.read()
                    souptext=BeautifulSoup(data1)
                    gettext(souptext,b)
                    time.sleep(1)
                except Exception,e1:
                    print e1
                    continue
            urlpre=urlcurrent
            for aa in soup1.find_all('a'):
                if (aa.get('id')=='key_nextpage'):
                    urlcurrent=aa.get('href')
            if(urlcurrent==urlpre):
                whilerun=False
            pa=pa+1

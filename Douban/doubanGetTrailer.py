__author__ = 'chenk_group1'
from bs4 import BeautifulSoup
# from BeautifulSoup import NavigableString, Tag
import requests
import csv
import unicodedata
import re
import urllib2
import time
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
url='http://movie.douban.com/trailer/166683/?start=0#comments'
response = urllib2.urlopen(url,timeout=100)
data = response.read().decode('utf-8')
soup1 = BeautifulSoup(data)
entry=[]
entries=[]
concat_str1=''
concat_str2=''
concat_str3=''
def gettext(souptext ,filename):
    entry=[]
    entries=[]
    for dd in soup1.find_all('div'):
        if(dd.get('class') != None and ( dd.get('class')[0] == "comment-item")):
            aa=dd.find_all('a')
            ss=dd.find_all('span')
            pp=dd.find_all('p')
            for a in aa:
                if(a.get('class')!=None and a.get('class')[0]!='toggle-reply'):
                    concat_str1=(a.get_text().encode('utf-8')).strip()
            for s in ss:
                if(s.get('class')!=None and (s.get('class')[0] == "")):
                    concat_str2=(s.get_text().encode('utf-8')).strip()
            for p in pp:
                if(p.get('class')!=None):
                    concat_str3=((p.get_text().encode('utf-8')).replace("\n","")).strip()
            entry.append(concat_str1+'\t'+concat_str2+'\t'+concat_str3)
    entries.append(entry)
    with open(filename,'a') as output:
        writer = csv.writer(output, delimiter= '\n', lineterminator = '\n')
        writer.writerows(entries)
lines= open('D:\Comment&Review\\douban_trailer2.txt')
for line in lines:
    whilerun=True
    a=line.split('\t')
    b= a[0]+'.txt'
    c=str(a[1]).replace("\n","")
    urlpre=c
    urlcurrent=c
    pa=1
    print a[0]
    while whilerun:
        print urlcurrent
        time.sleep(1)
        response = urllib2.urlopen(urlcurrent,timeout=100)
        data = response.read().decode('utf-8')
        soup1 = BeautifulSoup(data)
        urlpre=urlcurrent
        for ss in soup1.find_all('span'):
            if (ss.get('class')!=None and ss.get('class')[0]=='next'):
                for aa in ss.find_all('a'):
                    urlcurrent=aa.get('href')
        if(urlcurrent==urlpre):
            whilerun=False
        gettext(soup1,b)
        pa=pa+1
        time.sleep(1)
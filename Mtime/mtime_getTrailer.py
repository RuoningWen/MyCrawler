__author__ = 'chenk_group1'
from bs4 import BeautifulSoup
# -*- coding: utf-8 -*-
# from BeautifulSoup import NavigableString, Tag
import requests
import csv
import unicodedata
import re
import urllib2
import json
import time




def gettext(data ,filename):
    entry=[]
    entries=[]
    s=json.loads(data)
    for a in s['value']['comments']:
        str1=a['nickName']
        str2=a['enterTime']
        str3=a['content']
        if str1=='':
            str1='Null'
        str4= ((str1+'\t'+str2+'\t'+str3).encode('utf-8')).strip()
        entry.append(str4)
    for a in s['value']['replies']:
        str1=a['nickName']
        str2=a['enterTime']
        str3=a['content']
        if str1=='':
            str1='Null'
        str4= ((str1+'\t'+str2+'\t'+str3).encode('utf-8')).strip()
        entry.append(str4)
    entries.append(entry)
    with open(filename,'a') as output:
        writer = csv.writer(output, delimiter= '\n', lineterminator = '\n')
        writer.writerows(entries)

lines= open('D:\Comment&Review\\mtime_trailer4.txt')
for line in lines:
    whilerun=True
    a=line.split('\t')
    b= a[0]+'.txt'
    c=a[1]
    d=str(a[2]).replace("\n","")
    url1='http://service.library.mtime.com/Comment.api?Ajax_CallBack=true&Ajax_CallBackType=Mtime.Library.Services&Ajax_CallBackMethod=GetVideoCommentList&Ajax_CrossDomain=1&Ajax_RequestUrl='+'http://video.mtime.com/%s/comment/?%s'%(c,d)+'&Ajax_CallBackArgument0=%s&Ajax_CallBackArgument1=1'%c
    url2='http://service.library.mtime.com/Comment.api?Ajax_CallBack=true&Ajax_CallBackType=Mtime.Library.Services&Ajax_CallBackMethod=GetVideoCommentList&Ajax_CrossDomain=1&Ajax_RequestUrl='+'http://video.mtime.com/%s/comment/?%s'%(c,d)+'&Ajax_CallBackArgument0=%s&Ajax_CallBackArgument1=2'%c
    url3='http://service.library.mtime.com/Comment.api?Ajax_CallBack=true&Ajax_CallBackType=Mtime.Library.Services&Ajax_CallBackMethod=GetVideoCommentList&Ajax_CrossDomain=1&Ajax_RequestUrl='+'http://video.mtime.com/%s/comment/?%s'%(c,d)+'&Ajax_CallBackArgument0=%s&Ajax_CallBackArgument1=3'%c
    time.sleep(1)
    try:
        print url1
        time.sleep(1)
        response = urllib2.urlopen(url1,timeout=100)
        data1 = response.read().decode('utf-8')
        data1=data1.replace("var videoCommentListResult = ","")
        data1=data1.replace("\S","")
        strJson = "".join([data1.strip().rsplit("}" , 1)[0] ,  "}"] )
        gettext(strJson,b)
    except Exception,e:
        print e
        continue
    try:
        print url2
        time.sleep(1)
        response2 = urllib2.urlopen(url2,timeout=100)
        data2 = response2.read().decode('utf-8')
        data2=data2.replace("var videoCommentListResult = ","")
        data2=data2.replace("\S","")
        strJson2 = "".join([data2.strip().rsplit("}" , 1)[0] ,  "}"] )
        gettext(strJson2,b)
    except Exception,e:
        print e
        continue
    try:
        print url3
        time.sleep(1)
        response3 = urllib2.urlopen(url3,timeout=100)
        data3 = response3.read().decode('utf-8')
        data3=data3.replace("var videoCommentListResult = ","")
        data3=data3.replace("\S","")
        strJson3 = "".join([data3.strip().rsplit("}" , 1)[0] ,  "}"] )
        gettext(strJson3,b)
    except Exception,e:
        print e
        continue
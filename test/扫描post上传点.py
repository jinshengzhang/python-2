# -*- coding: cp936 -*-
#coding=utf-8
from urlparse import urlparse
import urllib2
import re
import threading
import time

exitFlag = 0
threadLock = threading.Lock()
threads = []
gurllist=[]


def gethtml(url):
        print "���ڶ�ȡ��ҳ��"+url
        htmls=urllib2.urlopen(url)
        html=htmls.read()
        return html

    

def searchnew(url):
    coun = gurllist.count(url)
    if coun==0:
        page = gethtml(weburl)
        htmlurl = re.findall(r'[a-zA-z]+://[^\s("\s)<>]*(?!:.css|.js)',page)#��ҳ��ַ
        #htmlurl = re.findall(r'[a-zA-z]+://[^\s("\s)<>]*',page)#��ҳ��ַ
        getpost(url)
        gurllist.append(url)
        for index in range(len(htmlurl)):
            myth=mythread(index,htmlurl[index])
            myth.start()
        return
    else:
        return

def getpost(url):
    page = gethtml(url)
    pmet = re.findall(r'<form.*>',page)#post
    for index in range(len(pmet)):
        method=re.findall(r'method=\"(.+)\"',pmet[index])
        action=re.findall(r'action=\"(.+)\"',pmet[index])
        fp = open('myrecordweburl.txt','a')
        fp.write("�ϴ���Ϊ��"+action[0]+"�ϴ���ʽΪ��"+method[0]+"\n")
        fp.flush()
        fp.close()
    print url+"�������,��ҳ����"+str(len(pmet))+"���ϴ���"
    return

class mythread (threading.Thread):
    def __init__(self,threadID,myurl):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.url = myurl
    def run(self):
        threadLock.acquire()
        searchnew(self.url)
        threadLock.release()
        return 

print 'http or https?'
ch=raw_input('1.http  2.https:')

if ch == '1':
    weburl='http://'+raw_input("please input web url:")
elif ch== '2':
    weburl='https://'+raw_input("please input web url:")
else:
    print 'ERROR!'
    
searchnew(weburl)



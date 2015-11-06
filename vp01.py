#!/bin/python
# python for 'voilent python'

"""
import socket
socket.setdefaulttimeout(5)
s = socket.socket()
try:
    s.connect(("10.7.4.228", 21))
except Exception, e:
    print "[-] Error = " +str(e)

ans = s.recv(1024)
print ans

try:
    print "[+] 1377/0 = " +str(1377/0)
except Exception, e:
    print "[-] Error = " +str(e)

"""

import socket
import os
import sys
def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except:
        return
def checkVulns(banner, filename):
    f = open(filename, 'r')
    for line in f.readlines():
        if line.strip('\n') in banner:
            print '    [+] Server is vulnerable: ' + banner
def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print '[-] ' + filename +\
                ' does not exist.'
            exit(0)
        if not os.access(filename, os.R_OK):
            print '[-] ' + filename +\
                ' access denied.'
            exit(0)
    else:
        print '[-] Usage: ' + str(sys.argv[0]) +\
            ' <vuln filename>'
        exit(0)

    portList = [21,22,25,80,110,443]
    for x in range(228, 229):
        ip = '10.7.4.' + str(x)
        for port in portList:
            banner = retBanner(ip, port)
            if banner:
                #print '[+] ' + ip + ': ' + banner
                print '[+] %s:%d: %s' %(ip, port, banner.strip('\n'))
                checkVulns(banner, filename)

if __name__ == '__main__':
        main()

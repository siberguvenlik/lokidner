#!/usr/bin/python
# -*- coding: utf-8 -*

import urllib2
import colorama
import urlparse
from BeautifulSoup import BeautifulSoup
from colorama import Fore

##
# LOKIDNer Project is in progress...
##

banner = """
                                                                                                                                                            
###############################################################################
#################  #########################  ################    ##    #######
#################    #####################    ################  ####  #########
###################   ####################   #################    ##  #########
###############################################################################
###     #######         ####    ###     ##    ##          ####    ###      ####
###     ######           ###    ##    ####    ##           ###    ###      ####
###     #####     ###     ##    #    #####    ##    ###     ##    ##       ####
###     #####    #####    ##        ######    ##    ####     #    #   #    ####
###     #####    #####    ##         #####    ##    ####     #       ##    ####
###     #####     ##      ##    #     ####    ##    ###     ##       ##    ####
###         ##           ###    ##     ###    ##           ###      ###    ####
###         ####       #####    ###     ##    ##         =####     ####    ####
###############################################################################
## Lapse of Keyboard at Internationalized Domain Name ## SCANNER ## by AkkuS ##
###############################################################################

>> LOKIDN is a new vector for Homograph Attacks
>> EDB-ID : 45567
>> https://pentest.com.tr/pdf/LOKIDN-EN.pdf
                                                                                                                                                                                                                                                                                                                                                   
"""

print banner
odomain = str(raw_input("Original Domain (https://lokidn.com) : ")) # Original Domain

  
print(Fore.BLUE + "- [*] Browsing web site...")

def getAllUrl(url):
    try:
        page = urllib2.urlopen( url ).read()
    except:
        return []
    urlList = []
    try:
        soup = BeautifulSoup(page)
        soup.prettify()
        for anchor in soup.findAll('a', href=True):
            if not 'http://' in anchor['href']:
                if urlparse.urljoin(url, anchor['href']) not in urlList:
                    urlList.append(urlparse.urljoin(url, anchor['href']))
            else:
                if anchor['href'] not in urlList:
                    urlList.append(anchor['href'])

        length = len(urlList)

        return urlList
    except urllib2.HTTPError, e:
        print e

def listAllUrl(urls):
    for x in urls:
        print x
        urls.remove(x)
        urls_tmp = getAllUrl(x)
        for y in urls_tmp:
            urls.append(y)


if __name__ == "__main__":
    urls = [odomain]
    while(urls.count>0):
        urls = getAllUrl(odomain)
        listAllUrl(urls)

##
# c/g/i/o/s/u  |  ç/ğ/ı/ö/ş/ü # IDN domain probabilities to be placed
##

##
# will be printed if there is IDN in (urls)
##

##
# calls to IDN from other sites with Google dork
##

##
# Reflecting the availability of IDN domains
##










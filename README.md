
```
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

```

<p align="center">
<img src="https://img.shields.io/badge/Python-2-yellow.svg"></a>
<a href="#"><img src="https://www.pentest.com.tr/images/Blackhat/blackhatUSA2019p.svg"></a>
<a href="#"><img src="https://www.pentest.com.tr/images/Defcon/defcon27p.svg"></a>
</p>

#### Articles and Links

+ EDB-ID: 45567 **LOKIDN (EN)** - https://www.exploit-db.com/exploits/45567/
+ My Blog **LOKIDN (TR)** - https://pentest.com.tr/blog/Lapse-of-Keyboard-at-Internationalized-Domain-Name-TR.html
+ OWASP List **LOKIDN (EN)** - http://lists.owasp.org/pipermail/owasp-community/attachments/20180920/87818b1f/attachment-0001.pdf

<p align="center">
<img src="https://github.com/siberguvenlik/lokidner/blob/master/art-pdf.png" height="%50" width="60%">
</p>

#### Purpose

Creating a new **LOKIDN Homograph Attack** scenario.

+ Identify the IDN types of the target domain
+ Scan the application files of the original domain
+ Find the **Lapse of Keyboard** on the discovered URLs
+ Scan to target IDN domain with Google dork
+ Reflecting the availability of IDN domains


#### Soon to be added features 

+ To think like a Turk by Artificial Intelligence and to discover high probability LOKIDN domain names

**Screenshots:**
<p align="center">
<img src="https://github.com/siberguvenlik/lokidner/blob/master/usage.png" height="%50" width="60%">
</p>


### --------------------------------------------------------------------------------

Download LOKIDNer:

`git clone https://github.com/siberguvenlik/lokidner.git`

It's done!

Run the program with following command: 

Run:

```python
cd lokidner-master
python lokidner.py
```

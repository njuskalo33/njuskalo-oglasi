import requests as re
import regex as r
import time
import smtplib

gmail_user = 'njuskalo.test123@gmail.com'
gmail_password = 'radilca123'

sent_from = gmail_user
to = "nikola.pavich7@gmail.com"


server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(gmail_user, gmail_password)

oldOglasi = {}
oglasiFilter = {}
start = "https://www.njuskalo.hr"


def saveToFile():
    file.write(
    file = open("test.txt")


while True:
    site = re.get("https://www.njuskalo.hr/?ctl=search_ads&keywords=oneplus+mclaren")
    list = r.findall("<h3 class=\"entity\-title\"><a name=\"\d*\" class=\"link\" href=\".+\">(.+)<\/a>", site.text)
    list2 = r.findall("<h3 class=\"entity\-title\"><a name=\"\d*\" class=\"link\" href=\"(.+)\">.+<\/a>", site.text)
    oglasi = {list[a]: list2[a] for a in range(list.__len__())}
    # print(oglasi)
    
    oglasiFilter = {}
    for a in oglasi:
        if a.lower().find("oneplus") == 0 or a.lower().find("one plus") == 0:
            oglasiFilter[a] = oglasi[a]
    # print(oglasiFilter)
    
    # print(oglasiFilter.__len__(), oldOglasi.__len__())
    if oglasiFilter.__len__() != oldOglasi.__len__():
        noviOglasi = {a: oglasiFilter[a] for a in oglasiFilter if a not in oldOglasi}
        print(noviOglasi)
    
        for oglas in noviOglasi:               
            subject = 'Novi oglas pog'
            body = oglas + "\n" + start + noviOglasi[oglas]
        
            email_text = """\
            From: %s
            To: %s
            Subject: %s

            %s
            """ % (sent_from, to, subject, body)
            
            server.sendmail(sent_from, to, email_text)
    
        oldOglasi = oglasiFilter
    
    time.sleep(1800)
    

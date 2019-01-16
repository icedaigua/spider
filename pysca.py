import requests
from lxml import etree
import os
import time
import re
import platform
# from multiprocessing.dummy import Pool



def OSconnector():
    if platform.system()=='Windows':
        return "\\"
    else:
        return '/'

def getHtml(url):
    html = requests.get(url).content
    selector = etree.HTML(html)
    return selector

def getContent(htm, xpathStr):
    selector = htm
    content = selector.xpath(xpathStr)  
    return content

def getDownPdf(cons, title, folder):
    fn = '%s' % title.split('\n')[0].split(':')[0]
    # pa = os.path.dirname(__file__) + '\\' + 'arxiv' + '\\%s' % folder
    pa = os.path.dirname(__file__) + '\\' + 'arxiv'
    # check and create folder
    if not os.path.exists(pa):
        os.mkdir(pa)
    fl = pa + '\\%s.pdf' % fn
    r = requests.get(cons)
    with open(fl, "wb") as code:
        code.write(r.content)


def search_newCV_fromarxiv():
    url0 = 'http://arxiv.org/list/cs.CV/recent'
    print(url0)

    # xpath of each page
    xp1 = '//dl[1]//*[@class="list-identifier"]//a[2]//@href'  # pdf href list
    xp2 = '//dl[1]//*[@class="list-title mathjax"]/text()'  # Title
    xp_date = '//*[@id="dlpage"]/h3[1]/text()'  # date->folder

    htm0 = getHtml(url0)
    cons1 = getContent(htm0, xp1)  # get pdfs' href
    cons2 = getContent(htm0, xp2)  # get papers' title
    cons_date = getContent(htm0, xp_date) # get date

    folder = cons_date[0].split(', ') # get date string

    print(folder[1] + ': having %s' % len(cons1) + '  files')
    print('pdfs are downloading...')

    for indx in range(0, len(cons1)):
        href = 'http://arxiv.org' + cons1[indx]
        title = cons2[2 * indx + 1]
        print('%s.' % (1 + indx) + ' ' + href + ' ' + title)
        getDownPdf(href, title, folder[1])


def search_SLAM_fromarxiv():
    url0 = 'https://arxiv.org/search/?query=slam&searchtype=all&source=header&start=0'
    print(url0)


    # xpath of each page
    xp1 = '//dl[1]//*[@class="is-marginless"]//a[2]//@href'  # pdf href list
    xp2 = '//dl[1]//*[@class="title is-5 mathjax"]/text()'  # Title
    xp_date = '//*[@id="dlpage"]/h3[1]/text()'  # date->folder

    htm0 = getHtml(url0)
    cons1 = getContent(htm0, xp1)  # get pdfs' href
    cons2 = getContent(htm0, xp2)  # get papers' title
    cons_date = getContent(htm0, xp_date) # get date

    folder = cons_date[0].split(', ') # get date string

    print(folder[1] + ': having %s' % len(cons1) + '  files')
    print('pdfs are downloading...')

    for indx in range(0, len(cons1)):
        href = 'http://arxiv.org' + cons1[indx]
        title = cons2[2 * indx + 1]
        print('%s.' % (1 + indx) + ' ' + href + ' ' + title)
        getDownPdf(href, title, folder[1])

if __name__=='__main__':
    # print(OSconnector())
    # search_newCV_fromarxiv()
    search_SLAM_fromarxiv()
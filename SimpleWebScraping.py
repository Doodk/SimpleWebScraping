#Title: SimpleWebScraping
# Ver 1.1
# Author: Doodk
#
# Create Date: July 25, 2018
# Last Modify Date: July 26, 2018
#
# Dependency: requests, BeautifulSoup(beautifulsoup4), lxml
# To install:
#   >> $ pip install beautifulsoup4
#   >> $ pip install requests
#   >> $ pip install lxml
#
# Usage:
# GetPageHTMLFromIndexPage("http://news.qq.com/", ".head > .Q-tpList .text
#           .linkto", ".content-article, .Cnt-Main-Article-QQ", False)
# GetPageHTMLFromIndexPage(mainUrl, mainSelectorRule, subSelectorRule,
#           discardBlank=False)
#   mainUrl:
#       The first web url, which contain url/title list for the articles
#   mainSelectorRule:
#       The CSS select rule, to specific the <a> tag position in the first web
#       page
#   subSelectorRule:
#       The CSS select rule, to specific the content position in the articles
#       web page
#   discardBlank [Default=False]:
#       Whether discard the null result from scraping the articles (this may
#       cause by incorrect css selector, web page lazy load, etc.)
#
#
import requests
from bs4 import BeautifulSoup

# Get HTML code from the url, within the DOM selector
def GetHTMLbySelectDOM(url, selectorRule):
    r = requests.get(url)   # Get HTML content
    myhtml = BeautifulSoup(r.content, "lxml")   # transform the HTML content to bs4's data type
    ret = myhtml.select(selectorRule)  # get HTML content by selector's rule
    return ret

# Get tag's attribute value (Default: href), and content
def GetTagAttribAndContent(tagHTML, attrib="href"):
    return tagHTML.get(attrib), tagHTML.string

# Combine Function:
# Get link list from first page, then scrape content inside each link
def GetPageHTMLFromIndexPage(mainUrl, mainSelectorRule, subSelectorRule, discardBlank=False):
    ret = []
    subPage = GetHTMLbySelectDOM(mainUrl, mainSelectorRule)
    for link in subPage:
        subUrl, title = GetTagAttribAndContent(link)
        subHTML = GetHTMLbySelectDOM(subUrl, subSelectorRule)
        if subHTML != []:
            ret.append([title, subUrl, subHTML[0]])
        elif subHTML == [] and discardBlank == False:
            ret.append([title, subUrl, ""])
    return ret



myli = GetPageHTMLFromIndexPage("http://news.qq.com/", ".head > .Q-tpList .text .linkto", ".content-article, .Cnt-Main-Article-QQ", False)
for eachli in myli:
    print(eachli)
    print('\n')

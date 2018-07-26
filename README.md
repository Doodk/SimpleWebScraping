# Simple Web Scraping

A simple function for scraping web page for a website.

## Dependency: 

* requests
* BeautifulSoup(beautifulsoup4)
* lxml

#### To install:
    
    $ pip install requests
    $ pip install beautifulsoup4
    $ pip install lxml

## Usage:

    GetPageHTMLFromIndexPage(mainUrl, mainSelectorRule, subSelectorRule, discardBlank)
* **mainUrl**: The first web url, which contain url/title list for the articles
* **mainSelectorRule**: The CSS select rule, to specific the <a> tag position in the first web page
* **subSelectorRule**:The CSS select rule, to specific the content position in the articlesweb page
* **discardBlank** *[Default=False]*: Whether discard the null result from scraping the articles (this maycause by incorrect css selector, web page lazy load, etc.)<br>

#### Sample:

    GetPageHTMLFromIndexPage("http://news.qq.com/", ".head > .Q-tpList .text .linkto", ".content-article, .Cnt-Main-Article-QQ", False)

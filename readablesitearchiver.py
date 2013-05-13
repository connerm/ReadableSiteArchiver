#currently setup for BBC news, change article div and contense, more support for this soon

#modules
import urllib2
from bs4 import BeautifulSoup
import re

#writes urls and atricles sets to text (.txt) files
def write_out_files(urls, articles):
  #urls
  urls_out = open('urls.txt', 'a')
  for url in urls:
    urls_out.write(url + '\n')
  urls_out.close()
  #articles
  articles_out = open('articles.txt', 'a')
  for article in articles:
    articles_out.write(article + '\n')
  articles_out.close()

#creates the html page for each article link
#parses html and extracts article content
# creates html with just article title and paragraphs
def htmlfile(url):
  r = urllib2.urlopen(url)
  soup = BeautifulSoup(r)
  
  html = []
  #html- title, css (body width 960px)
  html.append('<html><head><title>'+soup.title.string+'</title><link rel="stylesheet" type="text/css" href="page.css"></head><body>')
  
  #parses for content only in article div - depends on site oblicously
  content =  soup.find('div', {'class': 'layout-block-a'})
  
  #gets hhtml paragraphs and h1 headings - should be alterd for websites style
  for text in content.find_all(['p', 'h1']):
    if text.name == 'p':
      html.append(str(text).decode("ascii", "ignore"))
    else:
      html.append(str(text).decode("ascii", "ignore"))
    
  html.append('</body></html>')
    
  # creates html files here
  out = open(soup.title.string+'.html', 'a')
  for line in html:
    out.write(line)
  out.close()

#finds what urls are considered articles - depends on the website url
def get_articles(urls, articles):
  print 'creating html files for...'
  for url in urls: 
    #match - ends with numbers (meaning an article)
    match = re.search(r'(\d+)$', url)
    if match:
      articles.add(url)
      print url
      htmlfile(url)
  
def main():
  
  #start urls - given starter urls in text file
  urls = set(open('urls.txt'))
  articles = set(open('articles.txt'))
  
  print 'crawling site for links'
  
  #parse of x links
  for i in range(3):
    #in each iteration, url is popped form the urls set,
    #then parsed for links
    #links are procressed, only keeping internal links
    urlstring = urls.pop()
    #fix for needed get method
    urls.add(urlstring)
    url = urllib2.urlopen(urlstring)
    html = BeautifulSoup(url)
    links = html.find_all('a')
    for link in links:
      link = (link.get('href'))
      #for internally refenerenced links - adds full http://...
      if link.startswith('/news/'):
	urls.add('http://www.bbc.co.uk' + link)
      if link.startswith('http://www.bbc.co.uk/news/'):
	urls.add(link)
	
  #method calls
  get_articles(urls, articles)
  
  write_out_files(urls, articles)
  
if __name__ == '__main__':
  main()
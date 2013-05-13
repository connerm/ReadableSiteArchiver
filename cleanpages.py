#module for parsing html and creating readable html docs

import urllib2
from bs4 import BeautifulSoup


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
  out.close(
  
if __name__ == '__main__':
  main()
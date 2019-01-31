import urllib.request
from bs4 import BeautifulSoup
url = input('Enter quizlet URL:')
print('Retrieving...')
html = urllib.request.urlopen(url).read()
html = BeautifulSoup(html,'html.parser')
container = html.findAll('div',{'class':'SetPageTerm-content'})
j=0
for i in container:
	j=j+1
	b = i.findAll(class_='TermText notranslate lang-en')
	print('Question',j,':',b[0].getText())
	print('Answer',j,':',b[1].getText())
	print()

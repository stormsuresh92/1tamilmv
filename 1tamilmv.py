from requests_html import HTMLSession
import pandas as pd

s = HTMLSession()

data = []
url = 'https://www.1tamilmv.cloud/'
r = s.get(url)
cont = r.html.find('ul > li.ipsWidget.ipsWidget_horizontal.ipsBox.ipsResponsive_block.ipsResponsive_hideTablet > div > p > strong')
for item in cont:
	try:
		ti = item.find('span', first=True).text.split(' (20')[-2]
		url = item.find('a', first=True).attrs['href']
		data.append([ti, url])
	except:
		pass
df = pd.DataFrame(data, columns=['movie','Url'])
df.to_csv('movie.csv', index=False)
		
	
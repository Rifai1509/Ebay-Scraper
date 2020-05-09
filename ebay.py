from requests import get
from bs4 import BeautifulSoup

html_requests = get('https://www.ebay.com/sch/i.html',
                    params={'_from':'R40', '_trksid':'m570.l1313', '_nkw':'iphone', '_sacat':'0'''})
soup = BeautifulSoup(html_requests.text, 'html.parser')

product = soup.find_all(attrs={'class': 's-item__wrapper clearfix'})
image = soup.find_all(attrs={'class': 's-item__image'})
for p in product:
    for img in image:
        print (img)
        print (p.find('img')['alt'])
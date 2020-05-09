import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def image():
    html_requests = requests.get('https://www.ebay.com/sch/i.html',
                                 params={'_from': 'R40', '_trksid': 'm570.l1313', '_nkw': 'iphone', '_sacat': '0'})
    soup = BeautifulSoup(html_requests.text, 'html.parser')
    product = soup.find_all(attrs={'class': 's-item__wrapper clearfix'})
    return render_template('image.html', semua=product)

@app.route('/nimage')
def nimage():
    html_requests = requests.get('https://www.ebay.com/sch/i.html',
                                 params={'_from': 'R40', '_trksid': 'm570.l1313', '_nkw': 'iphone', '_sacat': '0'})
    soup = BeautifulSoup(html_requests.text, 'html.parser')
    product = soup.find_all(attrs={'class': 's-item__wrapper clearfix'})
    return render_template('nimage.html', semua=product)

if __name__ == '__main__':
    app.run(debug=True)

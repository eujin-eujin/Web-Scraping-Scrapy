import scrapy
from bs4 import BeautifulSoup
from scrapy.exporters import CsvItemExporter
from scrapy import  Request
from ..items import ReviewItem
import re
class review_spider(scrapy.Spider):


    name = 'review'
    allowed_domains = ['amazon.in']
    domain = 'https://www.amazon.in'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }

    def start_requests(self):
        urls = ['https://www.amazon.in/Mini-UPS-Router-WiFi-12V/dp/B08HLZ28QC/ref=sr_1_1_sspa?crid=148WGJFXFNJ9S&keywords=oakter+mini+ups&qid=1676869787&sprefix=oakter+min+ups%2Caps%2C202&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1']
        for url in urls:
            yield  Request(url=url,headers=self.headers,callback=self.parse)

    def parse(self,response):
        soup = BeautifulSoup(response.text,'html.parser')
        # relative_link = soup.find('a',attrs={'data-hook':'see-all-reviews-link-foot'})['href']
        review_url = self.domain+soup.find('a',class_='a-link-emphasis a-text-bold')['href']
        yield Request(url=review_url,headers=self.headers,callback=self.parse_review)

    def parse_review(self,response):

        soup = BeautifulSoup(response.text,'lxml')
        reveiws = soup.find_all('div',class_='a-section celwidget')


        #extract some data

        for review in reveiws:
            try :
                user_name = review.find('span',class_='a-profile-name').text.strip()
            except:
                user_name = ''
            try:
                ratings = review.find('a',title=re.compile("out of")).text.strip()
            except:
                ratings = ''
            try:
                review_title = review.find('a', attrs={'data-hook': 'review-title'}).text.strip()
            except:
                review_title = ''
            try:
                review = review.find('span', attrs={'data-hook': 'review-body'}).text.strip()
            except:
                review = ''

            data = {
                'url' : response.url,
                'user name' :user_name,
                'ratings' : ratings,
                'review title' : review_title,
                'review' : review
            }


            yield data
            next_page = self.domain+soup.find('ul',class_='a-pagination').find_all('li')[-1].a['href']

            # yield data
            if next_page:
                yield Request(url=next_page,headers=self.headers,callback=self.parse_review)

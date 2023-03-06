# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ReviewItem(scrapy.Item):
    user_name = scrapy.Field()
    ratings = scrapy.Field()
    review_title = scrapy.Field()
    review = scrapy.Field()
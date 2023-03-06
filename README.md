# Amazon Reviews Scraper
This is a Scrapy project that scrapes reviews from an Amazon product page and saves the data in a CSV file.

### Requirements
To run this project, you need to have Python 3 and Scrapy library installed in your system.

### Installation
* create project using scrapy startproject ups_review
* Navigate to the project directory in your terminal or command prompt
* Run the command scrapy crawl review -o reviews.csv to start the spider and save the scraped data in a CSV file named reviews.csv.
### Project Details
The review_spider.py file contains the main code for scraping the reviews. The start_requests method sends a request to the specified URL and the parse method extracts the URL of the reviews page.

The parse_review method extracts the required data from each review on the page and yields it as a dictionary. It also follows the pagination links to scrape all the reviews on the product page.
The scraped data is saved in a CSV file using the command 'scrapy crawl review -o reviews.csv' 

## Usage
To use this project, you can modify the start_requests method to scrape reviews from a different Amazon product page. You can also modify the data you want to scrape from each review by changing the variables in the parse_review method.

Happy scraping!






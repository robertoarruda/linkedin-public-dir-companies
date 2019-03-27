import sys

from crawler import Crawler
from linkedin import LinkedIn
from scraper import Scraper
from time import sleep


class Main():
    __PROXIES = {}

    def __init__(self):
        self.linkedin = LinkedIn(proxies=self.__PROXIES)

        self.crawler = Crawler(linkedin=self.linkedin)
        self.scraper = Scraper(linkedin=self.linkedin)

    def crawl_companies(self, letter='a', page=1, sub_page=1):
        crawler = main.crawler.get_crawler()
        if not crawler:
            crawler = {'letter': 'a', 'page': 1, 'sub_page': 1}

        self.__try_letter(crawler['letter'],
                          crawler['page'], crawler['sub_page'])

    def __try_letter(self, letter, page, sub_page):
        while ord(letter) < 122:
            self.__try_page(letter, page, sub_page)
            letter = chr(ord(letter) + 1)
            page = 1
            sub_page = 1

    def __try_page(self, letter, page, sub_page):
        while page:
            self.__try_sub_page(letter, page, sub_page)
            page += 1
            sub_page = 1

    def __try_sub_page(self, letter, page, sub_page):
        while sub_page:
            try:
                companies = self.crawler.companies(letter, page, sub_page)
            except Exception as exception:
                if len(exception.args) > 1:
                    if exception.args[1]['response'].status_code == 404:
                        break

                    print(exception.args[1]['response'])

                raise exception

            for company in companies:
                print(company['linkedin'])

            print(f'letter: {letter}', f'page: {page}',
                  f'sub_page: {sub_page}')

            sub_page += 1
            # sleep(1)

    def scrape_company(self):
        while True:
            current = self.scraper.get_next_company()
            if not current:
                return False

            company = self.scraper.company(current['linkedin'])
            company.pop('raw_scraper', None)
            print(company, "\n")
            # sleep(1)


main = Main()

if len(sys.argv) <= 1:
    print('Please tell us what you want to run ("scraper" or "crawler").')
    raise SystemExit

if sys.argv[1] == 'crawler':
    main.crawl_companies()

if sys.argv[1] == 'scraper':
    main.scrape_company()

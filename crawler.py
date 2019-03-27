from companies_collection import CompaniesCollection
from company_directory_interface import CompanyDirectoryInterface
from crawlers_collection import CrawlersCollection
from time import sleep


class Crawler():
    def __init__(self, linkedin):
        self.linkedin = linkedin
        self.db = {'companies': CompaniesCollection(),
                   'crawlers': CrawlersCollection()}

    def companies(self, letter, page, sub_page, retrying=False):
        try:
            data = self.linkedin.companies_directory(
                letter, page=page, sub_page=sub_page)
        except Exception as exception:
            if retrying:
                raise exception

            self.linkedin.refresh_cookies()
            sleep(2)
            return self.companies(letter, page=page, sub_page=sub_page,
                                  retrying=True)

        interface = CompanyDirectoryInterface(data)
        companies = interface.extract()

        self.save_companies(companies)
        self.__update_crawler(letter, page, sub_page)

        return companies

    def save_companies(self, companies):
        for company in companies:
            company['linkedin'] = company['linkedin'].strip('/')
            if self.db['companies'].find_by_linkedin(company['linkedin']):
                return False

            self.db['companies'].insert(company)

        return True

    def get_crawler(self):
        return self.db['crawlers'].last()

    def __update_crawler(self, letter, page, sub_page):
        return self.db['crawlers'].update(letter=letter, page=page,
                                          sub_page=sub_page)

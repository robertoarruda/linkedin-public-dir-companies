from companies_collection import CompaniesCollection
from company_page_interface import CompanyPageInterface
from scrapers_collection import ScrapersCollection
from time import sleep


class Scraper():
    def __init__(self, linkedin):
        self.linkedin = linkedin
        self.db = {'companies': CompaniesCollection(),
                   'scrapers': ScrapersCollection()}

    def company(self, company='intexfy', retrying=False):
        try:
            data = self.linkedin.company_page(company)
        except Exception as exception:
            if retrying:
                raise exception

            self.linkedin.refresh_cookies()
            sleep(2)
            return self.company(company, retrying=True)

        interface = CompanyPageInterface(data)
        company = interface.extract()

        self.save_company(company)
        self.__update_scraper(company)

        return company

    def save_company(self, company):
        return self.db['companies'].update(company)

    def get_next_company(self):
        scraper = self.db['scrapers'].last()
        if not scraper:
            return self.db['companies'].first()

        return self.db['companies'].get_next(scraper['current']['linkedin'])

    def __update_scraper(self, linkedin):
        return self.db['scrapers'].update(linkedin)

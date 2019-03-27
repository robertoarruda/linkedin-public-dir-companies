from bs4 import BeautifulSoup


class CompanyDirectoryInterface():
    def __init__(self, html=''):
        self.html = html
        self.soup = BeautifulSoup(html, 'html.parser')

    def extract(self):
        companies_list = self.soup.find('ul', {'class': 'column dual-column'})
        links = companies_list.findChildren('li', recursive=False)

        data = []
        for link in links:
            linkedin = link.a['href'].split('?')[0]
            linkedin = linkedin.split('/')[-1]
            data.append({'linkedin': linkedin, 'raw_crawler': self.html})

        return data

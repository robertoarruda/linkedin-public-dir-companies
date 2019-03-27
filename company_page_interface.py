from bs4 import BeautifulSoup


class CompanyPageInterface():
    __INDEXES = {'name': 'name',
                 'sector': 'sector',
                 'Sobre nós': 'about_us',
                 'Site': 'website',
                 'Sede': 'headquarters',
                 'Ano de fundação': 'year_founded',
                 'Tipo de empresa': 'company_type',
                 'Tamanho': 'size',
                 'Especializações': 'specialties',
                 'linkedin': 'linkedin',
                 'employees': 'employees',
                 'raw_scraper': 'raw_scraper'}

    def __init__(self, html=''):
        self.html = html
        self.soup = BeautifulSoup(html, 'html.parser')

    def extract(self):
        title = self.soup.find('h1', {'class': 'top-card__title'})
        sector = self.soup.find(
            'span', {'class': 'top-card__information-text'})
        linkedin = self.soup.find('link', {'rel': 'canonical'})
        linkedin = linkedin['href'].split('?')[0].split('/')[-1]

        data = {'name': title.text.strip(),
                'sector': sector.text.strip(),
                **self.__extract_about_us_box(),
                'linkedin': linkedin,
                'employees': self.__extract_employees_box(),
                'raw_scraper': self.html}

        return self.__normalize_company_data(data)

    def __extract_about_us_box(self):
        data = {}
        elements = self.soup\
            .find('div', {'class': 'about__primary-content'})

        if not elements:
            return data

        for elem in elements:
            current_class = elem['class']
            header_class = ['about__header', 'about__detail-header']

            if not [True for value in current_class if value in header_class]:
                continue

            data[elem.text.strip()] = elem.nextSibling.text.strip()

        return data

    def __extract_employees_box(self):
        data = []
        employees = self.soup.select('li.mini-profile--employees')

        for employee in employees:
            section = employee.findChildren('section', recursive=False)[0]
            linkedin = employee.findChildren('a')[0]['href'].split('?')[0]
            linkedin = linkedin.split('/')[-1]

            data.append({'name': section.findChildren('h3')[0].text,
                         'position': section.findChildren('h4')[0].text,
                         'linkedin': linkedin})

        return data

    def __normalize_company_data(self, data):
        data = self.__translate_indexes(data)
        data = {k.replace(' ', '_').lower(): v for k, v in data.items()}

        data = {'name': '',
                'sector': '',
                'about_us': '',
                'website': '',
                'headquarters': '',
                'year_founded': '',
                'company_type': '',
                'size': '',
                'specialties': '',
                'linkedin': '',
                'employees': [],
                **data}

        data['specialties'] = data['specialties'].split(', ')

        return data

    def __translate_indexes(self, data):
        translated = {}

        for index in self.__INDEXES:
            if not index in data:
                continue

            translated[self.__INDEXES[index]] = data[index]

        return translated

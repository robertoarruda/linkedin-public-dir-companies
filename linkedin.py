import htmlmin
import requests

from http.cookiejar import LWPCookieJar


class LinkedIn():

    __URL = 'https://www.linkedin.com'

    __HEADERS = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=\
    0.9,image/webp,image/apng,*/*;q=0.8',
                 'Accept-Encoding': 'gzip, deflate, br',
                 'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
                 'Cache-Control': 'no-cache',
                 'Pragma': 'no-cache',
                 'Referer': 'https://www.linkedin.com/',
                 'Upgrade-Insecure-Requests': '1',
                 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53\
7.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}

    def __init__(self, proxies={}, cookie_file='cookiejar'):
        self.__session = requests.Session()
        self.__cookie_file = cookie_file
        self.setProxies(proxies)
        self.__save_cookies(reset=True)

    def __save_cookies(self, reset=False):
        if reset:
            self.__session.cookies = LWPCookieJar(self.__cookie_file)

        self.__session.cookies.save(ignore_discard=True)

    def __load_cookies(self):
        self.__session.cookies.load(ignore_discard=True)

    def setProxies(self, proxies):
        protocols = ['http', 'https', 'socks4', 'socks5']

        filtered = {}
        for proxy in proxies:
            if proxy in protocols:
                filtered[proxy] = proxies[proxy]

        self.__proxies = filtered

        return self.__proxies

    def __request(self, uri='', proxies={}):
        self.__load_cookies()
        response = self.__session.get(self.__URL+uri,
                                      headers=self.__HEADERS, proxies=proxies)
        self.__save_cookies()

        if response.status_code != requests.codes.ok:
            raise Exception(f'[{response.status_code}] {response.reason}',
                            {'response': response})

        return htmlmin.minify(response.text, remove_empty_space=True)

    def refresh_cookies(self):
        print('Refreshing cookies...')
        self.__save_cookies(reset=True)

        return self.__request('/', proxies=self.__proxies)

    def companies_directory(self, letter, page, sub_page):
        return self.__request(f'/directory/companies-{letter}-{page}-\
{sub_page}/', proxies=self.__proxies)

    def company_page(self, company):
        return self.__request('/company/'+company, proxies=self.__proxies)

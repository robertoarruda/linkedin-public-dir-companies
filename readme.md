# [Crawler + Scraper] LinkedIn Companies Public Directory

## Prerequisites
- Python 3.7 `sudo apt-get install python3.7`
- Pip `sudo apt-get install python3-pip`
- VirtualEnv `sudo pip3 install virtualenv`
- MongoDB with collections `linkedin_companies`,` linkedin_crawlers` and `linkedin_scrapers`
- Writing permission in the app directory to save cookies

## Considerations
To run the crawler and scraper scalably, you will need to use a residential proxies server.

## Installation

### Clone the project:
```
git clone git@github.com:robertoarruda/linkedin_companies.git
```

### Enter the project directory:
```
cd ./linkedin_companies
```

### Create the Environment:
Within the project root, run the command below:
```
virtualenv venv --python=python3.7
```

### Activate the environment:
Run the command below to enable:
```
source venv/bin/activate
```

### Install dependencies:
Run the command below to install the project dependencies:
```
pip install -r requirements.txt
```

### Configure MongoDB
Enter the connection settings with the database in the [client_db.py](client_db.py#L6) file.
```
class ClientDB():
    __MONGO = 'mongodb://root:123456@127.0.0.1:80'
```

### [Opcional step] Setting residential proxy
Enter the host of your home proxies server in the [main.py](main.py#L10) file.
```
class Main():
    __PROXIES = {
        'http': 'http://127.0.0.1:80'
    }
```

### Execute the crawler:
Execute the command below to run the crawler:
```
python main.py crawler
```
The crawler data is saved in the `linkedin_crawlers` collection. The crawled companies are saved in the `linkedin_companies` collection.

### Execute the scraper:
Execute the command below to run the scraper:
```
python main.py scraper
```
The scraper data is saved in the `linkedin_scrapers` collection. The scraped companies are updated in the collection `linkedin_companies`.

### Turn off the environment:
Execute the command below to deactivate:
```
deactivate
```

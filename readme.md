# Search API

## Pré-requisitos
- Python 3.7 `sudo apt-get install python3.7`
- Pip `sudo apt-get install python3-pip`
- VirtualEnv `sudo pip3 install virtualenv`
- MongoDB com as collections `linkedin_companies`, `linkedin_crawlers` e `linkedin_scrapers`
- Permissão de escrita no diretório do app para gravação dos cookies

## Considerações
Para executar o crawler e o scraper de forma escalável, será necessário o uso de um servidor de proxies residenciais.

## Instalação

### Clone o projeto:
```
git clone git@github.com:robertoarruda/linkedin_companies.git
```

### Entre no diretório do projeto:
```
cd ./linkedin_companies
```

### Crie o ambiente:
Dentro da raiz do projeto, execute o comando abaixo:
```
virtualenv venv --python=python3.7
```

### Ative o ambiente:
Execute o comando abaixo para ativar:
```
source venv/bin/activate
```

### Instale as dependencias:
Execute o comando abaixo para instalar as dependencias do projeto:
```
pip install -r requirements.txt
```

### Configure o MongoDB
Insira as configs de conexão com o banco
[client_db.py](client_db.py:6)

### Execute o crawler:
Execute o comando abaixo para rodar o crawler:
```
python main.py crawler
```
Os dados do crawler é salvo na collection `linkedin_crawlers`. As empresas crawleadas são salvas na collection `linkedin_companies`.

### Execute o scraper:
Execute o comando abaixo para rodar o scraper:
```
python main.py scraper
```
Os dados do scraper é salvo na collection `linkedin_scrapers`. As empresas scrapadas são salvas na collection `linkedin_companies`.

### Desative o ambiente:
Execute o comando abaixo para desativar:
```
deactivate
```
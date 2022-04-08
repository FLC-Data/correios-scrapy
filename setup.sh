pip install poetry==1.2.0a2
poetry install
git config --global http.sslverify "false"
poetry run pre-commit install
cd correios_cep
echo Iniciando o Spider
poetry run scrapy crawl correios
mkdir ../data
mv output.json ..data/

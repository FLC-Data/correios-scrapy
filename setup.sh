pip install poetry==1.2.0a2
poetry install
git config --global http.sslverify "false"
poetry run pre-commit install

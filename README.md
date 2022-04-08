# Correios Cep Scrapy

Esse repositório contém o spider para realizar coleta de dados pertinentes ao intervalo de ceps por UF do Correios.

## Requisitos

- [poetry](https://pypi.org/project/poetry/1.2.0a2/)

## Instalando Dependências

```shell
poetry install -vv
```

## Ativando Ambiente virtual do Python (venv)

```shell
poetry env use python
```

### Instalando pre-commit

```shell
git config --global http.sslverify "false" && \
poetry run pre-commit install
```

- Padronização de branches de desenvolvimento: release, feature, bugfix, hotfix

## Existe um auto setup para facilitar no setup do ambiente de desenvolvimento

- Ao Clonar o Repositório rode o seguinte comando no terminal:
  - Terminal bash: `. setup.sh`
  - Terminal windows: `bash --rcfile setup.sh`

## Rodando o Crawler

Para rodar o crawler precisa estar no diretório `./correios_cep/`

```shell
poetry run scrapy crawl correios
```

O output será registrado no diretório `data/` com o nome de `output.jsonl`

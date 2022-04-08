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
pre-commit install
```

## Existe um auto setup para facilitar no setup do ambiente de desenvolvimento

- Ao Clonar o Repositório rode o seguinte comando no terminal:
  - Terminal bash: `. setup.sh`
  - Terminal windows: `bash --rcfile setup.sh`

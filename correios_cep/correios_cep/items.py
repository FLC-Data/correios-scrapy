# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import hashlib

import scrapy
from itemloaders.processors import TakeFirst
from utils import normalize


class CorreiosLoader(scrapy.ItemLoader):
    default_output_processor = TakeFirst()

    def add_fields(self, fields):
        uf, localidade, faixa_de_cep, situacao, tipo_de_faixa = fields
        id = hashlib.sha256(''.join(fields[1:]).encode('utf-8'))
        id = id.hexdigest()
        self.add_value('id', id)
        self.add_value('uf', uf)
        self.add_value('localidade', normalize(localidade))
        self.add_value('faixa_de_cep', normalize(faixa_de_cep))
        self.add_value('situacao', normalize(situacao))
        self.add_value('tipo_de_faixa', normalize(tipo_de_faixa))
        pass


class CorreiosItem(scrapy.Item):
    id = scrapy.Field()
    uf = scrapy.Field()
    localidade = scrapy.Field()
    faixa_de_cep = scrapy.Field()
    situacao = scrapy.Field()
    tipo_de_faixa = scrapy.Field()
    pass

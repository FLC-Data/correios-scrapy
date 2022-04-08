import scrapy
# from correios.items import CorreiosLoader, CorreiosItem


class CorreiosSpider(scrapy.Spider):
    name = 'correios'
    start_urls = [
        'https://www2.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm'
    ]

    def parse(self, response):
        array_uf = response.xpath('//select[@class="f1col"]/option[not(contains(text(), "\r"))]//text()').getall()

        for uf in array_uf:

            formdata = {
                'UF': uf,
                'qtdrow': '100'
            }

            cb_kwargs = {
                'uf': uf
            }

            yield scrapy.FormRequest.from_response(
                response,
                formdata=formdata,
                cb_kwargs=cb_kwargs,
                callback=self.parse_content
            )

    def parse_content(self, response, uf):
        print(uf)
        pass

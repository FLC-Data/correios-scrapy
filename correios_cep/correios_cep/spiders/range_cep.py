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
        last_row = response.xpath('//div[@class="ctrlcontent"]/text()').re(r"\r\xa0\xa01 a 100 de (\d*)")
        last_row = 1 if not last_row else int(last_row[0])//100 + 1

        for page in range(1, last_row+1):
            if page == 1:
                for row in response.xpath('//table[@class="tmptabela"][last()]//tr'):
                    # Precisa Criar o item e o itemLoader >> TASK 8
                    print('row')
                pass
            else:
                pass
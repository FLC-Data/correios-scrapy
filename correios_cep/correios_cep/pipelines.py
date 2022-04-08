# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import os

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DeleteOutputPipeline:

    def open_spider(self, spider):
        try:
            os.remove("output.jsonl")
        except OSError as e:
            pass


class DuplicatesPipeline(object):
    def __init__(self):
        self.ids = set()

    def process_item(self, item, spider):
        if item['id'] in self.ids:
            raise DropItem(f"Duplicate item found: {item}")
        else:
            self.ids.add(item['id'])
            return item

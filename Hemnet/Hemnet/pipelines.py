# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class HemnetPipeline(object):
    # 构造方法
    def __init__(self):
        self.fp = None  # 定义一个文件描述符属性

    #开启爬虫，只执行一次
    def open_spider(self, spider):
        print('爬虫开始')
        self.fp = open('./data.csv', 'w' ,encoding='utf-8') #创建文件

    def process_item(self, item, spider):
        print(item['sale_names'])
        self.fp.write(item['sale_names']) #写入数据
        return item

    #结束爬虫，只执行一次
    def close_spider(self, spider):
        self.fp.close()
        print('爬虫结束')
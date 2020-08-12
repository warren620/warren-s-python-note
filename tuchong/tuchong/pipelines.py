# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import scrapy

class TuchongPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['url'])

    # 指定图片存储的路径
    def file_path(self, request, response=None, info=None):
        imgName = request.url.split('/')[-1]+'.jpg'
        return imgName

    def item_completed(self, results, item, info):
        return item  # 返回给下一个即将被执行的管道类
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymysql
import settings

class MeiciPipeline(object):
    def process_item(self, item, spider):
        return item

class WebcrawlerScrapyPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host=settings.MYSQL_HOST,
            db=settings.MYSQL_DBNAME,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True)
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        print item['meiciid']
        self.cursor.execute("""select meiciid from goods where meiciid = %s;""", item['meiciid'])

        ret = self.cursor.fetchone()


        if not ret:
            self.cursor.execute(
                """insert into goods(brand,productitle,price,color,
                szie,proimg,prodata,brandstory,brandimg,meiciid) 
                values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);""",
                (item['brand'],
                 item['productitle'],
                 item['price'],
                 item['color'],
                 item['szie'],
                 item['proimg'],
                 item['prodata'],
                 item['brandstory'],
                 item['brandimg'],
                 item['meiciid']))
            self.connect.commit()
            print "商品保存成功"
        else:
            pass


# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

from ximalaya.settings import MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT, MYSQL_DATABASE


class XimalayaPipeline(object):
    def process_item(self, item, spider):
        return item


class MySQLPipline():

    def __init__(self, user, password, host, port, database):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            database=MYSQL_DATABASE
        )

    def open_spider(self, spider):
        # 获取连接和游标
        self.conn = pymysql.Connection(user=self.user, password=self.password,
                                       host=self.host, port=self.port,
                                       database=self.database)
        self.cursor = self.conn.cursor()

    def close_spider(self, spider):
        # 关闭数据库连接
        self.conn.close()

    def process_item(self, item, spider):

            # 保存数据到mysql中
        sql0 = f'select id from ximalaya where book_name="{item["title"]}";'
        self.cursor.execute(sql0)
        book_cunzai = self.cursor.fetchone()
        if book_cunzai==None:

            sql1 = f'insert into ximalaya (book_name, book_zhubo,book_href) ' \
                f'values ("{item["title"]}", "{item["zhubo"]}","{item["detail_href"]}")'
            self.cursor.execute(sql1)
            self.conn.commit()

        # 查询当前保存的漫画的id值
        sql3 = f'select id from ximalaya where book_name="{item["title"]}";'
        self.cursor.execute(sql3)
        books_id = self.cursor.fetchone()[0]

        # 插入漫画章节内容
        for data in item['chapter']:
            sql2 = f'insert into book_chapter (chapter_title, metia_href, book_id)' \
                f' values ("{data["title"]}", "{data["metia_href"]}", {books_id})'
            self.cursor.execute(sql2)
            self.conn.commit()

        return item
from sqlalchemy import Column, BigInteger, Integer, String, Text, DateTime

from orm import CrawlerBase


class CrawlProduct(CrawlerBase):

    __tablename__ = 'crawl_product'

    id = Column(BigInteger, primary_key=True)
    product_code = Column(String)
    group_id = Column(String)
    spider_name = Column(String)
    url = Column(String)
    name = Column(String)
    color = Column(String)
    brand = Column(String)
    description = Column(String)
    breadcrumb = Column(String)
    more_info = Column(Text)
    detail_images = Column(String)
    original_images = Column(String)
    display_image = Column(String)
    price = Column(Integer)
    discount_price = Column(Integer)
    currency_unit = Column(String)
    create_time = Column(DateTime)

    def save(self, session):

        session.add(self)

    def __repr__(self):

        return f'<CrawlProduct(id={self.id})>'

    @classmethod
    def get_by_id(cls, crawl_id, session):

        return session.query(cls).filter(cls.id == int(crawl_id)).one()

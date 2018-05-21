from sqlalchemy.dialects.mysql import BIT
from sqlalchemy import Column, Integer, String, Boolean

from orm import OfflineFlowBase


class ProductIdentification(OfflineFlowBase):

    __tablename__ = 'product_identification'

    id = Column(Integer, primary_key=True, autoincrement=True)
    crawl_id = Column(Integer)
    group_id = Column(String)
    product_code = Column(String)
    merchant_id = Column(Integer)
    brand_id = Column(Integer)
    site_mark = Column(String)
    cloth_id = Column(Integer)
    is_ready = Column(Boolean)
    is_ocb = Column(BIT)

    def save(self, session):

        session.add(self)

    def __repr__(self):

        return '<ProductIdentification(crawl_id=%r, product_code="%s")>' % (self.crawl_id, self.product_code)

    @classmethod
    def get_by_id(cls, product_id, session):

        return session.query(cls).filter(cls.id == int(product_id)).one()

    @classmethod
    def get_by_crawl_id(cls, crawl_id, session):

        return session.query(cls).filter(cls.crawl_id == int(crawl_id)).first()


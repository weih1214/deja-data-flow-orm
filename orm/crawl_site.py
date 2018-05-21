from sqlalchemy import Column, Integer, BigInteger, String
from sqlalchemy.dialects.mysql import BIT

from orm import CrawlerBase


class CrawlSite(CrawlerBase):

    __tablename__ = 'crawl_site'

    id = Column(BigInteger, primary_key=True)
    brand_id = Column(Integer)
    brand_name = Column(String)
    site_mark = Column(String)
    is_ocb = Column(BIT)

    def __repr__(self):

        return f'<CrawlSite(site_mark={self.site_mark})>'

    @classmethod
    def get_by_site_mark(cls, site_mark, session):

        return session.query(cls).filter(cls.site_mark == site_mark).one()

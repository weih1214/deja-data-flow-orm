from sqlalchemy import Column, Integer, BigInteger, String

from orm import OfflineFlowBase


class ProductTags(OfflineFlowBase):

    NO_PATTERN_THRESHOLD = 0.68
    PATTERN_THRESHOLD = 0.73

    __tablename__ = 'product_tags'

    id = Column(BigInteger, primary_key=True)
    category = Column(Integer)
    sub_category = Column(Integer)
    color = Column(Integer)
    pattern = Column(Integer)
    length = Column(Integer)
    sleeve_length = Column(Integer)
    neckline = Column(Integer)
    autotag_version = Column(Integer)
    autotag_version_desc = Column(String)

    @property
    def pattern_threshold(self):
        if self.pattern == 0:
            return self.NO_PATTERN_THRESHOLD ** 2
        return self.PATTERN_THRESHOLD ** 2

    def save(self, session):
        session.add(self)

    def __repr__(self):
        return f'<ProductTags(id={self.id})>'

    @classmethod
    def get_by_id(cls, product_id, session):
        return session.query(cls).filter(cls.id == product_id).first()

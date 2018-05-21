from sqlalchemy import Integer, Column, String, Text
from sqlalchemy.orm import relationship

from orm import OfflineFlowBase
from orm.product_identification import ProductIdentification


class ProductBasic(OfflineFlowBase):

    __tablename__ = 'product_basic'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    shop_url = Column(String)
    color = Column(String)
    breadcrumb = Column(String)
    description = Column(String)
    detail_description = Column(Text)
    display_image = Column(String)
    original_price = Column(Integer)
    current_price = Column(Integer)
    currency = Column(String)
    all_images = Column(String)

    product_identification = relationship(ProductIdentification, foreign_keys=[id],
                                          primaryjoin='ProductBasic.id == ProductIdentification.id')

    def save(self, session):

        session.add(self)

    def __repr__(self):

        return '<ProductBasic(id=%r, name="%s")>' % (self.id, self.name)

    @classmethod
    def get_by_id(cls, product_id, session):

        return session.query(cls).filter(cls.id == int(product_id)).first()

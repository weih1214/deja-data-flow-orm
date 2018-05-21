from sqlalchemy import Column, BigInteger, Text

from orm import OfflineFlowBase


class ProductFeatures(OfflineFlowBase):

    __tablename__ = 'product_features'

    id = Column(BigInteger, primary_key=True)
    max_area_image_feature = Column(Text)

    def save(self, session):

        session.add(self)

    def __repr__(self):

        return f'<ProductFeatures(id={self.id})>'

    @classmethod
    def get_by_id(cls, product_id, session):

        return session.query(cls).filter(cls.id == int(product_id)).first()

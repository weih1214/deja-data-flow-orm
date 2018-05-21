from sqlalchemy import Column, BigInteger, Text

from orm import OfflineFlowBase


class ProductImageFeature(OfflineFlowBase):

    __tablename__ = 'product_image_feature'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    image_id = Column(BigInteger)
    feature = Column(Text)
    feature_version = Column(BigInteger)

    def save(self, session):

        session.add(self)

    def delete(self, session):

        session.delete(self)

    def __repr__(self):

        return f'<ProductImageFeature(id={self.id}, iamge_id={self.image_id})>'

    @classmethod
    def get_by_image_ids(cls, image_ids, session):

        return session.query(cls).filter(cls.image_id.in_(image_ids)).all()

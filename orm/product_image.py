from sqlalchemy import Integer, Column, String

from orm import OfflineFlowBase


class ProductImage(OfflineFlowBase):

    __tablename__ = 'product_image'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer)
    phash = Column(String)
    origin_url = Column(String)
    local_path = Column(String)
    attribute = Column(String, default='')
    width = Column(Integer)
    height = Column(Integer)
    autotag_bbox = Column(String, default='')
    parsed_path = Column(String, default='')
    parsed_area = Column(Integer, default=0)

    def save(self, session):

        session.add(self)

    def delete(self, session):

        session.delete(self)

    def __repr__(self):

        return '<ProductImage(product_id="%r", phash="%s")>' % (self.product_id, self.phash)

    @classmethod
    def get_by_product_id_and_p_hash(cls, product_id, p_hash, session):

        return session.query(cls).filter(cls.product_id == product_id).filter(cls.phash == p_hash).first()

    @classmethod
    def get_by_product_id(cls, product_id, session):

        return session.query(cls).filter(cls.product_id == product_id).all()

    @classmethod
    def get_by_ids(cls, image_ids, session):

        return session.query(cls).filter(cls.id.in_(image_ids)).all()

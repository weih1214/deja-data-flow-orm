import sqlalchemy as sa

from orm import OfflineFlowBase


class PSRelation(OfflineFlowBase):

    __tablename__ = 'ps_relation'

    id = sa.Column('id', sa.BigInteger, primary_key=True, autoincrement=True)
    product_id = sa.Column('product_id', sa.BigInteger)
    street_analysis_id = sa.Column('street_analysis_id', sa.BigInteger)
    sub_category = sa.Column('sub_category', sa.Integer)
    is_online_purchasable = sa.Column('is_online_purchasable', sa.Boolean)
    street_type = sa.Column('street_type', sa.Integer)
    street_image_path = sa.Column('street_image_path', sa.String(200))
    street_item_id = sa.Column('street_item_id', sa.BigInteger)
    distance = sa.Column('distance', sa.Float)

    def save(self, session):

        session.add(self)

    @classmethod
    def __rec_generator_by_product_id(cls, product_id, session):

        yield from session.query(cls).filter(cls.product_id == product_id).yield_per(100)

    @classmethod
    def get_by_product_id(cls, product_id, session):

        return list(cls.__rec_generator_by_product_id(product_id, session))

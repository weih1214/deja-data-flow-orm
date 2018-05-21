from typing import List, Type

from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import relationship

from orm import OfflineFlowBase
from orm.product_inventory_metadata import ProductInventoryMetadata
from orm.product_tags import ProductTags


class ProductFeature(OfflineFlowBase):
    __tablename__ = 'product_features'

    id = Column(Integer, primary_key=True)
    max_area_image_feature = Column(Text)

    product_tag = relationship(ProductTags, foreign_keys=[id], primaryjoin='ProductFeature.id == ProductTags.id')

    def __repr__(self):
        return '<ProductImageFeature(id=%d)>' % self.id

    @classmethod
    def get_by_id(cls, id, session) -> Type['ProductFeature']:
        result = session.query(cls).filter_by(id=id).first()
        return result

    @classmethod
    def get_records_by_sub_category_ocb(cls, sub_category, session) -> List['ProductFeature']:
        sub_category_sq = session.query(ProductTags.id).filter_by(sub_category=sub_category).subquery()
        ocb_sq = session.query(ProductInventoryMetadata.id).subquery()
        result = session.query(cls) \
            .filter(cls.id.in_(sub_category_sq)) \
            .filter(cls.id.in_(ocb_sq)) \
            .all()
        return result

    @classmethod
    def get_records_by_sub_category(cls, sub_category, session) -> List['ProductFeature']:
        sub_category_sq = session.query(ProductTags.id).filter_by(sub_category=sub_category).subquery()
        result = session.query(cls) \
            .filter(cls.id.in_(sub_category_sq)) \
            .all()
        return result

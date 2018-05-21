from sqlalchemy import Column, Integer, DateTime, String, Text

from deja_orm import OfflineFlowBase


class ProductTagOld(OfflineFlowBase):
    __tablename__ = 'product_tags_old'

    id = Column(Integer, primary_key=True)
    category = Column(Integer)
    sub_category = Column(Integer)
    color = Column(Integer)
    pattern = Column(Integer)
    length = Column(Integer)
    sleeve_length = Column(Integer)
    neckline = Column(Integer)
    autotag_version = Column(Integer)
    autotag_version_desc = Column(String)
    max_area_image_feature = Column(Text)
    add_on = Column(DateTime)
    last_update_on = Column(DateTime)

    def __repr__(self):
        return "<ProductTag(id=%id)>" % self.id

    @classmethod
    def get_feature_by_id_list(cls, session, sub_category):
        sq = session.query(cls.id).filter_by(sub_category=sub_category).subquery()
        result = session.query(cls.max_area_image_feature).filter(cls.id.in_(sq)).all()
        return result

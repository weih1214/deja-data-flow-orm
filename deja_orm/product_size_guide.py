import json

from sqlalchemy import Column, Integer, Text

from deja_orm import OfflineFlowBase


class ProductSizeGuide(OfflineFlowBase):

    __tablename__ = 'product_size_guide'

    id = Column(Integer, primary_key=True)
    size_guide_table = Column(Text)
    size_guide_description = Column(Text)

    @classmethod
    def insert_new_record(cls, id, size_guide_table, size_guide_description, session):
        existing_record = session.query(cls).filter_by(id=id).first()
        if existing_record is None:
            new_record = cls(id=id,
                             size_guide_table=json.dumps(size_guide_table),
                             size_guide_description=size_guide_description)
            session.add(new_record)
        return

    @classmethod
    def check_existence(cls, id, session):
        existing_record = session.query(cls).filter_by(id=id).first()
        if existing_record is None:
            return False
        return True
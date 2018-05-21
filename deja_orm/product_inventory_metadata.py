from sqlalchemy import Integer, Column, String, DateTime, func

from deja_orm import OfflineFlowBase


class ProductInventoryMetadata(OfflineFlowBase):

    __tablename__ = 'product_inventory_metadata'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    merchant_id = Column(Integer)
    site_mark = Column(String)
    product_code = Column(String)
    shop_url = Column(String)
    color = Column(String)
    add_on = Column(DateTime, default=func.current_timestamp())
    last_update_on = Column(DateTime, default=func.current_timestamp())

    def __repr__(self):
        return '<ProductInventoryMetadata(id=%d)>' % self.id

    @classmethod
    def insert_or_update_record(cls, session, instance:'ProductInventoryMetadata'):
        existing_record = session.query(cls).filter_by(id=instance.id).first()
        if existing_record is None:
            session.add(instance)
        else:
            update_dict = instance.to_dict()
            del update_dict['id']
            session.query(cls).filter_by(id=instance.id).update(update_dict)

    def to_dict(self):
        result = {k:v for k, v in self.__dict__.items() if not k.startswith('_')}
        return result

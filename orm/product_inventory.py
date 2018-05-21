import json

from sqlalchemy import Integer, Column, Text, Boolean, DateTime, func

from orm import OfflineFlowBase


class ProductInventory(OfflineFlowBase):
    __tablename__ = 'product_inventory'

    id = Column(Integer, primary_key=True)
    inventory_list = Column(Text, nullable=False)
    is_purchasable = Column(Boolean, default=False)
    last_update_on = Column(DateTime, default=func.current_timestamp())

    @classmethod
    def insert_or_update_record(cls, id, inventory_list, is_purchasable, session):
        existing_record = session.query(cls).filter_by(id=id).first()
        if existing_record is None:
            new_record = cls(id=id, inventory_list=json.dumps(inventory_list), is_purchasable=is_purchasable)
            session.add(new_record)
        else:
            existing_record.inventory_list = json.dumps(inventory_list)
            existing_record.is_purchasable = is_purchasable
            existing_record.last_update_on = func.current_timestamp()
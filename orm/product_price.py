from sqlalchemy import Column, Integer, DateTime, func

from orm import OfflineFlowBase


class ProductPrice(OfflineFlowBase):
    __tablename__ = 'product_price'

    id = Column(Integer, primary_key=True)
    original_price = Column(Integer)
    current_price = Column(Integer)
    add_on = Column(DateTime, default=func.current_timestamp())
    last_update_on = Column(DateTime, default=func.current_timestamp())


    def __repr__(self):
        return '<ProductPrice(id=%d, original_price=%d, current_price=%d)>' % (
        self.id, self.original_price, self.current_price)

    @classmethod
    def insert_or_update_record(cls, id, original_price, current_price, session):
        existing_record = session.query(cls).filter_by(id=id).first()
        if existing_record is None:
            new_record = cls(id=id, original_price=original_price, current_price=current_price)
            session.add(new_record)
        else:
            existing_record.original_price = original_price
            existing_record.current_price = current_price
            existing_record.last_update_on = func.current_timestamp()
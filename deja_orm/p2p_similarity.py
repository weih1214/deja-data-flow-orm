from sqlalchemy import Column, Integer, Text, DateTime, func

from deja_orm import OfflineFlowBase


class P2PSimilarity(OfflineFlowBase):
    __tablename__ = 'p2p_relation'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    similarity_result = Column(Text, nullable=False)
    add_on = Column(DateTime, default=func.current_timestamp())
    last_update_on = Column(DateTime, default=func.current_timestamp())

    def __repr__(self):
        return "<P2PSimilarity(id=%d)>" % self.id

    @classmethod
    def insert_or_update_record(cls, session, id, similarity_result: str):
        existing_record = session.query(cls).filter_by(id=id).first()
        if existing_record is None:
            new_record = cls(id=id,
                             similarity_result=similarity_result)
            session.add(new_record)
        else:
            existing_record.similarity_result = similarity_result
            existing_record.last_update_on = func.current_timestamp()
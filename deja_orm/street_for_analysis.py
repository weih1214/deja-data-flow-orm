import sqlalchemy as sa

from deja_orm import OfflineFlowBase


class StreetForAnalysis(OfflineFlowBase):

    __tablename__ = 'street_for_analysis'

    id = sa.Column('id', sa.BigInteger, primary_key=True, autoincrement=True)
    street_type = sa.Column('street_type', sa.Integer)
    reference = sa.Column('reference', sa.String(50))
    eligible_item_count = sa.Column('eligible_item_count', sa.Integer)
    image_local_path = sa.Column('image_local_path', sa.String(200))

    def save(self, session):

        session.add(self)

    @classmethod
    def get_by_ids(cls, street_analysis_ids, session):

        return session.query(cls).filter(cls.id.in_(street_analysis_ids)).all()

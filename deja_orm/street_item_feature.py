import sqlalchemy as sa

from deja_orm import OfflineFlowBase


class StreetItemFeature(OfflineFlowBase):

    __tablename__ = 'street_item_feature'

    street_item_id = sa.Column('street_item_id', sa.BigInteger, primary_key=True)
    feature = sa.Column('feature', sa.Text)

    def save(self, session):

        session.add(self)

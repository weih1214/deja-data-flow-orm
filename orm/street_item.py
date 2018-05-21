import sqlalchemy as sa

from orm import OfflineFlowBase


class StreetItem(OfflineFlowBase):

    __tablename__ = 'street_item'

    id = sa.Column('id', sa.BigInteger, primary_key=True, autoincrement=True)
    street_for_analysis_id = sa.Column('street_for_analysis_id', sa.BigInteger)
    sub_category = sa.Column('sub_category', sa.Integer)
    parsed_path = sa.Column('parsed_path', sa.String(200))
    parsed_area = sa.Column('parsed_area', sa.Integer)
    is_eligible = sa.Column('is_eligible', sa.Boolean)

    def save(self, session):

        session.add(self)
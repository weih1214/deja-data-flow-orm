from sqlalchemy import orm
from sqlalchemy.orm import scoping
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sa


OfflineFlowBase = declarative_base(name='offline_flow')
CrawlerBase = declarative_base(name='deja_crawler')


class DBManager:

    def __init__(self, connection=None):
        self.connection = connection
        self.engine = sa.create_engine(self.connection)
        self.DBSession = scoping.scoped_session(
            orm.sessionmaker(
                bind=self.engine,
                autocommit=False
            )
        )

    @property
    def session(self):
        return self.DBSession()


def yield_limit(qry, pk_attr, batch_count=100):
    """specialized windowed query generator (using LIMIT/OFFSET)

    This recipe is to select through a large number of rows thats too
    large to fetch at once. The technique depends on the primary key
    of the FROM clause being an integer value, and selects items
    using LIMIT."""

    first_id = None
    while True:
        q = qry
        if first_id is not None:
            q = qry.filter(pk_attr > first_id)
        rec = None
        for rec in q.order_by(pk_attr).limit(batch_count):
            yield rec
        if rec is None:
            break
        first_id = pk_attr.__get__(rec, pk_attr) if rec else None

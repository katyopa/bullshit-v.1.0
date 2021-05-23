import sqlalchemy as sql


# вот здесь была ошибка - каждый раз создавало
# таблицу заново: :memory: вместо tags.db название бд
engine = sql.create_engine('sqlite:///tags.db', echo=True)

metadata = sql.MetaData()

tagcounter_db = sql.Table('tagcounter_db', metadata,
                          sql.Column('site_name', sql.String(60)),
                          sql.Column('url', sql.String(250)),
                          sql.Column('date_time', sql.String(60)),
                          sql.Column('tagcount', sql.Integer)

                          )


metadata.create_all(engine)

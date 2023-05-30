from sqlalchemy import create_engine, Column, Integer, String, Table, MetaData, ForeignKey, text

engine = create_engine('sqlite:///:memory:')

metadata_obj = MetaData()
user = Table(
    'user',
    metadata_obj,
    Column('user_id', Integer, primary_key=True),
    Column('user_name', String(40), nullable=False),
    Column('email_address', String(60)),
    Column('nickname', String(50), nullable=False)
)
sql_insert = text("insert into user values(1, 'juliana', 'email@email.com', 'ju')")
engine.execute(sql_insert)

user_prefs = Table(
    'userprefs', metadata_obj,
    Column('pref_id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey('user.user_id'), nullable=False),
    Column('pref_name', String(40), nullable=False),
    Column('pref_value', String(100)),
)

metadata_obj.create_all(engine)

metadata_db_obj = MetaData()
financial_info = Table(
    'financial_info',
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('value', String(100), nullable=False)
)

for table in metadata_obj.sorted_tables:
    print(table)

print('Executando statement sql')
sql = text('select * from user')
print(engine.execute(sql))
result = engine.execute(sql)
for num in result:
    print(num)






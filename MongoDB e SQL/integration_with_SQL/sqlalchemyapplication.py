import sqlalchemy as sqlA
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship
from sqlalchemy import Column, func
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy import inspect
from sqlalchemy import create_engine
from sqlalchemy import select


Base = declarative_base()

class User(Base):
    __tablename__ = 'user_account'
    #atributos
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    address = relationship("Address", back_populates="user", cascade="all, delete-orphan")
    def __repr__(self):
        return f'User(id={self.id}, name={self.name}, fullname={self.fullname})'


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    email_address = Column(String(30), nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)

    user = relationship("User", back_populates="address")

    def __repr__(self):
        return f'Address(id={self.id}, email_address={self.email_address})'


print(User.__tablename__)
print(Address.__tablename__)

#conecxao com banco de dados
engine = create_engine("sqlite://")

#criando as classes como tablelas na db
Base.metadata.create_all(engine)

insp = inspect(engine)
print(insp.has_table("user_account"))
print(insp.default_schema_name)
print(insp.get_table_names())

with Session(engine) as session:
    nino = User(
        name="NINO",
        fullname="NINOseg",
        address=[Address(email_address="byttencourt@hotmail.com")]
    )

    nico = User(
        name="Nicolas",
        fullname="Nicolas Alves",
        address=[Address(email_address="nikko@hotmail.com")]
    )

    jose = User(
        name="Jose",
        fullname="jose Alves"
    )

    #enviar para db
    session.add_all([nino, nico, jose])

    session.commit()


stmt = select(User).where(User.name.in_(["nino", 'nico']))
print('Recuperando usuarios a partir de condição de filtragem')
for user in session.scalars(stmt):
    print(user)

stmt_address = select(Address).where(Address.user_id.in_([2]))
print('Recuperando usuarios a partir de condição de filtragem')
for address in session.scalars(stmt_address):
    print(address)

stmt_order = select(User).order_by(User.fullname.desc())
for result in session.scalars(stmt_order):
    print(result)

stmt_join = select(User.fullname, Address.email_address).join_from(Address, User)
for result in session.scalars(stmt_join):
    print(result)

connection = engine.connect()
results = connection.execute(stmt_join)
print('Executando statement a partir da connection')
for result in results:
    print(result)

stmt_count = select(func.count('*')).select_from(User)
print('Total de instancias em User ', end='')
for result in session.scalars(stmt_count):
    print(result)







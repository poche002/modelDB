from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, Table, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref,sessionmaker

engine = create_engine('sqlite:///usersandbadges.db', echo=True)
Base = declarative_base()


user_badges = Table('user_badges', Base.metadata,
     Column('user_id', Integer, ForeignKey('users.id')),
     Column('badge_id', Integer, ForeignKey('badges.id'))
    )

class Badge(Base):
    __tablename__ = 'badges'

    id = Column(Integer, primary_key=True)
    num_needed = Column(Integer)
    description = Column(String)
    ####user_id = Column(Integer, ForeignKey('users.id'))

    ####user = relationship("User", backref=backref('badges', order_by=id))

    def __repr__(self):
        return "<Badge(amount_needed'%s')>" % (self.num_needed)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    ####user_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    # many to many users<->badges
    badges = relationship('Badge', secondary=user_badges, backref='users')


    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)

user1 = User(name='User1', fullname='Ed Jones1', password='pass1')
user2 = User(name='User2', fullname='Ed Jones2', password='pass2')
badge1 = Badge(num_needed = 10, description = 'este es el badge1')
badge2 = Badge(num_needed = 15, description = 'este es el badge2')
badge3 = Badge(num_needed = 20, description = 'este es el badge3')


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, Table, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref,sessionmaker

engine = create_engine('sqlite:///usersandbadges.db', echo=True)
Base = declarative_base()


user_badges = Table('user_badges', Base.metadata,
     Column('user_id', Integer, ForeignKey('users.id')),
     Column('badge_id', Integer, ForeignKey('badges.id'))
    )

class Datosbadge(Base):
    __tablename__ = 'datosbadges'

    id = Column(Integer, primary_key=True)
    key_name = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    badge_id = Column(Integer, ForeignKey('badges.id'))
    cant_act = Column(Integer)

    def __repr__(self):
        return "<Badge(amount_existing'%s')>" % (self.cant_act)

class Badge(Base):
    __tablename__ = 'badges'

    id = Column(Integer, primary_key=True)
    key_name = Column(String)
    num_needed = Column(Integer)
    description = Column(String)
    datosbadges = relationship("Datosbadge")

    def __repr__(self):
        return "<Badge(amount_needed'%s')>" % (self.num_needed)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    fullname = Column(String)
    password = Column(String)

    # many to many users<->badges
    badges = relationship('Badge', secondary=user_badges, backref='users')
    datosbadges = relationship("Datosbadge")

    def __repr__(self):
        return "<User(user_id='%s', fullname='%s', password='%s')>" % (self.user_id, self.fullname, self.password)

user1 = User(user_id='User1', fullname='Ed Jones1', password='pass1')
user2 = User(user_id='User2', fullname='Ed Jones2', password='pass2')
badge1 = Badge(num_needed = 10, description = 'este es el badge1')
badge2 = Badge(num_needed = 15, description = 'este es el badge2')
badge3 = Badge(num_needed = 20, description = 'este es el badge3')


def init_model():
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()

def commit():
    session = init_model()
    session.commit()
    session.close()

def start():
    pass

def start_read_only():
    pass

def rollback():
    session = init_model()
    session.rollback()
    session.close()

def clear():
    session = init_model()
    #session.remove()
    session.close()

def get_user(user_id):
    session = init_model()
    user = session.query(User).filter_by(user_id=user_id).first()
    session.close()
    return user

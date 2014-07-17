from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, Table, Text, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref,sessionmaker, scoped_session
from pecan import conf

#engine = create_engine('sqlite:///usersandbadges.db', echo=True)
Base = declarative_base()

class Badge(Base):
    __tablename__ = 'badges'

    id = Column(Integer, primary_key=True)
    badge_id = Column(String)
    amount_necessary = Column(Integer)
    description = Column(String)

    def __repr__(self):
        return "<Badge(amount_necessary'%s')>" % (self.amount_necessary)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    fullname = Column(String)
    password = Column(String)

    #badges = relationship('UserBadges', backref='users')
    #userBadges = relationship('UserBadges', backref='users')

    def __repr__(self):
        return "<User(user_id='%s', fullname='%s', password='%s')>" % (self.user_id, self.fullname, self.password)

class UserBadges(Base):
    __tablename__ = 'user_badges'

    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    badge_id = Column(Integer, ForeignKey('badges.id'), primary_key=True)
    cant_act = Column(Integer)

    user = relationship(User, backref='users')
    badge = relationship(Badge, backref='badges')

    def __init__(self, badge, user, cant_act=0):
        self.user = user
        self.badge = badge
        self.cant_act = cant_act


    def __repr__(self):
        return "<userBadge(amount_existing'%s')>" % (self.cant_act)




user1 = User(user_id='User1', fullname='Ed Jones1', password='pass1')
user2 = User(user_id='User2', fullname='Ed Jones2', password='pass2')
badge1 = Badge(badge_id='Badge1', amount_necessary = 10, description = 'este es el badge1')
badge2 = Badge(badge_id='Badge2', amount_necessary = 15, description = 'este es el badge2')
badge3 = Badge(badge_id='Badge3', amount_necessary = 20, description = 'este es el badge3')
userBadge11 = UserBadges(user=user1, badge=badge1, cant_act=11)
userBadge13 = UserBadges(user=user1, badge=badge3, cant_act=13)
userBadge21 = UserBadges(user=user2, badge=badge1, cant_act=21)
userBadge22 = UserBadges(user=user2, badge=badge2, cant_act=22)






Session = scoped_session(sessionmaker())

def _engine_from_config(configuration):
    configuration = dict(configuration)
    url = configuration.pop('url')
    return create_engine(url, **configuration)

def init_model():
    conf.sqlalchemy.engine = _engine_from_config(conf.sqlalchemy)
    Base.metadata.create_all(conf.sqlalchemy.engine)

def start():
    Session.bind = conf.sqlalchemy.engine
    Base.metadata.bind = Session.bind
    import ipdb; ipdb.set_trace()

def start_read_only():
    start()

def commit():
    Session.commit()

def rollback():
    Session.rollback()

def clear():
    Session.remove()

def get_user(user_id):
    user = Session.query(User).filter_by(user_id=user_id).first()
    return user

def get_all_users():
    return Session.query(User).all()

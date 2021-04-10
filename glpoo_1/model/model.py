from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


engine = create_engine('sqlite:///:memory:', echo=True)
Base=declarative_base()


Session = sessionmaker(bind=engine)
session = Session()

class Member(Base):
    __tablename__ = 'members'
    id = Column(Integer, primary_key=True)
    right= Column(String)#user ou admin
    name = Column(String)
    fullname = Column(String)
    user= Column(String)#nom d'utilisateur
    password = Column(String)
    #jointure avec une table pour trouver les clubs


    def __repr__(self):
        return "(ID='%s', name='%s', fullname='%s', user='%s',password='%s',right='%s')" % (
            self.id, self.name, self.fullname, self.user,self.password,self.right)


class Member_license(Base):#association entre member et licence
    __tablename__ = 'members_license'
    id = Column(Integer, primary_key=True)
    #id_licence=Column(Integer,ForeignKey('id_licence'))
    #license = relationship("Club",back_populates="L_licence")
    id_member=Column(Integer,ForeignKey('members.id'))
    member=relationship("members",back_populates="id_members")#creer relation entre cette table et la table membre
    statut= Column(Integer)#membre(0), bureau(1),chef(2)
    #jointure avec une table pour trouver les clubs


    def __repr__(self):
        return "(ID='%s', id_club='%s', id_member='%s')" % (
            self.id, self.id_licence, self.id_member,self.statut)


Base.metadata.create_all(engine)


def add_member(add_name, add_fullname, add_user,add_password,add_right):
    add_user = Member(name=add_name, fullname=add_fullname,user=add_user,password=add_password,right=add_right)

    session.add(add_user)
    session.commit()


def list_member():
    for member in session.query(Member):
        print(member)


def del_member(ida):
    session.delete(session.query(Member).filter_by(id=ida).one())
    session.commit()


def modify_name(ida,name=None,fullname=None,user=None,password=None):
    mod=session.query(Member).filter_by(id=ida).one()
    if name:
        mod.name=name
    if fullname:
        mod.fullname=fullname
    if user:
        mod.user=user
    if password:
        mod.password=password







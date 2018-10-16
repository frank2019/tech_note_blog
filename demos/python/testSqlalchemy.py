
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import  String,Column,Integer
from sqlalchemy.orm import sessionmaker

import datetime
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("mysql+mysqldb://root:root1230ROOT!@#@192.168.1.70:3306/mx_video?charset=utf8", max_overflow=5,encoding='utf-8')
Session = sessionmaker(bind=engine)

Base = declarative_base()

class AdminUser(Base):    #必须继承declaraive_base得到的那个基类
    __tablename__ = "tb_admin"    #必须要有__tablename__来指出这个类对应什么表，这个表可以暂时在库中不存在，SQLAlchemy会帮我们创建这个表
    name = Column(String(45),primary_key=True)    #Column类创建一个字段
    passwd = Column(String(45),nullable=False,unique=True,index=True)    #nullable就是决定是否not null，unique就是决定是否unique。。这里假定没人重名，设置index可以让系统自动根据这个字段为基础建立索引
    passwd_md5 = Column(String(45),nullable=False)
    role = Column(String(45),nullable=False)
    createtime = Column(DateTime, default=datetime.datetime.utcnow,nullable=False)

    def __repr__(self):
        return "<AdminUser>{}:{}".format(self.name,self.role)

session = Session()
print(session.query(AdminUser).filter_by(name="admin").first() )
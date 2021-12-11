from database import Base,engine
#from sqlalchemy import String,Boolean,Integer,Column,Float''' #Import used only to create the database and 
                                                               # to be placed in the modelz folder

#The Class below was used only to create the database and was therefore placed in the modelz folder                                                              
'''
class Games(Base):
    __tablename__ = 'games'
    id= Column(Integer,primary_key=True)
    name= Column(String(255),nullable=False,unique=True)
    multiplatform= Column(Boolean,default=False)
    price= Column(Float,nullable=False)
    for_sale= Column(Boolean,default=False)

    
    def __repr__(self):
        return f"<Games nome={self.name} preco={self.price}>" '''


Base.metadata.create_all(engine)

print('Creating a database......')

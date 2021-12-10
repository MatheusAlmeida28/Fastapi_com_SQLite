from database import Base
from sqlalchemy import String,Boolean,Integer,Column,Float

class Games(Base):
    __tablename__ = 'games'
    id= Column(Integer,primary_key=True)
    name= Column(String(255),nullable=False,unique=True)
    multiplatform= Column(Boolean,default=False)
    price= Column(Float,nullable=False)
    for_sale= Column(Boolean,default=False)

    
    def __repr__(self):
        return f"<Item nome={self.name} preco={self.price}>"



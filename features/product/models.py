from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

class ProductBase(SQLModel):
  name: str = Field(max_length=50, title='product\'s name')
  description: str = Field(title='product\'s description')
  prize: float
  currency: str = 'naira'


# class ProductLike(SQLModel, table=True):
#   user_id: Optional[int] = Field(foreign_key='user.id', primary_key=True)
#   product_id: Optional[int] = Field(foreign_key='product.id', primary_key=True)

class Product(ProductBase, table=True):
  id: int = Field(default=None, primary_key=True)

  # likes: List['ProductLike'] = Relationship(back_populates='products', link_model=ProductLike)



class ProductCreate(ProductBase):
  class Config:
    schema_extra = {
      'example': {
        'name': 'Nike Show',
        'description': 'Nike branded show in multiple colors',
        'prize': 18000
      }
    }


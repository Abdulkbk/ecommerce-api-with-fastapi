from typing import Dict
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from features.product.models import Product, ProductCreate

async def get_products(session: AsyncSession):
  query = select(Product)
  result = await session.execute(query)
  return result.scalars().all()

async def add_product(owner: int, session: AsyncSession, product: ProductCreate):
  product = Product(**product.dict(), owner_id=owner)
  session.add(product)
  await session.commit()
  await session.refresh(product)
  return Product(**product.dict())

async def get_product_by_id(session: AsyncSession, id: int):
  query = select(Product).where(Product.id == id)
  result = await session.execute(query)
  return result.one()

async def update_product_by_id(session: AsyncSession, id: int, values: Dict):
  query = select(Product).where(Product.id == id)
  result = await session.execute(query)
  product = result.one()
  for el in values.keys():
    if el in product.keys():
      product.el = values.get(el)
  await session.commit()
  await session.refresh(product)
  return product



async def delete_product_by_id(session: AsyncSession, id: int):
  query = select(Product).where(Product.id == id)
  result = await session.execute(query)
  product = result.one()
  await session.delete(product)
  await session.commit()
  return id


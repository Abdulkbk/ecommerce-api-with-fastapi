from sqlalchemy.ext.asyncio import AsyncSession
from features.product.models import ProductCreate
from features.product.repo import add_product, delete_product_by_id, get_product_by_id, get_products


async def get_all_products(session: AsyncSession):
  return await get_products(session)


async def get_one_product(session: AsyncSession, id: int):
  return await get_product_by_id(session, id)


async def add_one_product(session: AsyncSession, product: ProductCreate):
  return await add_product(session, product)


async def update_one_product():
  pass


async def delete_one_product(session: AsyncSession, id: int):
  return await delete_product_by_id(session, id)

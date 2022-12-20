from typing import List
from fastapi import Depends, status

from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from starlette.responses import JSONResponse, Response

from common.database.db import get_session
from features.product.cruds import add_one_product, delete_one_product, get_all_products
from features.product.models import Product, ProductCreate


product_router = InferringRouter(prefix='/product')


@cbv(product_router)
class ProductRoute:

  @product_router.get(
    '',
    status_code=status.HTTP_200_OK,
    response_model=List[Product]
  )
  async def get_products(self, session: AsyncSession = Depends(get_session)):
    return await get_all_products(session)


  @product_router.post(
    '',
    status_code=status.HTTP_200_OK,
    response_model=Product
  )
  async def add_product(self, product: ProductCreate, session: AsyncSession = Depends(get_session)):
    return await add_one_product(session, product)
  
  @product_router.get(
    '/{product_id}',
    status_code=status.HTTP_200_OK
  )
  async def get_product(self):
    pass


  @product_router.put(
    '/{product_id}',
    status_code=status.HTTP_200_OK
  )
  async def update_product(self, product_id: int, session: AsyncSession = Depends(get_session)):
    pass

  @product_router.delete(
    '/{product_id}',
    status_code=status.HTTP_200_OK
  )
  async def delete_product(self, product_id: int, session: AsyncSession = Depends(get_session)):
    return await delete_one_product(session, product_id)
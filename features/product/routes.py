from typing import List
from fastapi import Depends, status, Request

from common.config import cfg
from common.database.redis import redis_client

from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from starlette.responses import JSONResponse, Response
from authentication.cruds import get_user

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
  async def get_products(self, session: AsyncSession = Depends(get_session), user = Depends(get_user)):
    cache_key = f'{cfg.CACHE_PREFIX}products'
    cached_products = await redis_client.get(cache_key)

    if cached_products:
      return cached_products
      
    return await get_all_products(session)


  @product_router.post(
    '',
    status_code=status.HTTP_200_OK,
    response_model=Product
  )
  async def add_product(self, product: ProductCreate, session: AsyncSession = Depends(get_session), user = Depends(get_user)):
    return await add_one_product(user['id'], session, product)
  
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
  async def delete_product(self, product_id: int, session: AsyncSession = Depends(get_session), user = Depends(get_user)):
    return await delete_one_product(session, product_id)
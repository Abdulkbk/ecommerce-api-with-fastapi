import asyncio
import aioredis 

from common.config import cfg

async def create_redis_client():
  redis_pool = await aioredis.create_redis_pool(
    cfg.cache_host,
    cfg.cache_password,
    db=0
  )
  return redis_pool

redis_client = create_redis_client()
import bcrypt
from fastapi import Depends, status

from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from starlette.responses import JSONResponse, Response
from authentication.models import User, UserCreate

from common.concurrency import cpu_bound_task
from common.database.db import get_session
from common.injection import on


auth_router = InferringRouter()


@cbv(auth_router)
class AuthCrud:

  @auth_router.post(
    '/register',
    status_code=status.HTTP_201_CREATED
  )
  async def register(self, user_in: UserCreate, session: AsyncSession = Depends(get_session)):
    user = User(name=user_in.name, email=user_in.email, password=user_in.password, phone=user_in.phone)
    user.password = (
      await cpu_bound_task(
        bcrypt.hashpw, user.password.encode(), bcrypt.gensalt()
      )
    ).decode()
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user
    

import bcrypt
from fastapi import Depends, status

from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from starlette.responses import JSONResponse, Response
from authentication.cruds import authenticate_user, register_user
from authentication.models import LoginIn, User, UserCreate, UserProfile

from common.concurrency import cpu_bound_task
from common.database.db import get_session
from common.injection import on


auth_router = InferringRouter()


@cbv(auth_router)
class AuthCrud:

  @auth_router.post(
    '/register',
    response_model=UserProfile,
    status_code=status.HTTP_201_CREATED
  )
  async def register(self, user_in: UserCreate, session: AsyncSession = Depends(get_session)):
    return await register_user(session, user_in)

  
  @auth_router.post(
    '/login',
    status_code=status.HTTP_200_OK
  )
  async def login(self, login: LoginIn, session: AsyncSession = Depends(get_session)):
    """Perform a login attempt; if successful, refresh token cookie is set
        and access token is returned to the client."""
    
    return await authenticate_user(session, login)
    

    

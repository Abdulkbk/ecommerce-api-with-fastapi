import bcrypt
import jwt
import datetime as dt

from common.config import cfg

from sqlalchemy.future import select

from authentication.models import JwtUser, LoginIn, User, UserCreate, UserProfile
from sqlalchemy.ext.asyncio import AsyncSession
from authentication.repo import get_user_by_email

from common.concurrency import cpu_bound_task


async def register_user(session: AsyncSession, user: UserCreate):
  user = User(**user.dict())
  user.password = (
      await cpu_bound_task(
        bcrypt.hashpw, user.password.encode(), bcrypt.gensalt()
      )
    ).decode()
  session.add(user)
  await session.commit()
  await session.refresh(user)
  return UserProfile(**user.dict())


async def authenticate_user(session: AsyncSession, user_data: LoginIn):

  email, password = user_data.email, user_data.password

  user = await get_user_by_email(session, email)

  pass_is_match = await _check_password(password, user.password)

  if pass_is_match:
    payload = {'id': user.id, 'name': user.name}

    access_token = _generate_jwt_access_token(payload)
    refresh_token = _generate_jwt_refresh_token(payload)

    return JwtUser(**user.dict(), access_token=access_token, refresh_token=refresh_token)


def _generate_jwt_access_token(profile_data):
  iat = dt.datetime.now(dt.timezone.utc)
  exp = iat + dt.timedelta(minutes=cfg.access_exp)
  user_payload = {
    'user': profile_data,
    'exp': exp,
    'iat': iat
  }
  payload = jwt.encode(
    payload=user_payload, key=cfg.jwt_secret,
  )
  return payload

def _generate_jwt_refresh_token(profile_data):
  iat = dt.datetime.now(dt.timezone.utc)
  exp = iat + dt.timedelta(days=cfg.refresh_exp)
  user_payload = profile_data
  payload = jwt.encode(
    payload=user_payload, key=cfg.refresh_secret
  )
  return payload
  
async def _check_password(password: str, password_hash: str) -> bool:
  return await cpu_bound_task(
    bcrypt.checkpw, password.encode(), password_hash.encode()
  )


async def _extract_user_from_token(acces_token: str):
  decoded = jwt.decode(
    acces_token,
    key=cfg.jwt_secret,
  )['user']
  return decoded
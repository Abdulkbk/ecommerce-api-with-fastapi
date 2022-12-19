from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from authentication.models import User

async def get_user_by_email(session: AsyncSession, email: str):
  query = select(User).where(User.email == email)
  result = await session.execute(query)
  return result.scalar()
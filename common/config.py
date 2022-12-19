from pydantic import BaseSettings

class Settings(BaseSettings):
  prod: bool = False
  fastapi_log_level: str = 'info'
  domain_name: str = 'http://localhost:8000'

  class Config:
    env_file = '.env'
    env_file_encoding = 'utf-8'

  
class DevSettings(Settings):
  prod: bool = True
  fastapi_log_level: str = 'debug'
  domain_name: str = 'http://localhost:8000'
  database_uri: str = ''
  jwt_secret: str = ''
  refresh_secret: str = ''
  access_exp: float
  refresh_exp: float


class ProdSettings(Settings):
  prod: bool = False
  fastapi_log_level: str = 'info'
  domain_name: str = 'http://localhost:8000'


cfg = ProdSettings() if Settings().prod else DevSettings()





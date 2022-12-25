import uvicorn
from fastapi import APIRouter, FastAPI

from common.log import logger

from authentication.routes import auth_router
from features.product.routes import product_router

# Init FastAPI app
app = FastAPI(
  title='Ecommerce API',
  version='0.1.0',
  swagger_ui_parameters={'syntaxHighlight.theme': 'obsidian'},
)


# Routers
api_router = APIRouter(prefix='/api')

api_router.include_router(auth_router, tags=['auth'])
api_router.include_router(product_router, tags=['product'])

app.include_router(api_router)

# Startup event
# @app.on_event('startup')
# async def startup():
#   ...

# Shutdown event
async def shutdown():
  ...

@app.get('/')
async def root():
  logger.info(msg='GET Request to /')
  return {'message': f'Head to /docs to view api documentation'}


if __name__ == "__main__":
  uvicorn.run(app)
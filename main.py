import uvicorn
from fastapi import APIRouter, FastAPI


# Init FastAPI app
app = FastAPI(
  title='Ecommerce API',
  version='0.1.0',
  swagger_ui_parameters={'syntaxHighlight.theme': 'obsidian'},
)


# Routers
api_router = APIRouter(prefix='/api')

app.include_router(api_router)

# Startup event
@app.on_event('startup')
async def startup():
  ...

# Shutdown event
async def shutdown():
  ...

@app.get('/')
async def root():
  return {'message': f'Head to /docs to view api documentation'}


if __name__ == "__main__":
  uvicorn.run(app)
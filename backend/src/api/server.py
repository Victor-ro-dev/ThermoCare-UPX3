from fastapi import FastAPI
from src.api.routes.sensor_route import router as sensor_temp_router
from fastapi.middleware.cors import CORSMiddleware
from src.api.routes.nursing_route import router as nursing_home_router
from src.api.routes.user_route import router as user_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir as rotas do sensor_temp_router
app.include_router(sensor_temp_router, prefix="/api/v1")
app.include_router(nursing_home_router, prefix="/api/v1")
app.include_router(user_router, prefix="/api/v1")

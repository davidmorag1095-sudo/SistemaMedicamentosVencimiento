from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config.database import init_db
from app.controller.centro_recepcion_controller_api import router as centro_router
from app.controller.donacion_controller_api import router as donacion_router
from app.controller.entrega_controller_api import router as entrega_router
from app.controller.medicamento_controller_api import router as medicamento_router
from app.controller.solicitud_controller_api import router as solicitud_router
from app.controller.usuario_controller_api import router as usuario_router

app = FastAPI(title="Sistema Medicamentos API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()

app.include_router(usuario_router)
app.include_router(centro_router)
app.include_router(medicamento_router)
app.include_router(donacion_router)
app.include_router(solicitud_router)
app.include_router(entrega_router)

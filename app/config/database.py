import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Conexion para MySQL usando WAMP.
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "mysql+pymysql://root:@localhost:3306/sistema_medicamentos_db"
)

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


def init_db():
    # Importa las entidades para que SQLAlchemy las registre.
    from app.entity.usuario import UsuarioORM
    from app.entity.centro_recepcion import CentroRecepcionORM
    from app.entity.medicamento import MedicamentoORM
    from app.entity.donacion import DonacionORM, DetalleDonacionORM
    from app.entity.solicitud import SolicitudORM, DetalleSolicitudORM
    from app.entity.entrega import EntregaORM

    Base.metadata.create_all(bind=engine)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://root:@localhost:3306/sistema_medicamentos_db"
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


def init_db():
    from app.entity.usuario import UsuarioORM
    from app.entity.centro_recepcion import CentroRecepcionORM
    from app.entity.medicamento import MedicamentoORM
    from app.entity.donacion import DonacionORM, DetalleDonacionORM
    from app.entity.solicitud import SolicitudORM, DetalleSolicitudORM
    from app.entity.entrega import EntregaORM

    Base.metadata.create_all(engine)

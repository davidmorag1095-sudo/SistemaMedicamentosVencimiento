from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://root:@localhost:3306/sistema_medicamentos_db"
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


def init_db():
    from entity.usuario import UsuarioORM
    from entity.centro_recepcion import CentroRecepcionORM
    from entity.medicamento import MedicamentoORM
    from entity.donacion import DonacionORM, DetalleDonacionORM
    from entity.solicitud import SolicitudORM, DetalleSolicitudORM
    from entity.entrega import EntregaORM

    Base.metadata.create_all(engine)

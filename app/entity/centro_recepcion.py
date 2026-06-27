from sqlalchemy import Column, Integer, String

from config.database import Base


class CentroRecepcionORM(Base):
    __tablename__ = 'centros_recepcion'

    id_centro = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    direccion = Column(String(200), nullable=False)
    telefono = Column(String(20), nullable=False)
    responsable = Column(String(100), nullable=False)

    def __repr__(self):
        return f"{self.nombre} {self.direccion} {self.telefono}"

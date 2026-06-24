from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.config.database import Base


class CentroRecepcionORM(Base):
    __tablename__ = "centros_recepcion"

    id_centro = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    direccion = Column(String(200), nullable=False)
    telefono = Column(String(20), nullable=False)
    responsable = Column(String(100), nullable=False)

    donaciones = relationship("DonacionORM", back_populates="centro")

    def __repr__(self):
        return f"CentroRecepcion(id_centro={self.id_centro}, nombre='{self.nombre}')"

from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.config.database import Base


class EntregaORM(Base):
    __tablename__ = "entregas"

    id_entrega = Column(Integer, primary_key=True, autoincrement=True)
    id_solicitud = Column(Integer, ForeignKey("solicitudes.id_solicitud"), nullable=False)
    id_detalle_donacion = Column(Integer, ForeignKey("detalle_donacion.id_detalle"), nullable=False)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
    cantidad_entregada = Column(Integer, nullable=False)
    fecha_entrega = Column(DateTime, default=datetime.now)

    solicitud = relationship("SolicitudORM", back_populates="entregas")
    detalle_donacion = relationship("DetalleDonacionORM", back_populates="entregas")
    usuario = relationship("UsuarioORM", back_populates="entregas")

    def __repr__(self):
        return f"Entrega(id_entrega={self.id_entrega}, cantidad_entregada={self.cantidad_entregada})"

from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.config.database import Base


class SolicitudORM(Base):
    __tablename__ = "solicitudes"

    id_solicitud = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
    fecha_solicitud = Column(DateTime, default=datetime.now)
    estado = Column(String(30), default="pendiente")
    observacion = Column(String(250))

    usuario = relationship("UsuarioORM", back_populates="solicitudes")
    detalles = relationship("DetalleSolicitudORM", back_populates="solicitud")
    entregas = relationship("EntregaORM", back_populates="solicitud")

    def __repr__(self):
        return f"Solicitud(id_solicitud={self.id_solicitud}, estado='{self.estado}')"


class DetalleSolicitudORM(Base):
    __tablename__ = "detalle_solicitud"

    id_detalle_solicitud = Column(Integer, primary_key=True, autoincrement=True)
    id_solicitud = Column(Integer, ForeignKey("solicitudes.id_solicitud"), nullable=False)
    id_medicamento = Column(Integer, ForeignKey("medicamentos.id_medicamento"), nullable=False)
    cantidad_solicitada = Column(Integer, nullable=False)
    cantidad_aprobada = Column(Integer, default=0)

    solicitud = relationship("SolicitudORM", back_populates="detalles")
    medicamento = relationship("MedicamentoORM", back_populates="detalles_solicitud")

    def __repr__(self):
        return (
            f"DetalleSolicitud(id_detalle_solicitud={self.id_detalle_solicitud}, "
            f"cantidad_solicitada={self.cantidad_solicitada})"
        )

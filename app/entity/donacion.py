from datetime import datetime

from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.config.database import Base


class DonacionORM(Base):
    __tablename__ = "donaciones"

    id_donacion = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
    id_centro = Column(Integer, ForeignKey("centros_recepcion.id_centro"), nullable=False)
    fecha_donacion = Column(DateTime, default=datetime.now)
    estado = Column(String(30), default="registrada")

    usuario = relationship("UsuarioORM", back_populates="donaciones")
    centro = relationship("CentroRecepcionORM", back_populates="donaciones")
    detalles = relationship("DetalleDonacionORM", back_populates="donacion")

    def __repr__(self):
        return f"Donacion(id_donacion={self.id_donacion}, estado='{self.estado}')"


class DetalleDonacionORM(Base):
    __tablename__ = "detalle_donacion"

    id_detalle = Column(Integer, primary_key=True, autoincrement=True)
    id_donacion = Column(Integer, ForeignKey("donaciones.id_donacion"), nullable=False)
    id_medicamento = Column(Integer, ForeignKey("medicamentos.id_medicamento"), nullable=False)
    cantidad = Column(Integer, nullable=False)
    fecha_vencimiento = Column(Date, nullable=False)
    lote = Column(String(50), nullable=False)
    estado_medicamento = Column(String(30), default="disponible")

    donacion = relationship("DonacionORM", back_populates="detalles")
    medicamento = relationship("MedicamentoORM", back_populates="detalles_donacion")
    entregas = relationship("EntregaORM", back_populates="detalle_donacion")

    def __repr__(self):
        return f"DetalleDonacion(id_detalle={self.id_detalle}, lote='{self.lote}', cantidad={self.cantidad})"

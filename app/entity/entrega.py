from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer

from config.database import Base


class EntregaORM(Base):
    __tablename__ = 'entregas'

    id_entrega = Column(Integer, primary_key=True)
    id_solicitud = Column(Integer, ForeignKey('solicitudes.id_solicitud'), nullable=False)
    id_detalle_donacion = Column(Integer, ForeignKey('detalle_donacion.id_detalle'), nullable=False)
    id_usuario = Column(Integer, ForeignKey('usuarios.id_usuario'), nullable=False)
    cantidad_entregada = Column(Integer, nullable=False)
    fecha_entrega = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return f"Entrega: {self.id_entrega} Cantidad: {self.cantidad_entregada}"

from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from app.config.database import Base


class SolicitudORM(Base):
    __tablename__ = 'solicitudes'

    id_solicitud = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuarios.id_usuario'), nullable=False)
    fecha_solicitud = Column(DateTime, default=datetime.now)
    estado = Column(String(30), default='pendiente')
    observacion = Column(String(250))

    def __repr__(self):
        return f"Solicitud: {self.id_solicitud} Estado: {self.estado}"


class DetalleSolicitudORM(Base):
    __tablename__ = 'detalle_solicitud'

    id_detalle_solicitud = Column(Integer, primary_key=True)
    id_solicitud = Column(Integer, ForeignKey('solicitudes.id_solicitud'), nullable=False)
    id_medicamento = Column(Integer, ForeignKey('medicamentos.id_medicamento'), nullable=False)
    cantidad_solicitada = Column(Integer, nullable=False)
    cantidad_aprobada = Column(Integer, default=0)

    def __repr__(self):
        return f"Medicamento: {self.id_medicamento} Cantidad solicitada: {self.cantidad_solicitada}"

from datetime import datetime

from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, String

from config.database import Base


class DonacionORM(Base):
    __tablename__ = 'donaciones'

    id_donacion = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuarios.id_usuario'), nullable=False)
    id_centro = Column(Integer, ForeignKey('centros_recepcion.id_centro'), nullable=False)
    fecha_donacion = Column(DateTime, default=datetime.now)
    estado = Column(String(30), default='en proceso')

    def __repr__(self):
        return f"Donacion: {self.id_donacion} Estado: {self.estado}"


class DetalleDonacionORM(Base):
    __tablename__ = 'detalle_donacion'

    id_detalle = Column(Integer, primary_key=True)
    id_donacion = Column(Integer, ForeignKey('donaciones.id_donacion'), nullable=False)
    id_medicamento = Column(Integer, ForeignKey('medicamentos.id_medicamento'), nullable=False)
    cantidad = Column(Integer, nullable=False)
    fecha_vencimiento = Column(Date, nullable=False)
    lote = Column(String(50), nullable=False)
    estado_medicamento = Column(String(30), default='disponible')

    def __repr__(self):
        return f"Lote: {self.lote} Cantidad: {self.cantidad} Vence: {self.fecha_vencimiento}"

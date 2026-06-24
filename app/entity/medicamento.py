from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from app.config.database import Base


class MedicamentoORM(Base):
    __tablename__ = "medicamentos"

    id_medicamento = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(200))
    categoria = Column(String(80), nullable=False)
    presentacion = Column(String(80), nullable=False)
    requiere_receta = Column(Boolean, default=False)

    detalles_donacion = relationship("DetalleDonacionORM", back_populates="medicamento")
    detalles_solicitud = relationship("DetalleSolicitudORM", back_populates="medicamento")

    def __repr__(self):
        return f"Medicamento(id_medicamento={self.id_medicamento}, nombre='{self.nombre}')"

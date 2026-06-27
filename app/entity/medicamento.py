from sqlalchemy import Boolean, Column, Integer, String

from config.database import Base


class MedicamentoORM(Base):
    __tablename__ = 'medicamentos'

    id_medicamento = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(200))
    categoria = Column(String(80), nullable=False)
    presentacion = Column(String(80), nullable=False)
    requiere_receta = Column(Boolean, default=False)

    def __repr__(self):
        return f"{self.nombre} {self.categoria} {self.presentacion}"

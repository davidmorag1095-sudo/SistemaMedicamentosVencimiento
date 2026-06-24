from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from app.config.database import Base


class UsuarioORM(Base):
    __tablename__ = "usuarios"

    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    correo = Column(String(100), nullable=False, unique=True)
    contrasena = Column(String(255), nullable=False)
    rol = Column(String(30), nullable=False)
    activo = Column(Boolean, default=True)

    donaciones = relationship("DonacionORM", back_populates="usuario")
    solicitudes = relationship("SolicitudORM", back_populates="usuario")
    entregas = relationship("EntregaORM", back_populates="usuario")

    def __repr__(self):
        return f"Usuario(id_usuario={self.id_usuario}, nombre='{self.nombre}', rol='{self.rol}')"

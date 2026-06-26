from sqlalchemy import Boolean, Column, Integer, String

from app.config.database import Base


class UsuarioORM(Base):
    __tablename__ = 'usuarios'

    id_usuario = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    correo = Column(String(100), nullable=False, unique=True)
    contrasena = Column(String(255), nullable=False)
    rol = Column(String(30), nullable=False)
    activo = Column(Boolean, default=True)

    def __repr__(self):
        return f"{self.nombre} {self.correo} {self.rol}"

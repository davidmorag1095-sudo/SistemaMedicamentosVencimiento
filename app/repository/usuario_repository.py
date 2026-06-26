from app.config.database import SessionLocal
from app.entity.usuario import UsuarioORM


class UsuarioRepository():
    def __init__(self):
        self.db = SessionLocal()

    def save(self, id_usuario, nombre, correo, contrasena, rol, activo=True):
        usuario = UsuarioORM(
            id_usuario=id_usuario,
            nombre=nombre,
            correo=correo,
            contrasena=contrasena,
            rol=rol,
            activo=activo
        )
        self.db.add(usuario)
        self.db.commit()
        return usuario

    def get_all(self):
        return self.db.query(UsuarioORM).all()

    def get_by_id(self, id_usuario):
        return self.db.query(UsuarioORM).filter_by(id_usuario=id_usuario).first()

    def get_by_correo(self, correo):
        return self.db.query(UsuarioORM).filter_by(correo=correo).first()

    def update(self, id_usuario, nombre, correo, contrasena, rol, activo=True):
        usuario = self.get_by_id(id_usuario)

        if usuario:
            usuario.nombre = nombre
            usuario.correo = correo
            usuario.contrasena = contrasena
            usuario.rol = rol
            usuario.activo = activo
            self.db.commit()
        return usuario

    def delete(self, id_usuario):
        usuario = self.get_by_id(id_usuario)

        if usuario:
            self.db.delete(usuario)
            self.db.commit()
        return usuario

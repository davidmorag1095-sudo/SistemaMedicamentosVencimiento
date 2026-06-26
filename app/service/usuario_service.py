from app.repository.usuario_repository import UsuarioRepository


class UsuarioService:

    def __init__(self):
        self.repo = UsuarioRepository()

    def create_usuario(self, id_usuario, nombre, correo, contrasena, rol, activo=True):
        return self.repo.create(id_usuario, nombre, correo, contrasena, rol, activo)

    def get_usuario(self, id_usuario):
        return self.repo.get(id_usuario)

    def list_usuarios(self):
        return self.repo.get_all()

    def update_usuario(self, id_usuario, nombre, correo, contrasena, rol, activo=True):
        return self.repo.update(id_usuario, nombre, correo, contrasena, rol, activo)

    def delete_usuario(self, id_usuario):
        return self.repo.delete(id_usuario)

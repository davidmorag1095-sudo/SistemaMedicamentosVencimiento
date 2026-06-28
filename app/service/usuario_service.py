from repository.usuario_repository import UsuarioRepository

ROLES_USUARIO = [
    "Administrador",
    "Donante",
    "Solicitante",
    "Usuario"
]


class UsuarioService:

    def __init__(self):
        self.repo = UsuarioRepository()

    def get_roles(self):
        return ROLES_USUARIO

    def validar_rol(self, rol):
        if rol not in ROLES_USUARIO:
            raise ValueError("Rol no permitido")

    def create_usuario(self, id_usuario, nombre, correo, contrasena, rol, activo=True):
        self.validar_rol(rol)
        return self.repo.create(id_usuario, nombre, correo, contrasena, rol, activo)

    def get_usuario(self, id_usuario):
        return self.repo.get(id_usuario)

    def list_usuarios(self):
        return self.repo.get_all()

    def update_usuario(self, id_usuario, nombre, correo, contrasena, rol, activo=True):
        self.validar_rol(rol)
        return self.repo.update(id_usuario, nombre, correo, contrasena, rol, activo)

    def delete_usuario(self, id_usuario):
        return self.repo.delete(id_usuario)

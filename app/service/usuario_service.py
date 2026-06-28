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
#--------------------------------------------------------------------------------------------------------------

    def get_roles(self):
        return ROLES_USUARIO
#--------------------------------------------------------------------------------------------------------------

    def validar_rol(self, rol):
        if not rol.strip():
            raise ValueError("Debe completar todos los campos")

        if rol not in ROLES_USUARIO:
            raise ValueError("Rol no permitido")
#--------------------------------------------------------------------------------------------------------------

    def validar_correo(self, correo, id_usuario=None):
        if not correo.strip():
            raise ValueError("Debe completar todos los campos")

        if "@" not in correo:
            raise ValueError("Correo invalido por favor intente de nuevo")

        usuario = self.repo.get_by_correo(correo)

        if usuario and usuario.id_usuario != id_usuario:
            raise ValueError("Correo ingresado ya esta registrado")
#--------------------------------------------------------------------------------------------------------------

    def validar_activo(self, activo):
        if not isinstance(activo, bool):
            raise ValueError("Activo debe ser S o N")
#--------------------------------------------------------------------------------------------------------------

    def create_usuario(self, id_usuario, nombre, correo, contrasena, rol, activo=True):
        if not nombre.strip() or not correo.strip() or not contrasena.strip() or not rol.strip():
            raise ValueError("Debe completar todos los campos")

        self.validar_rol(rol)
        self.validar_correo(correo)
        self.validar_activo(activo)
        return self.repo.create(id_usuario, nombre, correo, contrasena, rol, activo)
#--------------------------------------------------------------------------------------------------------------

    def get_usuario(self, id_usuario):
        return self.repo.get(id_usuario)
#--------------------------------------------------------------------------------------------------------------

    def list_usuarios(self):
        return self.repo.get_all()
#--------------------------------------------------------------------------------------------------------------

    def update_usuario(self, id_usuario, nombre, correo, contrasena, rol, activo=True):
        if not self.repo.get(id_usuario):
            raise ValueError("Usuario no encontrado")

        if not nombre.strip() or not correo.strip() or not contrasena.strip() or not rol.strip():
            raise ValueError("Debe completar todos los campos")

        self.validar_rol(rol)
        self.validar_correo(correo, id_usuario)
        self.validar_activo(activo)
        return self.repo.update(id_usuario, nombre, correo, contrasena, rol, activo)
#--------------------------------------------------------------------------------------------------------------

    def delete_usuario(self, id_usuario):
        return self.repo.delete(id_usuario)
#--------------------------------------------------------------------------------------------------------------

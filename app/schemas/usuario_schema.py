from pydantic import BaseModel, ConfigDict


class UsuarioSchema(BaseModel):
    id_usuario: int
    nombre: str
    correo: str
    contrasena: str
    rol: str
    activo: bool = True

    model_config = ConfigDict(from_attributes=True)

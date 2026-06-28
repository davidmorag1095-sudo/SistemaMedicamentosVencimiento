from fastapi import APIRouter, HTTPException

from schemas.usuario_schema import UsuarioSchema
from service.usuario_service import UsuarioService

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])
service = UsuarioService()


@router.post("/", response_model=UsuarioSchema)
def create_usuario(usuario: UsuarioSchema):
    try:
        return service.create_usuario(
            usuario.id_usuario,
            usuario.nombre,
            usuario.correo,
            usuario.contrasena,
            usuario.rol,
            usuario.activo
        )
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router.get("/{id_usuario}", response_model=UsuarioSchema)
def get_usuario(id_usuario: int):
    usuario = service.get_usuario(id_usuario)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario


@router.get("/", response_model=list[UsuarioSchema])
def list_usuarios():
    return service.list_usuarios()


@router.put("/{id_usuario}", response_model=UsuarioSchema)
def update_usuario(id_usuario: int, usuario: UsuarioSchema):
    try:
        updated = service.update_usuario(
            id_usuario,
            usuario.nombre,
            usuario.correo,
            usuario.contrasena,
            usuario.rol,
            usuario.activo
        )
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

    if not updated:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return updated


@router.delete("/{id_usuario}")
def delete_usuario(id_usuario: int):
    deleted = service.delete_usuario(id_usuario)
    if not deleted:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"message": "Usuario eliminado"}

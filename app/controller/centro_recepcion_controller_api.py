from fastapi import APIRouter, HTTPException

from app.schemas.centro_recepcion_schema import CentroRecepcionSchema
from app.service.centro_recepcion_service import CentroRecepcionService

router = APIRouter(prefix="/centros", tags=["Centros"])
service = CentroRecepcionService()


@router.post("/", response_model=CentroRecepcionSchema)
def create_centro(centro: CentroRecepcionSchema):
    return service.create_centro(
        centro.id_centro,
        centro.nombre,
        centro.direccion,
        centro.telefono,
        centro.responsable
    )


@router.get("/{id_centro}", response_model=CentroRecepcionSchema)
def get_centro(id_centro: int):
    centro = service.get_centro(id_centro)
    if not centro:
        raise HTTPException(status_code=404, detail="Centro no encontrado")
    return centro


@router.get("/", response_model=list[CentroRecepcionSchema])
def list_centros():
    return service.list_centros()


@router.put("/{id_centro}", response_model=CentroRecepcionSchema)
def update_centro(id_centro: int, centro: CentroRecepcionSchema):
    updated = service.update_centro(
        id_centro,
        centro.nombre,
        centro.direccion,
        centro.telefono,
        centro.responsable
    )
    if not updated:
        raise HTTPException(status_code=404, detail="Centro no encontrado")
    return updated


@router.delete("/{id_centro}")
def delete_centro(id_centro: int):
    deleted = service.delete_centro(id_centro)
    if not deleted:
        raise HTTPException(status_code=404, detail="Centro no encontrado")
    return {"message": "Centro eliminado"}

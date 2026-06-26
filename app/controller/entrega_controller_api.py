from fastapi import APIRouter, HTTPException

from app.schemas.entrega_schema import EntregaSchema
from app.service.entrega_service import EntregaService

router = APIRouter(prefix="/entregas", tags=["Entregas"])
service = EntregaService()


@router.post("/", response_model=EntregaSchema)
def create_entrega(entrega: EntregaSchema):
    return service.create_entrega(
        entrega.id_entrega,
        entrega.id_solicitud,
        entrega.id_detalle_donacion,
        entrega.id_usuario,
        entrega.cantidad_entregada,
        entrega.fecha_entrega
    )


@router.get("/{id_entrega}", response_model=EntregaSchema)
def get_entrega(id_entrega: int):
    entrega = service.get_entrega(id_entrega)
    if not entrega:
        raise HTTPException(status_code=404, detail="Entrega no encontrada")
    return entrega


@router.get("/", response_model=list[EntregaSchema])
def list_entregas():
    return service.list_entregas()


@router.put("/{id_entrega}", response_model=EntregaSchema)
def update_entrega(id_entrega: int, entrega: EntregaSchema):
    updated = service.update_entrega(
        id_entrega,
        entrega.id_solicitud,
        entrega.id_detalle_donacion,
        entrega.id_usuario,
        entrega.cantidad_entregada,
        entrega.fecha_entrega
    )
    if not updated:
        raise HTTPException(status_code=404, detail="Entrega no encontrada")
    return updated


@router.delete("/{id_entrega}")
def delete_entrega(id_entrega: int):
    deleted = service.delete_entrega(id_entrega)
    if not deleted:
        raise HTTPException(status_code=404, detail="Entrega no encontrada")
    return {"message": "Entrega eliminada"}

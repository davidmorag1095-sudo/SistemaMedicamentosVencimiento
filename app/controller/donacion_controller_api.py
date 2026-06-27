from fastapi import APIRouter, HTTPException

from app.schemas.donacion_schema import DonacionSchema, DetalleDonacionSchema
from app.service.donacion_service import DonacionService

router = APIRouter(prefix="/donaciones", tags=["Donaciones"])
service = DonacionService()


@router.post("/", response_model=DonacionSchema)
def create_donacion(donacion: DonacionSchema):
    try:
        return service.create_donacion(
            donacion.id_donacion,
            donacion.id_usuario,
            donacion.id_centro,
            donacion.fecha_donacion,
            donacion.estado
        )
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router.get("/{id_donacion}", response_model=DonacionSchema)
def get_donacion(id_donacion: int):
    donacion = service.get_donacion(id_donacion)
    if not donacion:
        raise HTTPException(status_code=404, detail="Donacion no encontrada")
    return donacion


@router.get("/", response_model=list[DonacionSchema])
def list_donaciones():
    return service.list_donaciones()


@router.put("/{id_donacion}", response_model=DonacionSchema)
def update_donacion(id_donacion: int, donacion: DonacionSchema):
    try:
        updated = service.update_donacion(
            id_donacion,
            donacion.id_usuario,
            donacion.id_centro,
            donacion.fecha_donacion,
            donacion.estado
        )
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

    if not updated:
        raise HTTPException(status_code=404, detail="Donacion no encontrada")
    return updated


@router.delete("/{id_donacion}")
def delete_donacion(id_donacion: int):
    deleted = service.delete_donacion(id_donacion)
    if not deleted:
        raise HTTPException(status_code=404, detail="Donacion no encontrada")
    return {"message": "Donacion eliminada"}


@router.post("/detalles/", response_model=DetalleDonacionSchema)
def create_detalle_donacion(detalle: DetalleDonacionSchema):
    try:
        return service.create_detalle_donacion(
            detalle.id_detalle,
            detalle.id_donacion,
            detalle.id_medicamento,
            detalle.cantidad,
            detalle.fecha_vencimiento,
            detalle.lote,
            detalle.estado_medicamento
        )
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router.get("/detalles/{id_detalle}", response_model=DetalleDonacionSchema)
def get_detalle_donacion(id_detalle: int):
    detalle = service.get_detalle_donacion(id_detalle)
    if not detalle:
        raise HTTPException(status_code=404, detail="Detalle no encontrado")
    return detalle


@router.get("/{id_donacion}/detalles", response_model=list[DetalleDonacionSchema])
def list_detalles_donacion(id_donacion: int):
    return service.list_detalles_donacion(id_donacion)


@router.put("/detalles/{id_detalle}", response_model=DetalleDonacionSchema)
def update_detalle_donacion(id_detalle: int, detalle: DetalleDonacionSchema):
    try:
        updated = service.update_detalle_donacion(
            id_detalle,
            detalle.id_medicamento,
            detalle.cantidad,
            detalle.fecha_vencimiento,
            detalle.lote,
            detalle.estado_medicamento
        )
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

    if not updated:
        raise HTTPException(status_code=404, detail="Detalle no encontrado")
    return updated


@router.delete("/detalles/{id_detalle}")
def delete_detalle_donacion(id_detalle: int):
    deleted = service.delete_detalle_donacion(id_detalle)
    if not deleted:
        raise HTTPException(status_code=404, detail="Detalle no encontrado")
    return {"message": "Detalle eliminado"}

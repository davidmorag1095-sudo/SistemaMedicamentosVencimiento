from fastapi import APIRouter, HTTPException

from app.schemas.solicitud_schema import SolicitudSchema, DetalleSolicitudSchema
from app.service.solicitud_service import SolicitudService

router = APIRouter(prefix="/solicitudes", tags=["Solicitudes"])
service = SolicitudService()


@router.post("/", response_model=SolicitudSchema)
def create_solicitud(solicitud: SolicitudSchema):
    try:
        return service.create_solicitud(
            solicitud.id_solicitud,
            solicitud.id_usuario,
            solicitud.fecha_solicitud,
            solicitud.estado,
            solicitud.observacion
        )
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router.get("/{id_solicitud}", response_model=SolicitudSchema)
def get_solicitud(id_solicitud: int):
    solicitud = service.get_solicitud(id_solicitud)
    if not solicitud:
        raise HTTPException(status_code=404, detail="Solicitud no encontrada")
    return solicitud


@router.get("/", response_model=list[SolicitudSchema])
def list_solicitudes():
    return service.list_solicitudes()


@router.put("/{id_solicitud}", response_model=SolicitudSchema)
def update_solicitud(id_solicitud: int, solicitud: SolicitudSchema):
    try:
        updated = service.update_solicitud(
            id_solicitud,
            solicitud.id_usuario,
            solicitud.fecha_solicitud,
            solicitud.estado,
            solicitud.observacion
        )
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

    if not updated:
        raise HTTPException(status_code=404, detail="Solicitud no encontrada")
    return updated


@router.delete("/{id_solicitud}")
def delete_solicitud(id_solicitud: int):
    deleted = service.delete_solicitud(id_solicitud)
    if not deleted:
        raise HTTPException(status_code=404, detail="Solicitud no encontrada")
    return {"message": "Solicitud eliminada"}


@router.post("/detalles/", response_model=DetalleSolicitudSchema)
def create_detalle_solicitud(detalle: DetalleSolicitudSchema):
    try:
        return service.create_detalle_solicitud(
            detalle.id_detalle_solicitud,
            detalle.id_solicitud,
            detalle.id_medicamento,
            detalle.cantidad_solicitada,
            detalle.cantidad_aprobada
        )
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router.get("/detalles/{id_detalle_solicitud}", response_model=DetalleSolicitudSchema)
def get_detalle_solicitud(id_detalle_solicitud: int):
    detalle = service.get_detalle_solicitud(id_detalle_solicitud)
    if not detalle:
        raise HTTPException(status_code=404, detail="Detalle no encontrado")
    return detalle


@router.get("/{id_solicitud}/detalles", response_model=list[DetalleSolicitudSchema])
def list_detalles_solicitud(id_solicitud: int):
    return service.list_detalles_solicitud(id_solicitud)


@router.put("/detalles/{id_detalle_solicitud}", response_model=DetalleSolicitudSchema)
def update_detalle_solicitud(id_detalle_solicitud: int, detalle: DetalleSolicitudSchema):
    try:
        updated = service.update_detalle_solicitud(
            id_detalle_solicitud,
            detalle.id_medicamento,
            detalle.cantidad_solicitada,
            detalle.cantidad_aprobada
        )
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

    if not updated:
        raise HTTPException(status_code=404, detail="Detalle no encontrado")
    return updated


@router.delete("/detalles/{id_detalle_solicitud}")
def delete_detalle_solicitud(id_detalle_solicitud: int):
    deleted = service.delete_detalle_solicitud(id_detalle_solicitud)
    if not deleted:
        raise HTTPException(status_code=404, detail="Detalle no encontrado")
    return {"message": "Detalle eliminado"}

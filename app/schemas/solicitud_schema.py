from datetime import datetime

from pydantic import BaseModel, ConfigDict


class SolicitudSchema(BaseModel):
    id_solicitud: int
    id_usuario: int
    fecha_solicitud: datetime
    estado: str
    observacion: str | None = None

    model_config = ConfigDict(from_attributes=True)


class DetalleSolicitudSchema(BaseModel):
    id_detalle_solicitud: int
    id_solicitud: int
    id_medicamento: int
    cantidad_solicitada: int
    cantidad_aprobada: int = 0

    model_config = ConfigDict(from_attributes=True)

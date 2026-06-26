from datetime import datetime

from pydantic import BaseModel, ConfigDict


class EntregaSchema(BaseModel):
    id_entrega: int
    id_solicitud: int
    id_detalle_donacion: int
    id_usuario: int
    cantidad_entregada: int
    fecha_entrega: datetime

    model_config = ConfigDict(from_attributes=True)

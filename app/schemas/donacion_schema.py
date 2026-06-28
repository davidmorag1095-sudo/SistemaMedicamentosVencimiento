from datetime import date, datetime

from pydantic import BaseModel, ConfigDict


class DonacionSchema(BaseModel):
    id_donacion: int | None = None
    id_usuario: int
    id_centro: int
    fecha_donacion: datetime
    estado: str

    model_config = ConfigDict(from_attributes=True)


class DetalleDonacionSchema(BaseModel):
    id_detalle: int | None = None
    id_donacion: int
    id_medicamento: int
    cantidad: int
    fecha_vencimiento: date
    lote: str
    estado_medicamento: str

    model_config = ConfigDict(from_attributes=True)

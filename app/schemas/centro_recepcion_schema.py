from pydantic import BaseModel, ConfigDict


class CentroRecepcionSchema(BaseModel):
    id_centro: int | None = None
    nombre: str
    direccion: str
    telefono: str
    responsable: str

    model_config = ConfigDict(from_attributes=True)

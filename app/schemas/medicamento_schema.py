from pydantic import BaseModel, ConfigDict


class MedicamentoSchema(BaseModel):
    id_medicamento: int
    nombre: str
    descripcion: str | None = None
    categoria: str
    presentacion: str
    requiere_receta: bool = False

    model_config = ConfigDict(from_attributes=True)

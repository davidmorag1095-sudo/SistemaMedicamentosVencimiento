from fastapi import APIRouter, HTTPException

from app.schemas.medicamento_schema import MedicamentoSchema
from app.service.medicamento_service import MedicamentoService

router = APIRouter(prefix="/medicamentos", tags=["Medicamentos"])
service = MedicamentoService()


@router.post("/", response_model=MedicamentoSchema)
def create_medicamento(medicamento: MedicamentoSchema):
    return service.create_medicamento(
        medicamento.id_medicamento,
        medicamento.nombre,
        medicamento.descripcion,
        medicamento.categoria,
        medicamento.presentacion,
        medicamento.requiere_receta
    )


@router.get("/{id_medicamento}", response_model=MedicamentoSchema)
def get_medicamento(id_medicamento: int):
    medicamento = service.get_medicamento(id_medicamento)
    if not medicamento:
        raise HTTPException(status_code=404, detail="Medicamento no encontrado")
    return medicamento


@router.get("/", response_model=list[MedicamentoSchema])
def list_medicamentos():
    return service.list_medicamentos()


@router.put("/{id_medicamento}", response_model=MedicamentoSchema)
def update_medicamento(id_medicamento: int, medicamento: MedicamentoSchema):
    updated = service.update_medicamento(
        id_medicamento,
        medicamento.nombre,
        medicamento.descripcion,
        medicamento.categoria,
        medicamento.presentacion,
        medicamento.requiere_receta
    )
    if not updated:
        raise HTTPException(status_code=404, detail="Medicamento no encontrado")
    return updated


@router.delete("/{id_medicamento}")
def delete_medicamento(id_medicamento: int):
    deleted = service.delete_medicamento(id_medicamento)
    if not deleted:
        raise HTTPException(status_code=404, detail="Medicamento no encontrado")
    return {"message": "Medicamento eliminado"}

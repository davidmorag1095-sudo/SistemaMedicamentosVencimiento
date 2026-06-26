from app.repository.medicamento_repository import MedicamentoRepository


class MedicamentoService:

    def __init__(self):
        self.repo = MedicamentoRepository()

    def create_medicamento(self, id_medicamento, nombre, descripcion, categoria, presentacion, requiere_receta=False):
        return self.repo.create(id_medicamento, nombre, descripcion, categoria, presentacion, requiere_receta)

    def get_medicamento(self, id_medicamento):
        return self.repo.get(id_medicamento)

    def list_medicamentos(self):
        return self.repo.get_all()

    def update_medicamento(self, id_medicamento, nombre, descripcion, categoria, presentacion, requiere_receta=False):
        return self.repo.update(id_medicamento, nombre, descripcion, categoria, presentacion, requiere_receta)

    def delete_medicamento(self, id_medicamento):
        return self.repo.delete(id_medicamento)

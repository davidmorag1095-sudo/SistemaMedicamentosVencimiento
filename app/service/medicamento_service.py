from repository.medicamento_repository import MedicamentoRepository

class MedicamentoService:

    def __init__(self):
        self.repo = MedicamentoRepository()
#--------------------------------------------------------------------------------------------------------------

    def get_categorias(self):
        return [
            "Analgesico",
            "Antibiotico",
            "Antialergico"
        ]
#--------------------------------------------------------------------------------------------------------------

    def get_presentaciones(self):
        return [
            "Tabletas",
            "Jarabe",
            "Inyectable"
        ]
#--------------------------------------------------------------------------------------------------------------

    def validar_categoria_presentacion(self, categoria, presentacion):
        if not categoria.strip() or not presentacion.strip():
            raise ValueError("Debe completar todos los campos")

        if categoria not in self.get_categorias():
            raise ValueError("Categoria no permitida")

        if presentacion not in self.get_presentaciones():
            raise ValueError("Presentacion no permitida")
#--------------------------------------------------------------------------------------------------------------

    def validar_requiere_receta(self, requiere_receta):
        if not isinstance(requiere_receta, bool):
            raise ValueError("Requiere receta debe ser S o N")
#--------------------------------------------------------------------------------------------------------------

    def create_medicamento(self, id_medicamento, nombre, descripcion, categoria, presentacion, requiere_receta=False):
        if not nombre.strip() or not descripcion.strip() or not categoria.strip() or not presentacion.strip():
            raise ValueError("Debe completar todos los campos")

        self.validar_categoria_presentacion(categoria, presentacion)
        self.validar_requiere_receta(requiere_receta)
        return self.repo.create(id_medicamento, nombre, descripcion, categoria, presentacion, requiere_receta)
#--------------------------------------------------------------------------------------------------------------

    def get_medicamento(self, id_medicamento):
        return self.repo.get(id_medicamento)
#--------------------------------------------------------------------------------------------------------------

    def list_medicamentos(self):
        return self.repo.get_all()
#--------------------------------------------------------------------------------------------------------------

    def update_medicamento(self, id_medicamento, nombre, descripcion, categoria, presentacion, requiere_receta=False):
        if not self.repo.get(id_medicamento):
            raise ValueError("Medicamento no encontrado")

        if not nombre.strip() or not descripcion.strip() or not categoria.strip() or not presentacion.strip():
            raise ValueError("Debe completar todos los campos")

        self.validar_categoria_presentacion(categoria, presentacion)
        self.validar_requiere_receta(requiere_receta)
        return self.repo.update(id_medicamento, nombre, descripcion, categoria, presentacion, requiere_receta)
#--------------------------------------------------------------------------------------------------------------

    def delete_medicamento(self, id_medicamento):
        return self.repo.delete(id_medicamento)
#--------------------------------------------------------------------------------------------------------------

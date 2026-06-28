from repository.medicamento_repository import MedicamentoRepository

CATEGORIAS_MEDICAMENTO = [
    "Analgesico",
    "Antibiotico",
    "Antialergico"
]

PRESENTACIONES_MEDICAMENTO = [
    "Tabletas",
    "Jarabe",
    "Inyectable"
]


class MedicamentoService:

    def __init__(self):
        self.repo = MedicamentoRepository()

    def get_categorias(self):
        return CATEGORIAS_MEDICAMENTO

    def get_presentaciones(self):
        return PRESENTACIONES_MEDICAMENTO

    def validar_categoria_presentacion(self, categoria, presentacion):
        if categoria not in CATEGORIAS_MEDICAMENTO:
            raise ValueError("Categoria no permitida")

        if presentacion not in PRESENTACIONES_MEDICAMENTO:
            raise ValueError("Presentacion no permitida")

    def validar_texto(self, valor, campo):
        if not valor or valor.strip() == "":
            raise ValueError(f"{campo} no puede estar vacio")

    def validar_requiere_receta(self, requiere_receta):
        if not isinstance(requiere_receta, bool):
            raise ValueError("Requiere receta debe ser S o N")

    def create_medicamento(self, id_medicamento, nombre, descripcion, categoria, presentacion, requiere_receta=False):
        self.validar_texto(nombre, "Nombre")
        self.validar_categoria_presentacion(categoria, presentacion)
        self.validar_requiere_receta(requiere_receta)
        return self.repo.create(id_medicamento, nombre, descripcion, categoria, presentacion, requiere_receta)

    def get_medicamento(self, id_medicamento):
        return self.repo.get(id_medicamento)

    def list_medicamentos(self):
        return self.repo.get_all()

    def update_medicamento(self, id_medicamento, nombre, descripcion, categoria, presentacion, requiere_receta=False):
        self.validar_texto(nombre, "Nombre")
        self.validar_categoria_presentacion(categoria, presentacion)
        self.validar_requiere_receta(requiere_receta)
        return self.repo.update(id_medicamento, nombre, descripcion, categoria, presentacion, requiere_receta)

    def delete_medicamento(self, id_medicamento):
        return self.repo.delete(id_medicamento)

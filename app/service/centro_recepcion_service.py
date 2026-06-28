from repository.centro_recepcion_repository import CentroRecepcionRepository

NOMBRES_CENTRO = [
    "Centro de Salud Central",
    "Clinica Comunitaria Norte",
    "Punto de Recepcion Sur"
]


class CentroRecepcionService:

    def __init__(self):
        self.repo = CentroRecepcionRepository()

    def get_nombres_centro(self):
        return NOMBRES_CENTRO

    def validar_nombre_centro(self, nombre):
        if nombre not in NOMBRES_CENTRO:
            raise ValueError("Nombre de centro no permitido")

    def validar_texto(self, valor, campo):
        if not valor or valor.strip() == "":
            raise ValueError(f"{campo} no puede estar vacio")

    def create_centro(self, id_centro, nombre, direccion, telefono, responsable):
        self.validar_nombre_centro(nombre)
        self.validar_texto(direccion, "Direccion")
        self.validar_texto(telefono, "Telefono")
        self.validar_texto(responsable, "Responsable")
        return self.repo.create(id_centro, nombre, direccion, telefono, responsable)

    def get_centro(self, id_centro):
        return self.repo.get(id_centro)

    def list_centros(self):
        return self.repo.get_all()

    def update_centro(self, id_centro, nombre, direccion, telefono, responsable):
        self.validar_nombre_centro(nombre)
        self.validar_texto(direccion, "Direccion")
        self.validar_texto(telefono, "Telefono")
        self.validar_texto(responsable, "Responsable")
        return self.repo.update(id_centro, nombre, direccion, telefono, responsable)

    def delete_centro(self, id_centro):
        return self.repo.delete(id_centro)

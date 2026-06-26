from app.repository.centro_recepcion_repository import CentroRecepcionRepository


class CentroRecepcionService:

    def __init__(self):
        self.repo = CentroRecepcionRepository()

    def create_centro(self, id_centro, nombre, direccion, telefono, responsable):
        return self.repo.create(id_centro, nombre, direccion, telefono, responsable)

    def get_centro(self, id_centro):
        return self.repo.get(id_centro)

    def list_centros(self):
        return self.repo.get_all()

    def update_centro(self, id_centro, nombre, direccion, telefono, responsable):
        return self.repo.update(id_centro, nombre, direccion, telefono, responsable)

    def delete_centro(self, id_centro):
        return self.repo.delete(id_centro)

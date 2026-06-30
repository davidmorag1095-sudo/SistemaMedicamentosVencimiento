from repository.centro_recepcion_repository import CentroRecepcionRepository

class CentroRecepcionService:

    def __init__(self):
        self.repo = CentroRecepcionRepository()
#--------------------------------------------------------------------------------------------------------------

    def get_nombres_centro(self):
        return [
            "Centro de Salud Central",
            "Clinica Comunitaria Norte",
            "Punto de Recepcion Sur"
        ]
#--------------------------------------------------------------------------------------------------------------

    def validar_nombre_centro(self, nombre):
        if not nombre.strip():
            raise ValueError("Debe completar todos los campos")

        if nombre not in self.get_nombres_centro():
            raise ValueError("Nombre de centro no permitido")
#--------------------------------------------------------------------------------------------------------------

    def create_centro(self, id_centro, nombre, direccion, telefono, responsable):
        if not nombre.strip() or not direccion.strip() or not telefono.strip() or not responsable.strip():
            raise ValueError("Debe completar todos los campos")

        self.validar_nombre_centro(nombre)
        return self.repo.create(id_centro, nombre, direccion, telefono, responsable)
#--------------------------------------------------------------------------------------------------------------

    def get_centro(self, id_centro):
        return self.repo.get(id_centro)
#--------------------------------------------------------------------------------------------------------------

    def list_centros(self):
        return self.repo.get_all()
#--------------------------------------------------------------------------------------------------------------

    def update_centro(self, id_centro, nombre, direccion, telefono, responsable):
        if not nombre.strip() or not direccion.strip() or not telefono.strip() or not responsable.strip():
            raise ValueError("Debe completar todos los campos")

        self.validar_nombre_centro(nombre)
        return self.repo.update(id_centro, nombre, direccion, telefono, responsable)
#--------------------------------------------------------------------------------------------------------------

    def delete_centro(self, id_centro):
        return self.repo.delete(id_centro)
#--------------------------------------------------------------------------------------------------------------

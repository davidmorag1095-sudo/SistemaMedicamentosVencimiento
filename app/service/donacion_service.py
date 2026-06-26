from app.repository.donacion_repository import DonacionRepository


class DonacionService:

    def __init__(self):
        self.repo = DonacionRepository()

    def create_donacion(self, id_donacion, id_usuario, id_centro, fecha_donacion, estado):
        return self.repo.create(id_donacion, id_usuario, id_centro, fecha_donacion, estado)

    def get_donacion(self, id_donacion):
        return self.repo.get(id_donacion)

    def list_donaciones(self):
        return self.repo.get_all()

    def update_donacion(self, id_donacion, id_usuario, id_centro, fecha_donacion, estado):
        return self.repo.update(id_donacion, id_usuario, id_centro, fecha_donacion, estado)

    def delete_donacion(self, id_donacion):
        return self.repo.delete(id_donacion)

    def create_detalle_donacion(self, id_detalle, id_donacion, id_medicamento, cantidad, fecha_vencimiento, lote, estado_medicamento):
        return self.repo.create_detalle(id_detalle, id_donacion, id_medicamento, cantidad, fecha_vencimiento, lote, estado_medicamento)

    def get_detalle_donacion(self, id_detalle):
        return self.repo.get_detalle(id_detalle)

    def list_detalles_donacion(self, id_donacion):
        return self.repo.get_detalles_by_donacion(id_donacion)

    def update_detalle_donacion(self, id_detalle, id_medicamento, cantidad, fecha_vencimiento, lote, estado_medicamento):
        return self.repo.update_detalle(id_detalle, id_medicamento, cantidad, fecha_vencimiento, lote, estado_medicamento)

    def delete_detalle_donacion(self, id_detalle):
        return self.repo.delete_detalle(id_detalle)

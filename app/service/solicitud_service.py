from app.repository.solicitud_repository import SolicitudRepository


class SolicitudService:

    def __init__(self):
        self.repo = SolicitudRepository()

    def create_solicitud(self, id_solicitud, id_usuario, fecha_solicitud, estado, observacion):
        return self.repo.create(id_solicitud, id_usuario, fecha_solicitud, estado, observacion)

    def get_solicitud(self, id_solicitud):
        return self.repo.get(id_solicitud)

    def list_solicitudes(self):
        return self.repo.get_all()

    def update_solicitud(self, id_solicitud, id_usuario, fecha_solicitud, estado, observacion):
        return self.repo.update(id_solicitud, id_usuario, fecha_solicitud, estado, observacion)

    def delete_solicitud(self, id_solicitud):
        return self.repo.delete(id_solicitud)

    def create_detalle_solicitud(self, id_detalle_solicitud, id_solicitud, id_medicamento, cantidad_solicitada, cantidad_aprobada):
        return self.repo.create_detalle(id_detalle_solicitud, id_solicitud, id_medicamento, cantidad_solicitada, cantidad_aprobada)

    def get_detalle_solicitud(self, id_detalle_solicitud):
        return self.repo.get_detalle(id_detalle_solicitud)

    def list_detalles_solicitud(self, id_solicitud):
        return self.repo.get_detalles_by_solicitud(id_solicitud)

    def update_detalle_solicitud(self, id_detalle_solicitud, id_medicamento, cantidad_solicitada, cantidad_aprobada):
        return self.repo.update_detalle(id_detalle_solicitud, id_medicamento, cantidad_solicitada, cantidad_aprobada)

    def delete_detalle_solicitud(self, id_detalle_solicitud):
        return self.repo.delete_detalle(id_detalle_solicitud)

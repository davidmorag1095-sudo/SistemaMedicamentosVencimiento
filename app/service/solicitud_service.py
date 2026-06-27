from repository.medicamento_repository import MedicamentoRepository
from repository.solicitud_repository import SolicitudRepository
from repository.usuario_repository import UsuarioRepository


class SolicitudService:

    def __init__(self):
        self.repo = SolicitudRepository()
        self.usuario_repo = UsuarioRepository()
        self.medicamento_repo = MedicamentoRepository()

    def create_solicitud(self, id_solicitud, id_usuario, fecha_solicitud, estado, observacion):
        self.validar_solicitud(id_usuario, estado)
        return self.repo.create(id_solicitud, id_usuario, fecha_solicitud, estado, observacion)

    def get_solicitud(self, id_solicitud):
        return self.repo.get(id_solicitud)

    def list_solicitudes(self):
        return self.repo.get_all()

    def update_solicitud(self, id_solicitud, id_usuario, fecha_solicitud, estado, observacion):
        self.validar_solicitud(id_usuario, estado)
        return self.repo.update(id_solicitud, id_usuario, fecha_solicitud, estado, observacion)

    def delete_solicitud(self, id_solicitud):
        return self.repo.delete(id_solicitud)

    def create_detalle_solicitud(self, id_detalle_solicitud, id_solicitud, id_medicamento, cantidad_solicitada, cantidad_aprobada):
        self.validar_detalle_solicitud(id_solicitud, id_medicamento, cantidad_solicitada, cantidad_aprobada)
        return self.repo.create_detalle(id_detalle_solicitud, id_solicitud, id_medicamento, cantidad_solicitada, cantidad_aprobada)

    def get_detalle_solicitud(self, id_detalle_solicitud):
        return self.repo.get_detalle(id_detalle_solicitud)

    def list_detalles_solicitud(self, id_solicitud):
        return self.repo.get_detalles_by_solicitud(id_solicitud)

    def update_detalle_solicitud(self, id_detalle_solicitud, id_medicamento, cantidad_solicitada, cantidad_aprobada):
        detalle = self.repo.get_detalle(id_detalle_solicitud)

        if not detalle:
            raise ValueError("Detalle de solicitud no encontrado")

        self.validar_detalle_solicitud(detalle.id_solicitud, id_medicamento, cantidad_solicitada, cantidad_aprobada)
        return self.repo.update_detalle(id_detalle_solicitud, id_medicamento, cantidad_solicitada, cantidad_aprobada)

    def delete_detalle_solicitud(self, id_detalle_solicitud):
        return self.repo.delete_detalle(id_detalle_solicitud)

    def validar_solicitud(self, id_usuario, estado):
        estados_validos = ["pendiente", "aprobada", "rechazada", "entregada"]

        if not self.usuario_repo.get(id_usuario):
            raise ValueError("Usuario no encontrado")

        if estado not in estados_validos:
            raise ValueError("Estado de solicitud no valido")

    def validar_detalle_solicitud(self, id_solicitud, id_medicamento, cantidad_solicitada, cantidad_aprobada):
        if not self.repo.get(id_solicitud):
            raise ValueError("Solicitud no encontrada")

        if not self.medicamento_repo.get(id_medicamento):
            raise ValueError("Medicamento no encontrado")

        if cantidad_solicitada <= 0:
            raise ValueError("La cantidad solicitada debe ser mayor que cero")

        if cantidad_aprobada < 0:
            raise ValueError("La cantidad aprobada no puede ser negativa")

        if cantidad_aprobada > cantidad_solicitada:
            raise ValueError("La cantidad aprobada no puede ser mayor que la solicitada")

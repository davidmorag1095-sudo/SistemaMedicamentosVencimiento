from datetime import date, datetime

from repository.donacion_repository import DonacionRepository
from repository.entrega_repository import EntregaRepository
from repository.solicitud_repository import SolicitudRepository
from repository.usuario_repository import UsuarioRepository


class EntregaService:

    def __init__(self):
        self.repo = EntregaRepository()
        self.donacion_repo = DonacionRepository()
        self.solicitud_repo = SolicitudRepository()
        self.usuario_repo = UsuarioRepository()
#--------------------------------------------------------------------------------------------------------------

    def create_entrega(self, id_entrega, id_solicitud, id_detalle_donacion, id_usuario, cantidad_entregada, fecha_entrega):
        self.validar_entrega(None, id_solicitud, id_detalle_donacion, id_usuario, cantidad_entregada)
        return self.repo.create(id_entrega, id_solicitud, id_detalle_donacion, id_usuario, cantidad_entregada, fecha_entrega)
#--------------------------------------------------------------------------------------------------------------

    def get_entrega(self, id_entrega):
        return self.repo.get(id_entrega)
#--------------------------------------------------------------------------------------------------------------

    def list_entregas(self):
        return self.repo.get_all()
#--------------------------------------------------------------------------------------------------------------

    def update_entrega(self, id_entrega, id_solicitud, id_detalle_donacion, id_usuario, cantidad_entregada, fecha_entrega):
        self.validar_entrega(id_entrega, id_solicitud, id_detalle_donacion, id_usuario, cantidad_entregada)
        return self.repo.update(id_entrega, id_solicitud, id_detalle_donacion, id_usuario, cantidad_entregada, fecha_entrega)
#--------------------------------------------------------------------------------------------------------------

    def delete_entrega(self, id_entrega):
        return self.repo.delete(id_entrega)
#--------------------------------------------------------------------------------------------------------------

    def validar_entrega(self, id_entrega, id_solicitud, id_detalle_donacion, id_usuario, cantidad_entregada):
        solicitud = self.solicitud_repo.get(id_solicitud)
        detalle_donacion = self.donacion_repo.get_detalle(id_detalle_donacion)

        if not solicitud:
            raise ValueError("Solicitud no encontrada")

        if not detalle_donacion:
            raise ValueError("Detalle de donacion no encontrado")

        if not self.usuario_repo.get(id_usuario):
            raise ValueError("Usuario no encontrado")

        if cantidad_entregada <= 0:
            raise ValueError("La cantidad entregada debe ser mayor que cero")

        fecha_vencimiento = detalle_donacion.fecha_vencimiento
        fecha = fecha_vencimiento.date() if isinstance(fecha_vencimiento, datetime) else fecha_vencimiento

        if fecha <= date.today():
            raise ValueError("No se puede entregar un medicamento vencido")

        cantidad_entregada_actual = self.repo.get_cantidad_entregada_by_detalle(id_detalle_donacion, id_entrega)
        cantidad_disponible = detalle_donacion.cantidad - cantidad_entregada_actual

        if cantidad_entregada > cantidad_disponible:
            raise ValueError("No hay stock suficiente para la entrega")
#--------------------------------------------------------------------------------------------------------------

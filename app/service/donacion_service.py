from datetime import date, datetime

from repository.centro_recepcion_repository import CentroRecepcionRepository
from repository.donacion_repository import DonacionRepository
from repository.medicamento_repository import MedicamentoRepository
from repository.usuario_repository import UsuarioRepository


class DonacionService:

    def __init__(self):
        self.repo = DonacionRepository()
        self.usuario_repo = UsuarioRepository()
        self.centro_repo = CentroRecepcionRepository()
        self.medicamento_repo = MedicamentoRepository()

    def create_donacion(self, id_donacion, id_usuario, id_centro, fecha_donacion, estado):
        self.validar_donacion(id_usuario, id_centro)
        return self.repo.create(id_donacion, id_usuario, id_centro, fecha_donacion, estado)

    def get_donacion(self, id_donacion):
        return self.repo.get(id_donacion)

    def list_donaciones(self):
        return self.repo.get_all()

    def update_donacion(self, id_donacion, id_usuario, id_centro, fecha_donacion, estado):
        self.validar_donacion(id_usuario, id_centro)
        return self.repo.update(id_donacion, id_usuario, id_centro, fecha_donacion, estado)

    def delete_donacion(self, id_donacion):
        return self.repo.delete(id_donacion)

    def create_detalle_donacion(self, id_detalle, id_donacion, id_medicamento, cantidad, fecha_vencimiento, lote, estado_medicamento):
        self.validar_detalle_donacion(id_donacion, id_medicamento, cantidad, fecha_vencimiento, estado_medicamento)
        return self.repo.create_detalle(id_detalle, id_donacion, id_medicamento, cantidad, fecha_vencimiento, lote, estado_medicamento)

    def get_detalle_donacion(self, id_detalle):
        return self.repo.get_detalle(id_detalle)

    def list_detalles_donacion(self, id_donacion):
        return self.repo.get_detalles_by_donacion(id_donacion)

    def update_detalle_donacion(self, id_detalle, id_medicamento, cantidad, fecha_vencimiento, lote, estado_medicamento):
        detalle = self.repo.get_detalle(id_detalle)

        if not detalle:
            raise ValueError("Detalle de donacion no encontrado")

        self.validar_detalle_donacion(detalle.id_donacion, id_medicamento, cantidad, fecha_vencimiento, estado_medicamento)
        return self.repo.update_detalle(id_detalle, id_medicamento, cantidad, fecha_vencimiento, lote, estado_medicamento)

    def delete_detalle_donacion(self, id_detalle):
        return self.repo.delete_detalle(id_detalle)

    def validar_donacion(self, id_usuario, id_centro):
        if not self.usuario_repo.get(id_usuario):
            raise ValueError("Usuario no encontrado")

        if not self.centro_repo.get(id_centro):
            raise ValueError("Centro de recepcion no encontrado")

    def validar_detalle_donacion(self, id_donacion, id_medicamento, cantidad, fecha_vencimiento, estado_medicamento):
        estados_validos = ["disponible", "entregado", "vencido", "descartado"]

        if not self.repo.get(id_donacion):
            raise ValueError("Donacion no encontrada")

        if not self.medicamento_repo.get(id_medicamento):
            raise ValueError("Medicamento no encontrado")

        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero")

        fecha = fecha_vencimiento.date() if isinstance(fecha_vencimiento, datetime) else fecha_vencimiento

        if fecha <= date.today():
            raise ValueError("No se puede registrar un medicamento vencido")

        if estado_medicamento not in estados_validos:
            raise ValueError("Estado de medicamento no valido")

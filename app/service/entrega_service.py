from app.repository.entrega_repository import EntregaRepository


class EntregaService:

    def __init__(self):
        self.repo = EntregaRepository()

    def create_entrega(self, id_entrega, id_solicitud, id_detalle_donacion, id_usuario, cantidad_entregada, fecha_entrega):
        return self.repo.create(id_entrega, id_solicitud, id_detalle_donacion, id_usuario, cantidad_entregada, fecha_entrega)

    def get_entrega(self, id_entrega):
        return self.repo.get(id_entrega)

    def list_entregas(self):
        return self.repo.get_all()

    def update_entrega(self, id_entrega, id_solicitud, id_detalle_donacion, id_usuario, cantidad_entregada, fecha_entrega):
        return self.repo.update(id_entrega, id_solicitud, id_detalle_donacion, id_usuario, cantidad_entregada, fecha_entrega)

    def delete_entrega(self, id_entrega):
        return self.repo.delete(id_entrega)

from app.config.database import SessionLocal
from app.entity.entrega import EntregaORM


class EntregaRepository():
    def __init__(self):
        self.db = SessionLocal()

    def save(self, id_entrega, id_solicitud, id_detalle_donacion, id_usuario, cantidad_entregada, fecha_entrega):
        entrega = EntregaORM(
            id_entrega=id_entrega,
            id_solicitud=id_solicitud,
            id_detalle_donacion=id_detalle_donacion,
            id_usuario=id_usuario,
            cantidad_entregada=cantidad_entregada,
            fecha_entrega=fecha_entrega
        )
        self.db.add(entrega)
        self.db.commit()
        return entrega

    def get_all(self):
        return self.db.query(EntregaORM).all()

    def get_by_id(self, id_entrega):
        return self.db.query(EntregaORM).filter_by(id_entrega=id_entrega).first()

    def update(self, id_entrega, id_solicitud, id_detalle_donacion, id_usuario, cantidad_entregada, fecha_entrega):
        entrega = self.get_by_id(id_entrega)

        if entrega:
            entrega.id_solicitud = id_solicitud
            entrega.id_detalle_donacion = id_detalle_donacion
            entrega.id_usuario = id_usuario
            entrega.cantidad_entregada = cantidad_entregada
            entrega.fecha_entrega = fecha_entrega
            self.db.commit()
        return entrega

    def delete(self, id_entrega):
        entrega = self.get_by_id(id_entrega)

        if entrega:
            self.db.delete(entrega)
            self.db.commit()
        return entrega

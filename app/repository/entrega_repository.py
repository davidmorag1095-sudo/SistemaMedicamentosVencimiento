from sqlalchemy import func

from config.database import SessionLocal
from entity.entrega import EntregaORM


class EntregaRepository():
    def __init__(self):
        self.db = SessionLocal()

    def create(self, id_entrega, id_solicitud, id_detalle_donacion, id_usuario, cantidad_entregada, fecha_entrega):
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

    def get(self, id_entrega):
        return self.db.query(EntregaORM).filter_by(id_entrega=id_entrega).first()

    def get_cantidad_entregada_by_detalle(self, id_detalle_donacion, id_entrega=None):
        consulta = self.db.query(func.coalesce(func.sum(EntregaORM.cantidad_entregada), 0)).filter_by(
            id_detalle_donacion=id_detalle_donacion
        )

        if id_entrega is not None:
            consulta = consulta.filter(EntregaORM.id_entrega != id_entrega)

        return consulta.scalar()

    def update(self, id_entrega, id_solicitud, id_detalle_donacion, id_usuario, cantidad_entregada, fecha_entrega):
        entrega = self.get(id_entrega)

        if entrega:
            entrega.id_solicitud = id_solicitud
            entrega.id_detalle_donacion = id_detalle_donacion
            entrega.id_usuario = id_usuario
            entrega.cantidad_entregada = cantidad_entregada
            entrega.fecha_entrega = fecha_entrega
            self.db.commit()
        return entrega

    def delete(self, id_entrega):
        entrega = self.get(id_entrega)

        if entrega:
            self.db.delete(entrega)
            self.db.commit()
        return entrega

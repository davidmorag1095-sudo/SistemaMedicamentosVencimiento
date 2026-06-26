from app.config.database import SessionLocal
from app.entity.donacion import DonacionORM, DetalleDonacionORM


class DonacionRepository():
    def __init__(self):
        self.db = SessionLocal()

    def save(self, id_donacion, id_usuario, id_centro, fecha_donacion, estado):
        donacion = DonacionORM(
            id_donacion=id_donacion,
            id_usuario=id_usuario,
            id_centro=id_centro,
            fecha_donacion=fecha_donacion,
            estado=estado
        )
        self.db.add(donacion)
        self.db.commit()
        return donacion

    def get_all(self):
        return self.db.query(DonacionORM).all()

    def get_by_id(self, id_donacion):
        return self.db.query(DonacionORM).filter_by(id_donacion=id_donacion).first()

    def save_detalle(self, id_detalle, id_donacion, id_medicamento, cantidad, fecha_vencimiento, lote, estado_medicamento):
        detalle = DetalleDonacionORM(
            id_detalle=id_detalle,
            id_donacion=id_donacion,
            id_medicamento=id_medicamento,
            cantidad=cantidad,
            fecha_vencimiento=fecha_vencimiento,
            lote=lote,
            estado_medicamento=estado_medicamento
        )
        self.db.add(detalle)
        self.db.commit()
        return detalle

    def get_detalle_by_id(self, id_detalle):
        return self.db.query(DetalleDonacionORM).filter_by(id_detalle=id_detalle).first()

    def get_detalles_by_donacion(self, id_donacion):
        return self.db.query(DetalleDonacionORM).filter_by(id_donacion=id_donacion).all()

    def update(self, id_donacion, id_usuario, id_centro, fecha_donacion, estado):
        donacion = self.get_by_id(id_donacion)

        if donacion:
            donacion.id_usuario = id_usuario
            donacion.id_centro = id_centro
            donacion.fecha_donacion = fecha_donacion
            donacion.estado = estado
            self.db.commit()
        return donacion

    def update_detalle(self, id_detalle, id_medicamento, cantidad, fecha_vencimiento, lote, estado_medicamento):
        detalle = self.get_detalle_by_id(id_detalle)

        if detalle:
            detalle.id_medicamento = id_medicamento
            detalle.cantidad = cantidad
            detalle.fecha_vencimiento = fecha_vencimiento
            detalle.lote = lote
            detalle.estado_medicamento = estado_medicamento
            self.db.commit()
        return detalle

    def delete(self, id_donacion):
        donacion = self.get_by_id(id_donacion)

        if donacion:
            self.db.delete(donacion)
            self.db.commit()
        return donacion

    def delete_detalle(self, id_detalle):
        detalle = self.get_detalle_by_id(id_detalle)

        if detalle:
            self.db.delete(detalle)
            self.db.commit()
        return detalle

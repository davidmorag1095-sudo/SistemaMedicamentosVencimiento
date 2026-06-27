from config.database import SessionLocal
from entity.solicitud import SolicitudORM, DetalleSolicitudORM


class SolicitudRepository():
    def __init__(self):
        self.db = SessionLocal()

    def create(self, id_solicitud, id_usuario, fecha_solicitud, estado, observacion):
        solicitud = SolicitudORM(
            id_solicitud=id_solicitud,
            id_usuario=id_usuario,
            fecha_solicitud=fecha_solicitud,
            estado=estado,
            observacion=observacion
        )
        self.db.add(solicitud)
        self.db.commit()
        return solicitud

    def get_all(self):
        return self.db.query(SolicitudORM).all()

    def get(self, id_solicitud):
        return self.db.query(SolicitudORM).filter_by(id_solicitud=id_solicitud).first()

    def create_detalle(self, id_detalle_solicitud, id_solicitud, id_medicamento, cantidad_solicitada, cantidad_aprobada):
        detalle = DetalleSolicitudORM(
            id_detalle_solicitud=id_detalle_solicitud,
            id_solicitud=id_solicitud,
            id_medicamento=id_medicamento,
            cantidad_solicitada=cantidad_solicitada,
            cantidad_aprobada=cantidad_aprobada
        )
        self.db.add(detalle)
        self.db.commit()
        return detalle

    def get_detalle(self, id_detalle_solicitud):
        return self.db.query(DetalleSolicitudORM).filter_by(id_detalle_solicitud=id_detalle_solicitud).first()

    def get_detalles_by_solicitud(self, id_solicitud):
        return self.db.query(DetalleSolicitudORM).filter_by(id_solicitud=id_solicitud).all()

    def update(self, id_solicitud, id_usuario, fecha_solicitud, estado, observacion):
        solicitud = self.get(id_solicitud)

        if solicitud:
            solicitud.id_usuario = id_usuario
            solicitud.fecha_solicitud = fecha_solicitud
            solicitud.estado = estado
            solicitud.observacion = observacion
            self.db.commit()
        return solicitud

    def update_detalle(self, id_detalle_solicitud, id_medicamento, cantidad_solicitada, cantidad_aprobada):
        detalle = self.get_detalle(id_detalle_solicitud)

        if detalle:
            detalle.id_medicamento = id_medicamento
            detalle.cantidad_solicitada = cantidad_solicitada
            detalle.cantidad_aprobada = cantidad_aprobada
            self.db.commit()
        return detalle

    def delete(self, id_solicitud):
        solicitud = self.get(id_solicitud)

        if solicitud:
            self.db.delete(solicitud)
            self.db.commit()
        return solicitud

    def delete_detalle(self, id_detalle_solicitud):
        detalle = self.get_detalle(id_detalle_solicitud)

        if detalle:
            self.db.delete(detalle)
            self.db.commit()
        return detalle

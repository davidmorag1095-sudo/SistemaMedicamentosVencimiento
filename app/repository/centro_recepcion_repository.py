from config.database import SessionLocal
from entity.centro_recepcion import CentroRecepcionORM


class CentroRecepcionRepository():
    def __init__(self):
        self.db = SessionLocal()

    def create(self, id_centro, nombre, direccion, telefono, responsable):
        datos_centro = {
            "nombre": nombre,
            "direccion": direccion,
            "telefono": telefono,
            "responsable": responsable
        }

        if id_centro is not None:
            datos_centro["id_centro"] = id_centro

        centro = CentroRecepcionORM(**datos_centro)
        self.db.add(centro)
        self.db.commit()
        self.db.refresh(centro)
        return centro

    def get_all(self):
        return self.db.query(CentroRecepcionORM).all()

    def get(self, id_centro):
        return self.db.query(CentroRecepcionORM).filter_by(id_centro=id_centro).first()

    def update(self, id_centro, nombre, direccion, telefono, responsable):
        centro = self.get(id_centro)

        if centro:
            centro.nombre = nombre
            centro.direccion = direccion
            centro.telefono = telefono
            centro.responsable = responsable
            self.db.commit()
        return centro

    def delete(self, id_centro):
        centro = self.get(id_centro)

        if centro:
            self.db.delete(centro)
            self.db.commit()
        return centro

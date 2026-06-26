from app.config.database import SessionLocal
from app.entity.medicamento import MedicamentoORM


class MedicamentoRepository():
    def __init__(self):
        self.db = SessionLocal()

    def create(self, id_medicamento, nombre, descripcion, categoria, presentacion, requiere_receta=False):
        medicamento = MedicamentoORM(
            id_medicamento=id_medicamento,
            nombre=nombre,
            descripcion=descripcion,
            categoria=categoria,
            presentacion=presentacion,
            requiere_receta=requiere_receta
        )
        self.db.add(medicamento)
        self.db.commit()
        return medicamento

    def get_all(self):
        return self.db.query(MedicamentoORM).all()

    def get(self, id_medicamento):
        return self.db.query(MedicamentoORM).filter_by(id_medicamento=id_medicamento).first()

    def update(self, id_medicamento, nombre, descripcion, categoria, presentacion, requiere_receta=False):
        medicamento = self.get(id_medicamento)

        if medicamento:
            medicamento.nombre = nombre
            medicamento.descripcion = descripcion
            medicamento.categoria = categoria
            medicamento.presentacion = presentacion
            medicamento.requiere_receta = requiere_receta
            self.db.commit()
        return medicamento

    def delete(self, id_medicamento):
        medicamento = self.get(id_medicamento)

        if medicamento:
            self.db.delete(medicamento)
            self.db.commit()
        return medicamento

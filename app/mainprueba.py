from config.database import init_db
from service.medicamento_service import MedicamentoService


def menu():
    print("\n=== SISTEMA DE MEDICAMENTOS ===")
    print("1. Agregar medicamento")
    print("2. Buscar medicamento")
    print("3. Listar medicamentos")
    print("4. Actualizar medicamento")
    print("5. Eliminar medicamento")
    print("6. Salir")


def mostrar_medicamento(medicamento):
    if medicamento:
        print(f"Id: {medicamento.id_medicamento}")
        print(f"Nombre: {medicamento.nombre}")
        print(f"Descripcion: {medicamento.descripcion}")
        print(f"Categoria: {medicamento.categoria}")
        print(f"Presentacion: {medicamento.presentacion}")
        print(f"Requiere receta: {medicamento.requiere_receta}")
    else:
        print("No se encontro el medicamento")


def leer_requiere_receta():
    respuesta = input("Requiere receta? S/N: ").strip().lower()
    return respuesta == "s"


def agregar_medicamento(service):
    id_medicamento = int(input("Id medicamento: "))
    nombre = input("Nombre: ")
    descripcion = input("Descripcion: ")
    categoria = input("Categoria: ")
    presentacion = input("Presentacion: ")
    requiere_receta = leer_requiere_receta()

    service.create_medicamento(
        id_medicamento,
        nombre,
        descripcion,
        categoria,
        presentacion,
        requiere_receta
    )
    print("Medicamento agregado correctamente")


def buscar_medicamento(service):
    id_medicamento = int(input("Id medicamento: "))
    medicamento = service.get_medicamento(id_medicamento)
    mostrar_medicamento(medicamento)


def listar_medicamentos(service):
    medicamentos = service.list_medicamentos()

    if not medicamentos:
        print("No hay medicamentos registrados")
        return

    for medicamento in medicamentos:
        print("------------------------------")
        mostrar_medicamento(medicamento)


def actualizar_medicamento(service):
    id_medicamento = int(input("Id medicamento: "))
    nombre = input("Nuevo nombre: ")
    descripcion = input("Nueva descripcion: ")
    categoria = input("Nueva categoria: ")
    presentacion = input("Nueva presentacion: ")
    requiere_receta = leer_requiere_receta()

    medicamento = service.update_medicamento(
        id_medicamento,
        nombre,
        descripcion,
        categoria,
        presentacion,
        requiere_receta
    )

    if medicamento:
        print("Medicamento actualizado correctamente")
    else:
        print("No se encontro el medicamento")


def eliminar_medicamento(service):
    id_medicamento = int(input("Id medicamento: "))
    medicamento = service.delete_medicamento(id_medicamento)

    if medicamento:
        print("Medicamento eliminado correctamente")
    else:
        print("No se encontro el medicamento")


if __name__ == "__main__":
    init_db()
    service = MedicamentoService()

    while True:
        menu()
        opcion = input("Seleccione una opcion: ")

        try:
            if opcion == "1":
                agregar_medicamento(service)

            elif opcion == "2":
                buscar_medicamento(service)

            elif opcion == "3":
                listar_medicamentos(service)

            elif opcion == "4":
                actualizar_medicamento(service)

            elif opcion == "5":
                eliminar_medicamento(service)

            elif opcion == "6":
                print("Saliendo del sistema")
                break

            else:
                print("Opcion invalida")

        except Exception as error:
            service.repo.db.rollback()
            print(f"Error: {error}")

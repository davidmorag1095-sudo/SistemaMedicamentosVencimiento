from datetime import date, datetime

from config.database import init_db
from service.centro_recepcion_service import CentroRecepcionService
from service.donacion_service import DonacionService
from service.entrega_service import EntregaService
from service.medicamento_service import MedicamentoService
from service.solicitud_service import SolicitudService
from service.usuario_service import UsuarioService


def menu_principal():
    print("\n=== SISTEMA DE MEDICAMENTOS ===")
    print("1. Usuarios")
    print("2. Centros de recepcion")
    print("3. Medicamentos")
    print("4. Donaciones")
    print("5. Solicitudes")
    print("6. Entregas")
    print("7. Salir")


def leer_opcion(titulo, opciones):
    print(f"\n{titulo}")

    for indice, opcion in enumerate(opciones, start=1):
        print(f"{indice}. {opcion}")

    seleccion = int(input("Seleccione una opcion: "))

    if seleccion < 1 or seleccion > len(opciones):
        raise ValueError("Opcion invalida")

    return opciones[seleccion - 1]


def leer_texto_default(mensaje, valor_default):
    valor = input(f"{mensaje} ({valor_default}): ").strip()
    return valor if valor else valor_default


def leer_fecha(mensaje):
    valor = input(f"{mensaje} (YYYY-MM-DD): ").strip()
    return date.fromisoformat(valor)


def leer_fecha_hora(mensaje):
    valor = input(f"{mensaje} (YYYY-MM-DD HH:MM, enter para ahora): ").strip()

    if valor == "":
        return datetime.now()

    return datetime.strptime(valor, "%Y-%m-%d %H:%M")


def leer_si_no(mensaje):
    respuesta = input(f"{mensaje} S/N: ").strip().lower()
    return respuesta == "s"


def rollback_services(services):
    for service in services.values():
        for repo in service.__dict__.values():
            if hasattr(repo, "db"):
                repo.db.rollback()


def ejecutar_accion(accion, services):
    try:
        accion()
    except Exception as error:
        rollback_services(services)
        print(f"Error: {error}")


def mostrar_usuario(usuario):
    if usuario:
        print(f"Id: {usuario.id_usuario}")
        print(f"Nombre: {usuario.nombre}")
        print(f"Correo: {usuario.correo}")
        print(f"Rol: {usuario.rol}")
        print(f"Activo: {usuario.activo}")
    else:
        print("No se encontro el usuario")


def agregar_usuario(service):
    id_usuario = int(input("Id usuario: "))
    nombre = input("Nombre: ")
    correo = input("Correo: ")
    contrasena = input("Contrasena: ")
    rol = input("Rol: ")
    activo = leer_si_no("Activo?")

    service.create_usuario(id_usuario, nombre, correo, contrasena, rol, activo)
    print("Usuario agregado correctamente")


def buscar_usuario(service):
    id_usuario = int(input("Id usuario: "))
    mostrar_usuario(service.get_usuario(id_usuario))


def listar_usuarios(service):
    usuarios = service.list_usuarios()

    if not usuarios:
        print("No hay usuarios registrados")
        return

    for usuario in usuarios:
        print("------------------------------")
        mostrar_usuario(usuario)


def actualizar_usuario(service):
    id_usuario = int(input("Id usuario: "))
    nombre = input("Nuevo nombre: ")
    correo = input("Nuevo correo: ")
    contrasena = input("Nueva contrasena: ")
    rol = input("Nuevo rol: ")
    activo = leer_si_no("Activo?")

    usuario = service.update_usuario(id_usuario, nombre, correo, contrasena, rol, activo)

    if usuario:
        print("Usuario actualizado correctamente")
    else:
        print("No se encontro el usuario")


def eliminar_usuario(service):
    id_usuario = int(input("Id usuario: "))
    usuario = service.delete_usuario(id_usuario)

    if usuario:
        print("Usuario eliminado correctamente")
    else:
        print("No se encontro el usuario")


def menu_usuarios(service, services):
    while True:
        print("\n=== USUARIOS ===")
        print("1. Agregar usuario")
        print("2. Buscar usuario")
        print("3. Listar usuarios")
        print("4. Actualizar usuario")
        print("5. Eliminar usuario")
        print("6. Volver")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            ejecutar_accion(lambda: agregar_usuario(service), services)
        elif opcion == "2":
            ejecutar_accion(lambda: buscar_usuario(service), services)
        elif opcion == "3":
            ejecutar_accion(lambda: listar_usuarios(service), services)
        elif opcion == "4":
            ejecutar_accion(lambda: actualizar_usuario(service), services)
        elif opcion == "5":
            ejecutar_accion(lambda: eliminar_usuario(service), services)
        elif opcion == "6":
            break
        else:
            print("Opcion invalida")


def mostrar_centro(centro):
    if centro:
        print(f"Id: {centro.id_centro}")
        print(f"Nombre: {centro.nombre}")
        print(f"Direccion: {centro.direccion}")
        print(f"Telefono: {centro.telefono}")
        print(f"Responsable: {centro.responsable}")
    else:
        print("No se encontro el centro")


def agregar_centro(service):
    id_centro = int(input("Id centro: "))
    nombre = input("Nombre: ")
    direccion = input("Direccion: ")
    telefono = input("Telefono: ")
    responsable = input("Responsable: ")

    service.create_centro(id_centro, nombre, direccion, telefono, responsable)
    print("Centro agregado correctamente")


def buscar_centro(service):
    id_centro = int(input("Id centro: "))
    mostrar_centro(service.get_centro(id_centro))


def listar_centros(service):
    centros = service.list_centros()

    if not centros:
        print("No hay centros registrados")
        return

    for centro in centros:
        print("------------------------------")
        mostrar_centro(centro)


def actualizar_centro(service):
    id_centro = int(input("Id centro: "))
    nombre = input("Nuevo nombre: ")
    direccion = input("Nueva direccion: ")
    telefono = input("Nuevo telefono: ")
    responsable = input("Nuevo responsable: ")

    centro = service.update_centro(id_centro, nombre, direccion, telefono, responsable)

    if centro:
        print("Centro actualizado correctamente")
    else:
        print("No se encontro el centro")


def eliminar_centro(service):
    id_centro = int(input("Id centro: "))
    centro = service.delete_centro(id_centro)

    if centro:
        print("Centro eliminado correctamente")
    else:
        print("No se encontro el centro")


def menu_centros(service, services):
    while True:
        print("\n=== CENTROS DE RECEPCION ===")
        print("1. Agregar centro")
        print("2. Buscar centro")
        print("3. Listar centros")
        print("4. Actualizar centro")
        print("5. Eliminar centro")
        print("6. Volver")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            ejecutar_accion(lambda: agregar_centro(service), services)
        elif opcion == "2":
            ejecutar_accion(lambda: buscar_centro(service), services)
        elif opcion == "3":
            ejecutar_accion(lambda: listar_centros(service), services)
        elif opcion == "4":
            ejecutar_accion(lambda: actualizar_centro(service), services)
        elif opcion == "5":
            ejecutar_accion(lambda: eliminar_centro(service), services)
        elif opcion == "6":
            break
        else:
            print("Opcion invalida")


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


def leer_categoria(service):
    return leer_opcion("Categorias", service.get_categorias())


def leer_presentacion(service):
    return leer_opcion("Presentaciones", service.get_presentaciones())


def agregar_medicamento(service):
    id_medicamento = int(input("Id medicamento: "))
    nombre = input("Nombre: ")
    descripcion = input("Descripcion: ")
    categoria = leer_categoria(service)
    presentacion = leer_presentacion(service)
    requiere_receta = leer_si_no("Requiere receta?")

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
    categoria = leer_categoria(service)
    presentacion = leer_presentacion(service)
    requiere_receta = leer_si_no("Requiere receta?")

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


def menu_medicamentos(service, services):
    while True:
        print("\n=== MEDICAMENTOS ===")
        print("1. Agregar medicamento")
        print("2. Buscar medicamento")
        print("3. Listar medicamentos")
        print("4. Actualizar medicamento")
        print("5. Eliminar medicamento")
        print("6. Volver")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            ejecutar_accion(lambda: agregar_medicamento(service), services)
        elif opcion == "2":
            ejecutar_accion(lambda: buscar_medicamento(service), services)
        elif opcion == "3":
            ejecutar_accion(lambda: listar_medicamentos(service), services)
        elif opcion == "4":
            ejecutar_accion(lambda: actualizar_medicamento(service), services)
        elif opcion == "5":
            ejecutar_accion(lambda: eliminar_medicamento(service), services)
        elif opcion == "6":
            break
        else:
            print("Opcion invalida")


def mostrar_donacion(donacion):
    if donacion:
        print(f"Id: {donacion.id_donacion}")
        print(f"Id usuario: {donacion.id_usuario}")
        print(f"Id centro: {donacion.id_centro}")
        print(f"Fecha: {donacion.fecha_donacion}")
        print(f"Estado: {donacion.estado}")
    else:
        print("No se encontro la donacion")


def mostrar_detalle_donacion(detalle):
    if detalle:
        print(f"Id detalle: {detalle.id_detalle}")
        print(f"Id donacion: {detalle.id_donacion}")
        print(f"Id medicamento: {detalle.id_medicamento}")
        print(f"Cantidad: {detalle.cantidad}")
        print(f"Fecha vencimiento: {detalle.fecha_vencimiento}")
        print(f"Lote: {detalle.lote}")
        print(f"Estado medicamento: {detalle.estado_medicamento}")
    else:
        print("No se encontro el detalle")


def leer_estado_medicamento():
    estados = ["disponible", "entregado", "vencido", "descartado"]
    return leer_opcion("Estados de medicamento", estados)


def agregar_donacion(service):
    id_donacion = int(input("Id donacion: "))
    id_usuario = int(input("Id usuario: "))
    id_centro = int(input("Id centro: "))
    fecha_donacion = leer_fecha_hora("Fecha de donacion")
    estado = leer_texto_default("Estado", "registrada")

    service.create_donacion(id_donacion, id_usuario, id_centro, fecha_donacion, estado)
    print("Donacion agregada correctamente")


def buscar_donacion(service):
    id_donacion = int(input("Id donacion: "))
    mostrar_donacion(service.get_donacion(id_donacion))


def listar_donaciones(service):
    donaciones = service.list_donaciones()

    if not donaciones:
        print("No hay donaciones registradas")
        return

    for donacion in donaciones:
        print("------------------------------")
        mostrar_donacion(donacion)


def actualizar_donacion(service):
    id_donacion = int(input("Id donacion: "))
    id_usuario = int(input("Id usuario: "))
    id_centro = int(input("Id centro: "))
    fecha_donacion = leer_fecha_hora("Nueva fecha de donacion")
    estado = leer_texto_default("Estado", "registrada")

    donacion = service.update_donacion(id_donacion, id_usuario, id_centro, fecha_donacion, estado)

    if donacion:
        print("Donacion actualizada correctamente")
    else:
        print("No se encontro la donacion")


def eliminar_donacion(service):
    id_donacion = int(input("Id donacion: "))
    donacion = service.delete_donacion(id_donacion)

    if donacion:
        print("Donacion eliminada correctamente")
    else:
        print("No se encontro la donacion")


def agregar_detalle_donacion(service):
    id_detalle = int(input("Id detalle: "))
    id_donacion = int(input("Id donacion: "))
    id_medicamento = int(input("Id medicamento: "))
    cantidad = int(input("Cantidad: "))
    fecha_vencimiento = leer_fecha("Fecha de vencimiento")
    lote = input("Lote: ")
    estado_medicamento = leer_estado_medicamento()

    service.create_detalle_donacion(
        id_detalle,
        id_donacion,
        id_medicamento,
        cantidad,
        fecha_vencimiento,
        lote,
        estado_medicamento
    )
    print("Detalle de donacion agregado correctamente")


def buscar_detalle_donacion(service):
    id_detalle = int(input("Id detalle: "))
    mostrar_detalle_donacion(service.get_detalle_donacion(id_detalle))


def listar_detalles_donacion(service):
    id_donacion = int(input("Id donacion: "))
    detalles = service.list_detalles_donacion(id_donacion)

    if not detalles:
        print("No hay detalles registrados")
        return

    for detalle in detalles:
        print("------------------------------")
        mostrar_detalle_donacion(detalle)


def actualizar_detalle_donacion(service):
    id_detalle = int(input("Id detalle: "))
    id_medicamento = int(input("Id medicamento: "))
    cantidad = int(input("Cantidad: "))
    fecha_vencimiento = leer_fecha("Fecha de vencimiento")
    lote = input("Lote: ")
    estado_medicamento = leer_estado_medicamento()

    detalle = service.update_detalle_donacion(
        id_detalle,
        id_medicamento,
        cantidad,
        fecha_vencimiento,
        lote,
        estado_medicamento
    )

    if detalle:
        print("Detalle de donacion actualizado correctamente")
    else:
        print("No se encontro el detalle")


def eliminar_detalle_donacion(service):
    id_detalle = int(input("Id detalle: "))
    detalle = service.delete_detalle_donacion(id_detalle)

    if detalle:
        print("Detalle de donacion eliminado correctamente")
    else:
        print("No se encontro el detalle")


def menu_donaciones(service, services):
    while True:
        print("\n=== DONACIONES ===")
        print("1. Agregar donacion")
        print("2. Buscar donacion")
        print("3. Listar donaciones")
        print("4. Actualizar donacion")
        print("5. Eliminar donacion")
        print("6. Agregar detalle")
        print("7. Buscar detalle")
        print("8. Listar detalles por donacion")
        print("9. Actualizar detalle")
        print("10. Eliminar detalle")
        print("11. Volver")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            ejecutar_accion(lambda: agregar_donacion(service), services)
        elif opcion == "2":
            ejecutar_accion(lambda: buscar_donacion(service), services)
        elif opcion == "3":
            ejecutar_accion(lambda: listar_donaciones(service), services)
        elif opcion == "4":
            ejecutar_accion(lambda: actualizar_donacion(service), services)
        elif opcion == "5":
            ejecutar_accion(lambda: eliminar_donacion(service), services)
        elif opcion == "6":
            ejecutar_accion(lambda: agregar_detalle_donacion(service), services)
        elif opcion == "7":
            ejecutar_accion(lambda: buscar_detalle_donacion(service), services)
        elif opcion == "8":
            ejecutar_accion(lambda: listar_detalles_donacion(service), services)
        elif opcion == "9":
            ejecutar_accion(lambda: actualizar_detalle_donacion(service), services)
        elif opcion == "10":
            ejecutar_accion(lambda: eliminar_detalle_donacion(service), services)
        elif opcion == "11":
            break
        else:
            print("Opcion invalida")


def mostrar_solicitud(solicitud):
    if solicitud:
        print(f"Id: {solicitud.id_solicitud}")
        print(f"Id usuario: {solicitud.id_usuario}")
        print(f"Fecha: {solicitud.fecha_solicitud}")
        print(f"Estado: {solicitud.estado}")
        print(f"Observacion: {solicitud.observacion}")
    else:
        print("No se encontro la solicitud")


def mostrar_detalle_solicitud(detalle):
    if detalle:
        print(f"Id detalle: {detalle.id_detalle_solicitud}")
        print(f"Id solicitud: {detalle.id_solicitud}")
        print(f"Id medicamento: {detalle.id_medicamento}")
        print(f"Cantidad solicitada: {detalle.cantidad_solicitada}")
        print(f"Cantidad aprobada: {detalle.cantidad_aprobada}")
    else:
        print("No se encontro el detalle")


def leer_estado_solicitud():
    estados = ["pendiente", "aprobada", "rechazada", "entregada"]
    return leer_opcion("Estados de solicitud", estados)


def agregar_solicitud(service):
    id_solicitud = int(input("Id solicitud: "))
    id_usuario = int(input("Id usuario: "))
    fecha_solicitud = leer_fecha_hora("Fecha de solicitud")
    estado = leer_estado_solicitud()
    observacion = input("Observacion: ")

    service.create_solicitud(id_solicitud, id_usuario, fecha_solicitud, estado, observacion)
    print("Solicitud agregada correctamente")


def buscar_solicitud(service):
    id_solicitud = int(input("Id solicitud: "))
    mostrar_solicitud(service.get_solicitud(id_solicitud))


def listar_solicitudes(service):
    solicitudes = service.list_solicitudes()

    if not solicitudes:
        print("No hay solicitudes registradas")
        return

    for solicitud in solicitudes:
        print("------------------------------")
        mostrar_solicitud(solicitud)


def actualizar_solicitud(service):
    id_solicitud = int(input("Id solicitud: "))
    id_usuario = int(input("Id usuario: "))
    fecha_solicitud = leer_fecha_hora("Nueva fecha de solicitud")
    estado = leer_estado_solicitud()
    observacion = input("Observacion: ")

    solicitud = service.update_solicitud(id_solicitud, id_usuario, fecha_solicitud, estado, observacion)

    if solicitud:
        print("Solicitud actualizada correctamente")
    else:
        print("No se encontro la solicitud")


def eliminar_solicitud(service):
    id_solicitud = int(input("Id solicitud: "))
    solicitud = service.delete_solicitud(id_solicitud)

    if solicitud:
        print("Solicitud eliminada correctamente")
    else:
        print("No se encontro la solicitud")


def agregar_detalle_solicitud(service):
    id_detalle_solicitud = int(input("Id detalle solicitud: "))
    id_solicitud = int(input("Id solicitud: "))
    id_medicamento = int(input("Id medicamento: "))
    cantidad_solicitada = int(input("Cantidad solicitada: "))
    cantidad_aprobada = int(input("Cantidad aprobada: "))

    service.create_detalle_solicitud(
        id_detalle_solicitud,
        id_solicitud,
        id_medicamento,
        cantidad_solicitada,
        cantidad_aprobada
    )
    print("Detalle de solicitud agregado correctamente")


def buscar_detalle_solicitud(service):
    id_detalle_solicitud = int(input("Id detalle solicitud: "))
    mostrar_detalle_solicitud(service.get_detalle_solicitud(id_detalle_solicitud))


def listar_detalles_solicitud(service):
    id_solicitud = int(input("Id solicitud: "))
    detalles = service.list_detalles_solicitud(id_solicitud)

    if not detalles:
        print("No hay detalles registrados")
        return

    for detalle in detalles:
        print("------------------------------")
        mostrar_detalle_solicitud(detalle)


def actualizar_detalle_solicitud(service):
    id_detalle_solicitud = int(input("Id detalle solicitud: "))
    id_medicamento = int(input("Id medicamento: "))
    cantidad_solicitada = int(input("Cantidad solicitada: "))
    cantidad_aprobada = int(input("Cantidad aprobada: "))

    detalle = service.update_detalle_solicitud(
        id_detalle_solicitud,
        id_medicamento,
        cantidad_solicitada,
        cantidad_aprobada
    )

    if detalle:
        print("Detalle de solicitud actualizado correctamente")
    else:
        print("No se encontro el detalle")


def eliminar_detalle_solicitud(service):
    id_detalle_solicitud = int(input("Id detalle solicitud: "))
    detalle = service.delete_detalle_solicitud(id_detalle_solicitud)

    if detalle:
        print("Detalle de solicitud eliminado correctamente")
    else:
        print("No se encontro el detalle")


def menu_solicitudes(service, services):
    while True:
        print("\n=== SOLICITUDES ===")
        print("1. Agregar solicitud")
        print("2. Buscar solicitud")
        print("3. Listar solicitudes")
        print("4. Actualizar solicitud")
        print("5. Eliminar solicitud")
        print("6. Agregar detalle")
        print("7. Buscar detalle")
        print("8. Listar detalles por solicitud")
        print("9. Actualizar detalle")
        print("10. Eliminar detalle")
        print("11. Volver")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            ejecutar_accion(lambda: agregar_solicitud(service), services)
        elif opcion == "2":
            ejecutar_accion(lambda: buscar_solicitud(service), services)
        elif opcion == "3":
            ejecutar_accion(lambda: listar_solicitudes(service), services)
        elif opcion == "4":
            ejecutar_accion(lambda: actualizar_solicitud(service), services)
        elif opcion == "5":
            ejecutar_accion(lambda: eliminar_solicitud(service), services)
        elif opcion == "6":
            ejecutar_accion(lambda: agregar_detalle_solicitud(service), services)
        elif opcion == "7":
            ejecutar_accion(lambda: buscar_detalle_solicitud(service), services)
        elif opcion == "8":
            ejecutar_accion(lambda: listar_detalles_solicitud(service), services)
        elif opcion == "9":
            ejecutar_accion(lambda: actualizar_detalle_solicitud(service), services)
        elif opcion == "10":
            ejecutar_accion(lambda: eliminar_detalle_solicitud(service), services)
        elif opcion == "11":
            break
        else:
            print("Opcion invalida")


def mostrar_entrega(entrega):
    if entrega:
        print(f"Id: {entrega.id_entrega}")
        print(f"Id solicitud: {entrega.id_solicitud}")
        print(f"Id detalle donacion: {entrega.id_detalle_donacion}")
        print(f"Id usuario: {entrega.id_usuario}")
        print(f"Cantidad entregada: {entrega.cantidad_entregada}")
        print(f"Fecha entrega: {entrega.fecha_entrega}")
    else:
        print("No se encontro la entrega")


def agregar_entrega(service):
    id_entrega = int(input("Id entrega: "))
    id_solicitud = int(input("Id solicitud: "))
    id_detalle_donacion = int(input("Id detalle donacion: "))
    id_usuario = int(input("Id usuario: "))
    cantidad_entregada = int(input("Cantidad entregada: "))
    fecha_entrega = leer_fecha_hora("Fecha de entrega")

    service.create_entrega(
        id_entrega,
        id_solicitud,
        id_detalle_donacion,
        id_usuario,
        cantidad_entregada,
        fecha_entrega
    )
    print("Entrega agregada correctamente")


def buscar_entrega(service):
    id_entrega = int(input("Id entrega: "))
    mostrar_entrega(service.get_entrega(id_entrega))


def listar_entregas(service):
    entregas = service.list_entregas()

    if not entregas:
        print("No hay entregas registradas")
        return

    for entrega in entregas:
        print("------------------------------")
        mostrar_entrega(entrega)


def actualizar_entrega(service):
    id_entrega = int(input("Id entrega: "))
    id_solicitud = int(input("Id solicitud: "))
    id_detalle_donacion = int(input("Id detalle donacion: "))
    id_usuario = int(input("Id usuario: "))
    cantidad_entregada = int(input("Cantidad entregada: "))
    fecha_entrega = leer_fecha_hora("Fecha de entrega")

    entrega = service.update_entrega(
        id_entrega,
        id_solicitud,
        id_detalle_donacion,
        id_usuario,
        cantidad_entregada,
        fecha_entrega
    )

    if entrega:
        print("Entrega actualizada correctamente")
    else:
        print("No se encontro la entrega")


def eliminar_entrega(service):
    id_entrega = int(input("Id entrega: "))
    entrega = service.delete_entrega(id_entrega)

    if entrega:
        print("Entrega eliminada correctamente")
    else:
        print("No se encontro la entrega")


def menu_entregas(service, services):
    while True:
        print("\n=== ENTREGAS ===")
        print("1. Agregar entrega")
        print("2. Buscar entrega")
        print("3. Listar entregas")
        print("4. Actualizar entrega")
        print("5. Eliminar entrega")
        print("6. Volver")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            ejecutar_accion(lambda: agregar_entrega(service), services)
        elif opcion == "2":
            ejecutar_accion(lambda: buscar_entrega(service), services)
        elif opcion == "3":
            ejecutar_accion(lambda: listar_entregas(service), services)
        elif opcion == "4":
            ejecutar_accion(lambda: actualizar_entrega(service), services)
        elif opcion == "5":
            ejecutar_accion(lambda: eliminar_entrega(service), services)
        elif opcion == "6":
            break
        else:
            print("Opcion invalida")


if __name__ == "__main__":
    init_db()

    services = {
        "usuarios": UsuarioService(),
        "centros": CentroRecepcionService(),
        "medicamentos": MedicamentoService(),
        "donaciones": DonacionService(),
        "solicitudes": SolicitudService(),
        "entregas": EntregaService()
    }

    while True:
        menu_principal()
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            menu_usuarios(services["usuarios"], services)
        elif opcion == "2":
            menu_centros(services["centros"], services)
        elif opcion == "3":
            menu_medicamentos(services["medicamentos"], services)
        elif opcion == "4":
            menu_donaciones(services["donaciones"], services)
        elif opcion == "5":
            menu_solicitudes(services["solicitudes"], services)
        elif opcion == "6":
            menu_entregas(services["entregas"], services)
        elif opcion == "7":
            print("Saliendo del sistema")
            break
        else:
            print("Opcion invalida")

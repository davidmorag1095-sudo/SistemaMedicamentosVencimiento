const API_BASE = "http://127.0.0.1:8000";

const messageBox = document.getElementById("messageBox");

let usuarios = [];
let centros = [];
let medicamentos = [];
let donaciones = [];
let detallesDonacion = [];
let solicitudes = [];
let detallesSolicitud = [];
let entregas = [];

let usuarioEditando = null;
let centroEditando = null;
let medicamentoEditando = null;
let donacionEditando = null;
let detalleDonacionEditando = null;
let solicitudEditando = null;
let detalleSolicitudEditando = null;
let entregaEditando = null;

function showMessage(text, type = "success") {
    messageBox.textContent = text;
    messageBox.classList.remove("hidden");
    messageBox.style.background = type === "success" ? "#7a8a70" : "#b86b5f";
    messageBox.style.color = "white";

    setTimeout(() => {
        messageBox.classList.add("hidden");
    }, 3000);
}

function getValue(id) {
    return document.getElementById(id).value;
}

function getNumber(id) {
    return parseInt(document.getElementById(id).value);
}

function getChecked(id) {
    return document.getElementById(id).checked;
}

function setValue(id, value) {
    document.getElementById(id).value = value ?? "";
}

function setChecked(id, value) {
    document.getElementById(id).checked = value === true;
}

function formatoFecha(fecha) {
    if (!fecha) {
        return "";
    }

    return fecha.toString().substring(0, 10);
}

function formatoFechaHora(fecha) {
    if (!fecha) {
        return "";
    }

    return fecha.toString().replace("T", " ").substring(0, 16);
}

function valorFechaHora(fecha) {
    if (!fecha) {
        return "";
    }

    return fecha.toString().substring(0, 16);
}

function textoSiNo(value) {
    return value ? "Si" : "No";
}

function mostrarError(error, mensaje) {
    console.error(error);
    showMessage(error.message || mensaje, "error");
}

async function apiRequest(endpoint, options = {}) {
    const res = await fetch(API_BASE + endpoint, options);

    if (!res.ok) {
        let mensaje = "Error en la solicitud";

        try {
            const errorData = await res.json();

            if (typeof errorData.detail === "string") {
                mensaje = errorData.detail;
            }
        } catch (error) {
            mensaje = "Error en la solicitud";
        }

        throw new Error(mensaje);
    }

    return await res.json();
}

async function enviarDatos(endpoint, method, data) {
    return await apiRequest(endpoint, {
        method: method,
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });
}

function mostrarVacio(tableId, columnas, mensaje) {
    document.getElementById(tableId).innerHTML = `
        <tr>
            <td colspan="${columnas}" class="empty-row">${mensaje}</td>
        </tr>
    `;
}

function guardarEnLista(lista, item, campo) {
    const posicion = lista.findIndex(elemento => elemento[campo] === item[campo]);

    if (posicion >= 0) {
        lista[posicion] = item;
    } else {
        lista.push(item);
    }

    return lista;
}

function llenarSelect(id, data, valueField, labelFunction) {
    const select = document.getElementById(id);

    if (!select) {
        return;
    }

    const valorActual = select.value;
    const placeholder = select.dataset.placeholder || "Seleccione";
    select.innerHTML = `<option value="">${placeholder}</option>`;

    data.forEach(item => {
        const option = document.createElement("option");
        option.value = item[valueField];
        option.textContent = labelFunction(item);
        select.appendChild(option);
    });

    if (valorActual) {
        select.value = valorActual;
    }
}

function actualizarSelects() {
    llenarSelect("donacionUsuario", usuarios, "id_usuario", usuario => `${usuario.id_usuario} - ${usuario.nombre}`);
    llenarSelect("solicitudUsuario", usuarios, "id_usuario", usuario => `${usuario.id_usuario} - ${usuario.nombre}`);
    llenarSelect("entregaUsuario", usuarios, "id_usuario", usuario => `${usuario.id_usuario} - ${usuario.nombre}`);

    llenarSelect("donacionCentro", centros, "id_centro", centro => `${centro.id_centro} - ${centro.nombre}`);

    llenarSelect("detalleDonacionMedicamento", medicamentos, "id_medicamento", medicamento => `${medicamento.id_medicamento} - ${medicamento.nombre}`);
    llenarSelect("detalleSolicitudMedicamento", medicamentos, "id_medicamento", medicamento => `${medicamento.id_medicamento} - ${medicamento.nombre}`);

    llenarSelect("detalleDonacionDonacion", donaciones, "id_donacion", donacion => `Donacion ${donacion.id_donacion}`);
    llenarSelect("detalleSolicitudSolicitud", solicitudes, "id_solicitud", solicitud => `Solicitud ${solicitud.id_solicitud}`);
    llenarSelect("entregaSolicitud", solicitudes, "id_solicitud", solicitud => `Solicitud ${solicitud.id_solicitud}`);

    llenarSelect("entregaDetalleDonacion", detallesDonacion, "id_detalle", detalle => `Detalle ${detalle.id_detalle} - ${nombreMedicamento(detalle.id_medicamento)}`);
}

function nombreUsuario(idUsuario) {
    const usuario = usuarios.find(item => item.id_usuario === idUsuario);
    return usuario ? `${usuario.id_usuario} - ${usuario.nombre}` : idUsuario;
}

function nombreCentro(idCentro) {
    const centro = centros.find(item => item.id_centro === idCentro);
    return centro ? `${centro.id_centro} - ${centro.nombre}` : idCentro;
}

function nombreMedicamento(idMedicamento) {
    const medicamento = medicamentos.find(item => item.id_medicamento === idMedicamento);
    return medicamento ? `${medicamento.id_medicamento} - ${medicamento.nombre}` : idMedicamento;
}

function activarSeccion(sectionId) {
    document.querySelectorAll(".module-section").forEach(section => {
        section.classList.remove("active-section");
    });

    document.querySelectorAll(".menu-btn").forEach(button => {
        button.classList.remove("active");
    });

    document.getElementById(sectionId).classList.add("active-section");
    document.querySelector(`[data-section="${sectionId}"]`).classList.add("active");
}

document.querySelectorAll(".menu-btn").forEach(button => {
    button.addEventListener("click", () => {
        activarSeccion(button.dataset.section);
    });
});

// Usuarios
async function cargarUsuarios() {
    usuarios = await apiRequest("/usuarios/");
    renderUsuarios(usuarios);
    actualizarSelects();
}

function renderUsuarios(lista) {
    const tableBody = document.getElementById("usuariosTable");
    tableBody.innerHTML = "";

    if (lista.length === 0) {
        mostrarVacio("usuariosTable", 6, "No hay usuarios registrados");
        return;
    }

    lista.forEach(usuario => {
        tableBody.innerHTML += `
            <tr>
                <td>${usuario.id_usuario}</td>
                <td>${usuario.nombre}</td>
                <td>${usuario.correo}</td>
                <td>${usuario.rol}</td>
                <td>${textoSiNo(usuario.activo)}</td>
                <td>
                    <button class="action-btn edit-btn" onclick="editUsuario(${usuario.id_usuario})">Editar</button>
                    <button class="action-btn delete-btn" onclick="deleteUsuario(${usuario.id_usuario})">Eliminar</button>
                </td>
            </tr>
        `;
    });
}

document.getElementById("usuarioForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const usuarioData = {
        id_usuario: usuarioEditando,
        nombre: getValue("usuarioNombre"),
        correo: getValue("usuarioCorreo"),
        contrasena: getValue("usuarioContrasena"),
        rol: getValue("usuarioRol"),
        activo: getChecked("usuarioActivo")
    };

    const method = usuarioEditando === null ? "POST" : "PUT";
    const endpoint = usuarioEditando === null ? "/usuarios/" : `/usuarios/${usuarioEditando}`;

    try {
        const usuario = await enviarDatos(endpoint, method, usuarioData);
        showMessage(method === "POST" ? `Usuario agregado correctamente. El ID es ${usuario.id_usuario}` : "Usuario actualizado correctamente");
        limpiarUsuario();
        await cargarDatosIniciales();
    } catch (error) {
        mostrarError(error, "Error al guardar usuario");
    }
});

function editUsuario(idUsuario) {
    const usuario = usuarios.find(item => item.id_usuario === idUsuario);

    if (!usuario) {
        showMessage("Usuario no encontrado", "error");
        return;
    }

    usuarioEditando = idUsuario;
    setValue("usuarioNombre", usuario.nombre);
    setValue("usuarioCorreo", usuario.correo);
    setValue("usuarioContrasena", usuario.contrasena);
    setValue("usuarioRol", usuario.rol);
    setChecked("usuarioActivo", usuario.activo);
    showMessage("Modo edicion activado");
}

async function buscarUsuario() {
    const idUsuario = getValue("buscarUsuario").trim();

    if (!idUsuario) {
        showMessage("Ingrese un ID", "error");
        return;
    }

    try {
        const usuario = await apiRequest(`/usuarios/${idUsuario}`);
        usuarios = guardarEnLista(usuarios, usuario, "id_usuario");
        renderUsuarios([usuario]);
        actualizarSelects();
    } catch (error) {
        mostrarError(error, "Usuario no encontrado");
    }
}

async function deleteUsuario(idUsuario) {
    try {
        await apiRequest(`/usuarios/${idUsuario}`, { method: "DELETE" });
        showMessage("Usuario eliminado");

        if (usuarioEditando === idUsuario) {
            limpiarUsuario();
        }

        await cargarDatosIniciales();
    } catch (error) {
        mostrarError(error, "Error al eliminar usuario");
    }
}

function limpiarUsuario() {
    usuarioEditando = null;
    document.getElementById("usuarioForm").reset();
    document.getElementById("usuarioActivo").checked = true;
}

// Centros
async function cargarCentros() {
    centros = await apiRequest("/centros/");
    renderCentros(centros);
    actualizarSelects();
}

function renderCentros(lista) {
    const tableBody = document.getElementById("centrosTable");
    tableBody.innerHTML = "";

    if (lista.length === 0) {
        mostrarVacio("centrosTable", 6, "No hay centros registrados");
        return;
    }

    lista.forEach(centro => {
        tableBody.innerHTML += `
            <tr>
                <td>${centro.id_centro}</td>
                <td>${centro.nombre}</td>
                <td>${centro.direccion}</td>
                <td>${centro.telefono}</td>
                <td>${centro.responsable}</td>
                <td>
                    <button class="action-btn edit-btn" onclick="editCentro(${centro.id_centro})">Editar</button>
                    <button class="action-btn delete-btn" onclick="deleteCentro(${centro.id_centro})">Eliminar</button>
                </td>
            </tr>
        `;
    });
}

document.getElementById("centroForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const centroData = {
        id_centro: centroEditando,
        nombre: getValue("centroNombre"),
        direccion: getValue("centroDireccion"),
        telefono: getValue("centroTelefono"),
        responsable: getValue("centroResponsable")
    };

    const method = centroEditando === null ? "POST" : "PUT";
    const endpoint = centroEditando === null ? "/centros/" : `/centros/${centroEditando}`;

    try {
        const centro = await enviarDatos(endpoint, method, centroData);
        showMessage(method === "POST" ? `Centro agregado correctamente. El ID es ${centro.id_centro}` : "Centro actualizado correctamente");
        limpiarCentro();
        await cargarDatosIniciales();
    } catch (error) {
        mostrarError(error, "Error al guardar centro");
    }
});

function editCentro(idCentro) {
    const centro = centros.find(item => item.id_centro === idCentro);

    if (!centro) {
        showMessage("Centro no encontrado", "error");
        return;
    }

    centroEditando = idCentro;
    setValue("centroNombre", centro.nombre);
    setValue("centroDireccion", centro.direccion);
    setValue("centroTelefono", centro.telefono);
    setValue("centroResponsable", centro.responsable);
    showMessage("Modo edicion activado");
}

async function buscarCentro() {
    const idCentro = getValue("buscarCentro").trim();

    if (!idCentro) {
        showMessage("Ingrese un ID", "error");
        return;
    }

    try {
        const centro = await apiRequest(`/centros/${idCentro}`);
        centros = guardarEnLista(centros, centro, "id_centro");
        renderCentros([centro]);
        actualizarSelects();
    } catch (error) {
        mostrarError(error, "Centro no encontrado");
    }
}

async function deleteCentro(idCentro) {
    try {
        await apiRequest(`/centros/${idCentro}`, { method: "DELETE" });
        showMessage("Centro eliminado");

        if (centroEditando === idCentro) {
            limpiarCentro();
        }

        await cargarDatosIniciales();
    } catch (error) {
        mostrarError(error, "Error al eliminar centro");
    }
}

function limpiarCentro() {
    centroEditando = null;
    document.getElementById("centroForm").reset();
}

// Medicamentos
async function cargarMedicamentos() {
    medicamentos = await apiRequest("/medicamentos/");
    renderMedicamentos(medicamentos);
    actualizarSelects();
}

function renderMedicamentos(lista) {
    const tableBody = document.getElementById("medicamentosTable");
    tableBody.innerHTML = "";

    if (lista.length === 0) {
        mostrarVacio("medicamentosTable", 7, "No hay medicamentos registrados");
        return;
    }

    lista.forEach(medicamento => {
        tableBody.innerHTML += `
            <tr>
                <td>${medicamento.id_medicamento}</td>
                <td>${medicamento.nombre}</td>
                <td>${medicamento.descripcion}</td>
                <td>${medicamento.categoria}</td>
                <td>${medicamento.presentacion}</td>
                <td>${textoSiNo(medicamento.requiere_receta)}</td>
                <td>
                    <button class="action-btn edit-btn" onclick="editMedicamento(${medicamento.id_medicamento})">Editar</button>
                    <button class="action-btn delete-btn" onclick="deleteMedicamento(${medicamento.id_medicamento})">Eliminar</button>
                </td>
            </tr>
        `;
    });
}

document.getElementById("medicamentoForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const medicamentoData = {
        id_medicamento: medicamentoEditando,
        nombre: getValue("medicamentoNombre"),
        descripcion: getValue("medicamentoDescripcion"),
        categoria: getValue("medicamentoCategoria"),
        presentacion: getValue("medicamentoPresentacion"),
        requiere_receta: getChecked("medicamentoReceta")
    };

    const method = medicamentoEditando === null ? "POST" : "PUT";
    const endpoint = medicamentoEditando === null ? "/medicamentos/" : `/medicamentos/${medicamentoEditando}`;

    try {
        const medicamento = await enviarDatos(endpoint, method, medicamentoData);
        showMessage(method === "POST" ? `Medicamento agregado correctamente. El ID es ${medicamento.id_medicamento}` : "Medicamento actualizado correctamente");
        limpiarMedicamento();
        await cargarDatosIniciales();
    } catch (error) {
        mostrarError(error, "Error al guardar medicamento");
    }
});

function editMedicamento(idMedicamento) {
    const medicamento = medicamentos.find(item => item.id_medicamento === idMedicamento);

    if (!medicamento) {
        showMessage("Medicamento no encontrado", "error");
        return;
    }

    medicamentoEditando = idMedicamento;
    setValue("medicamentoNombre", medicamento.nombre);
    setValue("medicamentoDescripcion", medicamento.descripcion);
    setValue("medicamentoCategoria", medicamento.categoria);
    setValue("medicamentoPresentacion", medicamento.presentacion);
    setChecked("medicamentoReceta", medicamento.requiere_receta);
    showMessage("Modo edicion activado");
}

async function buscarMedicamento() {
    const idMedicamento = getValue("buscarMedicamento").trim();

    if (!idMedicamento) {
        showMessage("Ingrese un ID", "error");
        return;
    }

    try {
        const medicamento = await apiRequest(`/medicamentos/${idMedicamento}`);
        medicamentos = guardarEnLista(medicamentos, medicamento, "id_medicamento");
        renderMedicamentos([medicamento]);
        actualizarSelects();
    } catch (error) {
        mostrarError(error, "Medicamento no encontrado");
    }
}

async function deleteMedicamento(idMedicamento) {
    try {
        await apiRequest(`/medicamentos/${idMedicamento}`, { method: "DELETE" });
        showMessage("Medicamento eliminado");

        if (medicamentoEditando === idMedicamento) {
            limpiarMedicamento();
        }

        await cargarDatosIniciales();
    } catch (error) {
        mostrarError(error, "Error al eliminar medicamento");
    }
}

function limpiarMedicamento() {
    medicamentoEditando = null;
    document.getElementById("medicamentoForm").reset();
}

// Donaciones
async function cargarDonaciones() {
    donaciones = await apiRequest("/donaciones/");
    renderDonaciones(donaciones);
    actualizarSelects();
}

function renderDonaciones(lista) {
    const tableBody = document.getElementById("donacionesTable");
    tableBody.innerHTML = "";

    if (lista.length === 0) {
        mostrarVacio("donacionesTable", 6, "No hay donaciones registradas");
        return;
    }

    lista.forEach(donacion => {
        tableBody.innerHTML += `
            <tr>
                <td>${donacion.id_donacion}</td>
                <td>${nombreUsuario(donacion.id_usuario)}</td>
                <td>${nombreCentro(donacion.id_centro)}</td>
                <td>${formatoFechaHora(donacion.fecha_donacion)}</td>
                <td>${donacion.estado}</td>
                <td>
                    <button class="action-btn edit-btn" onclick="editDonacion(${donacion.id_donacion})">Editar</button>
                    <button class="action-btn delete-btn" onclick="deleteDonacion(${donacion.id_donacion})">Eliminar</button>
                </td>
            </tr>
        `;
    });
}

document.getElementById("donacionForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const donacionData = {
        id_donacion: donacionEditando,
        id_usuario: getNumber("donacionUsuario"),
        id_centro: getNumber("donacionCentro"),
        fecha_donacion: getValue("donacionFecha"),
        estado: getValue("donacionEstado")
    };

    const method = donacionEditando === null ? "POST" : "PUT";
    const endpoint = donacionEditando === null ? "/donaciones/" : `/donaciones/${donacionEditando}`;

    try {
        const donacion = await enviarDatos(endpoint, method, donacionData);
        showMessage(method === "POST" ? `Donacion agregada correctamente. El ID es ${donacion.id_donacion}` : "Donacion actualizada correctamente");
        limpiarDonacion();
        await cargarDatosIniciales();
    } catch (error) {
        mostrarError(error, "Error al guardar donacion");
    }
});

function editDonacion(idDonacion) {
    const donacion = donaciones.find(item => item.id_donacion === idDonacion);

    if (!donacion) {
        showMessage("Donacion no encontrada", "error");
        return;
    }

    donacionEditando = idDonacion;
    setValue("donacionUsuario", donacion.id_usuario);
    setValue("donacionCentro", donacion.id_centro);
    setValue("donacionFecha", valorFechaHora(donacion.fecha_donacion));
    setValue("donacionEstado", donacion.estado);
    showMessage("Modo edicion activado");
}

async function buscarDonacion() {
    const idDonacion = getValue("buscarDonacion").trim();

    if (!idDonacion) {
        showMessage("Ingrese un ID", "error");
        return;
    }

    try {
        const donacion = await apiRequest(`/donaciones/${idDonacion}`);
        donaciones = guardarEnLista(donaciones, donacion, "id_donacion");
        renderDonaciones([donacion]);
        actualizarSelects();
    } catch (error) {
        mostrarError(error, "Donacion no encontrada");
    }
}

async function deleteDonacion(idDonacion) {
    try {
        await apiRequest(`/donaciones/${idDonacion}`, { method: "DELETE" });
        showMessage("Donacion eliminada");

        if (donacionEditando === idDonacion) {
            limpiarDonacion();
        }

        await cargarDatosIniciales();
    } catch (error) {
        mostrarError(error, "Error al eliminar donacion");
    }
}

function limpiarDonacion() {
    donacionEditando = null;
    document.getElementById("donacionForm").reset();
}

// Detalles de donacion
async function cargarDetallesDonacion() {
    if (donaciones.length === 0) {
        detallesDonacion = [];
        renderDetallesDonacion(detallesDonacion);
        actualizarSelects();
        return;
    }

    const listas = await Promise.all(
        donaciones.map(donacion => apiRequest(`/donaciones/${donacion.id_donacion}/detalles`).catch(() => []))
    );

    detallesDonacion = listas.flat();
    renderDetallesDonacion(detallesDonacion);
    actualizarSelects();
}

function renderDetallesDonacion(lista) {
    const tableBody = document.getElementById("detallesDonacionTable");
    tableBody.innerHTML = "";

    if (lista.length === 0) {
        mostrarVacio("detallesDonacionTable", 8, "No hay detalles de donacion registrados");
        return;
    }

    lista.forEach(detalle => {
        tableBody.innerHTML += `
            <tr>
                <td>${detalle.id_detalle}</td>
                <td>${detalle.id_donacion}</td>
                <td>${nombreMedicamento(detalle.id_medicamento)}</td>
                <td>${detalle.cantidad}</td>
                <td>${formatoFecha(detalle.fecha_vencimiento)}</td>
                <td>${detalle.lote}</td>
                <td>${detalle.estado_medicamento}</td>
                <td>
                    <button class="action-btn edit-btn" onclick="editDetalleDonacion(${detalle.id_detalle})">Editar</button>
                    <button class="action-btn delete-btn" onclick="deleteDetalleDonacion(${detalle.id_detalle})">Eliminar</button>
                </td>
            </tr>
        `;
    });
}

document.getElementById("detalleDonacionForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const detalleData = {
        id_detalle: detalleDonacionEditando,
        id_donacion: getNumber("detalleDonacionDonacion"),
        id_medicamento: getNumber("detalleDonacionMedicamento"),
        cantidad: getNumber("detalleDonacionCantidad"),
        fecha_vencimiento: getValue("detalleDonacionVencimiento"),
        lote: getValue("detalleDonacionLote"),
        estado_medicamento: getValue("detalleDonacionEstado")
    };

    const method = detalleDonacionEditando === null ? "POST" : "PUT";
    const endpoint = detalleDonacionEditando === null ? "/donaciones/detalles/" : `/donaciones/detalles/${detalleDonacionEditando}`;

    try {
        const detalle = await enviarDatos(endpoint, method, detalleData);
        showMessage(method === "POST" ? `Detalle agregado correctamente. El ID es ${detalle.id_detalle}` : "Detalle actualizado correctamente");
        limpiarDetalleDonacion();
        await cargarDatosIniciales();
    } catch (error) {
        mostrarError(error, "Error al guardar detalle");
    }
});

function editDetalleDonacion(idDetalle) {
    const detalle = detallesDonacion.find(item => item.id_detalle === idDetalle);

    if (!detalle) {
        showMessage("Detalle no encontrado", "error");
        return;
    }

    detalleDonacionEditando = idDetalle;
    setValue("detalleDonacionDonacion", detalle.id_donacion);
    setValue("detalleDonacionMedicamento", detalle.id_medicamento);
    setValue("detalleDonacionCantidad", detalle.cantidad);
    setValue("detalleDonacionVencimiento", formatoFecha(detalle.fecha_vencimiento));
    setValue("detalleDonacionLote", detalle.lote);
    setValue("detalleDonacionEstado", detalle.estado_medicamento);
    document.getElementById("detalleDonacionDonacion").disabled = true;
    showMessage("Modo edicion activado");
}

async function buscarDetalleDonacion() {
    const idDetalle = getValue("buscarDetalleDonacion").trim();

    if (!idDetalle) {
        showMessage("Ingrese un ID", "error");
        return;
    }

    try {
        const detalle = await apiRequest(`/donaciones/detalles/${idDetalle}`);
        detallesDonacion = guardarEnLista(detallesDonacion, detalle, "id_detalle");
        renderDetallesDonacion([detalle]);
        actualizarSelects();
    } catch (error) {
        mostrarError(error, "Detalle no encontrado");
    }
}

async function deleteDetalleDonacion(idDetalle) {
    try {
        await apiRequest(`/donaciones/detalles/${idDetalle}`, { method: "DELETE" });
        showMessage("Detalle eliminado");

        if (detalleDonacionEditando === idDetalle) {
            limpiarDetalleDonacion();
        }

        await cargarDatosIniciales();
    } catch (error) {
        mostrarError(error, "Error al eliminar detalle");
    }
}

function limpiarDetalleDonacion() {
    detalleDonacionEditando = null;
    document.getElementById("detalleDonacionForm").reset();
    document.getElementById("detalleDonacionDonacion").disabled = false;
}

// Solicitudes
async function cargarSolicitudes() {
    solicitudes = await apiRequest("/solicitudes/");
    renderSolicitudes(solicitudes);
    actualizarSelects();
}

function renderSolicitudes(lista) {
    const tableBody = document.getElementById("solicitudesTable");
    tableBody.innerHTML = "";

    if (lista.length === 0) {
        mostrarVacio("solicitudesTable", 6, "No hay solicitudes registradas");
        return;
    }

    lista.forEach(solicitud => {
        tableBody.innerHTML += `
            <tr>
                <td>${solicitud.id_solicitud}</td>
                <td>${nombreUsuario(solicitud.id_usuario)}</td>
                <td>${formatoFechaHora(solicitud.fecha_solicitud)}</td>
                <td>${solicitud.estado}</td>
                <td>${solicitud.observacion}</td>
                <td>
                    <button class="action-btn edit-btn" onclick="editSolicitud(${solicitud.id_solicitud})">Editar</button>
                    <button class="action-btn delete-btn" onclick="deleteSolicitud(${solicitud.id_solicitud})">Eliminar</button>
                </td>
            </tr>
        `;
    });
}

document.getElementById("solicitudForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const solicitudData = {
        id_solicitud: solicitudEditando,
        id_usuario: getNumber("solicitudUsuario"),
        fecha_solicitud: getValue("solicitudFecha"),
        estado: getValue("solicitudEstado"),
        observacion: getValue("solicitudObservacion")
    };

    const method = solicitudEditando === null ? "POST" : "PUT";
    const endpoint = solicitudEditando === null ? "/solicitudes/" : `/solicitudes/${solicitudEditando}`;

    try {
        const solicitud = await enviarDatos(endpoint, method, solicitudData);
        showMessage(method === "POST" ? `Solicitud agregada correctamente. El ID es ${solicitud.id_solicitud}` : "Solicitud actualizada correctamente");
        limpiarSolicitud();
        await cargarDatosIniciales();
    } catch (error) {
        mostrarError(error, "Error al guardar solicitud");
    }
});

function editSolicitud(idSolicitud) {
    const solicitud = solicitudes.find(item => item.id_solicitud === idSolicitud);

    if (!solicitud) {
        showMessage("Solicitud no encontrada", "error");
        return;
    }

    solicitudEditando = idSolicitud;
    setValue("solicitudUsuario", solicitud.id_usuario);
    setValue("solicitudFecha", valorFechaHora(solicitud.fecha_solicitud));
    setValue("solicitudEstado", solicitud.estado);
    setValue("solicitudObservacion", solicitud.observacion);
    showMessage("Modo edicion activado");
}

async function buscarSolicitud() {
    const idSolicitud = getValue("buscarSolicitud").trim();

    if (!idSolicitud) {
        showMessage("Ingrese un ID", "error");
        return;
    }

    try {
        const solicitud = await apiRequest(`/solicitudes/${idSolicitud}`);
        solicitudes = guardarEnLista(solicitudes, solicitud, "id_solicitud");
        renderSolicitudes([solicitud]);
        actualizarSelects();
    } catch (error) {
        mostrarError(error, "Solicitud no encontrada");
    }
}

async function deleteSolicitud(idSolicitud) {
    try {
        await apiRequest(`/solicitudes/${idSolicitud}`, { method: "DELETE" });
        showMessage("Solicitud eliminada");

        if (solicitudEditando === idSolicitud) {
            limpiarSolicitud();
        }

        await cargarDatosIniciales();
    } catch (error) {
        mostrarError(error, "Error al eliminar solicitud");
    }
}

function limpiarSolicitud() {
    solicitudEditando = null;
    document.getElementById("solicitudForm").reset();
}

// Detalles de solicitud
async function cargarDetallesSolicitud() {
    if (solicitudes.length === 0) {
        detallesSolicitud = [];
        renderDetallesSolicitud(detallesSolicitud);
        actualizarSelects();
        return;
    }

    const listas = await Promise.all(
        solicitudes.map(solicitud => apiRequest(`/solicitudes/${solicitud.id_solicitud}/detalles`).catch(() => []))
    );

    detallesSolicitud = listas.flat();
    renderDetallesSolicitud(detallesSolicitud);
    actualizarSelects();
}

function renderDetallesSolicitud(lista) {
    const tableBody = document.getElementById("detallesSolicitudTable");
    tableBody.innerHTML = "";

    if (lista.length === 0) {
        mostrarVacio("detallesSolicitudTable", 6, "No hay detalles de solicitud registrados");
        return;
    }

    lista.forEach(detalle => {
        tableBody.innerHTML += `
            <tr>
                <td>${detalle.id_detalle_solicitud}</td>
                <td>${detalle.id_solicitud}</td>
                <td>${nombreMedicamento(detalle.id_medicamento)}</td>
                <td>${detalle.cantidad_solicitada}</td>
                <td>${detalle.cantidad_aprobada}</td>
                <td>
                    <button class="action-btn edit-btn" onclick="editDetalleSolicitud(${detalle.id_detalle_solicitud})">Editar</button>
                    <button class="action-btn delete-btn" onclick="deleteDetalleSolicitud(${detalle.id_detalle_solicitud})">Eliminar</button>
                </td>
            </tr>
        `;
    });
}

document.getElementById("detalleSolicitudForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const detalleData = {
        id_detalle_solicitud: detalleSolicitudEditando,
        id_solicitud: getNumber("detalleSolicitudSolicitud"),
        id_medicamento: getNumber("detalleSolicitudMedicamento"),
        cantidad_solicitada: getNumber("detalleSolicitudCantidad"),
        cantidad_aprobada: getNumber("detalleSolicitudAprobada")
    };

    const method = detalleSolicitudEditando === null ? "POST" : "PUT";
    const endpoint = detalleSolicitudEditando === null ? "/solicitudes/detalles/" : `/solicitudes/detalles/${detalleSolicitudEditando}`;

    try {
        const detalle = await enviarDatos(endpoint, method, detalleData);
        showMessage(method === "POST" ? `Detalle agregado correctamente. El ID es ${detalle.id_detalle_solicitud}` : "Detalle actualizado correctamente");
        limpiarDetalleSolicitud();
        await cargarDatosIniciales();
    } catch (error) {
        mostrarError(error, "Error al guardar detalle");
    }
});

function editDetalleSolicitud(idDetalleSolicitud) {
    const detalle = detallesSolicitud.find(item => item.id_detalle_solicitud === idDetalleSolicitud);

    if (!detalle) {
        showMessage("Detalle no encontrado", "error");
        return;
    }

    detalleSolicitudEditando = idDetalleSolicitud;
    setValue("detalleSolicitudSolicitud", detalle.id_solicitud);
    setValue("detalleSolicitudMedicamento", detalle.id_medicamento);
    setValue("detalleSolicitudCantidad", detalle.cantidad_solicitada);
    setValue("detalleSolicitudAprobada", detalle.cantidad_aprobada);
    document.getElementById("detalleSolicitudSolicitud").disabled = true;
    showMessage("Modo edicion activado");
}

async function buscarDetalleSolicitud() {
    const idDetalleSolicitud = getValue("buscarDetalleSolicitud").trim();

    if (!idDetalleSolicitud) {
        showMessage("Ingrese un ID", "error");
        return;
    }

    try {
        const detalle = await apiRequest(`/solicitudes/detalles/${idDetalleSolicitud}`);
        detallesSolicitud = guardarEnLista(detallesSolicitud, detalle, "id_detalle_solicitud");
        renderDetallesSolicitud([detalle]);
        actualizarSelects();
    } catch (error) {
        mostrarError(error, "Detalle no encontrado");
    }
}

async function deleteDetalleSolicitud(idDetalleSolicitud) {
    try {
        await apiRequest(`/solicitudes/detalles/${idDetalleSolicitud}`, { method: "DELETE" });
        showMessage("Detalle eliminado");

        if (detalleSolicitudEditando === idDetalleSolicitud) {
            limpiarDetalleSolicitud();
        }

        await cargarDatosIniciales();
    } catch (error) {
        mostrarError(error, "Error al eliminar detalle");
    }
}

function limpiarDetalleSolicitud() {
    detalleSolicitudEditando = null;
    document.getElementById("detalleSolicitudForm").reset();
    document.getElementById("detalleSolicitudSolicitud").disabled = false;
}

// Entregas
async function cargarEntregas() {
    entregas = await apiRequest("/entregas/");
    renderEntregas(entregas);
    actualizarSelects();
}

function renderEntregas(lista) {
    const tableBody = document.getElementById("entregasTable");
    tableBody.innerHTML = "";

    if (lista.length === 0) {
        mostrarVacio("entregasTable", 7, "No hay entregas registradas");
        return;
    }

    lista.forEach(entrega => {
        tableBody.innerHTML += `
            <tr>
                <td>${entrega.id_entrega}</td>
                <td>${entrega.id_solicitud}</td>
                <td>${entrega.id_detalle_donacion}</td>
                <td>${nombreUsuario(entrega.id_usuario)}</td>
                <td>${entrega.cantidad_entregada}</td>
                <td>${formatoFechaHora(entrega.fecha_entrega)}</td>
                <td>
                    <button class="action-btn edit-btn" onclick="editEntrega(${entrega.id_entrega})">Editar</button>
                    <button class="action-btn delete-btn" onclick="deleteEntrega(${entrega.id_entrega})">Eliminar</button>
                </td>
            </tr>
        `;
    });
}

document.getElementById("entregaForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const entregaData = {
        id_entrega: entregaEditando,
        id_solicitud: getNumber("entregaSolicitud"),
        id_detalle_donacion: getNumber("entregaDetalleDonacion"),
        id_usuario: getNumber("entregaUsuario"),
        cantidad_entregada: getNumber("entregaCantidad"),
        fecha_entrega: getValue("entregaFecha")
    };

    const method = entregaEditando === null ? "POST" : "PUT";
    const endpoint = entregaEditando === null ? "/entregas/" : `/entregas/${entregaEditando}`;

    try {
        const entrega = await enviarDatos(endpoint, method, entregaData);
        showMessage(method === "POST" ? `Entrega agregada correctamente. El ID es ${entrega.id_entrega}` : "Entrega actualizada correctamente");
        limpiarEntrega();
        await cargarDatosIniciales();
    } catch (error) {
        mostrarError(error, "Error al guardar entrega");
    }
});

function editEntrega(idEntrega) {
    const entrega = entregas.find(item => item.id_entrega === idEntrega);

    if (!entrega) {
        showMessage("Entrega no encontrada", "error");
        return;
    }

    entregaEditando = idEntrega;
    setValue("entregaSolicitud", entrega.id_solicitud);
    setValue("entregaDetalleDonacion", entrega.id_detalle_donacion);
    setValue("entregaUsuario", entrega.id_usuario);
    setValue("entregaCantidad", entrega.cantidad_entregada);
    setValue("entregaFecha", valorFechaHora(entrega.fecha_entrega));
    showMessage("Modo edicion activado");
}

async function buscarEntrega() {
    const idEntrega = getValue("buscarEntrega").trim();

    if (!idEntrega) {
        showMessage("Ingrese un ID", "error");
        return;
    }

    try {
        const entrega = await apiRequest(`/entregas/${idEntrega}`);
        entregas = guardarEnLista(entregas, entrega, "id_entrega");
        renderEntregas([entrega]);
        actualizarSelects();
    } catch (error) {
        mostrarError(error, "Entrega no encontrada");
    }
}

async function deleteEntrega(idEntrega) {
    try {
        await apiRequest(`/entregas/${idEntrega}`, { method: "DELETE" });
        showMessage("Entrega eliminada");

        if (entregaEditando === idEntrega) {
            limpiarEntrega();
        }

        await cargarDatosIniciales();
    } catch (error) {
        mostrarError(error, "Error al eliminar entrega");
    }
}

function limpiarEntrega() {
    entregaEditando = null;
    document.getElementById("entregaForm").reset();
}

async function ejecutarCarga(funcion, mensaje) {
    try {
        await funcion();
    } catch (error) {
        mostrarError(error, mensaje);
    }
}

async function cargarDatosIniciales() {
    try {
        await cargarUsuarios();
        await cargarCentros();
        await cargarMedicamentos();
        await cargarDonaciones();
        await cargarSolicitudes();
        await cargarDetallesDonacion();
        await cargarDetallesSolicitud();
        await cargarEntregas();
        actualizarSelects();
    } catch (error) {
        mostrarError(error, "No se pudieron cargar los datos");
    }
}

document.getElementById("btnBuscarUsuario").addEventListener("click", buscarUsuario);
document.getElementById("btnCargarUsuarios").addEventListener("click", () => ejecutarCarga(cargarUsuarios, "No se pudieron cargar los usuarios"));
document.getElementById("btnLimpiarUsuario").addEventListener("click", limpiarUsuario);

document.getElementById("btnBuscarCentro").addEventListener("click", buscarCentro);
document.getElementById("btnCargarCentros").addEventListener("click", () => ejecutarCarga(cargarCentros, "No se pudieron cargar los centros"));
document.getElementById("btnLimpiarCentro").addEventListener("click", limpiarCentro);

document.getElementById("btnBuscarMedicamento").addEventListener("click", buscarMedicamento);
document.getElementById("btnCargarMedicamentos").addEventListener("click", () => ejecutarCarga(cargarMedicamentos, "No se pudieron cargar los medicamentos"));
document.getElementById("btnLimpiarMedicamento").addEventListener("click", limpiarMedicamento);

document.getElementById("btnBuscarDonacion").addEventListener("click", buscarDonacion);
document.getElementById("btnCargarDonaciones").addEventListener("click", () => ejecutarCarga(cargarDonaciones, "No se pudieron cargar las donaciones"));
document.getElementById("btnLimpiarDonacion").addEventListener("click", limpiarDonacion);

document.getElementById("btnBuscarDetalleDonacion").addEventListener("click", buscarDetalleDonacion);
document.getElementById("btnCargarDetallesDonacion").addEventListener("click", () => ejecutarCarga(cargarDetallesDonacion, "No se pudieron cargar los detalles"));
document.getElementById("btnLimpiarDetalleDonacion").addEventListener("click", limpiarDetalleDonacion);

document.getElementById("btnBuscarSolicitud").addEventListener("click", buscarSolicitud);
document.getElementById("btnCargarSolicitudes").addEventListener("click", () => ejecutarCarga(cargarSolicitudes, "No se pudieron cargar las solicitudes"));
document.getElementById("btnLimpiarSolicitud").addEventListener("click", limpiarSolicitud);

document.getElementById("btnBuscarDetalleSolicitud").addEventListener("click", buscarDetalleSolicitud);
document.getElementById("btnCargarDetallesSolicitud").addEventListener("click", () => ejecutarCarga(cargarDetallesSolicitud, "No se pudieron cargar los detalles"));
document.getElementById("btnLimpiarDetalleSolicitud").addEventListener("click", limpiarDetalleSolicitud);

document.getElementById("btnBuscarEntrega").addEventListener("click", buscarEntrega);
document.getElementById("btnCargarEntregas").addEventListener("click", () => ejecutarCarga(cargarEntregas, "No se pudieron cargar las entregas"));
document.getElementById("btnLimpiarEntrega").addEventListener("click", limpiarEntrega);

cargarDatosIniciales();

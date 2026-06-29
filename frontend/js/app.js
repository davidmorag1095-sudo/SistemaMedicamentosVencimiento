const API_URL = "http://127.0.0.1:8000/medicamentos/";

const form = document.getElementById("medicamentoForm");
const tableBody = document.getElementById("medicamentosTable");
const messageBox = document.getElementById("messageBox");
const btnLoad = document.getElementById("btnLoad");
const btnSearch = document.getElementById("btnSearch");
let medicamentoEditando = null;
let medicamentos = [];

function showMessage(text, type = "success") {
    messageBox.textContent = text;
    messageBox.classList.remove("hidden");
    messageBox.style.background = type === "success" ? "#5cb85c" : "#d9534f";
    messageBox.style.color = "white";

    setTimeout(() => {
        messageBox.classList.add("hidden");
    }, 3000);
}

async function loadMedicamentos() {
    try {
        const res = await fetch(API_URL);

        if (!res.ok) {
            throw new Error("Error al consultar la API");
        }

        const data = await res.json();
        medicamentos = data;
        tableBody.innerHTML = "";

        data.forEach(medicamento => {
            agregarFilaMedicamento(medicamento);
        });

    } catch (error) {
        console.error(error);
        showMessage("No se pudieron cargar los medicamentos", "error");
    }
}

function agregarFilaMedicamento(medicamento) {
    const requiereReceta = medicamento.requiere_receta ? "Si" : "No";

    const row = `
        <tr>
            <td>${medicamento.id_medicamento}</td>
            <td>${medicamento.nombre}</td>
            <td>${medicamento.descripcion}</td>
            <td>${medicamento.categoria}</td>
            <td>${medicamento.presentacion}</td>
            <td>${requiereReceta}</td>
            <td>
                <button
                    class="action-btn edit-btn"
                    onclick="editMedicamento(${medicamento.id_medicamento})">
                    Editar
                </button>
                <button
                    class="action-btn delete-btn"
                    onclick="deleteMedicamento(${medicamento.id_medicamento})">
                    Eliminar
                </button>
            </td>
        </tr>
    `;

    tableBody.innerHTML += row;
}

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const nombre = document.getElementById("nombre").value;
    const descripcion = document.getElementById("descripcion").value;
    const categoria = document.getElementById("categoria").value;
    const presentacion = document.getElementById("presentacion").value;
    const requiereReceta = document.getElementById("requiereReceta").checked;

    const medicamentoData = {
        id_medicamento: medicamentoEditando,
        nombre: nombre,
        descripcion: descripcion,
        categoria: categoria,
        presentacion: presentacion,
        requiere_receta: requiereReceta
    };

    let url = API_URL;
    let method = "POST";

    if (medicamentoEditando !== null) {
        url = API_URL + medicamentoEditando;
        method = "PUT";
    }

    try {
        const res = await fetch(url, {
            method: method,
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(medicamentoData)
        });

        if (res.ok) {
            if (method === "POST") {
                const nuevoMedicamento = await res.json();
                showMessage("Medicamento agregado correctamente. El ID es " + nuevoMedicamento.id_medicamento);
            } else {
                showMessage("Medicamento actualizado correctamente");
            }

            activarModoAgregar();
            loadMedicamentos();

        } else {
            const errorData = await res.json();
            showMessage(errorData.detail || "Error al guardar o actualizar", "error");
        }

    } catch (error) {
        console.error(error);
        showMessage("Error de conexion con la API", "error");
    }
});

function activarModoAgregar() {
    medicamentoEditando = null;
    form.reset();
}

function editMedicamento(idMedicamento) {
    const medicamento = medicamentos.find(item => item.id_medicamento === idMedicamento);

    if (!medicamento) {
        showMessage("Medicamento no encontrado", "error");
        return;
    }

    medicamentoEditando = idMedicamento;

    document.getElementById("nombre").value = medicamento.nombre;
    document.getElementById("descripcion").value = medicamento.descripcion;
    document.getElementById("categoria").value = medicamento.categoria;
    document.getElementById("presentacion").value = medicamento.presentacion;
    document.getElementById("requiereReceta").checked = medicamento.requiere_receta;

    showMessage("Modo edicion activado");
}

async function searchMedicamento() {
    const idMedicamento = document.getElementById("searchMedicamento").value.trim();

    if (!idMedicamento) {
        showMessage("Ingrese un ID", "error");
        return;
    }

    try {
        const res = await fetch(API_URL + idMedicamento);

        if (!res.ok) {
            throw new Error("Medicamento no encontrado");
        }

        const medicamento = await res.json();
        medicamentos = [medicamento];
        tableBody.innerHTML = "";
        agregarFilaMedicamento(medicamento);

    } catch (error) {
        showMessage("Medicamento no encontrado", "error");
        tableBody.innerHTML = "";
    }
}

async function deleteMedicamento(idMedicamento) {
    try {
        const res = await fetch(API_URL + idMedicamento, {
            method: "DELETE"
        });

        if (res.ok) {
            showMessage("Medicamento eliminado");
            loadMedicamentos();

            if (medicamentoEditando === idMedicamento) {
                activarModoAgregar();
            }

        } else {
            showMessage("Error al eliminar", "error");
        }

    } catch (error) {
        console.error(error);
        showMessage("Error de conexion con la API", "error");
    }
}

btnLoad.addEventListener("click", loadMedicamentos);
btnSearch.addEventListener("click", searchMedicamento);

loadMedicamentos();

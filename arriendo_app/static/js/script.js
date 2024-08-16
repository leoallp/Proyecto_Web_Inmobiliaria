
const filtrarComunas = async (regionId) => {
    const csrfTokenValue = document.querySelector("[name=csrfmiddlewaretoken]").value;
    const headers = {
        "X-CSRFToken": csrfTokenValue,
    };
    let url = "/filtrar-comunas/";

    console.log("Enviando regionId:", regionId);

    try {
        const response = await axios.post(url, { regionId }, { headers }); // Enviar solicitud POST
        const { data, status } = response; // Obtener datos y estado de la respuesta
        if (status == 200) {
            let selectComunas = document.querySelector("#comunas") || document.querySelector("#id_comuna"); // Obtener select de comunas
            if (!selectComunas) return;

            selectComunas.innerHTML = "";

            const defaultOption = document.createElement("option"); // Crear opción por defecto
            defaultOption.value = "";
            defaultOption.text = "Seleccione";
            selectComunas.appendChild(defaultOption); // Añadir opción por defecto

            data.data.forEach((item) => {  // Añadir opciones de comunas
                const option = document.createElement("option");
                option.value = item.id;
                option.text = item.nombre;
                selectComunas.appendChild(option);
            });
        } else {
            console.log("No hay comunas disponibles"); // Log si no hay comunas disponibles
        }
    } catch (error) {
        console.log("Error en la petición ", error); // Log de error
    }
};
// Añadir event listener cuando el DOM esté cargado
document.addEventListener('DOMContentLoaded', () => {
    const regionSelect = document.querySelector('#id_region') || document.querySelector('#regiones');
    if (regionSelect) {
        regionSelect.addEventListener('change', (event) => {
            const regionId = event.target.value; // Obtener regionId seleccionado
            if (regionId) {
                filtrarComunas(regionId); // Llamar a filtrarComunas con regionId
            }
        });
    }
});

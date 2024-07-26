// static/js/script.js
const filtrarComunas = async (regionId) => {
    const csrfTokenValue = document.querySelector("[name=csrfmiddlewaretoken]").value;
    const headers = {
        "X-CSRFToken": csrfTokenValue,
    };
    let url = "/filtrar-comunas/";

    console.log("Enviando regionId:", regionId);

    try {
        const response = await axios.post(url, { regionId }, { headers });
        const { data, status } = response;
        if (status == 200) {
            let selectComunas = document.querySelector("#comunas") || document.querySelector("#id_comuna");
            if (!selectComunas) return;

            selectComunas.innerHTML = "";

            const defaultOption = document.createElement("option");
            defaultOption.value = "";
            defaultOption.text = "Seleccione";
            selectComunas.appendChild(defaultOption);

            data.data.forEach((item) => {
                const option = document.createElement("option");
                option.value = item.id;
                option.text = item.nombre;
                selectComunas.appendChild(option);
            });
        } else {
            console.log("No hay comunas disponibles");
        }
    } catch (error) {
        console.log("Error en la petición ", error);
    }
};

document.addEventListener('DOMContentLoaded', () => {
    const regionSelect = document.querySelector('#id_region') || document.querySelector('#regiones');
    if (regionSelect) {
        regionSelect.addEventListener('change', (event) => {
            const regionId = event.target.value;
            if (regionId) {
                filtrarComunas(regionId);
            }
        });
    }
});

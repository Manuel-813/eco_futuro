// Datos simulados (puedes reemplazar por un dataset real)
const datosRenovables = {
        eolica: 1200, // kWh producidos por energía eólica
        solar: 800, // kWh producidos por energía solar
        hidroelectrica: 1500, // kWh producidos por energía hidroeléctrica
        geotermica: 500, // kWh producidos por energía geotérmica
};

// Calcular el total de energía renovable
const totalRenovable = Object.values(datosRenovables).reduce(
    (a, b) => a + b,
    0
);

// Supongamos que el total de energía generada (renovable + no renovable) es:
const totalEnergiaGenerada = 5000; // ejemplo

// Porcentaje de energía renovable en la generación total
const porcentajeRenovableSistema =
    (totalRenovable / totalEnergiaGenerada) * 100;

// Escucha el formulario
document
    .getElementById("form-calculo")
    .addEventListener("submit", function (e) {
        e.preventDefault();

        const consumo = parseFloat(document.getElementById("consumo").value);

        if (isNaN(consumo) || consumo <= 0) {
            document.getElementById("resultado").innerHTML =
                "⚠️ Por favor, ingresa un valor válido.";
            return;
        }

        // Cálculo: qué porcentaje de su consumo podría ser renovable
        const energiaRenovableEstim = (consumo * porcentajeRenovableSistema) / 100;

        document.getElementById(
            "resultado"
        ).innerHTML = `De tu consumo total de <strong>${consumo} kWh</strong>, aproximadamente <strong>${energiaRenovableEstim.toFixed(
            2
        )} kWh</strong> (${porcentajeRenovableSistema.toFixed(
            1
        )}%) provienen de fuentes renovables. 🌞💨💧🔥`;
    });

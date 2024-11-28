document.addEventListener('DOMContentLoaded', function() {

    // Función para generar las tarjetas según los datos recibidos
    function generarTarjetas(data) {
        const resultadosDiv = document.getElementById('resultados');
        resultadosDiv.innerHTML = ''; // Limpiar resultados previos

        data.forEach(item => {
            let tarjetaContenido = '';
            // Recorrer las propiedades del objeto item dinámicamente
            for (const key in item) {
                if (item.hasOwnProperty(key)) {
                    tarjetaContenido += `<p><strong>${key}:</strong> ${item[key]}</p>`;
                }
            }

            // Crear la tarjeta con la información
            const tarjeta = `
                <div class="col-md-4">
                    <div class="card mb-4 shadow-sm">
                        <div class="card-body">
                            <h5 class="card-title">Resultado</h5>
                            ${tarjetaContenido}
                        </div>
                    </div>
                </div>
            `;
            resultadosDiv.innerHTML += tarjeta;
        });
    }

    // Función para hacer la solicitud al backend
    async function llamarProcedimiento(endpoint) {
        const response = await fetch(endpoint);
        const data = await response.json();
        generarTarjetas(data);
    }

    // Configurar botones para cada procedimiento
    document.getElementById('btn-obtener-usuarios').addEventListener('click', function() {
        llamarProcedimiento('/usuarios');
    });

    document.getElementById('btn-contar-vehiculos').addEventListener('click', function() {
        llamarProcedimiento('/vehiculos_post2018');
    });

    document.getElementById('btn-contar-vehiculoXMarca').addEventListener('click', function() {
        llamarProcedimiento('/contarAutoXMarca');
    });

    document.getElementById('btn-contar-VehiculosPorMarcaMinima').addEventListener('click', function() {
        llamarProcedimiento('/vehiculosPorMarcaMinima');
    });

    document.getElementById('btn-solicitudes-ordenadas').addEventListener('click', function() {
        llamarProcedimiento('/solicitudesOrdenadas');
    });

    document.getElementById('btn-top5autosantiguos').addEventListener('click', function() {
        llamarProcedimiento('/top5autosantiguos');
    });

    document.getElementById('btn-marcasDistintas').addEventListener('click', function() {
        llamarProcedimiento('/marcasDistintas');
    });

    document.getElementById('btn-solicitudesIncompletas').addEventListener('click', function() {
        llamarProcedimiento('/solicitudesIncompletas');
    });
});

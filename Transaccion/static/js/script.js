document.addEventListener('DOMContentLoaded', function () {
    function generarTarjetas(data) {
        const resultadosDiv = document.getElementById('resultados');
        resultadosDiv.innerHTML = ''; // Limpiar resultados previos
        data.forEach(item => {
            let tarjetaContenido = '';
            for (const key in item) {
                tarjetaContenido += `<p><strong>${key}:</strong> ${item[key]}</p>`;
            }
            const tarjeta = `
                <div class="col-md-4">
                    <div class="card mb-4 shadow-sm">
                        <div class="card-body">
                            ${tarjetaContenido}
                        </div>
                    </div>
                </div>`;
            resultadosDiv.innerHTML += tarjeta;
        });
    }

    async function llamarProcedimiento(endpoint) {
        try {
            const response = await fetch(endpoint);
            const data = await response.json();
            generarTarjetas(data);
        } catch (error) {
            console.error('Error:', error);
        }
    }

    const botones = [
        { id: 'btn-obtener-usuarios', endpoint: '/usuarios' },
        { id: 'btn-contar-vehiculos', endpoint: '/vehiculos_post2018' },
        { id: 'btn-contar-vehiculoXMarca', endpoint: '/contarAutoXMarca' },
        { id: 'btn-contar-VehiculosPorMarcaMinima', endpoint: '/vehiculosPorMarcaMinima' },
        { id: 'btn-solicitudes-ordenadas', endpoint: '/solicitudesOrdenadas' },
        { id: 'btn-top5autosantiguos', endpoint: '/top5autosantiguos' },
        { id: 'btn-marcasDistintas', endpoint: '/marcasDistintas' },
        { id: 'btn-solicitudesIncompletas', endpoint: '/solicitudesIncompletas' }
    ];

    botones.forEach(boton => {
        const elemento = document.getElementById(boton.id);
        if (elemento) {
            elemento.addEventListener('click', () => llamarProcedimiento(boton.endpoint),
            );
        }
    });
});


document.addEventListener('DOMContentLoaded', function () {
    const btnInsertarVehiculo = document.getElementById('btn-insertarVehiculo');
    const formContainer = document.getElementById('resultados');
    const alertasDiv = document.getElementById('alertas');

     // Función para mostrar las alertas
     async function obtenerAlertas() {
        const response = await fetch('/obtener_alertas');
        const alertas = await response.json();

        console.log(alertas)

        alertasDiv.innerHTML = '';  // Limpiar alertas anteriores

        alertas.forEach(alerta => {
            const alertaElemento = document.createElement('div');
            alertaElemento.classList.add('alert', 'alert-warning');
            alertaElemento.innerHTML = `
                <strong>${alerta.tipo}:</strong> ${alerta.mensaje} <br>
                <small>Fecha: ${new Date(alerta.fecha).toLocaleString()}</small>
            `;
            alertasDiv.appendChild(alertaElemento);

            // Hacer que la alerta desaparezca después de 6 segundos
            setTimeout(() => {
                alertaElemento.style.transition = 'opacity 1s ease-out'; // Agregar una transición suave
                alertaElemento.style.opacity = 0; // Hacerla transparente
                setTimeout(() => {
                    alertasDiv.innerHTML = ''; // Eliminar el elemento después de la transición
                }, 1000); // Esperar a que termine la transición
            }, 4000); // 6 segundos antes de que empiece a desvanecerse
        });
        
    }
    
    // Función para crear el formulario dinámicamente
    function crearFormulario() {
        // Verificar si ya hay un formulario
        if (formContainer.innerHTML !== '') {
            formContainer.innerHTML = ''; // Limpiar el contenedor si ya tiene el formulario
        }

        // Crear el formulario
        const formulario = `
            <form id="formVehiculo">
                <div class="mb-3">
                    <label for="marca" class="form-label">Marca</label>
                    <input type="text" class="form-control" id="marca" required>
                </div>
                <div class="mb-3">
                    <label for="modelo" class="form-label">Modelo</label>
                    <input type="text" class="form-control" id="modelo" required>
                </div>
                <div class="mb-3">
                    <label for="anio" class="form-label">Año</label>
                    <input type="number" class="form-control" id="anio" required>
                </div>
                <div class="mb-3">
                    <label for="id_usuario" class="form-label">ID Usuario</label>
                    <input type="number" class="form-control" id="id_usuario" required>
                </div>
                <div class="mb-3">
                    <label for="placa" class="form-label">Placa</label>
                    <input type="text" class="form-control" id="placa" required>
                </div>
                <div class="mb-3">
                    <label for="tipo_de_vehiculo_id" class="form-label">Tipo de Vehículo ID</label>
                    <input type="number" class="form-control" id="tipo_de_vehiculo_id" required>
                </div>
                <button type="submit" class="btn btn-primary">Guardar</button>
            </form>
        `;

        // Insertar el formulario en el contenedor
        formContainer.innerHTML = formulario;
        
        // Agregar el manejador del evento de envío
        const form = document.getElementById('formVehiculo');
        form.addEventListener('submit', async function (event) {
            event.preventDefault();

            const data = {
                marca: document.getElementById('marca').value,
                modelo: document.getElementById('modelo').value,
                anio: parseInt(document.getElementById('anio').value),
                id_usuario: parseInt(document.getElementById('id_usuario').value),
                placa: document.getElementById('placa').value,
                tipo_de_vehiculo_id: parseInt(document.getElementById('tipo_de_vehiculo_id').value),
            };

            const anio = parseInt(document.getElementById('anio').value);
            console.log(anio)

            try {
                const response = await fetch('/insertar_vehiculo', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(data),
                });

                const result = await response.json();
                alert(result.message);  // Mostrar el mensaje de éxito
                
                // Después de insertar el vehículo, consultar las alertas
                    if (anio <= 1980) {
                        obtenerAlertas();
                    }

            } catch (error) {
                console.error('Error:', error);
            }
        });
    }
    // Event listener para el botón
    btnInsertarVehiculo.addEventListener('click', function () {
        crearFormulario();  // Crear el formulario cuando se haga clic
    });
});


from flask import Flask, render_template, jsonify, request
from collections import OrderedDict
import pyodbc

app = Flask(__name__)

# Conexión a la base de datos
def get_db_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=CHRIS\\SQLEXPRESS;DATABASE=Mechanic-D;"
        "Trusted_Connection=yes;"
    )

# Ruta para renderizar el frontend
@app.route('/')
def home():
    return render_template('index2.html')

# Ruta para obtener datos de usuarios
@app.route('/usuarios')
def obtener_usuarios():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("EXEC ObtenerUsuarios")
        resultados = cursor.fetchall()
        # Devolver los resultados en formato JSON
        usuarios = [
            OrderedDict([("Nombre", row[0]), ("apellido", row[1]),]) 
            for row in resultados
        ]
        return jsonify(usuarios)
    except Exception as e:
        return jsonify({"error": str(e)})
    finally:
        cursor.close()
        conn.close()

# Ruta para obtener datos de contar vehiculos
@app.route('/vehiculos_post2018')
def vehiculos_post2018():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("EXEC ListarVehiculosPosterioresA2018")
        resultados = cursor.fetchall()

        print(resultados)

        vehiculos = [{"marca": row[1], "modelo": row[3]} for row in resultados]
        return jsonify(vehiculos)

        
    
    except Exception as e:
        return jsonify({"error": str(e)})
    finally:
        cursor.close()
        conn.close()

# Ruta para mostrar vehiculos y sus marcas
@app.route('/contarAutoXMarca')
def contarAutoXMarca():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT marca, COUNT(*) AS cantidad FROM Vehiculos.Vehiculo GROUP BY marca;")
        resultados = cursor.fetchall()
        # Devolver los resultados en formato JSON
        vehiculos = [{"marca": row[0], "Cantidad": row[1]} for row in resultados]
        return jsonify(vehiculos)
    
    except Exception as e:
        return jsonify({"error": str(e)})
    finally:
        cursor.close()
        conn.close()


@app.route('/vehiculosPorMarcaMinima')
def vehiculosPorMarcaMinima():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT marca, COUNT(*) AS cantidad FROM Vehiculos.vehiculo GROUP BY marca HAVING COUNT(*) >= 2;")
        resultados = cursor.fetchall()
        # Devolver los resultados en formato JSON
        vehiculos = [{"Marca": row[0], "cantidad": row[1]} for row in resultados]
        return jsonify(vehiculos)
    
    except Exception as e:
        return jsonify({"error": str(e)})
    finally:
        cursor.close()
        conn.close()

@app.route('/solicitudesOrdenadas')
def solicitudesOrdenadas():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Solicitud ORDER BY fecha_solicitud DESC;")
        resultados = cursor.fetchall()
        # Devolver los resultados en formato JSON
        vehiculos = [{"Descripcion De Falla": row[3], "Ubicacion Actual": row[4], "Estado": row[5], "Fecha de Solicitud": row[6]} for row in resultados]
        return jsonify(vehiculos)
    
    except Exception as e:
        return jsonify({"error": str(e)})
    finally:
        cursor.close()
        conn.close()

@app.route('/top5autosantiguos')
def top5autosantiguos():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT TOP 5 id_vehiculo, marca, modelo, anio, placa FROM Vehiculos.Vehiculo ORDER BY anio ASC;")
        resultados = cursor.fetchall()
        # Devolver los resultados en formato JSON
        vehiculos = [{"Marca": row[1], "modelo": row[2], "año": row[3], "placa": row[4]} for row in resultados]
        return jsonify(vehiculos)
    
    except Exception as e:
        return jsonify({"error": str(e)})
    finally:
        cursor.close()
        conn.close()


@app.route('/marcasDistintas')
def marcasDistintas():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT marca FROM Vehiculos.Vehiculo ORDER BY marca ASC;")
        resultados = cursor.fetchall()
        # Devolver los resultados en formato JSON
        vehiculos = [{"Marca": row[0]} for row in resultados]
        return jsonify(vehiculos)
    
    except Exception as e:
        return jsonify({"error": str(e)})
    finally:
        cursor.close()
        conn.close()


@app.route('/insertar_vehiculo', methods=['POST'])
def insertar_vehiculo():
    try:
        # Obtener los datos del frontend (JSON)
        data = request.json
        
        # Establecer la conexión a la base de datos
        conn = get_db_connection()
        cursor = conn.cursor()

        # Ejecutar el procedimiento almacenado
        cursor.execute("EXEC InsertarVehiculo ?, ?, ?, ?, ?, ?", 
                       data['marca'], 
                       data['modelo'], 
                       data['anio'], 
                       data['id_usuario'], 
                       data['placa'], 
                       data['tipo_de_vehiculo_id'])
        
        # Confirmar la inserción
        conn.commit()

        return jsonify({"message": "Vehículo insertado correctamente"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()


@app.route('/obtener_alertas', methods=['GET'])
def obtener_alertas():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Consultamos las alertas generadas por el trigger
        cursor.execute("SELECT TOP 1 mensaje, tipo, fecha FROM Alerta ORDER BY id_alerta DESC;")
        alertas = cursor.fetchall()
        
        # Devolver las alertas como JSON
        alertas_lista = [{"mensaje": row[0], "tipo": row[1], "fecha": row[2]} for row in alertas]
        return jsonify(alertas_lista)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()



if __name__ == '__main__':
    app.run(debug=True)
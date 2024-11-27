from flask import Flask, render_template, jsonify
from collections import OrderedDict
import pyodbc

app = Flask(__name__)

# Conexión a la base de datos
def get_db_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=DESKTOP-2KUH2GO\\SQLEXPRESS;DATABASE=Mechanic-D;"
        "Trusted_Connection=yes;"
    )

# Ruta para renderizar el frontend
@app.route('/')
def home():
    return render_template('index.html')

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
        cursor.execute("EXEC ContarVehiculosPorMarca")
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
        cursor.execute("EXEC ContarVehiculosPorMarcaMinima")
        resultados = cursor.fetchall()
        # Devolver los resultados en formato JSON
        vehiculos = [{"Marca": row[0], "cantidad": row[1]} for row in resultados]
        return jsonify(vehiculos)
    
    except Exception as e:
        return jsonify({"error": str(e)})
    finally:
        cursor.close()
        conn.close()



if __name__ == '__main__':
    app.run(debug=True)
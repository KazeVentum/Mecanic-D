
# Mechanic-D

Este proyecto implementa un sistema web que interactúa con procedimientos almacenados en SQL Server, utilizando Flask como backend y JavaScript con Bootstrap para el frontend.

---

## Tecnologías Utilizadas

- **Frontend**: HTML, CSS, JavaScript, Bootstrap.  
- **Backend**: Flask (Python).  
- **Base de Datos**: SQL Server.  
- **Conexión DB**: PyODBC.  
- **Ambiente Virtual**: venv.  

---

## Configuración del Entorno

### 1. Instalación del Ambiente Virtual

1. **Crear un ambiente virtual**:
   ```bash
   python -m venv venv
   ```

2. **Activar el ambiente virtual**:
   - En **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - En **Mac/Linux**:
     ```bash
     source venv/bin/activate
     ```

3. **Instalar las dependencias**:
   ```bash
   pip install Flask pyodbc
   ```

---

### 2. Configuración de SQL Server

1. Asegúrese de que SQL Server esté instalado y en ejecución.  
2. Configure el servidor para aceptar conexiones locales.  
3. Ejecute los procedimientos almacenados requeridos en su base de datos.  

---

### 3. Conexión a SQL Server desde Python

1. Instale el controlador ODBC necesario:
   - Descargue e instale el [ODBC Driver 17 for SQL Server](https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server).

2. Configure la conexión en el archivo Python:
   ```python
   def get_db_connection():
       return pyodbc.connect(
           "DRIVER={ODBC Driver 17 for SQL Server};"
           "SERVER=CHRIS\\SQLEXPRESS;DATABASE=Mechanic-D;"
           "Trusted_Connection=yes;"
       )
   ```

---

### 4. Ejecución del Proyecto

1. **Inicie el servidor Flask**:
   ```bash
   python app.py
   ```

2. **Acceda al frontend**:
   Abra un navegador web y diríjase a:
   ```
   http://127.0.0.1:5000/
   ```

---

## Funcionamiento

### 1. Interfaz Web

La interfaz presenta botones para ejecutar procedimientos almacenados en SQL Server. Los resultados se muestran dinámicamente como tarjetas en la página.

### 2. Procedimientos Disponibles

- **Obtener Usuarios**: Consulta la base de datos y lista los usuarios registrados.  
- **Contar Vehículos Posteriores a 2018**: Filtra vehículos registrados después de 2018.  
- **contar vehículos x marca**: Consulta cuantos vehículos de cada marca están disponibles
- **Mostrar solicitudes ordenadas de manera descendente**: Consulta las solicitudes ordenadas de manera descendente.
- **Mostrar los 5 vehículos más antiguos**: consultara cuales son los 5 vehículos más antiguos de la base de datos.
- **Obtener las marcas únicas distintas**: Obtiene las marcas distintas
- **Mostrar los carros de marca Toyota superiores al año 2015**: Consultara en la base de datos que automóviles de marca Toyota son superiores al año 2015
- **Mostrar las solicitudes que no están completas**: Mostrara las solicitudes que no estén completadas, o que no tengan el estado "Completado  

### 3. Flujo de Trabajo

1. Al hacer clic en un botón, se ejecuta una solicitud al backend Flask.  
2. Flask ejecuta un procedimiento almacenado en SQL Server.  
3. Los datos obtenidos se envían al frontend y se muestran dinámicamente en tarjetas.  

---

## Ejemplo de Uso del Ambiente Virtual (venv)

### 1. Activar Ambiente Virtual

- En Windows:
  ```bash
  venv\Scripts\activate
  ```

- En Mac/Linux:
  ```bash
  source venv/bin/activate
  ```

### 2. Instalar Dependencias

Con el ambiente virtual activado:
```bash
pip install Flask pyodbc
```

### 3. Desactivar Ambiente Virtual

Cuando termine de trabajar:
```bash
deactivate
```

---

## Requerimientos Previos

- Python 3.7 o superior.  
- SQL Server configurado y accesible.  
- Navegador web actualizado.  

---

## Créditos

Desarrollado por **Andres Felipe Pardo Hernandez y Cristian Camilo Pardo Hernandez**.

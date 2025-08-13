
# App Web Sencilla: Frontend + Backend + Docker

Este repositorio contiene una aplicación web de ejemplo que ilustra la arquitectura de un servicio web moderno. Incluye un backend sencillo en Python con Flask que expone una API REST, y un frontend en HTML y JavaScript que consume esa API para realizar operaciones de gestión de usuarios.

El proyecto está diseñado para demostrar cómo se comunican las diferentes partes de una aplicación web, y cómo se puede empaquetar todo usando Docker para facilitar su despliegue.

## Estructura del Proyecto

La estructura de carpetas del repositorio es la siguiente:

```
├── backend
│   ├── back.py
│   └── requirements.txt
├── frontend
│   └── index.html
└── prueba_docker
    ├── backend
    │   ├── Dockerfile
    │   ├── back.py
    │   └── requirements.txt
    ├── docker-compose.yml
    └── frontend
        ├── index.html
        └── nginx.conf

```


## Uso de la Aplicación

Puedes usar la aplicación de dos maneras: directamente en los sistemas operativos de base o usando docker

-----

### Opción 1: Uso sin Docker (Local)


1.  **Instalar dependencias del Backend:**
    Navega a la carpeta `backend` e instala Flask y Flask-CORS.

    ```bash
    pip install -r requirements.txt
    ```
    Se recomienda utilizar un environment de python
    
```bash
    sudo apt install python3-venv
    python3 -m venv prueba_flask
    source prueba_flask/bin/activate
    pip install -r requirements.txt
```


    


2.  **Ejecutar el Backend:**
    Ejecuta el servidor Flask en una terminal.

    ```bash
    python3 app.py
    ```

3.  **Ejecutar el Frontend:**
    Copia el archivo frontend/index.html en /var/www/html

    ```bash
    sudo cp frontend/index.html /var/www/index.html
    ```
4. Verifica que el servidor apache esté ejecutándose. En caso que no, reinicialo

   ```bash
    sudo systemctl status apache2.service
   sudo systemctl restart apache2.service 
    ```

-----

### Opción 2: Uso con Docker

0. **Instalar docker en el servidor**
   [Instalación de docker](https://docs.docker.com/engine/install/ubuntu/)

2.  **Construir y ejecutar los contenedores:**
    Navega a la carpeta `prueba_docker` y usa `docker-compose` para levantar los servicios.

    ```bash
    cd docker
    docker compose up --build
    ```

    El `Dockerfile` en la carpeta backend define cómo se construyen las imágenes, y `docker-compose.yml` orquesta su comunicación.

3.  **Acceder a la Aplicación:**
    Una vez que los contenedores estén corriendo, abre tu navegador y accede a la URL en la que se está ejecutando el servidor http



## Endpoints de la API REST

El backend expone los siguientes endpoints para la gestión de usuarios:

  * **`GET /users`**: Obtener todos los usuarios.
  * **`POST /users`**: Crear un nuevo usuario. (Envía `{"name": "nuevo_usuario"}`)
  * **`DELETE /users/<id>`**: Borrar un usuario específico por su ID.


"""
API RESTful para la gestión de usuarios.

Este script de Flask implementa un backend sencillo para una aplicación de gestión
de usuarios. Utiliza un diccionario en memoria como base de datos.
El servidor expone los siguientes endpoints de una API REST para realizar
operaciones CRUD básicas (Crear, Leer, Borrar) sobre la colección de usuarios:

- GET /users: Retorna la lista completa de usuarios.
- POST /users: Crea un nuevo usuario. Espera un JSON con el campo 'name'.
- DELETE /users/<id>: Borra un usuario específico por su ID.

Para permitir que un frontend se comunique con esta API desde un origen
diferente, se ha habilitado la gestión de CORS.

Para ejecutar el servidor, simplemente corre este script:
$ python3 app.py
El servidor escuchará en todas las IPs del host, en el puerto 5000.

Los decoradores @app.route([recurso], methods=['[Método]'] son funciones 
que reciben funciones como argumento. Entonces una vez se reciba una petición
con ese método a ese recurso se ejecutará el código de la función sobre la que
se pone el decorador.

"""

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

users = {
    1: {"name": "Alice"},
    2: {"name": "Bob"}
}
user_id_counter = 3

@app.route('/users', methods=['GET'])
def get_users():
    users_list = [{"id": uid, "name": user["name"]} for uid, user in users.items()]
    return jsonify(users_list)

@app.route('/users', methods=['POST'])
def create_user():
    global user_id_counter
    new_user_data = request.get_json()
    
    if "name" not in new_user_data:
        return jsonify({"error": "El campo 'name' es requerido"}), 400
    
    new_user = {"name": new_user_data["name"]}
    users[user_id_counter] = new_user
    new_user_id = user_id_counter
    user_id_counter += 1
    
    return jsonify({"id": new_user_id, "name": new_user["name"]}), 201

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({"message": f"Usuario con ID {user_id} borrado"}), 200
    else:
        return jsonify({"error": "Usuario no encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)

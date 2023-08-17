from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
    {"label": "My first task", "done": False},
    {"label": "My second task", "done": False}
]


@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text, 200


@app.route('/todos', methods=['POST'])
def add_new_todo():
    # print("¿Que contiene request? :" , request.data)
    # request_body = request.json
    # print("Incoming request with the following body", request_body)
    # return 'Response for the POST todo'

    decoded = request.get_json()  # decodifica la peticion
    print("peticion es igual:", decoded)

    # Agrego el diccionario a la lista todos:
    todos.append(decoded)
    print(todos)

    # Devolver la lista jsonificada:
    json_text = jsonify(todos)
    return json_text, 200


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ", position)


    longitud = len(todos)  # cantidad de elementos
    print("longitud:", longitud)

    max_index = longitud-1
    if position > max_index:
        return jsonify({"message": "el numero es mayor a la cantidad de indices"})

    if longitud == 0:
        return jsonify({"message": "la lista esta vacia y por eso max_index esta vacia"})

    # Ahora eliminamos elementos de la lista segun su indice

    todos.pop(position)

    json_text = jsonify(todos)
    return json_text, 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)

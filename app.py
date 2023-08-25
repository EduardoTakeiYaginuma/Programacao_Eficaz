from flask import Flask, request

sabores_sorvete = ["pistache", "vanila", "chocolate", "passas ao rum", ]

app = Flask("Minha sorveteria")

@app.route("/")
def hello_world():
    return "<p>Hello, World! Edu </p>"

@app.route("/sabores", methods = ["GET"])
def sabores():

    dict_resp = {"sabores": sabores_sorvete}

    return dict_resp

@app.route("/adicionar_sabor", methods = ["POST"])
def adicionando_sabor():
    request_data = request.json
    print(request_data)
    # request.get_json(force=True) # o force=True faz com que ele tente transoformar o conteudo em json caso a pessoa tenha esquecido de colocar no formato

    if "sabor" not in request_data:
        return "Sabor não informado", 400

    sabores_sorvete.append(request_data["sabor"])
    return "Foi adicionado com sucesso"

@app.route("/apagar_sabor", methods = ["GET"])
def apagar_sabor():

    if "sabor" not in request.args:
        return "Sabor não informado", 400
    
    arg_sabor = request.args.get("sabor")
    # request.get_json(force=True) # o force=True faz com que ele tente transoformar o conteudo em json caso a pessoa tenha esquecido de colocar no formato

    if arg_sabor not in sabores_sorvete:
        return "Sabor não encontrado", 404
    
    sabores_sorvete.remove(arg_sabor)
    return "Sabor apagado"

@app.route("/sabor/<int:id_list>", methods = ["GET"])
def sabor(id_list):
    dict_resp = {"sabor": sabores_sorvete[id_list]}
    return dict_resp


if __name__ == "__main__":
    app.run(debug=True)
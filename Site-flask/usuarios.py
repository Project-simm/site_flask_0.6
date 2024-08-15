from flask import Flask, render_template, request,redirect,url_for
"""
    /usuario/ (get)  - index/lista dos remedios cadastrados
    /usuario/ (post)
    /usuario/cadastro  (get) - renderizar o formulario para outro remedio
    /usuarios/<id> (get) obter dados do remedio
    /usuarios/<id>/edit(get) - renderizar o formulario para editar o remedio
    /usuarios/<id>/update(put) - atualizar o remedio
    /usuarios/<id>/delete (delete) - deleta o remedio
"""
app = Flask(__name__)
#rota para login do gogle
@app.route("/")
def home(user):
    #para colocar o Ola pessoa no site
    medicamentos = 0 #colocar o codigo do banco
    nome = user.usuario
    return render_template("index.html", nome=nome, medicamentos=medicamentos)
#Ao cadastrar o remedio no /cadastro ele ira para o home e atualizara a pagina e fará a função abaixo inserir_remedio
@app.route("/cadastro", methods=['GET','POST'])
def inserir_remedio():
    if request.method == 'POST':
        nome = request.form['nome']
        data = request.form['date']
        tempo = request.form['time']
        quantidade = request.form['qtd']
        repetir = request.form['number']
        print(f"nome{nome}")
    else:
        return render_template("gerenciador.html")


@app.route("/edit/<int:remedio_id>/edit", methods=['GET','POST'])
def editar_remedio(remedio_id):
    #pegar o id do remedio
    if request.method == 'POST':
        nome = request.form['nome']
        data = request.form['date']
        tempo = request.form['time']
        quantidade = request.form['qtd']
        repetir = request.form['number']
        #atualizar o remedio
        return redirect(url_for("/"))
    return render_template('gerenciador.html', remedio=remedio)
@app.route("/<int:remedio_id>/update", methods=["PUT"])
def atualizar_remedio(remedio_id):
    pass
@app.route("/<id:remedio_id>/delete",methods=['POST'])
def deletar_remedio(remedio_id):
    #usar o id para achar o remedio
    #mostrar informações do remedio 
    return print("mensagens")# colocar como alerta 
    return redirect(url_for('/'))
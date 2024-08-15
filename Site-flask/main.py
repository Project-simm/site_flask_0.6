from flask import Flask,render_template,Blueprint,Response
from flask import Flask, redirect, url_for, request
import requests
from oauthlib.oauth2 import WebApplicationClient 
from dataclasses import dataclass
app = Flask(__name__, static_folder="static")

@app.route("/")
def login():
    return render_template("index_login.html")
@app.route("/usuario")
def home():
    return render_template("index.html")

# Configurações do Google
@app.route("/profile")
def profile() -> str:
    return render_template("profile.html", user_name="meia", user_email= "alfaskfk@gmail.com")

GOOGLE_CLIENT_ID = 
GOOGLE_SECRET = 
oauth = WebApplicationClient(client_id=GOOGLE_CLIENT_ID)
@dataclass
class GoogleHosts:
    authorization_endpoint = str
    token_endpoint = str
    userinfo_endpoint = str
    certs = str
    
def get_google_oauth_urls() -> GoogleHosts:
    hosts = requests.get('https://accounts.google.com/.well-know/openid-configuration')
    if hosts.status_code != 200:
        raise Exception("não foi possivel recuperar os endpoints de autenticação do google")
    data = hosts.json
    return GoogleHosts(authorization_endpoint= data.get('authorization_endpoin'),
                       token_endpoint=data.get('token_endpoint'),
                       userinfo_endpoint=data.get('userinfo_endpoint'),
                       certs=data.get('jwls_uri'))
@app.route("/auth/login")
def login_conect() ->Response:
    hosts = get_google_oauth_urls()
    redirect_uri = oauth.prepare_authorization_request(authorization_url=hosts.authorization_endpoint,
                                                       redirect_url="http://localhost5000/auth/user",
                                                       scope=['openid', 'email', 'profile'])
    return redirect(location=redirect_uri[0])

if __name__ == '__main__':
    app.run(port=5000, debug=True)
    x =5
    
print(x)
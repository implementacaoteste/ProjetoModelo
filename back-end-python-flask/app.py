
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# # Importando as rotas
# from routes import *

# if __name__ == '__main__':
#     app.run(debug=True)






# app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate
#from app.routes import bp as routes_bp

# # Criação da aplicação Flask
app = Flask(__name__)

# # Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
##migrate = Migrate(app, db)

# # Registro das rotasv
# app.register_blueprint(routes_bp)

# if __name__ == '__main__':
#     # Execução do servidor web
#     app.run(debug=True)






# from flask import Flask

# app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Olá, Mundo!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

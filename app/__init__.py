from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_debugtoolbar import DebugToolbarExtension
from config import Config
from flask_login import LoginManager

#from flask_sqlalchemy import SQLAlchemy

app                 = Flask(__name__)
app.config.from_object(Config)
login_manager       = LoginManager(app)
db                  = SQLAlchemy(app)
migrate             = Migrate(app, db)
#toolban             = DebugToolbarExtension(app)

#app.config['SECRET_KEY']='anything'

from app.main.routes import blue
from app.admin.routes import blue
from app.account.routes import blue
from app.payment.routes import blue
from app.student.routes import blue
from app.login.routes import blue
#from app.logout.routes import blue

app.register_blueprint(main.routes.blue)
app.register_blueprint(admin.routes.blue)
app.register_blueprint(account.routes.blue)
app.register_blueprint(payment.routes.blue)
app.register_blueprint(student.routes.blue)
app.register_blueprint(login.routes.blue)
#app.register_blueprint(logout.routes.blue)

from app.main import routes, models

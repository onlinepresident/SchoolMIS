from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_debugtoolbar import DebugToolbarExtension
from config import Config
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


#app.config['SECRET_KEY']='anything'
# toolban = DebugToolbarExtension(app)


from app.main.routes import blue
from app.admin.routes import blue
from app.account.routes import blue
from app.payment.routes import blue
from app.student.routes import blue
from app.login.routes import blue

app.register_blueprint(main.routes.blue)
app.register_blueprint(admin.routes.blue)
app.register_blueprint(account.routes.blue)
app.register_blueprint(payment.routes.blue)
app.register_blueprint(student.routes.blue)
app.register_blueprint(login.routes.blue)

from app.main import routes, models

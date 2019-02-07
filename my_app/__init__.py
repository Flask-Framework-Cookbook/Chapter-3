from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from redis import Redis


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.debug = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)

redis = Redis()

from my_app.catalog.views import catalog
app.register_blueprint(catalog)

db.create_all()

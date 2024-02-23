from flask import Flask
from app.config import config_options as AppConfig
from app.models import db
from flask_migrate import Migrate

def create_app(config_name="prd"):
    app = Flask(__name__)
    current_config = AppConfig[config_name]
    print("Current Config is: ", current_config)

    app.config['SQLALCHEMY_DATABASE_URI'] = current_config.SQLALCHEMY_DATABASE_URI
    app.config.from_object(current_config)
    
    db.init_app(app)
    migrate = Migrate(app, db, render_as_batch=True)

    from app.bookStore.views import get_index
    app.add_url_rule("/", view_func=get_index,endpoint="landing")


    from app.bookStore import bookStore_blueprint
    app.register_blueprint(bookStore_blueprint)


    return app
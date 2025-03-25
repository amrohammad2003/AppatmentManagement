from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

# ✅ Define db before importing models
db = SQLAlchemy()
migrate = Migrate()

def configure_app(app):
    """Configure app with database and other settings."""

    # ✅ Ensure `SQLALCHEMY_DATABASE_URI` is set BEFORE initializing `db`
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345@localhost/ApartmentManagementDB'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # ✅ Initialize database and migrations BEFORE importing models
    db.init_app(app)
    migrate.init_app(app, db)

    # ✅ Now, import models AFTER initializing db
    from Classes.User import User  
    from Classes.Apartment import Apartment  

    # Enable CORS for the entire app
    CORS(app)

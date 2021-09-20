from quart import Quart

import quart.flask_patch

from flask_sqlalchemy import SQLAlchemy

from config import DevConfig

app = Quart(__name__)
app.config.from_object(DevConfig)

db = SQLAlchemy(app)

from app import models

db.create_all()


def get_db_session() -> db.Session:
    return db.session


app_api = Api(app)

from app.api.resources import material

# app_api.add_resource(material.MaterialResource, '/api/material/<int:m_id>')
# app_api.add_resource(material.MaterialsResource, '/api/materials')

# app.register_blueprint(blueprint_relations)

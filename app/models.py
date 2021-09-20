from app import db
from sqlalchemy_serializer import SerializerMixin

part_product = db.Table('part_product',
                        db.Column('part_id', db.Integer, db.ForeignKey('part.id')),
                        db.Column('product_id', db.Integer, db.ForeignKey('product.id'))
                        )


class OperationPart(db.Model, SerializerMixin):
    operation_id = db.Column(db.Integer, db.ForeignKey('operation.id'), primary_key=True)
    operation = db.relationship('Operation', backref=db.backref('parts',
                                                                cascade='save-update, merge, delete, delete-orphan'))

    part_id = db.Column(db.Integer, db.ForeignKey('part.id'), primary_key=True)
    part = db.relationship('Part', backref=db.backref('operations',
                                                      cascade='save-update, merge, delete, delete-orphan'))

    time = db.Column(db.Float, nullable=False)


class RawMaterial(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    waste_coef = db.Column(db.Float, nullable=False)

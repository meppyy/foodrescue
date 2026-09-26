from ..extensions import db


class Volunteer(db.Model):
    __tablename__ = "volunteers"

    volunteer_id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.user_id"),
        nullable=False,
        unique=True,
    )

    availability = db.Column(db.String(100), nullable=False)
    service_area = db.Column(db.String(150), nullable=False)

    user = db.relationship("User", back_populates="volunteer")

    allocations = db.relationship(
        "Allocation",
        back_populates="volunteer",
    )
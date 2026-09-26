from ..extensions import db


class Allocation(db.Model):
    __tablename__ = "allocations"

    allocation_id = db.Column(db.Integer, primary_key=True)

    request_id = db.Column(
        db.Integer,
        db.ForeignKey("food_requests.request_id"),
        nullable=False,
        unique=True,
    )

    volunteer_id = db.Column(
        db.Integer,
        db.ForeignKey("volunteers.volunteer_id"),
        nullable=True,
    )

    pickup_time = db.Column(db.DateTime)
    delivery_time = db.Column(db.DateTime)

    status = db.Column(
        db.String(30),
        nullable=False,
        default="Unassigned",
    )

    request = db.relationship(
        "FoodRequest",
        back_populates="allocation",
    )

    volunteer = db.relationship(
        "Volunteer",
        back_populates="allocations",
    )
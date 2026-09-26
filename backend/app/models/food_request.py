from datetime import datetime

from ..extensions import db


class FoodRequest(db.Model):
    __tablename__ = "food_requests"

    request_id = db.Column(db.Integer, primary_key=True)

    listing_id = db.Column(
        db.Integer,
        db.ForeignKey("food_listings.listing_id"),
        nullable=False,
    )

    recipient_id = db.Column(
        db.Integer,
        db.ForeignKey("recipients.recipient_id"),
        nullable=False,
    )

    requested_quantity = db.Column(
        db.Numeric(10, 2),
        nullable=False,
    )

    request_time = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    status = db.Column(
        db.String(30),
        nullable=False,
        default="Pending",
    )

    listing = db.relationship(
        "FoodListing",
        back_populates="requests",
    )

    recipient = db.relationship(
        "Recipient",
        back_populates="food_requests",
    )

    allocation = db.relationship(
        "Allocation",
        back_populates="request",
        uselist=False,
        cascade="all, delete-orphan",
    )
from datetime import datetime

from ..extensions import db


class FoodListing(db.Model):
    __tablename__ = "food_listings"

    listing_id = db.Column(db.Integer, primary_key=True)

    donor_id = db.Column(
        db.Integer,
        db.ForeignKey("donors.donor_id"),
        nullable=False,
    )

    food_name = db.Column(db.String(150), nullable=False)
    category = db.Column(db.String(100), nullable=False)

    quantity = db.Column(db.Numeric(10, 2), nullable=False)
    unit = db.Column(db.String(30), nullable=False)

    preparation_time = db.Column(db.DateTime, nullable=False)
    listing_time = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False,
    )
    expiry_time = db.Column(db.DateTime, nullable=False)

    location = db.Column(db.Text, nullable=False)
    dietary_type = db.Column(db.String(50), nullable=False)

    packaging_info = db.Column(db.String(255))
    description = db.Column(db.Text)
    special_handling_requirements = db.Column(db.Text)

    priority_level = db.Column(
        db.String(20),
        nullable=False,
        default="Low",
    )

    status = db.Column(
        db.String(30),
        nullable=False,
        default="Available",
    )

    donor = db.relationship(
        "Donor",
        back_populates="food_listings",
    )

    requests = db.relationship(
        "FoodRequest",
        back_populates="listing",
        cascade="all, delete-orphan",
    )
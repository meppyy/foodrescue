from ..extensions import db


class Donor(db.Model):
    __tablename__ = "donors"

    donor_id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.user_id"),
        nullable=False,
        unique=True,
    )

    organization_name = db.Column(db.String(150))
    address = db.Column(db.Text, nullable=False)

    user = db.relationship("User", back_populates="donor")

    food_listings = db.relationship(
        "FoodListing",
        back_populates="donor",
        cascade="all, delete-orphan",
    )
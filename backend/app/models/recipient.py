from ..extensions import db


class Recipient(db.Model):
    __tablename__ = "recipients"

    recipient_id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.user_id"),
        nullable=False,
        unique=True,
    )

    organization_name = db.Column(db.String(150))
    verification_status = db.Column(
        db.String(20),
        nullable=False,
        default="pending",
    )
    address = db.Column(db.Text, nullable=False)

    user = db.relationship("User", back_populates="recipient")

    food_requests = db.relationship(
        "FoodRequest",
        back_populates="recipient",
        cascade="all, delete-orphan",
    )
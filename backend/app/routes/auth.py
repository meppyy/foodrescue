from flask import Blueprint, jsonify, request
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from ..extensions import db
from ..models import Donor, Recipient, User, Volunteer

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")


ALLOWED_ROLES = {"donor", "recipient", "volunteer"}


@auth_bp.post("/register")
def register():
    data = request.get_json(silent=True) or {}

    name = data.get("name", "").strip()
    email = data.get("email", "").strip().lower()
    password = data.get("password", "")
    phone = data.get("phone", "").strip()
    role = data.get("role", "").strip().lower()

    if not name or not email or not password or not role:
        return jsonify({
            "status": "error",
            "message": "Name, email, password, and role are required",
            "error_code": "MISSING_FIELDS",
        }), 400

    if role not in ALLOWED_ROLES:
        return jsonify({
            "status": "error",
            "message": "Invalid registration role",
            "error_code": "INVALID_ROLE",
        }), 400

    if len(password) < 8:
        return jsonify({
            "status": "error",
            "message": "Password must contain at least 8 characters",
            "error_code": "WEAK_PASSWORD",
        }), 400

    existing_user = User.query.filter_by(email=email).first()

    if existing_user:
        return jsonify({
            "status": "error",
            "message": "An account with this email already exists",
            "error_code": "EMAIL_EXISTS",
        }), 409

    user_status = "active"

    if role == "recipient":
        user_status = "pending"

    user = User(
        name=name,
        email=email,
        password=generate_password_hash(password),
        phone=phone or None,
        role=role,
        status=user_status,
    )

    db.session.add(user)
    db.session.flush()

    if role == "donor":
        donor = Donor(
            user_id=user.user_id,
            organization_name=data.get("organization_name"),
            address=data.get("address", "").strip(),
        )
        db.session.add(donor)

    elif role == "recipient":
        recipient = Recipient(
            user_id=user.user_id,
            organization_name=data.get("organization_name"),
            verification_status="pending",
            address=data.get("address", "").strip(),
        )
        db.session.add(recipient)

    elif role == "volunteer":
        volunteer = Volunteer(
            user_id=user.user_id,
            availability=data.get("availability", "").strip(),
            service_area=data.get("service_area", "").strip(),
        )
        db.session.add(volunteer)

    db.session.commit()

    message = "Registration successful"

    if role == "recipient":
        message = "Registration submitted. Await administrator verification."

    return jsonify({
        "status": "success",
        "message": message,
        "data": {
            "user_id": user.user_id,
            "name": user.name,
            "email": user.email,
            "role": user.role,
            "status": user.status,
        },
    }), 201


@auth_bp.post("/login")
def login():
    data = request.get_json(silent=True) or {}

    email = data.get("email", "").strip().lower()
    password = data.get("password", "")

    if not email or not password:
        return jsonify({
            "status": "error",
            "message": "Email and password are required",
            "error_code": "MISSING_CREDENTIALS",
        }), 400

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        return jsonify({
            "status": "error",
            "message": "Invalid email or password",
            "error_code": "INVALID_CREDENTIALS",
        }), 401

    if user.status != "active":
        return jsonify({
            "status": "error",
            "message": "This account is not active",
            "error_code": "ACCOUNT_INACTIVE",
        }), 403

    login_user(user)

    return jsonify({
        "status": "success",
        "message": "Login successful",
        "data": {
            "user_id": user.user_id,
            "name": user.name,
            "email": user.email,
            "role": user.role,
        },
    }), 200


@auth_bp.post("/logout")
@login_required
def logout():
    logout_user()

    return jsonify({
        "status": "success",
        "message": "Logout successful",
    }), 200


@auth_bp.get("/me")
@login_required
def get_current_user():
    return jsonify({
        "status": "success",
        "data": {
            "user_id": current_user.user_id,
            "name": current_user.name,
            "email": current_user.email,
            "phone": current_user.phone,
            "role": current_user.role,
            "status": current_user.status,
        },
    }), 200

## admin accounts will be created through a controlled process later
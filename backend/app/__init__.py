from flask import Flask

from .extensions import db, login_manager


def create_app():
    app = Flask(
        __name__,
        template_folder="../../frontend/templates",
        static_folder="../../frontend/static",
    )

    app.config.from_object("app.config.Config")

    db.init_app(app)
    login_manager.init_app(app)

    @app.get("/api/health")
    def health_check():
        return {
            "status": "success",
            "message": "FoodRescue backend is running"
        }

    return app
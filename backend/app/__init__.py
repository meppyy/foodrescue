from flask import Flask


def create_app():
    app = Flask(
        __name__,
        template_folder="../../frontend/templates",
        static_folder="../../frontend/static",
    )

    app.config.from_object("app.config.Config")

    @app.get("/api/health")
    def health_check():
        return {
            "status": "success",
            "message": "FoodRescue backend is running"
        }

    return app
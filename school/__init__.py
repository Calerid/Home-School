import os

from flask import Flask
from school.routes import get_routes

from school.config import DevelopmentConfig, ProductionConfig, TestingConfig


def start_school():
    school = Flask(__name__)

    environment = os.getenv("FLASK_ENV", "development")

    if environment == "development":
        school.config.from_object(DevelopmentConfig)
    elif environment == "testing":
        school.config.from_object(TestingConfig)
    elif environment == "production":
        school.config.from_object(ProductionConfig)
    else:
        raise ValueError(f"Invalid environment:  {environment}")

    @get_routes
    def register_routes(school: Flask, routes):
        """
        Retrieves and registers an array of routes.
        """
        for route in routes
            school.register_blueprint(route)


    return school

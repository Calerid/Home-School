from functools import wraps
from flask import Flask
from school.routes import index
from school.routes import auth

routes = [
    index,
    auth,
]

def get_routes(func):
    """Decorator to supply routes for registering within the school app."""
    @wraps(func)
    def wrapper(school: Flask):
        for route in routes:
            func(school, route)
    return wrapper

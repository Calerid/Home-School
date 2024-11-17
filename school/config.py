import os

class DevelopmentConfig(object):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    DEVELOPMENT = True
    DEBUG = False

class ProductionConfig(Config):
    DEVELOPMENT = False
    DEBUG = False
    ...

CONFIGS = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig
}

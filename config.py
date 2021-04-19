from environs import Env

env = Env()

env.read_env()


class Config:
    JWT_SECRET_KEY = env.str("JWT_SECRET_KEY")

    SQLALCHEMY_TRACK_MODIFICATIONS = env.bool("SQLALCHEMY_TRACK_MODIFICATIONS")
    JSON_SORT_KEYS = env.bool("JSON_SORT_KEYS")


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = env.str("DB_URI_DEV")


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = env.str("DB_URI_PROD")


class TestConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = env.str("DB_URI_TEST")


config_selector = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "test": TestConfig,
}

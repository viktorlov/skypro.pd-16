# Licensed under the Apache License, Version 2.0 (the "License");
# ----------------------------------------------------------------
# ok
# ----------------------------------------------------------------
from config import BASE_DIR, DevelopmentConfig, TestingConfig
from server import create_app


class TestConfig:
    def test_development(self):
        app_config = create_app(DevelopmentConfig).config
        assert app_config["TESTING"] is False
        assert app_config["DEBUG"] is True
        assert app_config["SQLALCHEMY_DATABASE_URI"] == "sqlite:///" + BASE_DIR.joinpath('project.db').as_posix()
        assert app_config["SQLALCHEMY_ECHO"] is True
        assert app_config["HOST"] == '127.0.0.175'
        assert app_config["PORT"] == 10175

    def test_testing(self):
        app_config = create_app(TestingConfig).config
        assert app_config["TESTING"] is True
        assert app_config["SQLALCHEMY_DATABASE_URI"] == "sqlite:///:memory:"
        assert app_config["DEBUG"] is False

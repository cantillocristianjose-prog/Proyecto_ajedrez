"""Ctrl + Shift + P y poner "Python: Select Interpreter" y seleccionar el interprete de python que diga venv"""
import reflex as rx
import styles.styles as styles
from fastapi import FastAPI
from pages.index import index
from pages.libros import libros
from api.api import API_hello
from fastapi import FastAPI

api = FastAPI()

app = rx.App(
    style=styles.BASE_STYLE,
    stylesheets=styles.STYLESHEETS,
    api_transformer=API_hello
)

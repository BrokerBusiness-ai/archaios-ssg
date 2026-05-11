"""WSGI entry point dla Cyber_Folks Phusion Passenger.

Cyber_Folks używa Passenger który wymaga WSGI callable.
FastAPI jest ASGI — używamy adapter `a2wsgi` żeby owinąć ASGI app jako WSGI.
"""

import os
import sys

# Dodaj katalog projektu do PYTHONPATH (żeby `from app.main import app` działało)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from a2wsgi import ASGIMiddleware
from app.main import app as fastapi_app

# Cyber_Folks Passenger oczekuje obiektu o nazwie `application`
application = ASGIMiddleware(fastapi_app)

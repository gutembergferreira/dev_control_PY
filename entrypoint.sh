#!/bin/bash
echo "Iniciando servidor Flask"
export FLASK_DEBUG=1
export FLASK_APP=wsgi.py
gunicorn -b 0.0.0.0:5000 wsgi:app --timeout 300

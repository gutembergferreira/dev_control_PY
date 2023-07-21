#!/bin/bash
echo "Iniciando servidor Flask"
export FLASK_DEBUG=1
export FLASK_APP=app_dc.py

# Carregar variáveis de ambiente a partir do arquivo .env (se existir)
if [ -f .env ]; then
  echo "Carregando variáveis de ambiente do arquivo .env"
  export $(cat .env | grep -v '^#' | xargs)
fi

# Verificar se a variável PORT_APP foi definida
if [ -z "$PORT_APP" ]; then
  echo "A variável PORT_APP não foi definida. Usando porta padrão 8000."
  PORT_APP=8000
fi

gunicorn -b 0.0.0.0:${PORT_APP} app_dc:app --timeout 300 --log-level info --config services/logger_devicecontrol.py

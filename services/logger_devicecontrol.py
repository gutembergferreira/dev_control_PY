import re
import logging
from datetime import datetime
import pytz


def pre_request(worker, req):
    if req.method:
        if not re.match(r'^/static/.*', req.path):
            # Configurar o arquivo de log
            logging.basicConfig(filename='logs/access.log', level=logging.INFO)
            tz_amazonas = pytz.timezone('America/Manaus')
            current_time = datetime.now(tz_amazonas).strftime('%d-%m-%Y %H:%M:%S')
            logging.info(' %s - Request: %s - %s - remoteIP: %s', current_time, req.method, req.path, req.peer_addr)
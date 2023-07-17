import os
import json

basedir = os.path.dirname(os.path.realpath(__file__))
credential_path = os.path.join(basedir, 'credential', 'bot-monitor.json')
with open(credential_path) as file:
    credential = json.load(file)
template_dir = os.path.abspath('./web/templates/')
static_dir = os.path.abspath('./web/static/')
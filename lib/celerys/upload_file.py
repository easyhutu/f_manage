import requests
from app.models.admin.config import FConfig
from settings import SERVER_NAME


def upload_file(value_json: dict):
    ad_config = FConfig.query_one(server_name=SERVER_NAME)
    http = ad_config.backup_http
    host = ad_config.backup_ip
    port = ad_config.backup_port
    path = ad_config.backup_path
    backup_url = '{}//{}:{}{}'.format(http, host, port, path)

    with open(value_json['path'], 'rb') as f:
        html = requests.post(backup_url, json=value_json, data=f)
        if html.status_code == 200:

            return 'ok'
        else:
            return html.content

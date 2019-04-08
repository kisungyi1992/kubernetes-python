from __future__ import print_function
from auth.auth_parser import AuthParser
import urllib3, base64, os
from kubernetes import client, config
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class ApiInstanceGetter:

    def __init__(self):
        auth_parser = AuthParser()
        auth_type = auth_parser.get_auth_type()

        if auth_type == auth_parser.IN_CLUSTER_POD_AUTH:
            config.load_incluster_config()

        else:
            configuration = client.Configuration()
            configuration.host = auth_parser.kube_api_server_ip
            configuration.verify_ssl = False  # can be True with ca.crt issued by Kubernetes

            if auth_type == auth_parser.SERVICE_ACCOUNT_TOKEN_AUTH:
                configuration.api_key = {"authorization": "Bearer " + base64.decodebytes(str.encode(auth_parser.service_account_token)).decode()}

            elif auth_type == auth_parser.CERTIFICATE_AUTH:
                configuration.cert_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), auth_parser.cert_file_name)
                configuration.key_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),  auth_parser.cert_key_file_name)

            client.Configuration.set_default(configuration)

    def get_appv1_api_instance(self):
        appv1_api_instance = client.AppsV1Api()
        return appv1_api_instance


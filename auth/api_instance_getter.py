from __future__ import print_function
from auth.auth_parser import AuthParser
import urllib3, base64, os
from kubernetes import client, config
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class ApiInstanceGetter:

    def __set_default_auth(self):
        self.auth_parser = AuthParser()
        self.auth_type = self.auth_parser.get_auth_type()

        if self.auth_type == self.auth_parser.IN_CLUSTER_POD_AUTH:
            config.load_incluster_config()

        else:
            configuration = client.Configuration()
            configuration.host = self.auth_parser.kube_api_server_ip
            configuration.verify_ssl = False  # can be True with ca.crt issued by Kubernetes

            if self.auth_type == self.auth_parser.SERVICE_ACCOUNT_TOKEN_AUTH:
                configuration.api_key = {"authorization": "Bearer " + base64.decodebytes(str.encode(self.auth_parser.service_account_token)).decode()}

            elif self.auth_type == self.auth_parser.CERTIFICATE_AUTH:
                configuration.cert_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), self.auth_parser.cert_file_name)
                configuration.key_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),  self.auth_parser.cert_key_file_name)

            client.Configuration.set_default(configuration)

    def __get_custom_token_auth(self, token):
        configuration = client.Configuration()
        configuration.host = self.auth_parser.kube_api_server_ip
        configuration.verify_ssl = False  # can be True with ca.crt issued by Kubernetes
        configuration.api_key = {"authorization": "Bearer " + base64.decodebytes(token).decode()}
        client.Configuration.set_default(configuration)

    def get_appv1_api_instance(self, custom_token_auth=None):
        if custom_token_auth == None:
            """ Use default auth mounted into pod """
            self.__set_default_auth()
        else:
            self.__get_custom_token_auth(custom_token_auth)

        return client.AppsV1Api()

    def get_corev1_api_instance(self, custom_token_auth=None):
        if custom_token_auth == None:
            """ Use default auth mounted into pod """
            self.__set_default_auth()
        else:
            self.__get_custom_token_auth(custom_token_auth)
        return client.CoreV1Api()
from __future__ import print_function
import urllib3, base64, os
from kubernetes import client, config
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

IN_CLUSTER_POD = 1
SERVICE_ACCOUNT_TOKEN = 2


class ApiInstanceGetter:

    environment_flag = IN_CLUSTER_POD

    def __init__(self, token=False):
        if self.environment_flag == IN_CLUSTER_POD:
            config.load_incluster_config()

        elif self.environment_flag == SERVICE_ACCOUNT_TOKEN:
            configuration = client.Configuration()
            # configuration.host = ("https://KUBE_API_SERVER_IP:6443")
            configuration.host = ("https://" + os.environ['KUBERNETES_PORT_443_TCP_ADDR'])
            configuration.verify_ssl = False
            configuration.api_key = {"authorization": "Bearer " + base64.decodebytes(str.encode(token)).decode()}
            client.Configuration.set_default(configuration)

    # Load auth credential from Service Account token mounted in Pod
    def get_appv1_api_instance(self):
        appv1_api_instance = client.AppsV1Api()
        return appv1_api_instance

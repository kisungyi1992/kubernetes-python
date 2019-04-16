from kubernetes import client
from auth.api_instance_getter import ApiInstanceGetter

# Admission Controller for Service Account should be activated.
class ServiceaccountExamples():
    def create_serviceaccount(self, api_instance, namespace, name, image_pull_secret_name=None):
        body = client.V1ServiceAccount(api_version='v1',
                                       kind='ServiceAccount',
                                       metadata=client.V1ObjectMeta(name=name, namespace=namespace),
                                       automount_service_account_token=True,
                                       image_pull_secrets=image_pull_secret_name if image_pull_secret_name is None else
                                       [client.V1LocalObjectReference(name=image_pull_secret_name)])
        result = api_instance.create_namespaced_service_account(namespace, body)
        return result

    def get_serviceaccount_info(self, api_instance, namespace, name):
        """ exact and export will be removed in 1.18 (currently, deprecated) """
        serviceaccount_response = api_instance.read_namespaced_service_account(name=name, namespace=namespace, exact=True, export=True)
        secret_response = api_instance.read_namespaced_secret(name=serviceaccount_response.secrets[0].name,
                                                              namespace=namespace, exact=True, export=True)
        return secret_response

    def delete_serviceaccount(self, api_instance, namespace, name):
        result = api_instance.delete_namespaced_service_account(namespace=namespace, name=name,
                                                       body=client.V1DeleteOptions(), grace_period_seconds=10)
        return result


if __name__ == '__main__':
    api_instance = ApiInstanceGetter().get_corev1_api_instance()
    ServiceaccountExamples().create_serviceaccount(api_instance=api_instance, namespace='default', name='alicek106', image_pull_secret_name=None)
    serviceaccount_info = ServiceaccountExamples().get_serviceaccount_info(api_instance=api_instance, namespace='default', name='alicek106')
    ServiceaccountExamples().delete_serviceaccount(api_instance=api_instance, namespace='default', name='alicek106')

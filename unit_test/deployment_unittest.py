import unittest
from auth.api_instance_getter import ApiInstanceGetter
from resources.deployment_examples import DeploymentExamples


class DeplymentUnittest(unittest.TestCase):
    api_instance = None

    def setUp(self):
        self.api_instance = ApiInstanceGetter().get_appv1_api_instance()

    def test_list_deployment_all_namespace(self):
        result = DeploymentExamples().list_deployment_all_namespace(self.api_instance)

    def test_list_deployment_namespace(self):
        result = DeploymentExamples().list_deployment_namespace(self.api_instance)

    def test_list_deployment_namespace_by_selector(self):
        result = DeploymentExamples().list_deployment_namespace_by_selector(self.api_instance)

    def test_create_sample_deployment(self):
        result = DeploymentExamples().create_deployment_sample(self.api_instance)
        print(result)

    def test_delete_sample_deployment(self):
        result = DeploymentExamples().delete_deployment_sample(self.api_instance)
        print(result)


if __name__ == '__main__':
    DeplymentUnittest().test_get_deployment()
    unittest.main()
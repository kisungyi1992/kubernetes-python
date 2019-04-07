import unittest
from auth.api_instance_getter import ApiInstanceGetter
from resources.deployment_examples import DeploymentExamples

class DeplymentUnittest(unittest.TestCase):
    api_instance = None

    def setUp(self):
        self.api_instance = ApiInstanceGetter().get_appv1_api_instance()
        # self.api_instance = ApiInstanceGetter(token=value).get_appv1_api_instance()

    def test_get_deployment(self):
        result = DeploymentExamples().list_deployment_all_namespace(self.api_instance)


if __name__ == '__main__':
    unittest.main()
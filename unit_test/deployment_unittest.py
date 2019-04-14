from auth.api_instance_getter import ApiInstanceGetter
from resources.deployment_examples import DeploymentExamples
from messages.deployment_message import DeploymentMessage
import unittest


class DeplymentUnittest(unittest.TestCase):
    api_instance = None

    def setUp(self):
        self.api_instance = ApiInstanceGetter().get_appv1_api_instance()

    def test_sample_deployment(self):
        # List all deployments in namespace
        deployments_all_ns = DeploymentExamples().list_deployment_all_namespace(self.api_instance)
        self.assertGreater(len((deployments_all_ns.items)), 0)

        # Create sample deployment
        result, status = DeploymentExamples().create_deployment_sample(self.api_instance, DeploymentMessage('sample-deployment'))
        self.assertEqual(result['error_code'], 200)

        # Check deployment is created
        deployment_ns = DeploymentExamples().list_deployment_namespace(self.api_instance, 'default')
        self.assertGreater(len((deployment_ns.items)), 0)

        # Get deployment by metadata.name (selector)
        deployment_by_selector = DeploymentExamples().list_deployment_namespace_by_selector(self.api_instance, 'default', 'metadata.name=sample-deployment')
        self.assertEqual(len(deployment_by_selector.items), 1)

        # Get deployment by label
        deployment_by_selector = DeploymentExamples().list_deployment_namespace_by_label(self.api_instance, 'default', 'alicek106_love_is_you=ls')
        self.assertEqual(len(deployment_by_selector.items), 1)

        result, status = DeploymentExamples().delete_deployment_sample(self.api_instance, DeploymentMessage('sample-deployment'))
        self.assertEqual(result['error_code'], 200)

if __name__ == '__main__':
    unittest.main()
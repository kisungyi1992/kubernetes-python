from flask_restful import Resource
from flask import request
import time
import json
from flask import Response
from auth.api_instance_getter import ApiInstanceGetter


class DeploymentExamples(Resource):
    def list_deployment_all_namespace(self, api_instance):
        result = api_instance.list_deployment_for_all_namespaces()
        return result


if __name__ == '__main__':
    api_instance = ApiInstanceGetter().get_appv1_api_instance()
    print(DeploymentExamples().list_deployment_all_namespace(api_instance))

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import pprint
import unittest

from msrest import Deserializer
from msrest.universal_http import HTTPClientResponse


class _TestResponse(HTTPClientResponse):
    def __init__(self, text):
        super(_TestResponse, self).__init__(request=None, internal_response=None)
        self._text = text

    def text(self, encoding=None):
        return self._text


class TestDeserialization(unittest.TestCase):

    # https://github.com/microsoft/azure-devops-python-api/issues/268
    def test_deserialization_issue_268_71(self):
        from azure.devops.v7_1.task_agent import models
        self._test_deserialization(models.__dict__.items(), _268_type, _268_json)

    # https://github.com/microsoft/azure-devops-python-api/issues/268
    def test_deserialization_issue_268_70(self):
        from azure.devops.v7_0.task_agent import models
        self._test_deserialization(models.__dict__.items(), _268_type, _268_json)

    @staticmethod
    def _test_deserialization(models, data_type, json):
        client_models = {k: v for k, v in models if isinstance(v, type)}
        deserializer = Deserializer(client_models)
        response = _TestResponse(json)
        task_agent_response = deserializer(data_type, response)
        pprint.pprint(task_agent_response.__dict__)


if __name__ == '__main__':
    unittest.main()

_268_type = 'TaskAgentReference'
_268_json = '{"id":0,"name":null,"version":null,"osDescription":"Foo","provisioningState":null}'

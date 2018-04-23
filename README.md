[![Visual Studio Team services](https://mseng.visualstudio.com/_apis/public/build/definitions/698eacea-9ea2-4eb8-80a4-d06170edf6bc/5904/badge)]()
[![Python](https://img.shields.io/pypi/pyversions/vsts-cli.svg)](https://pypi.python.org/pypi/vsts)

# Microsoft Visual Studio Team Services Python API

This repository contains Microsoft Visual Studio Team Services Python API. This API is used to build the Visual Studio Team Services CLI. To learn more about the VSTS CLI, check out our [github repo](https://github.com/Microsoft/vsts-cli).

# Installation

```pip install vsts```

# Getting Started

Following is an example how to use the API directly:

```
from vsts.vss_connection import VssConnection
from msrest.authentication import BasicAuthentication
import pprint

token='REDACTED'
team_instance='https://REDACTED.visualstudio.com'

credentials = BasicAuthentication('', token)
connection = VssConnection(base_url=team_instance, creds=credentials)
core_client = connection.get_client('vsts.core.v4_0.core_client.CoreClient')

team_projects = core_client.get_projects()

for project in team_projects:
    pprint.pprint(project.__dict__)
```

# VSTS REST API Documentation

The python SDK is a thin wrapper around the VSTS REST APIs. Please consult our REST API documentation for API specific details while working with this python SDK.

[VSTS REST API Documentation](https://docs.microsoft.com/en-us/rest/api/vsts)

# Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

[![Visual Studio Team services](https://mseng.visualstudio.com/_apis/public/build/definitions/698eacea-9ea2-4eb8-80a4-d06170edf6bc/5904/badge)]()
[![Python](https://img.shields.io/pypi/pyversions/vsts-cli.svg)](https://pypi.python.org/pypi/vsts)

# Azure DevOps Python API

This repository contains Python APIs for interacting with and managing Azure DevOps. These APIs power the Azure DevOps Extension for Azure CLI. To learn more about the Azure DevOps Extension for Azure CLI, visit the [Microsoft/azure-devops-cli-extension](https://github.com/Microsoft/azure-devops-cli-extension) repo.

## Install 

```
pip install azure-devops
```

## Get started


To use the API, establish a connection using a [personal access token](https://docs.microsoft.com/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=vsts) and the URL to your Azure DevOps organization. Then get a client from the connection and make API calls.

```python
from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
import pprint

# Fill in with your personal access token and org URL
personal_access_token = 'YOURPAT'
organization_url = 'https://dev.azure.com/YOURORG'

# Create a connection to the org
credentials = BasicAuthentication('', personal_access_token)
connection = Connection(base_url=organization_url, creds=credentials)

# Get a client (the "core" client provides access to projects, teams, etc)
core_client = connection.clients.get_core_client()

# Get the list of projects in the org
projects = core_client.get_projects()

# Show details about each project in the console
for project in projects:
    pprint.pprint(project.__dict__)
```

## API documentation

This Python library provides a thin wrapper around the Azure DevOps REST APIs. See the [Azure DevOps REST API reference](https://docs.microsoft.com/en-us/rest/api/vsts/?view=vsts-rest-5.0) for details on calling different APIs.

## Samples

Learn how to call different APIs by viewing the samples in the [Microsoft/azure-devops-python-samples](https://github.com/Microsoft/azure-devops-python-samples) repo.

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

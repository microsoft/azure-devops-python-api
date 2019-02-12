from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
from azure.devops.v4_1.work_item_tracking.models import *
import pprint
import io
import mmap
import zipfile
from msrest.pipeline import ClientRawResponse
from azure.devops.v4_0.git.git_client import GitClient

import logging

logging.basicConfig(level=logging.DEBUG)

# Fill in with your personal access token and org URL
personal_access_token = 's7y2vnu66eqywexjurlozop74dm4cjyw6k4kxnwt6stz3wvt5svq'
organization_url = 'https://dev.azure.com/vsalmopen'

# Create a connection to the org
credentials = BasicAuthentication('x', personal_access_token)
connection = Connection(base_url=organization_url, creds=credentials)

# Get a client (the "core" client provides access to projects, teams, etc)
graph_client = connection.get_client('azure.devops.v4_1.graph.graph_client.GraphClient')


personal_access_token2 = 'wwz4hgy23yhzpzwivompixg6tsf27rvmuxgztnxlvy652r3rys7q'
organization_url2 = 'https://dev.azure.com/mseng'
credentials2 = BasicAuthentication('x', personal_access_token2)
connection2 = Connection(base_url=organization_url2, creds=credentials2)
git_client = GitClient(connection2.clients.get_git_client())

connection2.clients.connection
x = git_client.get_pull_request_iteration_changes('AzDevNext', 424307, 2, compare_to=1, project='AzureDevOps').as_dict()
pprint.pprint(x['change_entries'][0])


def upload_callback(chunk, response):
    pprint.pprint('Uploaded chunk of size: ' + str(len(chunk)))
    if response is not None:
        pprint.pprint(response.__dict__)


def upload_work_item_attachment(wit_client, work_item_id, file_name, callback=upload_callback):
    # upload file / create attachment
    with open(file_name, 'r+b') as file:
        # use mmap, so we don't load entire file in memory at the same time, and so we can start
        # streaming before we are done reading the file.
        mm = mmap.mmap(file.fileno(), 0)
        attachment = wit_client.create_attachment(mm, file_name=file_name, callback=upload_callback)

    # Link Work Item to attachment
    patch_document = [
        JsonPatchOperation(
            op="add",
            path="/relations/-",
            value={
                "rel": "AttachedFile",
                "url": attachment.url
            }
        )
    ]
    wit_client.update_work_item(patch_document, work_item_id)


wit_client = connection.get_client('azure.devops.v4_1.work_item_tracking.work_item_tracking_client.WorkItemTrackingClient')

upload_work_item_attachment(wit_client,
                            work_item_id=335,
                            file_name='SQL transient.xlsx')

#upload_work_item_attachment(wit_client,
#                            work_item_id=335,
#                            file_name='\\\\vsncstor\\Users\\tedchamb\\SQLServer2017-x64-ENU.iso')


# groups = graph_client.list_users()

# pprint.pprint(groups.__dict__)

# groups = graph_client.list_users(continuation_token=groups.continuation_token)

# pprint.pprint(groups.__dict__)

# wit_client: object = connection.get_client('azure.devops.v4_1.work_item_tracking.work_item_tracking_client.WorkItemTrackingClient')
#
# wiql = Wiql()
# wiql.query = "Select [System.Id], [System.Title], [System.State] From WorkItems Where [System.WorkItemType] = 'Task'"
#
# wiql_results = wit_client.query_by_wiql(wiql, top=100).work_items
# if wiql_results:
#     pprint.pprint(wiql_results)
#     work_items = (
#         wit_client.get_work_item(int(res.id), expand='Relations') for res in wiql_results
#     )
#     for work_item in work_items:
#         pprint.pprint(work_item)
#         if work_item.relations is not None:
#             for relation in work_item.relations:
#                 if relation.rel == 'AttachedFile':
#                     pprint.pprint(relation.__dict__)
#                     response = wit_client.get_attachment_zip(relation.url.split('/')[-1], download=True, callback=callback)
#                     with open(relation.attributes['name'], 'wb') as f:
#                         for x in response:
#                             f.write(x)



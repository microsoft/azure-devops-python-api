# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class BuildBadge(Model):
    """BuildBadge.

    :param build_id: Build id, if exists that this badge corresponds to
    :type build_id: int
    :param image_url: Self Url that generates SVG
    :type image_url: str
    """

    _attribute_map = {
        'build_id': {'key': 'buildId', 'type': 'int'},
        'image_url': {'key': 'imageUrl', 'type': 'str'}
    }

    def __init__(self, build_id=None, image_url=None):
        super(BuildBadge, self).__init__()
        self.build_id = build_id
        self.image_url = image_url

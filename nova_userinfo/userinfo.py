# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Nova UserInfo Extension
# Copyright 2011 Grid Dynamics
# Copyright 2011 OpenStack LLC.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from nova.api.openstack import extensions
from nova_userinfo.keypairs import UserInfoKeypairsController


class UserInfo(extensions.ExtensionDescriptor):
    """UserInfo Extension."""

    name = "UserInfo"
    alias = "gd-userinfo"
    namespace = "http://docs.openstack.org/compute/ext/userinfo/api/v1.1"
    updated = "2013-01-31T00:00:00+00:00"

    def get_resources(self):
        res = extensions.ResourceExtension(
            'keypairs',
            UserInfoKeypairsController(),
            parent=dict(
                member_name='user',
                collection_name='gd-userinfo'))
        return [res]

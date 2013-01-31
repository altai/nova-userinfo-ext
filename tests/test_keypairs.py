# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Nova UserInfo Extension
# Copyright 2013 Grid Dynamics
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

import unittest
import webob.exc

from nova_userinfo import keypairs


class ValidateTestCase(unittest.TestCase):

    def test_validates_simple(self):
        try:
            keypairs._validate_keypair_name('keypair1')
        except Exception, ex:
            self.fail('Unexpected exception: %s', ex)

    def test_validates_special(self):
        try:
            keypairs._validate_keypair_name('_-42')
        except Exception, ex:
            self.fail('Unexpected exception: %s', ex)

    def test_raises_on_space(self):
        self.assertRaises(webob.exc.HTTPBadRequest,
                          keypairs._validate_keypair_name, 'bad keypair')

    def test_raises_on_empty(self):
        self.assertRaises(webob.exc.HTTPBadRequest,
                          keypairs._validate_keypair_name, '')

    def test_raises_on_long(self):
        self.assertRaises(webob.exc.HTTPBadRequest,
                          keypairs._validate_keypair_name, 'a' * 1024)

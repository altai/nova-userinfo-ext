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

import string
import webob
import webob.exc

from nova.api.openstack import wsgi

from nova import exception
from nova import crypto
from nova import db

from nova.api.openstack.compute.contrib.keypairs import KeypairTemplate
from nova.api.openstack.compute.contrib.keypairs import KeypairsTemplate


_SAFE_KEYPAIR_CHARS = set("_-" + string.digits + string.ascii_letters)


def _validate_keypair_name(value):
    if not 0 < len(value) < 256:
        msg = _('Keypair name must be between 1 and 255 characters long')
        raise webob.exc.HTTPBadRequest(explanation=msg)
    if set(value).difference(_SAFE_KEYPAIR_CHARS):
        msg = _("Keypair name contains unsafe characters")
        raise webob.exc.HTTPBadRequest(explanation=msg)


class UserInfoKeypairsController(object):

    @wsgi.serializers(xml=KeypairsTemplate)
    def index(self, req, user_id):
        """List of keypairs for given user"""
        context = req.environ['nova.context']
        # TODO(imelnikov): authorize context

        key_pairs = db.key_pair_get_all_by_user(context, user_id)
        rval = []
        for key_pair in key_pairs:
            rval.append({'keypair': {
                'user_id': key_pair['user_id'],
                'name': key_pair['name'],
                'public_key': key_pair['public_key'],
                'fingerprint': key_pair['fingerprint'],
            }})

        return {'keypairs': rval}

    @wsgi.serializers(xml=KeypairTemplate)
    def show(self, req, user_id, id):
        context = req.environ['nova.context']
        # TODO(imelnikov): authorize context

        try:
            key_pair = db.key_pair_get(context, user_id, id)
        except exception.KeypairNotFound:
            raise webob.exc.HTTPNotFound()

        return {'keypair': {
            'user_id': key_pair['user_id'],
            'name': key_pair['name'],
            'public_key': key_pair['public_key'],
            'fingerprint': key_pair['fingerprint'],
        }}

    @wsgi.serializers(xml=KeypairTemplate)
    def create(self, req, user_id, body=None):
        """Import key pair"""
        context = req.environ['nova.context']
        # TODO(imelnikov): authorize context

        try:
            params = body['keypair']
        except (TypeError, KeyError):
            msg = _("Missing parameter dict.")
            raise webob.exc.HTTPBadRequest(explanation=msg)

        try:
            name = params['name']
            public_key = params['public_key']
        except KeyError, ex:
            msg = _("Missing '%s' parameter.") % ex.args[0]
            raise webob.exc.HTTPBadRequest(explanation=msg)

        _validate_keypair_name(name)

        try:
            fingerprint = crypto.generate_fingerprint(public_key)
        except exception.InvalidKeypair:
            msg = _("Keypair data is invalid")
            raise webob.exc.HTTPBadRequest(explanation=msg)

        keypair = {
            'user_id': context.user_id,
            'name': name,
            'public_key': public_key,
            'fingerprint': fingerprint
        }
        db.key_pair_create(context, keypair)
        return {'keypair': keypair}

    def delete(self, req, user_id, id):
        """Delete a keypair with a given name"""
        context = req.environ['nova.context']
        # TODO(imelnikov): authorize context

        try:
            db.key_pair_destroy(context, user_id, id)
        except exception.KeypairNotFound:
            raise webob.exc.HTTPNotFound()
        return webob.Response(status_int=202)

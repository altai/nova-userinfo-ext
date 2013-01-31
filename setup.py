#!/usr/bin/python2
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

import os
import sys

from setuptools import setup, find_packages


sys.path.append(os.path.dirname(__file__))

setup(name='nova-userinfo-ext',
      version='1.0',
      license='Apache 2.0',
      description='cloud computing fabric controller',
      author='Grid Dynamics Altai Team, (c) Grid Dynamics',
      author_email='openstack@griddynamics.com',
      url='http://www.griddynamics.com/openstack',
      packages=find_packages(exclude=['tests']),
      test_suite='tests',
      py_modules=[]
)

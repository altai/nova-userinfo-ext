To enable this extension, add to /etc/nova/nova.conf:

::

    osapi_compute_extension = nova.api.openstack.compute.contrib.standard_extensions
    osapi_compute_extension = nova_userinfo.userinfo.UserInfo

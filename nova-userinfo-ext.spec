%global with_doc 0

Name:             nova-userinfo-ext
Version:          1.0
Release:          0
Summary:          Additional user info from nova
License:          Apache 2.0
Vendor:           Grid Dynamics International, Inc.
URL:              http://www.griddynamics.com/openstack
Group:            Development/Languages/Python

Source0:          %{name}-%{version}.tar.gz
BuildArch:        noarch

BuildRequires:    python-setuptools

Requires:         python-webob
Requires:         python-nova


%description
Access SSH keys for any user and other information about user
that is maintained in nova's database.


%prep
%setup -q -n %{name}-%{version}


%build
%{__python} setup.py build


%install
%__rm -rf %{buildroot}

%{__python} setup.py install -O1 --skip-build --prefix=%{_prefix} --root=%{buildroot}


%clean
%__rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README.rst COPYING
%{python_sitelib}/*


%changelog
* Thu Jan 31 2013 Ivan A. Melnikov <imelnikov@griddynamics.com> - 1.0-0
- Initial release


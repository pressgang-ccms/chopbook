# sitelib for noarch packages, sitearch for others (remove the unneeded one)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name:           chopbook
Version:        1.0
Release:        1
Summary:        Utility tool for uploading Publican books to Pressgang CCMS
Group:          Applications/System
License:        LGPL
Vendor:         Red Hat, Inc.
URL:            https://github.com/pressgang-ccms/chopbook

Source0:        chopbook-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       python, python-lxml, python-progressbar, python-httplib2, python-urllib3
BuildArch:      noarch
BuildRequires:  python-devel, python-setuptools

%description
Chopbook is a tool for uploading Publican books to Pressgang CCMS.

%prep
%setup -q

%build
%{__python} setup.py build

%install
#rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
 
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
# For noarch packages: sitelib
%{python_sitelib}/*


%changelog
* Mon Jan 22 2014 Lee Newson <lnewson@redhat.com> - 1.0-1
- Created initial spec file

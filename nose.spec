#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nose
Version  : 1.3.7
Release  : 21
URL      : https://pypi.python.org/packages/source/n/nose/nose-1.3.7.tar.gz
Source0  : https://pypi.python.org/packages/source/n/nose/nose-1.3.7.tar.gz
Summary  : nose extends unittest to make testing easier
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: nose-bin
Requires: nose-python
Requires: nose-doc
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
Patch1: doc-install.patch

%description
Basic usage
***********
Use the nosetests script (after installation by setuptools):

%package bin
Summary: bin components for the nose package.
Group: Binaries

%description bin
bin components for the nose package.


%package doc
Summary: doc components for the nose package.
Group: Documentation

%description doc
doc components for the nose package.


%package python
Summary: python components for the nose package.
Group: Default

%description python
python components for the nose package.


%prep
%setup -q -n nose-1.3.7
%patch1 -p1

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/nosetests
/usr/bin/nosetests-2.7
/usr/bin/nosetests-3.5

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*

#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x4548B3A8C0D70C12 (john@szakmeister.net)
#
Name     : nose
Version  : 1.3.7
Release  : 50
URL      : http://pypi.debian.net/nose/nose-1.3.7.tar.gz
Source0  : http://pypi.debian.net/nose/nose-1.3.7.tar.gz
Source99 : http://pypi.debian.net/nose/nose-1.3.7.tar.gz.asc
Summary  : nose extends unittest to make testing easier
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: nose-bin
Requires: nose-python3
Requires: nose-man
Requires: nose-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-core
BuildRequires : python3-core
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : setuptools-legacypython
Patch1: doc-install.patch

%description
it easier to write, find and run tests.
        
            By default, nose will run tests in files or directories under the current
            working directory whose names include "test" or "Test" at a word boundary
            (like "test_this" or "functional_test" or "TestClass" but not
            "libtest"). Test output is similar to that of unittest, but also includes
            captured stdout output from failing tests, for easy print-style debugging.
        
            These features, and many more, are customizable through the use of
            plugins. Plugins included with nose provide support for doctest, code
            coverage and profiling, flexible attribute-based test selection,
            output capture and more. More information about writing plugins may be

%package bin
Summary: bin components for the nose package.
Group: Binaries
Requires: nose-man

%description bin
bin components for the nose package.


%package extras
Summary: extras components for the nose package.
Group: Default

%description extras
extras components for the nose package.


%package legacypython
Summary: legacypython components for the nose package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the nose package.


%package man
Summary: man components for the nose package.
Group: Default

%description man
man components for the nose package.


%package python
Summary: python components for the nose package.
Group: Default
Requires: nose-python3

%description python
python components for the nose package.


%package python3
Summary: python3 components for the nose package.
Group: Default
Requires: python3-core

%description python3
python3 components for the nose package.


%prep
%setup -q -n nose-1.3.7
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530373187
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test || :
%install
export SOURCE_DATE_EPOCH=1530373187
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/nosetests-2.7
/usr/bin/nosetests
/usr/bin/nosetests-3.7

%files extras
%defattr(-,root,root,-)
/usr/bin/nosetests-2.7

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files man
%defattr(-,root,root,-)
/usr/share/man/man1/nosetests.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

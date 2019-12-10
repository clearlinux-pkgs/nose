#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x4548B3A8C0D70C12 (john@szakmeister.net)
#
Name     : nose
Version  : 1.3.7
Release  : 59
URL      : http://pypi.debian.net/nose/nose-1.3.7.tar.gz
Source0  : http://pypi.debian.net/nose/nose-1.3.7.tar.gz
Source1  : http://pypi.debian.net/nose/nose-1.3.7.tar.gz.asc
Summary  : nose extends unittest to make testing easier
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: nose-bin = %{version}-%{release}
Requires: nose-man = %{version}-%{release}
Requires: nose-python = %{version}-%{release}
Requires: nose-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
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

%description bin
bin components for the nose package.


%package man
Summary: man components for the nose package.
Group: Default

%description man
man components for the nose package.


%package python
Summary: python components for the nose package.
Group: Default
Requires: nose-python3 = %{version}-%{release}

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
cd %{_builddir}/nose-1.3.7
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1576012043
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/nosetests
/usr/bin/nosetests-3.8

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/nosetests.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : docopt
Version  : 0.6.2
Release  : 18
URL      : https://files.pythonhosted.org/packages/a2/55/8f8cab2afd404cf578136ef2cc5dfb50baa1761b68c9da1fb1e4eed343c9/docopt-0.6.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/a2/55/8f8cab2afd404cf578136ef2cc5dfb50baa1761b68c9da1fb1e4eed343c9/docopt-0.6.2.tar.gz
Summary  : Pythonic argument parser, that will make you smile
Group    : Development/Tools
License  : MIT
Requires: docopt-license = %{version}-%{release}
Requires: docopt-python = %{version}-%{release}
Requires: docopt-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
======================================================================

%package license
Summary: license components for the docopt package.
Group: Default

%description license
license components for the docopt package.


%package python
Summary: python components for the docopt package.
Group: Default
Requires: docopt-python3 = %{version}-%{release}

%description python
python components for the docopt package.


%package python3
Summary: python3 components for the docopt package.
Group: Default
Requires: python3-core
Provides: pypi(docopt)

%description python3
python3 components for the docopt package.


%prep
%setup -q -n docopt-0.6.2
cd %{_builddir}/docopt-0.6.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1602133352
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/docopt
cp %{_builddir}/docopt-0.6.2/LICENSE-MIT %{buildroot}/usr/share/package-licenses/docopt/2bb1e4c032b9ab14d9e5b9141208aadd94e162c9
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/docopt/2bb1e4c032b9ab14d9e5b9141208aadd94e162c9

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

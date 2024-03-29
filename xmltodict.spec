#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xmltodict
Version  : 0.12.0
Release  : 24
URL      : https://files.pythonhosted.org/packages/58/40/0d783e14112e064127063fbf5d1fe1351723e5dfe9d6daad346a305f6c49/xmltodict-0.12.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/58/40/0d783e14112e064127063fbf5d1fe1351723e5dfe9d6daad346a305f6c49/xmltodict-0.12.0.tar.gz
Summary  : Makes working with XML feel like you are working with JSON
Group    : Development/Tools
License  : MIT
Requires: xmltodict-license = %{version}-%{release}
Requires: xmltodict-python = %{version}-%{release}
Requires: xmltodict-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
# xmltodict
`xmltodict` is a Python module that makes working with XML feel like you are working with [JSON](http://docs.python.org/library/json.html), as in this ["spec"](http://www.xml.com/pub/a/2006/05/31/converting-between-xml-and-json.html):

%package license
Summary: license components for the xmltodict package.
Group: Default

%description license
license components for the xmltodict package.


%package python
Summary: python components for the xmltodict package.
Group: Default
Requires: xmltodict-python3 = %{version}-%{release}

%description python
python components for the xmltodict package.


%package python3
Summary: python3 components for the xmltodict package.
Group: Default
Requires: python3-core
Provides: pypi(xmltodict)

%description python3
python3 components for the xmltodict package.


%prep
%setup -q -n xmltodict-0.12.0
cd %{_builddir}/xmltodict-0.12.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603408244
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
mkdir -p %{buildroot}/usr/share/package-licenses/xmltodict
cp %{_builddir}/xmltodict-0.12.0/LICENSE %{buildroot}/usr/share/package-licenses/xmltodict/befb3e75b2547f2d7e59a7335ef16a24f35edcfe
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xmltodict/befb3e75b2547f2d7e59a7335ef16a24f35edcfe

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

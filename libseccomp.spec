#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libseccomp
Version  : 2.3.1
Release  : 4
URL      : https://github.com/seccomp/libseccomp/archive/v2.3.1.tar.gz
Source0  : https://github.com/seccomp/libseccomp/archive/v2.3.1.tar.gz
Summary  : The enhanced seccomp library
Group    : Development/Tools
License  : LGPL-2.1
Requires: libseccomp-bin
Requires: libseccomp-lib
Requires: libseccomp-doc
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : setuptools

%description
libseccomp: An Enhanced Seccomp (mode 2) Helper Library
===============================================================================
https://github.com/seccomp/libseccomp

%package bin
Summary: bin components for the libseccomp package.
Group: Binaries

%description bin
bin components for the libseccomp package.


%package dev
Summary: dev components for the libseccomp package.
Group: Development
Requires: libseccomp-lib
Requires: libseccomp-bin
Provides: libseccomp-devel

%description dev
dev components for the libseccomp package.


%package doc
Summary: doc components for the libseccomp package.
Group: Documentation

%description doc
doc components for the libseccomp package.


%package lib
Summary: lib components for the libseccomp package.
Group: Libraries

%description lib
lib components for the libseccomp package.


%prep
%setup -q -n libseccomp-2.3.1

%build
%autogen --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/scmp_sys_resolver

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*

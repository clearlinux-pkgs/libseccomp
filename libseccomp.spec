#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x356CE62C2B524099 (tom.hromatka@oracle.com)
#
Name     : libseccomp
Version  : 2.4.3
Release  : 22
URL      : https://github.com/seccomp/libseccomp/releases/download/v2.4.3/libseccomp-2.4.3.tar.gz
Source0  : https://github.com/seccomp/libseccomp/releases/download/v2.4.3/libseccomp-2.4.3.tar.gz
Source1  : https://github.com/seccomp/libseccomp/releases/download/v2.4.3/libseccomp-2.4.3.tar.gz.asc
Summary  : The enhanced seccomp library
Group    : Development/Tools
License  : LGPL-2.1
Requires: libseccomp-bin = %{version}-%{release}
Requires: libseccomp-lib = %{version}-%{release}
Requires: libseccomp-license = %{version}-%{release}
Requires: libseccomp-man = %{version}-%{release}
BuildRequires : Cython
BuildRequires : buildreq-distutils3
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : libabigail

%description
===============================================================================
https://github.com/seccomp/libseccomp

%package bin
Summary: bin components for the libseccomp package.
Group: Binaries
Requires: libseccomp-license = %{version}-%{release}

%description bin
bin components for the libseccomp package.


%package dev
Summary: dev components for the libseccomp package.
Group: Development
Requires: libseccomp-lib = %{version}-%{release}
Requires: libseccomp-bin = %{version}-%{release}
Provides: libseccomp-devel = %{version}-%{release}
Requires: libseccomp = %{version}-%{release}
Requires: libseccomp = %{version}-%{release}

%description dev
dev components for the libseccomp package.


%package dev32
Summary: dev32 components for the libseccomp package.
Group: Default
Requires: libseccomp-lib32 = %{version}-%{release}
Requires: libseccomp-bin = %{version}-%{release}
Requires: libseccomp-dev = %{version}-%{release}

%description dev32
dev32 components for the libseccomp package.


%package lib
Summary: lib components for the libseccomp package.
Group: Libraries
Requires: libseccomp-license = %{version}-%{release}

%description lib
lib components for the libseccomp package.


%package lib32
Summary: lib32 components for the libseccomp package.
Group: Default
Requires: libseccomp-license = %{version}-%{release}

%description lib32
lib32 components for the libseccomp package.


%package license
Summary: license components for the libseccomp package.
Group: Default

%description license
license components for the libseccomp package.


%package man
Summary: man components for the libseccomp package.
Group: Default

%description man
man components for the libseccomp package.


%prep
%setup -q -n libseccomp-2.4.3
cd %{_builddir}/libseccomp-2.4.3
pushd ..
cp -a libseccomp-2.4.3 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583768304
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check
cd ../build32;
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1583768304
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libseccomp
cp %{_builddir}/libseccomp-2.4.3/LICENSE %{buildroot}/usr/share/package-licenses/libseccomp/4c04c844a5cb16b3629d0052f1304b7a565bd4a8
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/scmp_sys_resolver

%files dev
%defattr(-,root,root,-)
/usr/include/seccomp-syscalls.h
/usr/include/seccomp.h
/usr/lib64/libseccomp.so
/usr/lib64/pkgconfig/libseccomp.pc
/usr/share/man/man3/seccomp_api_get.3
/usr/share/man/man3/seccomp_api_set.3
/usr/share/man/man3/seccomp_arch_add.3
/usr/share/man/man3/seccomp_arch_exist.3
/usr/share/man/man3/seccomp_arch_native.3
/usr/share/man/man3/seccomp_arch_remove.3
/usr/share/man/man3/seccomp_arch_resolve_name.3
/usr/share/man/man3/seccomp_attr_get.3
/usr/share/man/man3/seccomp_attr_set.3
/usr/share/man/man3/seccomp_export_bpf.3
/usr/share/man/man3/seccomp_export_pfc.3
/usr/share/man/man3/seccomp_init.3
/usr/share/man/man3/seccomp_load.3
/usr/share/man/man3/seccomp_merge.3
/usr/share/man/man3/seccomp_release.3
/usr/share/man/man3/seccomp_reset.3
/usr/share/man/man3/seccomp_rule_add.3
/usr/share/man/man3/seccomp_rule_add_array.3
/usr/share/man/man3/seccomp_rule_add_exact.3
/usr/share/man/man3/seccomp_rule_add_exact_array.3
/usr/share/man/man3/seccomp_syscall_priority.3
/usr/share/man/man3/seccomp_syscall_resolve_name.3
/usr/share/man/man3/seccomp_syscall_resolve_name_arch.3
/usr/share/man/man3/seccomp_syscall_resolve_name_rewrite.3
/usr/share/man/man3/seccomp_syscall_resolve_num_arch.3
/usr/share/man/man3/seccomp_version.3

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libseccomp.so
/usr/lib32/pkgconfig/32libseccomp.pc
/usr/lib32/pkgconfig/libseccomp.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libseccomp.so.2
/usr/lib64/libseccomp.so.2.4.3

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libseccomp.so.2
/usr/lib32/libseccomp.so.2.4.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libseccomp/4c04c844a5cb16b3629d0052f1304b7a565bd4a8

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/scmp_sys_resolver.1

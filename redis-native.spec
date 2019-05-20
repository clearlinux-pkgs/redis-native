#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : redis-native
Version  : 5.0.5
Release  : 35
URL      : http://download.redis.io/releases/redis-5.0.5.tar.gz
Source0  : http://download.redis.io/releases/redis-5.0.5.tar.gz
Source1  : redis-native.tmpfiles
Source2  : redis.service
Summary  : An Extensible Extension Language
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause MIT
Requires: redis-native-bin = %{version}-%{release}
Requires: redis-native-config = %{version}-%{release}
Requires: redis-native-data = %{version}-%{release}
Requires: redis-native-license = %{version}-%{release}
Requires: redis-native-services = %{version}-%{release}
BuildRequires : jemalloc-dev
BuildRequires : lua-dev
BuildRequires : procps-ng
BuildRequires : tcl
Patch1: 0001-Use-O3-optimization.patch
Patch2: 0002-Install-to-usr-honor-DESTDIR-for-install.patch
Patch3: 0003-Modify-default-config-to-include-a-possible-local-ov.patch

%description
The test-lru.rb program can be used in order to check the behavior of the
Redis approximated LRU algorithm against the theoretical output of true
LRU algorithm.

%package bin
Summary: bin components for the redis-native package.
Group: Binaries
Requires: redis-native-data = %{version}-%{release}
Requires: redis-native-config = %{version}-%{release}
Requires: redis-native-license = %{version}-%{release}
Requires: redis-native-services = %{version}-%{release}

%description bin
bin components for the redis-native package.


%package config
Summary: config components for the redis-native package.
Group: Default

%description config
config components for the redis-native package.


%package data
Summary: data components for the redis-native package.
Group: Data

%description data
data components for the redis-native package.


%package doc
Summary: doc components for the redis-native package.
Group: Documentation

%description doc
doc components for the redis-native package.


%package license
Summary: license components for the redis-native package.
Group: Default

%description license
license components for the redis-native package.


%package services
Summary: services components for the redis-native package.
Group: Systemd services

%description services
services components for the redis-native package.


%prep
%setup -q -n redis-5.0.5
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1558333622
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
make  %{?_smp_mflags} MALLOC=libc


%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make -C src %{_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1558333622
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/redis-native
cp COPYING %{buildroot}/usr/share/package-licenses/redis-native/COPYING
cp deps/hiredis/COPYING %{buildroot}/usr/share/package-licenses/redis-native/deps_hiredis_COPYING
cp deps/jemalloc/COPYING %{buildroot}/usr/share/package-licenses/redis-native/deps_jemalloc_COPYING
cp deps/lua/COPYRIGHT %{buildroot}/usr/share/package-licenses/redis-native/deps_lua_COPYRIGHT
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/systemd/system/redis.service
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/tmpfiles.d/redis-native.conf
## install_append content
mkdir -p %{buildroot}/usr/share/doc/redis
install sentinel.conf %{buildroot}/usr/share/doc/redis/
mkdir -p %{buildroot}/usr/share/defaults/etc
install redis.conf %{buildroot}/usr/share/defaults/etc/
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/redis-benchmark
/usr/bin/redis-check-aof
/usr/bin/redis-check-rdb
/usr/bin/redis-cli
/usr/bin/redis-sentinel
/usr/bin/redis-server

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/redis-native.conf

%files data
%defattr(-,root,root,-)
/usr/share/defaults/etc/redis.conf

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/redis/sentinel.conf

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/redis-native/COPYING
/usr/share/package-licenses/redis-native/deps_hiredis_COPYING
/usr/share/package-licenses/redis-native/deps_jemalloc_COPYING
/usr/share/package-licenses/redis-native/deps_lua_COPYRIGHT

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/redis.service

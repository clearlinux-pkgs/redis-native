#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : redis-native
Version  : 5.0.6
Release  : 37
URL      : http://download.redis.io/releases/redis-5.0.6.tar.gz
Source0  : http://download.redis.io/releases/redis-5.0.6.tar.gz
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
Patch4: CVE-2014-5461.patch

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
%setup -q -n redis-5.0.6
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571441040
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
make  %{?_smp_mflags}  MALLOC=libc


%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make -C src %{_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1571441040
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/redis-native
cp %{_builddir}/redis-5.0.6/COPYING %{buildroot}/usr/share/package-licenses/redis-native/a19e8c78250e9af2bffc5c60e21478c392662dae
cp %{_builddir}/redis-5.0.6/deps/hiredis/COPYING %{buildroot}/usr/share/package-licenses/redis-native/e9c1298de98016808910005a33de3a5f25dce05e
cp %{_builddir}/redis-5.0.6/deps/jemalloc/COPYING %{buildroot}/usr/share/package-licenses/redis-native/32366cf8c310f3ab4c264217764166f95f030e00
cp %{_builddir}/redis-5.0.6/deps/lua/COPYRIGHT %{buildroot}/usr/share/package-licenses/redis-native/a6efc4d11f332f4843bc25b557c6bf3e5ef51458
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
/usr/share/package-licenses/redis-native/32366cf8c310f3ab4c264217764166f95f030e00
/usr/share/package-licenses/redis-native/a19e8c78250e9af2bffc5c60e21478c392662dae
/usr/share/package-licenses/redis-native/a6efc4d11f332f4843bc25b557c6bf3e5ef51458
/usr/share/package-licenses/redis-native/e9c1298de98016808910005a33de3a5f25dce05e

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/redis.service

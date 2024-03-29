#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
#
Name     : redis-native
Version  : 7.0.12
Release  : 71
URL      : https://download.redis.io/releases/redis-7.0.12.tar.gz
Source0  : https://download.redis.io/releases/redis-7.0.12.tar.gz
Source1  : redis-native.tmpfiles
Source2  : redis.service
Summary  : An Extensible Extension Language
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause CC0-1.0 MIT
Requires: redis-native-bin = %{version}-%{release}
Requires: redis-native-config = %{version}-%{release}
Requires: redis-native-data = %{version}-%{release}
Requires: redis-native-license = %{version}-%{release}
Requires: redis-native-services = %{version}-%{release}
BuildRequires : jemalloc-dev
BuildRequires : procps-ng
BuildRequires : systemd-dev
BuildRequires : tcl
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Use-O3-optimization.patch
Patch2: 0002-Install-to-usr-honor-DESTDIR-for-install.patch
Patch3: 0003-Modify-default-config-to-include-a-possible-local-ov.patch
Patch4: 0004-Accept-args-for-test-runner.patch

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
Requires: systemd

%description services
services components for the redis-native package.


%prep
%setup -q -n redis-7.0.12
cd %{_builddir}/redis-7.0.12
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
pushd ..
cp -a redis-7.0.12 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1689007893
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
make  %{?_smp_mflags}  MALLOC=libc \
USE_SYSTEMD=yes

pushd ../buildavx2
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
make  %{?_smp_mflags}  MALLOC=libc \
USE_SYSTEMD=yes
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make -C src %{_smp_mflags} check TEST_RUNNER_ARGS="--verbose --dont-clean --dump-logs" || :

%install
export SOURCE_DATE_EPOCH=1689007893
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/redis-native
cp %{_builddir}/redis-%{version}/COPYING %{buildroot}/usr/share/package-licenses/redis-native/44e5add5829f86c049fd08dffce57f00da52fd1f || :
cp %{_builddir}/redis-%{version}/deps/hdr_histogram/COPYING.txt %{buildroot}/usr/share/package-licenses/redis-native/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/redis-%{version}/deps/hdr_histogram/LICENSE.txt %{buildroot}/usr/share/package-licenses/redis-native/1f3f949bd5fdef93522f7eaad5a31dd1cca02ca1 || :
cp %{_builddir}/redis-%{version}/deps/hiredis/COPYING %{buildroot}/usr/share/package-licenses/redis-native/e9c1298de98016808910005a33de3a5f25dce05e || :
cp %{_builddir}/redis-%{version}/deps/jemalloc/COPYING %{buildroot}/usr/share/package-licenses/redis-native/c797cef3f1b13a960a5119a084fb88529a924fd7 || :
cp %{_builddir}/redis-%{version}/deps/lua/COPYRIGHT %{buildroot}/usr/share/package-licenses/redis-native/a6efc4d11f332f4843bc25b557c6bf3e5ef51458 || :
pushd ../buildavx2/
%make_install_v3
popd
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
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/redis-benchmark
/V3/usr/bin/redis-cli
/V3/usr/bin/redis-server
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
/usr/share/package-licenses/redis-native/1f3f949bd5fdef93522f7eaad5a31dd1cca02ca1
/usr/share/package-licenses/redis-native/44e5add5829f86c049fd08dffce57f00da52fd1f
/usr/share/package-licenses/redis-native/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/redis-native/a6efc4d11f332f4843bc25b557c6bf3e5ef51458
/usr/share/package-licenses/redis-native/c797cef3f1b13a960a5119a084fb88529a924fd7
/usr/share/package-licenses/redis-native/e9c1298de98016808910005a33de3a5f25dce05e

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/redis.service

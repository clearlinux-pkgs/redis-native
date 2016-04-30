#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : redis-native
Version  : 3.0.7
Release  : 3
URL      : http://download.redis.io/releases/redis-3.0.7.tar.gz
Source0  : http://download.redis.io/releases/redis-3.0.7.tar.gz
Summary  : An Extensible Extension Language
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause MIT
Requires: redis-native-bin
BuildRequires : jemalloc-dev
BuildRequires : lua-dev
Patch1: build.patch

%description
Where to find complete Redis documentation?
-------------------------------------------

%package bin
Summary: bin components for the redis-native package.
Group: Binaries

%description bin
bin components for the redis-native package.


%prep
cd ..
%setup -q -n redis-3.0.7
%patch1 -p1

%build
make V=1  %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/redis-benchmark
/usr/bin/redis-check-aof
/usr/bin/redis-check-dump
/usr/bin/redis-cli
/usr/bin/redis-sentinel
/usr/bin/redis-server

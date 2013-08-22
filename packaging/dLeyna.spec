Name:       dleyna
Summary:    dLeyna hosts a number of DLNA middleware components
Version:    0.2.1
Release:    0
Group:      System/Libraries
License:    LGPLv2+
URL:        https://01.org/dleyna/
Source0:    %{name}-%{version}.tar.gz
Requires:   dbus
Requires:   libsoup
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gupnp-1.0)
BuildRequires:  pkgconfig(gssdp-1.0)
BuildRequires:  pkgconfig(gupnp-av-1.0)
BuildRequires:  pkgconfig(gupnp-dlna-2.0)
BuildRequires:  pkgconfig(libsoup-2.4)


%description
dLeyna is a suite of middleware components designed to simplify
the task of writing DLNA enabled applications.
These components can be used to implement Digital Media Players,
Digital Media Controllers, and to easily integrate
two-box push into applications.


%package devel
Summary:    Development package for dleyna
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Development files for dleyna.


%prep
%setup -q -n %{name}-%{version}

%build
%configure --enable-master-build --disable-static --enable-debug --disable-never-quit --with-log-level=8 --with-log-type=1
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING 
%{_libexecdir}/dleyna-server-service
%{_libexecdir}/dleyna-renderer-service
%{_libdir}/libdleyna-core-1.0.so.*
%{_libdir}/dleyna-server/libdleyna-server-1.0.so.*
%{_libdir}/dleyna-renderer/libdleyna-renderer-1.0.so.*
%{_libdir}/dleyna-1.0/connectors/libdleyna-connector-dbus.so
%{_sysconfdir}/dleyna-server-service.conf
%{_sysconfdir}/dleyna-renderer-service.conf
%{_prefix}/share/dbus-1/services/*

%files devel
%defattr(-,root,root,-)
%{_includedir}/dleyna-1.0/libdleyna
%{_libdir}/libdleyna-core-1.0.so
%{_libdir}/dleyna-server/libdleyna-server-1.0.so
%{_libdir}/dleyna-renderer/libdleyna-renderer-1.0.so
%{_libdir}/pkgconfig/dleyna-connector-dbus-1.0.pc
%{_libdir}/pkgconfig/dleyna-core-1.0.pc
%{_libdir}/pkgconfig/dleyna-server-1.0.pc
%{_libdir}/pkgconfig/dleyna-renderer-1.0.pc
%{_libdir}/pkgconfig/dleyna-server-service-1.0.pc
%{_libdir}/pkgconfig/dleyna-renderer-service-1.0.pc

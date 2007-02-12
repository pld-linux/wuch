Summary:	RPM handler
Summary(pl.UTF-8):	Narzędzie do obsługi RPMów
Name:		wuch
Version:	0.21.2
Release:	1
License:	GPL
Group:		Applications/System
Source0:	ftp://ftp.pld-linux.org/software/wuch/%{name}-%{version}.tar.gz
# Source0-md5:	4c5663699b18993ac2d3b9a7892563eb
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	conflib-static
BuildRequires:	curl-devel
BuildRequires:	db1-devel
BuildRequires:	db3-devel
BuildRequires:	libtool
BuildRequires:	newt-devel
BuildRequires:	popt-devel
BuildRequires:	postgresql-backend-devel
BuildRequires:	postgresql-devel
BuildRequires:	rpm-devel
BuildRequires:	slang-devel
BuildRequires:	trurlib-devel
%if %{?BOOT:1}%{!?BOOT:0}
BuildRequires:	trurlib-static
%endif
Requires:	dml
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wuch is a tool to allow easy installation/upgrade of RPM packages.

%description -l pl.UTF-8
wuch jest narzędziem które pozwala na łatwą instalację/upgrade
pakietów RPM.

%package -n mop_server
Summary:	mop_server
Summary(pl.UTF-8):	Serwer mop
Group:		Applications/System

%description -n mop_server
MOP stands from Massive Opinion Project. It (will) allow users to
grade any package from distribution in set of categories (difrent for
any package), and browse statistic to decide if upgrade some package
or not. It's still not finished.

%description -n mop_server -l pl.UTF-8
MOP to Masowy Projekt Opiniowania pakietów. Umożliwi on użytkownikom
ocenianie pakietów pochodzących z dystrybucji w różnych kategoriach --
zaleznych od pakietu, oraz przegladanie tak powstalych statystyk w
celu zdecydowania czy dany pakiet pracuje wystarczajaco dobrze by go
zainstalowac. Ten program wciąż nie jest skończony.

%package BOOT
Summary:	%{name} for bootdisk
Summary(pl.UTF-8):	%{name} na bootkietkę
Group:		Applications/System

%description BOOT
%{name} for bootdisk.

%description BOOT -l pl.UTF-8
%{name} na bootkietkę.

%prep
%setup -q

%build
rm -f missing
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}

%if %{?BOOT:1}%{!?BOOT:0}
%configure --without-mop-server --disable-shared --disable-modular
%{__make}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install $RPM_BUILD_ROOT%{_bindir}/wuch wuch-BOOT
%{__make} distclean
%endif

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%if %{?BOOT:1}%{!?BOOT:0}
install -d $RPM_BUILD_ROOT%{_libdir}/bootdisk/sbin
install -d $RPM_BUILD_ROOT%{_libdir}/bootdisk%{_libdir}/wuch/modules
install wuch-BOOT $RPM_BUILD_ROOT%{_libdir}/bootdisk/sbin/wuch
%endif

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__perl} -pi -e "s/i586/%{_target_cpu}/g" $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.conf

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/wuch.conf
%attr(755,root,root) %{_bindir}/wuch
%attr(755,root,root) %{_libdir}/wuch/modules/*.so
%attr(755,root,root) %{_libdir}/libwuch.so.0.0.0
%dir %{_libdir}/wuch
%dir %{_libdir}/wuch/modules

%files -n mop_server
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mop_server

%if %{?BOOT:1}%{!?BOOT:0}
%files BOOT
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/bootdisk/sbin/*
%endif

Summary:	RPM handler
Summary(pl):	narzêdzie do obs³ugi RPMów
Name:		wuch
Version:	0.18.2
Release:	1
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	ftp://ftp.pld.org.pl/software/wuch/%{name}-%{version}.tar.gz
BuildRequires:	bzip2-devel
BuildRequires:	conflib-devel
BuildRequires:	db3-devel
BuildRequires:	db1-devel
BuildRequires:	newt-devel
BuildRequires:	popt-devel
BuildRequires:	postgresql-devel
BuildRequires:	rpm-devel
BuildRequires:	slang-devel
BuildRequires:	trurlib-devel
BuildRequires:  curl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc

%description
wuch is a tool to allow easy installation/upgrade of RPM packages.

%description -l pl
wuch jest narzêdziem które pozwala na ³atw± instalacjê/upgrade
pakietów RPM.

%package -n mop_server
Summary:	mop_server
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System

%description -n mop_server
MOP stands from Massive Opinion Project. It (will) allow users to grade
any package from distribution in set of categories (difrent for any package),
and browse statistic to decide if upgrade some package or not.
It's still not finished.

%description -n mop_server -l pl
MOP to Masowy Projekt Opiniowania pakietów. Umo¿liwi on u¿ytkownikom ocenianie 
pakietów pochodz±cych z dystrybucji w ró¿nych kategoriach -- zaleznych od 
pakietu, oraz przegladanie tak powstalych statystyk w celu zdecydowania czy dany
pakiet pracuje wystarczajaco dobrze by go zainstalowac.
Ten program wci±¿ nie jest skoñczony.

%if %{?BOOT:1}%{!?BOOT:0}
%package BOOT
Summary:	%{name} for bootdisk
Group:		Applications/System
%description BOOT
%endif

%prep
%setup -q

%build
aclocal
autoheader
automake --gnu
autoconf

%if %{?BOOT:1}%{!?BOOT:0}
%configure --without-mop-server --disable-shared --disable-modular
%{__make}
%{__make} install DESTDIR=$RPM_BUILD_ROOT
install $RPM_BUILD_ROOT%{_bindir}/wuch wuch-BOOT
%{__make} distclean
%endif

%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%if %{?BOOT:1}%{!?BOOT:0}
install -d $RPM_BUILD_ROOT/usr/lib/bootdisk/sbin
install -d $RPM_BUILD_ROOT/usr/lib/bootdisk/usr/lib/wuch/modules
install -s wuch-BOOT $RPM_BUILD_ROOT/usr/lib/bootdisk/sbin/wuch
%endif

%{__make} DESTDIR=$RPM_BUILD_ROOT install

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%config(noreplace) %{_sysconfdir}/wuch.conf
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
%attr(755,root,root) /usr/lib/bootdisk/sbin/*
%endif

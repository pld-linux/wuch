Summary:	RPM handler
Summary(pl):	narzÍdzie do obs≥ugi RPMÛw
Name:		wuch
Version:	0.21.0
Release:	1
License:	GPL
Group:		Applications/System
Group(cs):	Aplikace/SystÈm
Group(da):	Programmer/System
Group(de):	Applikationen/System
Group(es):	Aplicaciones/Sistema
Group(fr):	Applications/SystËme
Group(is):	Forrit/Kerfisforrit
Group(it):	Applicazioni/Sistema
Group(ja):	•¢•◊•Í•±°º•∑•Á•Û/•∑•π•∆•‡
Group(no):	Applikasjoner/System
Group(pl):	Aplikacje/System
Group(pt):	AplicaÁıes/Sistema
Group(pt_BR):	AplicaÁıes/Sistema
Group(ru):	“…Ãœ÷≈Œ…—/Û…”‘≈Õ¡
Group(sl):	Programi/Sistem
Group(sv):	Till‰mpningar/System
Group(uk):	“…ÀÃ¡ƒŒ¶ “œ«“¡Õ…/Û…”‘≈Õ¡
Source0:	ftp://ftp.pld.org.pl/software/wuch/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	curl-devel
BuildRequires:	db3-devel
BuildRequires:	db1-devel
BuildRequires:	newt-devel
BuildRequires:	libtool
BuildRequires:	popt-devel
BuildRequires:	postgresql-devel
BuildRequires:	postgresql-backend-devel
BuildRequires:	rpm-devel
BuildRequires:	slang-devel
BuildRequires:	trurlib-devel
BuildRequires:	conflib-static
%if %{?BOOT:1}%{!?BOOT:0}
BuildRequires:	trurlib-static
%endif
Requires:	dml
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc

%description
wuch is a tool to allow easy installation/upgrade of RPM packages.

%description -l pl
wuch jest narzÍdziem ktÛre pozwala na ≥atw± instalacjÍ/upgrade
pakietÛw RPM.

%package -n mop_server
Summary:	mop_server
Group:		Applications/System
Group(cs):	Aplikace/SystÈm
Group(da):	Programmer/System
Group(de):	Applikationen/System
Group(es):	Aplicaciones/Sistema
Group(fr):	Applications/SystËme
Group(is):	Forrit/Kerfisforrit
Group(it):	Applicazioni/Sistema
Group(ja):	•¢•◊•Í•±°º•∑•Á•Û/•∑•π•∆•‡
Group(no):	Applikasjoner/System
Group(pl):	Aplikacje/System
Group(pt):	AplicaÁıes/Sistema
Group(pt_BR):	AplicaÁıes/Sistema
Group(ru):	“…Ãœ÷≈Œ…—/Û…”‘≈Õ¡
Group(sl):	Programi/Sistem
Group(sv):	Till‰mpningar/System
Group(uk):	“…ÀÃ¡ƒŒ¶ “œ«“¡Õ…/Û…”‘≈Õ¡

%description -n mop_server
MOP stands from Massive Opinion Project. It (will) allow users to
grade any package from distribution in set of categories (difrent for
any package), and browse statistic to decide if upgrade some package
or not. It's still not finished.

%description -n mop_server -l pl
MOP to Masowy Projekt Opiniowania pakietÛw. Umoøliwi on uøytkownikom
ocenianie pakietÛw pochodz±cych z dystrybucji w rÛønych kategoriach --
zaleznych od pakietu, oraz przegladanie tak powstalych statystyk w
celu zdecydowania czy dany pakiet pracuje wystarczajaco dobrze by go
zainstalowac. Ten program wci±ø nie jest skoÒczony.

%package BOOT
Summary:	%{name} for bootdisk
Group:		Applications/System
Group(cs):	Aplikace/SystÈm
Group(da):	Programmer/System
Group(de):	Applikationen/System
Group(es):	Aplicaciones/Sistema
Group(fr):	Applications/SystËme
Group(is):	Forrit/Kerfisforrit
Group(it):	Applicazioni/Sistema
Group(ja):	•¢•◊•Í•±°º•∑•Á•Û/•∑•π•∆•‡
Group(no):	Applikasjoner/System
Group(pl):	Aplikacje/System
Group(pt):	AplicaÁıes/Sistema
Group(pt_BR):	AplicaÁıes/Sistema
Group(ru):	“…Ãœ÷≈Œ…—/Û…”‘≈Õ¡
Group(sl):	Programi/Sistem
Group(sv):	Till‰mpningar/System
Group(uk):	“…ÀÃ¡ƒŒ¶ “œ«“¡Õ…/Û…”‘≈Õ¡

%description BOOT
%{name} for bootdisk.

%prep
%setup -q

%build
rm -f missing
aclocal
autoheader
automake -a -c
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
install -d $RPM_BUILD_ROOT%{_libdir}/bootdisk/sbin
install -d $RPM_BUILD_ROOT%{_libdir}/bootdisk%{_libdir}/wuch/modules
install wuch-BOOT $RPM_BUILD_ROOT%{_libdir}/bootdisk/sbin/wuch
%endif

%{__make} DESTDIR=$RPM_BUILD_ROOT install
perl -pi -e "s/i586/%{_target_cpu}/g" $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.conf

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/wuch.conf
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

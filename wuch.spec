Summary:	RPM handler
Summary(pl):	narzêdzie do obs³ugi RPMów
Name:		wuch
Version:	0.17.0
Release:	1
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	ftp://ftp.pld.org.pl/software/wuch/%{name}-%{version}.tar.gz
BuildRequires:	bzip2-devel
BuildRequires:	db3-devel
BuildRequires:	db1-devel
BuildRequires:	newt-devel
BuildRequires:	popt-devel
BuildRequires:	postgresql-devel
BuildRequires:	rpm-devel
BuildRequires:	slang-devel
BuildRequires:	trurlib-devel
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

%prep
%setup -q

%build
%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%config(noreplace) %{_sysconfdir}/wuch.conf
%attr(755,root,root) %{_bindir}/wuch

%files -n mop_server
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mop_server

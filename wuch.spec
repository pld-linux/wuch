Summary:	RPM handler
Summary(pl):	narzêdzie do obs³ugi RPMów
Name:		wuch
Version:	20010131
Release:	1
License:	GPL
Group:		Utilities/System
Group(de):	Libraries
Group(pl):	Biblioteki
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	newt-devel
BuildRequires:	rpm-devel
BuildRequires:	trurlib-devel
BuildRequires:	slang-devel
BuildRequires:	popt-devel
BuildRequires:	db3-devel
BuildRequires:	db1-devel
BuildRequires:	bzip2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wuch is a tool to allow easy installation/upgrade of RPM packages.

%description -l pl
wuch jest narzêdziem które pozwala na ³atw± instalacjê/upgrade
pakietów RPM.

%prep
%setup -q

%build
./autogen.sh
%configure 

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install
gzip -9nf doc/README.pl 

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc doc/*.gz src/source.conf
%attr(755,root,root) %{_bindir}/*

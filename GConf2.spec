Summary:	GNOME2 configuration database system
Summary(pl):	System konfiguracyjnej bazy danych dla GNOME2
Summary(pt_BR):	Sistema de Configura��o do GNOME2
Name:		GConf2
Version:	1.2.1
Release:	3
License:	LGPL
Group:		X11/Applications
Source0:	ftp://ftp.gnome.org/pub/GNOME/pre-gnome2/sources/GConf/GConf-%{version}.tar.bz2
Patch0:		%{name}-NO_MAJOR_VERSION.patch
Patch1:		%{name}-am.patch
Patch2:		%{name}-path.patch
URL:		http://www.gnome.org/
BuildRequires:	ORBit2-devel
BuildRequires:	bonobo-activation-devel >= 1.0.3
#BuildRequires:	db3-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2.0.6
BuildRequires:	glib2-devel >= 2.0.6
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libGConf2

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11/GNOME2
%define		_gtkdocdir	%{_defaultdocdir}/gtk-doc/html

%description
GConf2 is a configuration database system, functionally similar to the
Windows registry but lots better. :-) It's being written for the
GNOME2 desktop but does not require GNOME2; configure should notice if
GNOME2 is not installed and compile the basic GConf2 library anyway.

%description -l pl
GConf2 jest systemem konfiguracyjnej bazy danych, funkcjonalnie
podobnej do rejestru Windows, ale o wiele lepszej :-). Jest pisana dla
desktopu GNOME2, ale nie wymaga GNOME2; skrypt configure powinien
wykry� brak gnome i skompilowa� tylko wersj� podstawow� GConf2.

%description -l pt_BR
Gconf2 � o sistema de banco de dados de configura��o do GNOME2.

%package devel
Summary:	GConf2 includes, etc
Summary(pl):	Pliki nag��wkowe GConf2
Summary(pt_BR):	Sistema de Configura��o do GNOME2 - arquivos para desenvolvimento
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Requires:	ORBit2-devel
Requires:	bonobo-activation-devel
Requires:	gtk-doc-common
Requires:	libxml2-devel
Obsoletes:	libGConf2-devel

%description devel
GConf2 includes etc.

%description devel -l pl
Pliki nag��wkowe GConf2.

%description devel -l pt_BR
Sistema de Configura��o do GNOME2 - arquivos para desenvolvimento.

%package static
Summary:	GConf2 static libraries
Summary(pl):	Biblioteki statyczne GConf2
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com gconf2
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
GConf2 static libraries.

%description static -l pl
Biblioteki statyczne GConf2.

%description static -l pt_BR
Bibliotecas est�ticas para desenvolvimento com gconf

%prep
%setup -q -n GConf-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f missing acinclude.m4
%{__libtoolize}
aclocal
%{__autoconf}
%{__automake}
%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_aclocaldir},%{_sysconfdir}/gconf/schemas}
install gconf.m4 $RPM_BUILD_ROOT%{_aclocaldir}/gconf-2.m4

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir} \
	HTML_DIR=%{_gtkdocdir} 
	
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gconf*
%attr(755,root,root) %{_libdir}/gconf-sanity-check-2
%attr(755,root,root) %{_libdir}/gconfd-2
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/GConf2
%attr(755,root,root) %{_libdir}/GConf2/lib*.so
%{_sysconfdir}/gconf

%files devel
%defattr(644,root,root,755)
# outdated and almost empty
#doc NEWS
%doc AUTHORS ChangeLog TODO README
%attr(755,root,root) %{_libdir}/lib*.??
%attr(755,root,root) %{_libdir}/GConf2/lib*.la
%doc %{_gtkdocdir}/gconf
%{_includedir}/gconf2
%{_aclocaldir}/*.m4
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/GConf2/lib*.a
%{_libdir}/lib*.a

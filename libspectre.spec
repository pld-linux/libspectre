Summary:	A library for rendering PostScript documents
Summary(pl.UTF-8):	Biblioteka do renderowania dokumentów postscriptowych
Name:		libspectre
Version:	0.2.6
Release:	2
License:	GPL v2+
Group:		Libraries
Source0:	http://libspectre.freedesktop.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	5c6db35f2097c3a04c48c7f435d4b507
URL:		http://libspectre.freedesktop.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.7
BuildRequires:	ghostscript-devel >= 8.62
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	ghostscript >= 8.62
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Small library for rendering PostScript documents. It provides a
convenient easy to use API for handling and rendering PostScript
documents.

%description -l pl.UTF-8
Mała biblioteka do renderowania dokumentów postscriptowych. Udostępnia
łatwe w użyciu API do obsługi i renderowania PostScriptu.

%package devel
Summary:	Header files for libspectre library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libspectre
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	ghostscript-devel >= 8.61-2

%description devel
Header files for libspectre library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libspectre.

%package static
Summary:	Static libspectre library
Summary(pl.UTF-8):	Statyczna biblioteka libspectre
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libspectre library.

%description static -l pl.UTF-8
Statyczna biblioteka libspectre.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--disable-test
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_libdir}/libspectre.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libspectre.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libspectre.so
%{_libdir}/libspectre.la
%{_includedir}/libspectre
%{_pkgconfigdir}/libspectre.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libspectre.a

Summary:	A library for rendering PostScript documents
Name:		libspectre
Version:	0.2.1
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://libspectre.freedesktop.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	e3e380e20d64bb2eef0fd203bc595c2c
URL:		http://libspectre.freedesktop.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.7
BuildRequires:	ghostscript-devel >= 8.61-2
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Small library for rendering PostScript documents. It provides a
convenient easy to use API for handling and rendering PostScript
documents.

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
%doc AUTHORS ChangeLog NEWS README TODO
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

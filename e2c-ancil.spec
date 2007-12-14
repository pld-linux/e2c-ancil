Summary:	Ancillary utilities for e2compr (ext2 compression)
Summary(pl.UTF-8):	Narzędzia uzupełniające dla e2compr (kompresji ext2)
Name:		e2c-ancil
Version:	0.4.1
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://dl.sourceforge.net/e2compr/%{name}-%{version}.tar.bz2
# Source0-md5:	a2253167c5663fc8b3b23b79afb6bdf0
URL:		http://e2compr.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ancillary utilities for e2compr (ext2 compression) consist of the
following small programs:
- e2ratio: Like `du', but also shows how many blocks would be used if
  each file weren't compressed.
- e2bitmap: Shows which clusters of a file are compressed.
- clear-e2c: Facilitates uninstalling e2compr from a filesystem.

%description -l pl.UTF-8
Narzędzia uzupełniające dla e2compr (kompresji ext2) składają się z
następujących małych programów:
- e2ratio - podobnego do du, ale pokazującego dodatkowo ile bloków
  zostałoby użytych, jeśli pliki byłyby nieskompresowane,
- e2bitmap - pokazującego, które klastry pliku są skompresowane,
- clear-e2c - pomagającego przy usuwaniu e2compr z systemu plików.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/e2bitmap
%attr(755,root,root) %{_bindir}/e2ratio
%attr(755,root,root) %{_sbindir}/clear-e2c
%{_mandir}/man1/e2bitmap.1*
%{_mandir}/man1/e2ratio.1*
%{_mandir}/man8/clear-e2c.8*

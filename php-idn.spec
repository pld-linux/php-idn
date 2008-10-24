%define		_modname	idn
Summary:	idn - binding to the GNU libidn
Summary(pl.UTF-8):	idn - wiązanie do GNU libidn
Name:		php-idn
Version:	1.2b
Release:	1
License:	GPL v2+
Group:		Development/Languages/PHP
Source0:	ftp://ftp.debian.org/debian/pool/main/p/php-idn/php-%{_modname}_%{version}-5.2.tar.gz
# Source0-md5:	0947a312338fe22421c1ab39345bac35
URL:		http://php-idn.bayour.com/
BuildRequires:	libidn-devel
BuildRequires:	php-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.344
%{?requires_php_extension}
Requires:	php-common >= 4:5.0.4
Conflicts:	php-pecl-idn
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Binding to the GNU libidn for using Internationalized Domain Names.

%description -l pl.UTF-8
Wiązanie do GNU libidn do używania umiędzynarodowionych nazw domen
(Internationalized Domain Names).

%prep
%setup -q

%build
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}

install modules/%{_modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{_modname}.ini
; Enable %{_modname} extension module
extension=%{_modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%php_webserver_restart

%postun
if [ "$1" = 0 ]; then
	%php_webserver_restart
fi

%files
%defattr(644,root,root,755)
%doc CHANGES CREDITS THANX_TO
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{_modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{_modname}.so

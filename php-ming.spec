%define modname ming
%define dirname %{modname}
%define soname %{modname}.so
%define inifile 33_%{modname}.ini

Summary:	Ming extension module for PHP
Name:		php-ming
Version:	5.2.3
Release:	%mkrel 1
Group:		Development/PHP
URL:		http://www.php.net
License:	PHP License
BuildRequires:	php-devel >= 3:5.2.0
BuildRequires:	libming-devel
Provides:	php5-ming
Obsoletes:	php5-ming

%description
This is a dynamic shared object (DSO) for PHP that will add ming (Flash - .swf
files) support.

%prep

%setup -c -T
cp -dpR %{_usrsrc}/php-devel/extensions/%{dirname}/* .

%build

phpize
%configure2_5x --with-libdir=%{_lib} \
    --with-%{modname}=shared,%{_prefix}

%make
mv modules/*.so .

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot} 


install -d %{buildroot}%{_libdir}/php/extensions
install -d %{buildroot}%{_sysconfdir}/php.d

install -m755 %{soname} %{buildroot}%{_libdir}/php/extensions/

cat > %{buildroot}%{_sysconfdir}/php.d/%{inifile} << EOF
extension = %{soname}
EOF

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc CREDITS EXPERIMENTAL
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/php.d/%{inifile}
%attr(0755,root,root) %{_libdir}/php/extensions/%{soname}



%define modname ming
%define dirname %{modname}
%define soname %{modname}.so
%define inifile 33_%{modname}.ini

Summary:	Ming extension module for PHP
Name:		php-ming
Version:	5.2.10
Release:	%mkrel 14
Group:		Development/PHP
URL:		http://www.php.net
License:	PHP License
# S0 is taken from php-5.2.x CVS
Source0:	ming.tar.gz
Patch0:		php-ming-0.4.3.diff
BuildRequires:	php-devel >= 3:5.2.0
BuildRequires:	ming-devel >= 0.4.3
Epoch:		1
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This is a dynamic shared object (DSO) for PHP that will add ming (Flash - .swf
files) support.

%prep

%setup -q -n ming
%patch0 -p1

%build

phpize
%configure2_5x --with-libdir=%{_lib} \
    --with-%{modname}=shared,%{_prefix}

%make
mv modules/*.so .

%install
rm -rf %{buildroot} 


install -d %{buildroot}%{_libdir}/php/extensions
install -d %{buildroot}%{_sysconfdir}/php.d

install -m755 %{soname} %{buildroot}%{_libdir}/php/extensions/

cat > %{buildroot}%{_sysconfdir}/php.d/%{inifile} << EOF
extension = %{soname}
EOF

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc CREDITS EXPERIMENTAL
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/php.d/%{inifile}
%attr(0755,root,root) %{_libdir}/php/extensions/%{soname}

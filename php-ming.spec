%define modname ming
%define dirname %{modname}
%define soname %{modname}.so
%define inifile 33_%{modname}.ini

Summary:	Ming extension module for PHP
Name:		php-ming
Version:	5.2.10
Release:	%mkrel 16
Group:		Development/PHP
URL:		http://www.php.net
License:	PHP License
# S0 is taken from php-5.2.x CVS
Source0:	ming.tar.gz
Patch0:		php-ming-0.4.4.diff
Patch1:		ming-php54x.diff
BuildRequires:	php-devel >= 3:5.2.0
BuildRequires:	ming-devel >= 0.4.4
Epoch:		1
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This is a dynamic shared object (DSO) for PHP that will add ming (Flash - .swf
files) support.

%prep

%setup -q -n ming
%patch0 -p1
%patch1 -p0

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


%changelog
* Sun May 06 2012 Oden Eriksson <oeriksson@mandriva.com> 1:5.2.10-16mdv2012.0
+ Revision: 797070
- sync with libming-0.4.4
- fix build (debian)
- rebuild for php-5.4.x

* Sun Jan 15 2012 Oden Eriksson <oeriksson@mandriva.com> 1:5.2.10-15
+ Revision: 761270
- rebuild

* Wed Aug 24 2011 Oden Eriksson <oeriksson@mandriva.com> 1:5.2.10-14
+ Revision: 696447
- rebuilt for php-5.3.8

* Fri Aug 19 2011 Oden Eriksson <oeriksson@mandriva.com> 1:5.2.10-13
+ Revision: 695442
- rebuilt for php-5.3.7

* Thu Apr 28 2011 Oden Eriksson <oeriksson@mandriva.com> 1:5.2.10-12
+ Revision: 659826
- fix deps
- increase epoch
- update P0 from ming-0.4.3
- rebuilt for php-5.3.6

* Sat Jan 08 2011 Oden Eriksson <oeriksson@mandriva.com> 0:5.2.10-10mdv2011.0
+ Revision: 629837
- rebuilt for php-5.3.5

* Mon Jan 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0:5.2.10-9mdv2011.0
+ Revision: 628164
- ensure it's built without automake1.7

* Wed Nov 24 2010 Oden Eriksson <oeriksson@mandriva.com> 0:5.2.10-8mdv2011.0
+ Revision: 600510
- rebuild

* Sun Oct 24 2010 Oden Eriksson <oeriksson@mandriva.com> 0:5.2.10-7mdv2011.0
+ Revision: 588848
- rebuild

* Fri Mar 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0:5.2.10-6mdv2010.1
+ Revision: 514577
- rebuilt for php-5.3.2

* Sat Jan 02 2010 Oden Eriksson <oeriksson@mandriva.com> 0:5.2.10-5mdv2010.1
+ Revision: 485407
- rebuilt for php-5.3.2RC1

* Sat Nov 21 2009 Oden Eriksson <oeriksson@mandriva.com> 0:5.2.10-4mdv2010.1
+ Revision: 468190
- rebuilt against php-5.3.1

* Wed Sep 30 2009 Oden Eriksson <oeriksson@mandriva.com> 0:5.2.10-3mdv2010.0
+ Revision: 451293
- rebuild

* Sun Jul 19 2009 Raphaël Gertz <rapsys@mandriva.org> 0:5.2.10-2mdv2010.0
+ Revision: 397557
- Rebuild

* Sun Jun 28 2009 Oden Eriksson <oeriksson@mandriva.com> 0:5.2.10-1mdv2010.0
+ Revision: 390399
- reintroduce the package

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Jun 01 2007 Oden Eriksson <oeriksson@mandriva.com> 5.2.3-1mdv2008.0
+ Revision: 33792
- rebuilt against new upstream version (5.2.3)

* Thu May 03 2007 Oden Eriksson <oeriksson@mandriva.com> 5.2.2-1mdv2008.0
+ Revision: 21313
- rebuilt against new upstream version (5.2.2)


* Thu Feb 08 2007 Oden Eriksson <oeriksson@mandriva.com> 5.2.1-1mdv2007.0
+ Revision: 117458
- rebuilt against new upstream version (5.2.1)

* Wed Nov 08 2006 Oden Eriksson <oeriksson@mandriva.com> 5.2.0-1mdv2007.0
+ Revision: 78089
- rebuilt for php-5.2.0
- Import php-ming

* Mon Aug 28 2006 Oden Eriksson <oeriksson@mandriva.com> 5.1.6-1
- rebuilt for php-5.1.6

* Thu Jul 27 2006 Oden Eriksson <oeriksson@mandriva.com> 5.1.4-2mdk
- rebuild

* Sat May 06 2006 Oden Eriksson <oeriksson@mandriva.com> 5.1.4-1mdk
- rebuilt for php-5.1.4

* Sat May 06 2006 Oden Eriksson <oeriksson@mandriva.com> 5.1.3-1mdk
- rebuilt for php-5.1.3

* Sun Jan 15 2006 Oden Eriksson <oeriksson@mandriva.com> 5.1.2-1mdk
- rebuilt against php-5.1.2

* Sun Oct 02 2005 Oden Eriksson <oeriksson@mandriva.com> 5.1.0-0.RC1.1mdk
- rebuilt against php-5.1.0RC1

* Wed Sep 07 2005 Oden Eriksson <oeriksson@mandriva.com> 5.0.5-1mdk
- rebuilt against php-5.0.5 (Major security fixes)

* Fri May 27 2005 Oden Eriksson <oeriksson@mandriva.com> 5.0.4-1mdk
- rename the package

* Sun Apr 17 2005 Oden Eriksson <oeriksson@mandriva.com> 5.0.4-1mdk
- 5.0.4

* Sun Mar 20 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.3-4mdk
- use the %%mkrel macro

* Sat Feb 12 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.3-3mdk
- rebuilt against a non hardened-php aware php lib

* Sun Jan 16 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.3-2mdk
- rebuild due to hardened-php-0.2.6

* Fri Dec 17 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.3-1mdk
- rebuilt for php-5.0.3

* Sat Sep 25 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.2-1mdk
- rebuilt for php-5.0.2

* Sun Aug 15 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.1-1mdk
- rebuilt for php-5.0.1

* Wed Aug 11 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.0-1mdk
- rebuilt for php-5.0.0
- major cleanups

* Thu Jul 15 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.8-1mdk
- rebuilt for php-4.3.8

* Tue Jul 13 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.7-2mdk
- remove redundant provides

* Tue Jun 15 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.7-1mdk
- rebuilt for php-4.3.7

* Tue May 25 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.6-2mdk
- move scandir to /etc/php.d
- phpize got broken for this extension, fall back to use buildext
- built against new ming

* Thu May 06 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.6-1mdk
- fix invalid-build-requires
- built for php 4.3.6


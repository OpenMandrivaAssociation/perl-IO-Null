%define upstream_name    IO-Null
%define upstream_version 1.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Class for null filehandles
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/IO/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This is a class for null filehandles.

Calling a constructor of this class always succeeds, returning a new null
filehandle.

Writing to any object of this class is always a no-operation, and returns
true.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc ChangeLog README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 1.10.0-2mdv2011.0
+ Revision: 655032
- rebuild for updated spec-helper

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 1.10.0-1mdv2011.0
+ Revision: 401654
- rebuild using %%perl_convert_version
- fixed license field

* Mon May 18 2009 Erin Wilkins <ewilkins@mandriva.org> 1.01-3mdv2010.0
+ Revision: 377269
- Practice checkout, change, build, commit as part of becoming maintainer

* Sat May 16 2009 Glen Ogilvie <nelg@mandriva.org> 1.01-2mdv2010.0
+ Revision: 376356
- update mkrel to test

* Sat Sep 06 2008 Jérôme Quelin <jquelin@mandriva.org> 1.01-1mdv2009.0
+ Revision: 281819
- import perl-IO-Null


* Sat Sep 06 2008 cpan2dist 1.01-1mdv
- initial mdv release, generated with cpan2dist


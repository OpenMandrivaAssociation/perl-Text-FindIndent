%define upstream_name    Text-FindIndent
%define upstream_version 0.10

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Heuristically determine the indent style
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
This is an experimental distribution that attempts to intuit the underlying
indent "policy" for a text file (most likely a source code file).

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
%doc README Changes LICENSE
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.100.0-2mdv2011.0
+ Revision: 657852
- rebuild for updated spec-helper

* Wed Jan 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.100.0-1mdv2011.0
+ Revision: 628738
- update to new version 0.10

* Sat Aug 28 2010 Jérôme Quelin <jquelin@mandriva.org> 0.90.0-1mdv2011.0
+ Revision: 573807
- update to 0.09

* Thu Jan 07 2010 Jérôme Quelin <jquelin@mandriva.org> 0.80.0-1mdv2011.0
+ Revision: 487050
- update to 0.08

* Thu Dec 24 2009 Jérôme Quelin <jquelin@mandriva.org> 0.70.0-1mdv2010.1
+ Revision: 482079
- update to 0.07

* Fri Nov 27 2009 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-1mdv2010.1
+ Revision: 470462
- update to 0.05

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2010.0
+ Revision: 401516
- rebuild using %%perl_convert_version
- fixed license field

* Sun Mar 08 2009 Jérôme Quelin <jquelin@mandriva.org> 0.04-1mdv2009.1
+ Revision: 352842
- update to new version 0.04

* Tue Dec 02 2008 Jérôme Quelin <jquelin@mandriva.org> 0.03-1mdv2009.1
+ Revision: 309269
- import perl-Text-FindIndent


* Tue Dec 02 2008 cpan2dist 0.03-1mdv
- initial mdv release, generated with cpan2dist


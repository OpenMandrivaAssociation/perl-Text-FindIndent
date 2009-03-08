
%define realname   Text-FindIndent
%define version    0.04
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Heuristically determine the indent style
Source:     http://www.cpan.org/modules/by-module/Text/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)

BuildArch: noarch

%description
This is an experimental distribution that attempts to intuit the underlying
indent "policy" for a text file (most likely a source code file).





%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes LICENSE
%{_mandir}/man3/*
%perl_vendorlib/*



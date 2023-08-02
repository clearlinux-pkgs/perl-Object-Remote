#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Object-Remote
Version  : 0.004001
Release  : 13
URL      : https://cpan.metacpan.org/authors/id/H/HA/HAARG/Object-Remote-0.004001.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/H/HA/HAARG/Object-Remote-0.004001.tar.gz
Summary  : 'Call methods on objects in other processes or on other hosts'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Object-Remote-bin = %{version}-%{release}
Requires: perl-Object-Remote-license = %{version}-%{release}
Requires: perl-Object-Remote-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Algorithm::C3)
BuildRequires : perl(Class::C3)
BuildRequires : perl(Class::Method::Modifiers)
BuildRequires : perl(Data::Dumper::Concise)
BuildRequires : perl(Devel::GlobalDestruction)
BuildRequires : perl(Exporter::Declare)
BuildRequires : perl(Future)
BuildRequires : perl(Log::Contextual)
BuildRequires : perl(MRO::Compat)
BuildRequires : perl(Meta::Builder)
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Moo)
BuildRequires : perl(Role::Tiny)
BuildRequires : perl(String::ShellQuote)
BuildRequires : perl(Sub::Exporter::Progressive)
BuildRequires : perl(Sub::Quote)
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Try::Tiny)
BuildRequires : perl(aliased)
BuildRequires : perl(strictures)

%description
NAME
Object::Remote - Call methods on objects in other processes or on other
hosts

%package bin
Summary: bin components for the perl-Object-Remote package.
Group: Binaries
Requires: perl-Object-Remote-license = %{version}-%{release}

%description bin
bin components for the perl-Object-Remote package.


%package dev
Summary: dev components for the perl-Object-Remote package.
Group: Development
Requires: perl-Object-Remote-bin = %{version}-%{release}
Provides: perl-Object-Remote-devel = %{version}-%{release}
Requires: perl-Object-Remote = %{version}-%{release}

%description dev
dev components for the perl-Object-Remote package.


%package license
Summary: license components for the perl-Object-Remote package.
Group: Default

%description license
license components for the perl-Object-Remote package.


%package perl
Summary: perl components for the perl-Object-Remote package.
Group: Default
Requires: perl-Object-Remote = %{version}-%{release}

%description perl
perl components for the perl-Object-Remote package.


%prep
%setup -q -n Object-Remote-0.004001
cd %{_builddir}/Object-Remote-0.004001

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Object-Remote
cp %{_builddir}/Object-Remote-0.004001/LICENSE %{buildroot}/usr/share/package-licenses/perl-Object-Remote/9ef6cb6bf8daa686a87a0d40ac8adcc38ff0a71c
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/object-remote-node
/usr/bin/object-remote-slave
/usr/bin/remoterepl

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Object::Remote.3
/usr/share/man/man3/Object::Remote::Connection.3
/usr/share/man/man3/Object::Remote::Future.3
/usr/share/man/man3/Object::Remote::Logging.3
/usr/share/man/man3/Object::Remote::Logging::Logger.3
/usr/share/man/man3/Object::Remote::Role::Connector::PerlInterpreter.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Object-Remote/9ef6cb6bf8daa686a87a0d40ac8adcc38ff0a71c

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*

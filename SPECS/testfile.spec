Name:		testfile
Version:	1.0
Release:	%{?BUILD_NUMBER}
Summary:	Testfile.txt dummy package, for practicing building and rpm install.

Group:		Development/System
License:	none
URL:		http://www.acbss.com
Source0:	%{name}.tar.gz
BuildRoot:	%{_buildrootdir}/%{name}-%{version}-%{release}
BuildArch:	noarch

%description
Test RPM package with a tar file that contains one file.  This spec file
shows how to setup an tar based rpm package (i.e. source code, for example).
There are other examples online.

%prep
%setup -q

%install
install -m 0755 -d $RPM_BUILD_ROOT/opt/testfile
install -m 0644 testfile.txt $RPM_BUILD_ROOT/opt/testfile/testfile.txt

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf %{_builddir}/*
rm -f  %{_tmppath}/*


%files
%dir /opt/testfile
/opt/testfile/testfile.txt

%defattr(-,root,root,-)
%doc
%changelog


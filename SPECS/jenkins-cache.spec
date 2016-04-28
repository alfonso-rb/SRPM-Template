%define		name	jenkins-cache
%define 	version	1.0

Summary:	jenkins-cache, a collection of files from /var/cache/jenkins
Name:		%{name}
Version:	%{version}
Release:	%{?BUILD_NUMBER}
License:	none

Group:		Applications/Text
BuildArch:	noarch
URL:		http://www.acbss.com
Vendor:		ACBSS, LLC
Packager:	info@acbss.com
Provides:	jenkins-cache
Requires:	htop

%description
This package contains jenkins-cache, a collection of files from
jenkins cache dir, just used for testing RPM creation from direct files.
It installs the files in the /tmp/jenkins-cache directory of the target
host.

%prep
exit 0

%build
exit 0

%install
exit 0

%clean
# exit 0
#rm -rf $RPM_BUILD_ROOT
rm -f  %{_tmppath}/*

%files
%defattr(-,root,root)
/tmp/jenkins-cache


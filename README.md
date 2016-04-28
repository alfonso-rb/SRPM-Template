Sample rpmbuild project.

Contains 2 sample rpm spec files and source content:
- testfile, which is one file stored in a tar file (in the SOURCES directory)
- jenkins-cache, which is some dummy files, with the directory structure in the
BUILDROOT directory.

Basically edit the spec files as needed, and replace the content with your own.
The following command is used right now to build the rpms:

rpmbuild --define "_topdir `pwd`" --define "_tmppath %{_topdir}/tmp"\
  --buildroot=%{_buildrootdir}/%{name} --define \
  "BUILD_NUMBER `date +%Y%m%d%H%M%S`" -bb SPECS/jenkins-cache.spec
  
rpmbuild --define "_topdir `pwd`" --define "_tmppath %{_topdir}/tmp"\
  --buildroot=%{_buildrootdir}/%{name} --define \
  "BUILD_NUMBER `date +%Y%m%d%H%M%S`" -bb SPECS/testfile.spec
  
edit as needed.  Eventually this will be a task associated with jenkins to do
automated builds.
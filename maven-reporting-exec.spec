Name:           maven-reporting-exec
Version:        1.1
Release:        5%{?dist}
BuildArch:      noarch
Summary:        Classes to manage report plugin executions with Maven 3

License:        ASL 2.0
URL:            http://maven.apache.org/shared/maven-reporting-exec/
Source0:        http://repo1.maven.org/maven2/org/apache/maven/reporting/%{name}/%{version}/%{name}-%{version}-source-release.zip

BuildRequires:  java-devel
BuildRequires:  jpackage-utils
BuildRequires:  maven-local
BuildRequires:  maven-invoker-plugin
BuildRequires:  maven-shared
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  plexus-containers-component-metadata

Requires:       java

%description
Classes to manage report plugin executions with Maven 3. Contains classes for
managing and configuring reports and their execution.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation
Requires:       jpackage-utils

%description javadoc
The API documentation of %{name}.



%prep
%setup -qn %{name}-%{version}
# convert CR+LF to LF
sed -i 's/\r//g' pom.xml src/main/java/org/apache/maven/reporting/exec/*

# We have different sonatype groupId and java package name
find -iname '*.java' -exec sed -i 's/org.eclipse.aether/org.sonatype.aether/g' '{}' ';'

%pom_xpath_set "pom:groupId[text()='org.eclipse.aether']" org.sonatype.aether
%pom_remove_plugin org.apache.maven.plugins:maven-enforcer-plugin

%build
# Test are skipped because there are errors with PlexusLogger
# More info possibly here:
# https://docs.sonatype.org/display/AETHER/Using+Aether+in+Maven+Plugins?focusedCommentId=10485782#comment-10485782
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE DEPENDENCIES

%files -f .mfiles-javadoc
%doc LICENSE NOTICE



%changelog
* Fri Aug  1 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-5
- Add missing build-requires on maven-shared
- Resolves: rhbz#1074929

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.1-4
- Mass rebuild 2013-12-27

* Mon Jun 10 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.1-3
- Remove unused source

* Mon May 06 2013 Tomas Radej <tradej@redhat.com> - 1.1-2
- Removed aether BR

* Mon Apr 22 2013 Tomas Radej <tradej@redhat.com> - 1.1-1
- Updated to latest upstream version
- Building with maven-local

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0.2-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 26 2012 Tomas Radej <tradej@redhat.com> - 1.0.2-1
- Updated to latest upstream version

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Aug 12 2011 tradej <tradej@redhat.com> 1.0.1-3
- Added dist macro to release

* Thu Aug 11 2011 tradej <tradej@redhat.com> 1.0.1-2
- Changed BuildArch to noarch

* Wed Aug 10 2011 tradej <tradej@redhat.com> 1.0.1-1
- Initial release (thanks to akurtakov, jcapik and the GULaG team for help)


Summary: Nexus manages software “artifacts” required for development, deployment, and provisioning.
Name: nexus
Version: 2.14.1
Release: 01
License: AGPL
Group: unknown
URL: http://nexus.sonatype.org/
Source0: %{name}-%{version}-%{release}-bundle.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires(pre): /usr/sbin/useradd, /usr/bin/getent
Requires(postun): /usr/sbin/userdel
AutoReqProv: no

%define __os_install_post %{nil}

%description
A package repository

%prep
%setup -q -n %{name}-%{version}-%{release}

%build
%define debug_package %{nil}

%pre
/usr/bin/getent passwd %{name} > /dev/null || /usr/sbin/useradd -r -d /var/lib/%{name} -s /bin/bash %{name}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/share/%{name}
mv * $RPM_BUILD_ROOT/usr/share/%{name}

mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d/
cd $RPM_BUILD_ROOT/etc/rc.d/init.d/
ln -sf /usr/share/%{name}/bin/nexus $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}

mkdir -p $RPM_BUILD_ROOT/etc/
ln -sf /usr/share/%{name}/conf $RPM_BUILD_ROOT/etc/%{name}

# patch work dir
sed -i -e 's/%{name}-work=.*/%{name}-work=\/var\/lib\/%{name}\//' $RPM_BUILD_ROOT/usr/share/%{name}/conf/nexus.properties
mkdir -p $RPM_BUILD_ROOT/var/lib/%{name}

# patch pid dir
sed -i -e 's/PIDDIR=.*/PIDDIR=\/var\/run\/%{name}/' $RPM_BUILD_ROOT/usr/share/%{name}/bin/nexus
mkdir -p $RPM_BUILD_ROOT/var/run/%{name}

# Patch user
sed -i -e 's/#RUN_AS_USER=.*/RUN_AS_USER=%{name}/' $RPM_BUILD_ROOT/usr/share/%{name}/bin/nexus

# patch logfile
mkdir -p $RPM_BUILD_ROOT/var/log/%{name}
sed -i -e 's/wrapper.logfile=.*/wrapper.logfile=\/var\/log\/%{name}\/%{name}.log/' $RPM_BUILD_ROOT/usr/share/%{name}/bin/jsw/conf/wrapper.conf

%preun
service %{name} stop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc
/etc/rc.d/init.d/%{name}
%attr(-,%{name},%{name}) /etc/%{name}
%attr(-,%{name},%{name}) /var/lib/%{name}
%attr(-,%{name},%{name}) /var/log/%{name}
%attr(-,%{name},%{name}) /var/run/%{name}
%attr(-,%{name},%{name}) /usr/share/%{name}

%changelog

* Sat Nov 12 2016 Julio Gonzalez <git@juliogonzalez.es> - 2.14.1-01
- Update to 2.14.1-01

* Sun May 29 2016 Julio Gonzalez <git@juliogonzalez.es> - 2.13.0-01
- Update to 2.13.0-01

* Sat Feb 13 2016 Julio Gonzalez <git@juliogonzalez.es> - 2.12.0-01
- Update to 2.12.0-01

* Tue Jul 21 2015 Julio Gonzalez <git@juliogonzalez.es> - 2.11.4-01
- Update to 2.11.4-01

* Fri Jun 26 2015 Julio Gonzalez <git@juliogonzalez.es> - 2.11.3-01
- Update to last version available
- Nexus will now listen at 8081 (this can be modified at
  /etc/nexus/nexus.properties)
- Nexus runs now without as system user, not as root
- Remove jdk dependency (no virtual package at CentOS 7)

* Thu Dec 22 2011 Jens Braeuer <braeuer.jens@googlemail.com> - 1.9.2.3-1
- Initial packaging.
- For now nexus will run as root and listen to port 80


Summary: Nexus manages software “artifacts” required for development, deployment, and provisioning.
Name: nexus
Version: 2.0.6
Release: 1
License: AGPL
Group: unknown
URL: http://nexus.sonatype.org/
Source0: %{name}-%{version}-bundle.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: jdk
AutoReqProv: no

%define __os_install_post %{nil}

%description
A package repository

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/share/%{name}
mv * $RPM_BUILD_ROOT/usr/share/%{name}

arch=$(echo "%{_arch}" | sed -e 's/_/-/')
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d/
cd $RPM_BUILD_ROOT/etc/rc.d/init.d/
ln -sf /usr/share/%{name}/bin/jsw/linux-$arch/nexus $RPM_BUILD_ROOT/etc/rc.d/init.d/

mkdir -p $RPM_BUILD_ROOT/etc/
ln -sf /usr/share/%{name}/conf $RPM_BUILD_ROOT/etc/nexus

# patch work dir
sed -i -e 's#nexus-work=.*#nexus-work=/var/lib/nexus/#g' $RPM_BUILD_ROOT/usr/share/%{name}/conf/nexus.properties
mkdir -p $RPM_BUILD_ROOT/var/lib/nexus

# patch tcp port
#sed -i -e 's#application-port=.*#application-port=80#g' $RPM_BUILD_ROOT/usr/share/%{name}/conf/plexus.properties

# patch pid dir
sed -i -e 's#PIDDIR=.*#PIDDIR=/var/run/#' $RPM_BUILD_ROOT/usr/share/%{name}/bin/jsw/linux-$arch/nexus

# patch logfile
mkdir -p $RPM_BUILD_ROOT/var/log/nexus
sed -i -e 's#wrapper.logfile=.*#wrapper.logfile=/var/log/nexus/nexus.log#' $RPM_BUILD_ROOT/usr/share/%{name}/bin/jsw/conf/wrapper.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc
/usr/share/%{name}
/etc/rc.d/init.d/nexus
/etc/nexus
/var/lib/nexus
/var/log/nexus

%changelog
* Thu Jul 13 2012 Mike Champion <mike.champion@gmail.com> - 2.0.6
- Upgrade to 2.0.6
* Thu Dec 22 2011 Jens Braeuer <braeuer.jens@googlemail.com> - 1.9.2.3-1
- Initial packaging.
- For now nexus will run as root and listen to port 80


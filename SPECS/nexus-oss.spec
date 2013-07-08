Summary: Nexus manages software “artifacts” required for development, deployment, and provisioning.
Name: nexus
Version: %{version}
Release: %{release}
License: AGPL
Group: unknown
URL: http://nexus.sonatype.org/
Source0: %{name}-%{version}-%{release}-bundle.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
AutoReqProv: no
Patch0: nexus_initd.patch

%define __os_install_post %{nil}

%description
A package repository

%prep
%setup -q -n %{name}-%{version}-%{release}
%patch0 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/share/%{name}
mv * $RPM_BUILD_ROOT/usr/share/%{name}

mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d/
cd $RPM_BUILD_ROOT/etc/rc.d/init.d/
ln -sf /usr/share/%{name}/bin/nexus $RPM_BUILD_ROOT/etc/rc.d/init.d/

mkdir -p $RPM_BUILD_ROOT/etc/
ln -sf /usr/share/%{name}/conf $RPM_BUILD_ROOT/etc/nexus

# patch work dir
sed -i -e 's#nexus-work=.*#nexus-work=/var/lib/nexus/#g' $RPM_BUILD_ROOT/usr/share/%{name}/conf/nexus.properties
mkdir -p $RPM_BUILD_ROOT/var/lib/nexus

# patch pid dir
sed -i -e 's#PIDDIR=.*#PIDDIR=/var/run#' $RPM_BUILD_ROOT/usr/share/%{name}/bin/nexus
sed -i -e 's/#RUN_AS_USER=.*/RUN_AS_USER=nexus/' $RPM_BUILD_ROOT/usr/share/%{name}/bin/nexus 

# patch logfile
mkdir -p $RPM_BUILD_ROOT/var/log/nexus
sed -i -e 's#wrapper.logfile=.*#wrapper.logfile=/var/log/nexus/nexus.log#' $RPM_BUILD_ROOT/usr/share/%{name}/bin/jsw/conf/wrapper.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,nexus,nexus,-)
%doc
/usr/share/%{name}
/etc/rc.d/init.d/nexus
/etc/nexus
/var/lib/nexus
/var/log/nexus

%pre
getent group nexus >/dev/null || groupadd -r nexus
getent passwd nexus >/dev/null || \
    useradd -r -g nexus -d /usr/share/%{name} -s /sbin/nologin \
    -c "Nexus OSS" nexus

%post
service nexus start

%preun
service nexus stop

%changelog
* Mon Jul 8 2013 Ilja Bobkevic <ilja.bobkevic@gmail.com>
- Addopt spec for external verison and release definition
- Use nexus credentials for the daemon
- Patch init.d script with proper headers and to use sudo instead su
* Thu Jul 13 2012 Mike Champion <mike.champion@gmail.com> - 2.0.6
- Upgrade to 2.0.6
* Thu Dec 22 2011 Jens Braeuer <braeuer.jens@googlemail.com> - 1.9.2.3-1
- Initial packaging.
- For now nexus will run as root and listen to port 80


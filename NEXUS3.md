# Requirements

- To build the RPM:
 - rpm-build
 - wget
 - tar
 - gz

- To run Nexus:
 - Any JDK/JRE (Oracle or OpenJDK) 1.8 installed (it is not included
   as dependency because CentOS 7 does not provide a virtual package for
   Java).

# How to build

```
./nexus-oss-rpm -v 3
```

# Upgrading from 2.x

According to [Nexus documentation](https://books.sonatype.com/nexus-book/3.0/reference/install.html#installation-upgrading) it is not possible to upgrade to
Nexus 3.x from Nexus 2.x at this moment.

# Daemon

Nexus configuration has been customized, so Nexus behaves more like a
"real" daemon, listening at port 8081 (you can change it at
/etc/nexus3/org.sonatype.nexus.cfg).

The RPM will create a user called 'nexus3' to run Nexus OSS.

Nexus will not be configured to run automatically, but you can enable
it by running:

```
chkconfig --add nexus3
```

# Linux-like directories

- Data: /var/lib/nexus3
- Logfiles: /var/log/nexus3
- Conf: /etc/nexus3
- Init file: /etc/init.d/nexus3

[![Build Status](https://jenkins-juliogonzalez.rhcloud.com/job/nexus-oss-rpm-build/badge/icon)](https://jenkins-juliogonzalez.rhcloud.com/job/nexus-oss-rpm-build/)

This repository holds files and scripts to build a Sonatype Nexus .rpm
package.

# Ingredients

- Nexus OSS 2.11.4-01: from http://www.sonatype.org/nexus/

# Licenses

- Nexus OSS: AGPL, Sonatype
- Scripts and Spec: AGPL, Jens Braeuer <braeuer.jens@googlemail.com>,
  Julio Gonzalez Gil <git@juliogonzalez.es>

# Requirements

- To build the RPM:
 - rpm-build
 - wget
 - tar
 - gz

- To run Nexus:
 - Any JDK/JRE (Oracle or OpenJDK) 1.7 or 1.8 installed
   (it is not included as dependency because CentOS 7 does not provide
   a virtual package for Java).

# How to build

- fetch Nexus OSS tar.gz:
```
./fetch-nexus-oos
```
- build RPM:
```
./rpm SPECS/nexus-oss.spec
```

# Daemon

Nexus configuration has been customized, so Nexus behaves more like a
"real" daemon, listening at port 8081 (you can change it at
/etc/nexus/nexus.properties).

The RPM will create a user called 'nexus' to run Nexus OSS.

Nexus will not be configured to run automatically, but you can enable
it by running:

```
chkconfig --add nexus
```

# Linux-like directories

- Logfiles: /var/log/nexus
- Pidfile: /var/run/
- Conf: /etc/nexus
- Init file: /etc/init.d/nexus

# Current state

This has been tested on CentOS Linux 7.1 x84. It should work
on RHEL and other derivates.

Have fun!
Jens


This repository holds files and scripts to build a Sonatype Nexus .rpm
package.

# Ingredients
- Nexus OSS 2.0.6: from http://nexus.sonatype.com

# Licenses
- Nexus OSS: AGPL, Sonatype
- Scripts and Spec: AGPL, Jens Braeuer <braeuer.jens@googlemail.com>

# How to build
- fetch Nexus OSS tar.gz: ./fetch-nexus-oos
- build RPM:              ./rpm SPECS/nexus-oss.spec

# Linux-like directories

Nexus configuration has been customized, so Nexus behaves more like a
"real" daemon.

- Logfiles: /var/log/nexus
- Pidfile: /var/run/
- Conf: /etc/nexus
- Init file: /etc/init.d/nexus

# Current state

This has been tested on Scientific Linux 6.1. It should work on CentOS
and RHEL too.  Currently Nexus is configured to run as root
user. While this not perfect, it is better than the manual
unzip/install steps .

Have fun!
Jens


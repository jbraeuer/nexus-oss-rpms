This repository holds files and scripts to build a Sonatype Nexus .rpm
package.

# Ingredients
- Nexus OSS Latest: from http://nexus.sonatype.com

# Licenses
- Nexus OSS: AGPL, Sonatype
- Scripts and Spec: AGPL, Jens Braeuer <braeuer.jens@googlemail.com>, Ilja Bobkevic <ilja.bobkevic@gmail.com>

# How to build
- fetch Nexus OSS tar.gz: ./fetch-nexus-oos
- build RPM:              ./rpm SPECS/nexus-oss.spec

# Linux-like directories

Nexus configuration has been customized, so Nexus behaves more like a
"real" daemon.

- Logfiles: /var/log/nexus
- Pidfile: /var/run
- Conf: /etc/nexus
- Init file: /etc/init.d/nexus

# Current state

This has been tested on Scientific Linux 6.1 and CentOS 6.4.
It should work on  RHEL too.

Have fun!


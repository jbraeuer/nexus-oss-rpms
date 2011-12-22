This repository holds files and scripts to build a Sonatype Nexus .rpm
package.

# Ingredients
- Nexus OSS 1.9.2.3: from http://nexus.sonatype.com

# Licenses
- Nexus OSS: AGPL
- Scripts and Spec: AGPL

# How to build
- fetch Nexus OSS tar.gz: ./fetch-nexus-oos
- build RPM:              ./rpm SPECS/nexus-oss.spec

# Current state
This has been tested on Scientific Linux 6.1. It should work on CentOS and RHEL too.

Have fun!
Jens Braeuer <braeuer.jens@googlemail.com>


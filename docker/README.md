# Nexus Docker images for Continous Integration

Current distributions available:

* CentOS 6
* CentoS 7
* Amazon Linux 2017.03
* openSUSE Leap 15.1

# Building images

Run:

```
./manage_images -h
```

# Running the images

To run, for example, the CentOS7 image:

```
docker run -t --name test juliogonzalez/centos7-nexusdev
```

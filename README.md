Chaperone
=========
[![Build Status](https://travis-ci.org/vmware/chaperone.svg?branch=master)](https://travis-ci.org/vmware/chaperone)

Chaperone is an Automation toolkit rooted in DevOps principals for deploying
and configuring a Software Defined Data Center (SDDC) based Hybrid Cloud
Management platform. It is intended to expedite and standardize  "typical"
deployments and configuration of VMware solutions including vSphere/vCenter,
NSX, VIO, vRA, vRO, vROps, vRLI, vRB and others as the toolkit grows.

Chaperone is a work in progress.  We will continue to
add new functionality and products to the Chaperone base.


## Chaperone Overview

### Current Standard Configurations Supported

The ansible playbooks are used to configure and deploy several standard platforms.
The following are under active development, but are considered fairly complete:

- Chaperone for VIO (Open Stack Integration)
- Chaperone for CNA (Cloud Native Application Platform)
- Chaperone for CMP (Hybrid Cloud Management Platform)

### Experimental Configurations

The following are under active development
- Chaperone for NSX
- Chaperone for VxRails
- Chaperone for kubernetes
- Chaperone for IOT platforms

### Setup and Run Chaperone

There are guides for [setting up](docs/setup.md) and [running](docs/run.md)
the Chaperone tools against an appropriate SDDC environment.

### Development

Read the [developer guide](docs/developer.md) if you are interested in the
development process of Chaperone

### Chaperone Sub-components

Chaperone is built from lots of smaller pieces with a glue of UI and Ansible Playbooks.

The following is a current list of sub-projects:

- [chaperone-ui](https://github.com/vmware/chaperone-ui)
- [ansible-playbooks-chaperone](https://github.com/vmware/ansible-playbooks-chaperone)
- [ansible-modules-extras-gpl3](https://github.com/vmware/ansible-modules-extras-gpl3)
- [ansible-module-chaperone](https://github.com/vmware/ansible-module-chaperone)
- [nsxansible.git](https://github.com/vmware/nsxansible.git)
- [nsxraml.git](https://github.com/vmware/nsxraml.git)
- [ansible-role-jenkins](https://github.com/vmware/ansible-role-jenkins)
- [ansible-role-haproxy](https://github.com/vmware/ansible-role-haproxy)
- [ansible-role-ansible](https://github.com/vmware/ansible-role-ansible)
- [ansible-role-assets](https://github.com/vmware/ansible-role-assets)
- [ansible-role-autodeploy](https://github.com/vmware/ansible-role-autodeploy)
- [ansible-role-chaperone](https://github.com/vmware/ansible-role-chaperone)
- [ansible-role-dnsmasq](https://github.com/vmware/ansible-role-dnsmasq)
- [ansible-role-docker](https://github.com/vmware/ansible-role-docker)
- [ansible-role-govc](https://github.com/vmware/ansible-role-govc)
- [ansible-role-iptables](https://github.com/vmware/ansible-role-iptables)
- [ansible-role-kibana](https://github.com/vmware/ansible-role-kibana)
- [ansible-role-kubernetes-master](https://github.com/vmware/ansible-role-kubernetes-master)
- [ansible-role-kubernetes-node](https://github.com/vmware/ansible-role-kubernetes-node)
- [ansible-role-elasticsearch](https://github.com/vmware/ansible-role-elasticsearch)
- [ansible-role-liota](https://github.com/vmware/ansible-role-liota)
- [ansible-role-logstash-server](https://github.com/vmware/ansible-role-logstash-server)
- [ansible-role-net](https://github.com/vmware/ansible-role-net)
- [ansible-role-nfs](https://github.com/vmware/ansible-role-nfs)
- [ansible-role-nsx](https://github.com/vmware/ansible-role-nsx)
- [ansible-role-ovftool](https://github.com/vmware/ansible-role-ovftool)
- [ansible-role-photon](https://github.com/vmware/ansible-role-photon)
- [ansible-role-pip](https://github.com/vmware/ansible-role-pip)
- [ansible-role-registrator](https://github.com/vmware/ansible-role-registrator)
- [ansible-role-repo](https://github.com/vmware/ansible-role-repo)
- [ansible-role-sshkeys](https://github.com/vmware/ansible-role-sshkeys)
- [ansible-role-sudo](https://github.com/vmware/ansible-role-sudo)
- [ansible-role-vcenter](https://github.com/vmware/ansible-role-vcenter)
- [ansible-role-vcsa](https://github.com/vmware/ansible-role-vcsa)
- [ansible-role-vio](https://github.com/vmware/ansible-role-vio)
- [ansible-role-vrops](https://github.com/vmware/ansible-role-vrops)
- [ansible-role-vra](https://github.com/vmware/ansible-role-vra)
- [ansible-role-vrli](https://github.com/vmware/ansible-role-vrli)
- [ansible-role-vrb](https://github.com/vmware/ansible-role-vrb)
- [ansible-role-vrpt](https://github.com/vmware/ansible-role-vrpt)
- [docker-chaperone](https://github.com/vmware/docker-chaperone)
- [docker-collectd](https://github.com/vmware/docker-collectd)
- [docker-elasticsearch](https://github.com/vmware/docker-elasticsearch)
- [docker-graphite-api](https://github.com/vmware/docker-graphite-api)
- [docker-jenkins](https://github.com/vmware/docker-jenkins)
- [docker-kibana](https://github.com/vmware/docker-kibana)
- [docker-logstash-server](https://github.com/vmware/docker-logstash-server)
- [docker-vrpt](https://github.com/vmware/docker-vrpt)
- [ViaSat/ansible-vsphere.git](https://github.com/ViaSat/ansible-vsphere.git)
- [tomhite/ansible-xml](https://github.com/tomhite/ansible-xml)
- [tomhite/ansible-role-apache.git](https://github.com/tomhite/ansible-role-apache.git)
- [tomhite/ansible-role-collectd](https://github.com/tomhite/ansible-role-collectd)
- [tomhite/ansible-role-consul](https://github.com/tomhite/ansible-role-consul)
- [tomhite/ansible-role-graphite-api](https://github.com/tomhite/ansible-role-graphite-api)
- [ajsalminen/ansible-role-hosts.git](https://github.com/ajsalminen/ansible-role-hosts.git)
- [weareinteractive/ansible-nginx.git](https://github.com/weareinteractive/ansible-nginx.git)
- [weareinteractive/ansible-openssl](https://github.com/weareinteractive/ansible-openssl)
- [weareinteractive/ansible-htpasswd.git](https://github.com/weareinteractive/ansible-htpasswd.git)
- Meta
  - [link to PRs](http://github.com/search?q=is%3Apr%20repo%3Avmware/chaperone-ui%20repo%3Avmware/ansible-playbooks-chaperone%20repo%3Avmware/ansible-modules-extras-gpl3%20repo%3Avmware/ansible-module-chaperone%20repo%3Avmware/nsxansible.git%20repo%3Avmware/nsxraml.git%20repo%3Avmware/ansible-role-jenkins%20repo%3Avmware/ansible-role-haproxy%20repo%3Avmware/ansible-role-ansible%20repo%3Avmware/ansible-role-assets%20repo%3Avmware/ansible-role-autodeploy%20repo%3Avmware/ansible-role-chaperone%20repo%3Avmware/ansible-role-dnsmasq%20repo%3Avmware/ansible-role-docker%20repo%3Avmware/ansible-role-govc%20repo%3Avmware/ansible-role-iptables%20repo%3Avmware/ansible-role-kibana%20repo%3Avmware/ansible-role-kubernetes-master%20repo%3Avmware/ansible-role-kubernetes-node%20repo%3Avmware/ansible-role-elasticsearch%20repo%3Avmware/ansible-role-liota%20repo%3Avmware/ansible-role-logstash-server%20repo%3Avmware/ansible-role-net%20repo%3Avmware/ansible-role-nfs%20repo%3Avmware/ansible-role-nsx%20repo%3Avmware/ansible-role-ovftool%20repo%3Avmware/ansible-role-photon%20repo%3Avmware/ansible-role-pip%20repo%3Avmware/ansible-role-registrator%20repo%3Avmware/ansible-role-repo%20repo%3Avmware/ansible-role-sshkeys%20repo%3Avmware/ansible-role-sudo%20repo%3Avmware/ansible-role-vcenter%20repo%3Avmware/ansible-role-vcsa%20repo%3Avmware/ansible-role-vio%20repo%3Avmware/ansible-role-vrops%20repo%3Avmware/ansible-role-vra%20repo%3Avmware/ansible-role-vrli%20repo%3Avmware/ansible-role-vrb%20repo%3Avmware/ansible-role-vrpt%20repo%3Avmware/docker-chaperone%20repo%3Avmware/docker-collectd%20repo%3Avmware/docker-elasticsearch%20repo%3Avmware/docker-graphite-api%20repo%3Avmware/docker-jenkins%20repo%3Avmware/docker-kibana%20repo%3Avmware/docker-logstash-server%20repo%3Avmware/docker-vrpt%20repo%3AViaSat/ansible-vsphere.git%20repo%3Atomhite/ansible-xml%20repo%3Atomhite/ansible-role-apache.git%20repo%3Atomhite/ansible-role-collectd%20repo%3Atomhite/ansible-role-consul%20repo%3Atomhite/ansible-role-graphite-api%20repo%3Aajsalminen/ansible-role-hosts.git%20repo%3Aweareinteractive/ansible-nginx.git%20repo%3Aweareinteractive/ansible-openssl%20repo%3Aweareinteractive/ansible-htpasswd.git)
  - [link to Issues](http://github.com/search?q=is%3Aissue%20repo%3Avmware/chaperone-ui%20repo%3Avmware/ansible-playbooks-chaperone%20repo%3Avmware/ansible-modules-extras-gpl3%20repo%3Avmware/ansible-module-chaperone%20repo%3Avmware/nsxansible.git%20repo%3Avmware/nsxraml.git%20repo%3Avmware/ansible-role-jenkins%20repo%3Avmware/ansible-role-haproxy%20repo%3Avmware/ansible-role-ansible%20repo%3Avmware/ansible-role-assets%20repo%3Avmware/ansible-role-autodeploy%20repo%3Avmware/ansible-role-chaperone%20repo%3Avmware/ansible-role-dnsmasq%20repo%3Avmware/ansible-role-docker%20repo%3Avmware/ansible-role-govc%20repo%3Avmware/ansible-role-iptables%20repo%3Avmware/ansible-role-kibana%20repo%3Avmware/ansible-role-kubernetes-master%20repo%3Avmware/ansible-role-kubernetes-node%20repo%3Avmware/ansible-role-elasticsearch%20repo%3Avmware/ansible-role-liota%20repo%3Avmware/ansible-role-logstash-server%20repo%3Avmware/ansible-role-net%20repo%3Avmware/ansible-role-nfs%20repo%3Avmware/ansible-role-nsx%20repo%3Avmware/ansible-role-ovftool%20repo%3Avmware/ansible-role-photon%20repo%3Avmware/ansible-role-pip%20repo%3Avmware/ansible-role-registrator%20repo%3Avmware/ansible-role-repo%20repo%3Avmware/ansible-role-sshkeys%20repo%3Avmware/ansible-role-sudo%20repo%3Avmware/ansible-role-vcenter%20repo%3Avmware/ansible-role-vcsa%20repo%3Avmware/ansible-role-vio%20repo%3Avmware/ansible-role-vrops%20repo%3Avmware/ansible-role-vra%20repo%3Avmware/ansible-role-vrli%20repo%3Avmware/ansible-role-vrb%20repo%3Avmware/ansible-role-vrpt%20repo%3Avmware/docker-chaperone%20repo%3Avmware/docker-collectd%20repo%3Avmware/docker-elasticsearch%20repo%3Avmware/docker-graphite-api%20repo%3Avmware/docker-jenkins%20repo%3Avmware/docker-kibana%20repo%3Avmware/docker-logstash-server%20repo%3Avmware/docker-vrpt%20repo%3AViaSat/ansible-vsphere.git%20repo%3Atomhite/ansible-xml%20repo%3Atomhite/ansible-role-apache.git%20repo%3Atomhite/ansible-role-collectd%20repo%3Atomhite/ansible-role-consul%20repo%3Atomhite/ansible-role-graphite-api%20repo%3Aajsalminen/ansible-role-hosts.git%20repo%3Aweareinteractive/ansible-nginx.git%20repo%3Aweareinteractive/ansible-openssl%20repo%3Aweareinteractive/ansible-htpasswd.git)

## License and Copyright

Copyright 2016 VMware, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.


## Author Information

Initially created in 2015 by [Tom Hite / VMware](http://www.vmware.com/).

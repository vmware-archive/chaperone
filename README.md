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

#### Experimental Configurations

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
The following are most of the sub-projects:

- [web based interfaces](https://github.com/vmware/chaperone-ui) for configuring and triggering the deployment of VMware solutions
- [Ansible playbooks](https://github.com/vmware/ansible-playbooks-chaperone) called by the web interface to combine sets of roles into useful groupings of features
- Ansible roles and modules supporting deployment of those solutions (list generated from [the repo manifest](vmwareorg.xml))
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
  
- Extras
  - External ansible roles.  For list, see the "other" [manifest](other.xml)
  - [docker-chaperone](https://github.com/vmware/docker-chaperone)


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

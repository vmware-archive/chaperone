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

The Chaperone toolkit consists of
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
  - [ansible-role-iptables](https://github.com/vmware/ansible-role-iptables)
  - [ansible-role-kibana](https://github.com/vmware/ansible-role-kibana)
  - [ansible-role-kubernetes-master](https://github.com/vmware/ansible-role-kubernetes-master)
  - [ansible-role-kubernetes-node](https://github.com/vmware/ansible-role-kubernetes-node)
  - [ansible-role-elasticsearch](https://github.com/vmware/ansible-role-elasticsearch)
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

### Current Standard Configurations Supported

The plays are used to configure and deploy one of several standard platforms.
The following are under active development, but are considered fairly complete:

- Chaperone for VIO (Open Stack Integration)
- Chaperone for CNA (Cloud Native Application Platform)
- Chaperone for CMP (Hybrid Cloud Management Platform)

### Setup and Run Chaperone

There are more documents for [setting up](docs/setup.md) and [running](docs/run.md)
the Chaperone tools against an appropriate SDDC environment.

### Web Based User Interfaces

There are two interfaces with which users of Chaperone
interact:

- chaperone-admin-ui (e.g., 'http://chaperone-admin-ui.corp.local')
- chaperone-ui (e.g., 'http://chaperone-ui.corp.local')

*Note the use of internal domains in the URLs above. This is common where
developers or users do not have rights to create new domains in their DNS
servers, and thus make use of locally defined domains. More on that in the
[setup documentation](docs/setup.md).*

#### Using the Chaperone Admin UI

The admin UI (chaperone-admin-ui) is an interface that allows one to
select from a list of SDDC features they would like to deploy, and basic
ambient environment information, such as DNS servers, NTP servers, etc. Once
entered into the various "Prepare" menu forms, clicking 'Save' saves the
configuration as a 'codified design.' Basically, that means the information
is saved in a YAML file as a set of parameters or, more commonly Ansible
variables.

Once the chaperone-admin-ui "Prepare" menu forms are complete and saved, the
next step is clicking on the "Install" menu and thereafter "Saving the Configuration."
That is a button on the "Install" menu that generates the second web interface,
the chaperone-ui site.

#### Using the Chaperone UI
The chaperone-ui site is the site used to configure the SDDC installations.
The process is the same as chaperone-admin-ui, wherein the user fills out the
"Prepare" forms and saves them. Thereafter, the "Install" menu provides buttons for
the various tasks that must be done to complete the SDDC install. To perform
the various installations and configurations, Chaperone generally runs Ansible
plays as a result of clicking on one of the Install menu buttons. The plays
configure and deploy the environment, pursuant to the saved "Prepare" values.

## Developer's Guide
### Prerequisites
The assumption Chaperone makes for developers is not something one would propose is
light, but not out of the norm for many. We assume reasonable competence in the
following:

-  VMware technologies
-  [Google Repo](https://code.google.com/p/git-repo/)
-  [git](https://git-scm.com/)
-  [gerrit](https://gerrit-review.googlesource.com/Documentation/install-quick.html)
-  [Python](https://www.python.org)
-  [Ansible](http://www.ansible.com)

### Contributing
The Chaperone team welcomes contributions from the community. 

Submit issues and PRs through github.

If you wish to contribute code and you have not signed our contributor license agreement
(CLA), our bot will update the issue when you open a 
[Pull Request](https://help.github.com/articles/creating-a-pull-request). 
For any questions about the CLA process, please refer to our [FAQ](https://cla.vmware.com/faq).

### Getting the code
[Instructions to setup](docs/setup.md), install and deploy the Chaperone UI
tools and underlying Ansible plays, Python modules and other required code
bases are [here](docs/setup.md)

### Structure and Standards
*TODO*

### Development Workflow

#### General public enhancements or fixes on individual code repositories 

##### Use case:
You've found bug found in a single role or playbook, you would like to submit a fix,
and you don't have push privileges to the original repository.

##### the steps
1. Use an existing Chaperone base or run a typical `repo init` as described
   in the [setup docs](docs/setup.md) to pull original Chaperone sources down
1. fork the original role or playbook repository in Github under your own account
1. add your remote in the source tree (` cd ansible/roles/role-to-fix; git remote add myfork https://github.com/myaccount/myrepo` )
1. make edits in the role/playbook, commit them
1. push your work to your fork: `git push myfork`
1. in github make a Pull Request from your fork to the origin repo

*new contributors will need to fill out the [CLA](https://cla.vmware.com/faq).*


#### Long Running Project

In some cases, we need to do work for customers or for specific projects
that will require long running divergence of the repo manifest.  These manifest changes
are may not intended to be pushed back to origin/master for public consumption, but
must be available to other people working on the same project.

##### Some examples of this use case:

* Isolated environments, where access to public repositories is blocked by firewall
* Team working on a feature not ready or intended for public release

##### the steps

1. Github fork the chaperone manifest repo (https://github.com/vmware/chaperone)
1. clone your fork: `git clone git@github.com:yourname/chaperone.git`
1. edit the manifest as needed to point to internal, forked, or non-standard role/playbook
   repositories
1. `git commit` and `git push` to your fork
1. in a new project directory, checkout the new manifest:
   `repo init https://github.com/yourname/chaperone`
1. make your changes as needed
1. use `repo` as normal to work with your set of repos
1. team members can use your same `repo init` to make changes on the same set of repos


If you later want to push changes back to the upstream master, create PRs back to the origin from your forked repos

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

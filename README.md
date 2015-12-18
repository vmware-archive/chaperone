Chaperone
=========
Chaperone is a DevOps Automation toolkit for deployment and configuration for an
SDDC based Hybrid Cloud Management platform. It is intended  to expedite and
standardize  "typical" deployments and configuration of VMware solutions
including VSphere/vCenter, NSX, VIO, vRA, vRO, vROps, vRLI, vRB.

The toolkit consists of GUI's used to configure and deploy  standard one of
several standard platforms. Desired settings are entered into the GUI, which
runs ansible scripts to configure and deploy the environment, Standard
configuration tools currently include:

- Chaperone for VIO (Open Stack Integration)
- Chaperone for CNA (Cloud Native Application Platform)
- Chaperone for CMP (Hybrid Cloud Management Platform)

##Developer's Guide
###Prerequisites
Assumption is that developers will have minimal competence in:

-  VMware technologies
-  Google Repo
-  git
-  [gerrit](https://gerrit-review.googlesource.com/Documentation/install-quick.html)
-  Python
-  Ansible

Developers will also need credentials to gerrit. *TODO: Add process*

###Getting Started

Instructions download, install and deploy the Chaperone UI tools to configure a
vCenter server environment are [here](docs/setup.md)

###Running Chaperone
Information on initial environments and running the Chaperone tools against the
environment are [here](docs/run.md)

###Structure and Standards
*TODO*

###Development Workflow
*TODO*

# License and Copyright
 
Copyright 2015 VMware, Inc.

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

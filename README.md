Chaperone
=========
Chaperone is an Automation toolkit rooted in DevOps principals for deploying
and configurating a SDDC based Hybrid Cloud Management platform. It is
intended to expedite and standardize  "typical" deployments and configuration
of VMware solutions including VSphere/vCenter, NSX, VIO, vRA, vRO, vROps, vRLI,
vRB and others as the toolkit grows.

It is a work in progress, and always will be such a facility as we add new
functionalities and products to the Chaperone base.

The toolkit consists of web based interfaces used to configure and deploy
standard one of several standard platforms. There are to interfaces with which
users of Chaperone interact:

- chaperone-admin-ui (e.g., http://chaperone-admin-ui.corp.local)
- chaperone-ui (e.g., http://chaperone-ui.corp.local)

The admin UI (chaperone-admin-ui) is an interface that allows one to select
from a list of SDDC features they would like to deploy, and basic ambient
environment information, such as DNS servers, NTP servers, etc. Once entered
into the various "Prepare" menu forms, clicking 'Save' saves the
configuration as a 'codified design.' Basically, that means the information
is saved in a YAML file as a set of 'parameters' or, more commonly Ansible
variables. 

Once the admin ui Prepare menu forms are complete and saved, the next step is
clicking on the Install menu and thereafter "Saving the Configuration." That
is a button on the Install menu that generates the second web interface, the
chaperone-ui site. 

The chaperone-ui site is the site used to configure the SDDC installations.
That process is the same as the admin UI, wherein the user fills out the Prepare
forms and saves them. Thereafter, the Install menu provides buttons for the
various tasks that must be done to complete the SDDC install. To perform
the various installations and configurations, Chaperone generally runs ansible
plays as a resulte of clicking on one of the 'Install' menu buttons. The plays
configure and deploy the environment, pursuant to the saved Prepare values.
Standard configurations we work on currently include:

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

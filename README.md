Chaperone
=========
Chaperone is an Automation toolkit rooted in DevOps principals for deploying
and configuring a Software Defined Data Center (SDDC) based Hybrid Cloud
Management platform. It is intended to expedite and standardize  "typical"
deployments and configuration of VMware solutions including vSphere/vCenter,
NSX, VIO, vRA, vRO, vROps, vRLI, vRB and others as the toolkit grows.

The project is a work in progress, and always will be such a facility as we
add new functionalities and products to the Chaperone base.

The toolkit consists of web based interfaces and (generally) Ansible code called
bu the web interfaces. The plays are used to configure and deploy standard one of
several standard platforms. There are to interfaces with which users of Chaperone
interact:

- chaperone-admin-ui (e.g., 'http://chaperone-admin-ui.corp.local')
- chaperone-ui (e.g., 'http://chaperone-ui.corp.local')

Note the use of internal domains in the URLs above. That is a common scenario in
which developers or users do not have rights to create new domains in their DNS
servers, thus make use of locally defined domains. More on that in the
[setup documentation](docs/setup.md).

There are two web interfaces with which you may interact with Chaperone.
First, the admin UI (chaperone-admin-ui) is an interface that allows one to
select from a list of SDDC features they would like to deploy, and basic
ambient environment information, such as DNS servers, NTP servers, etc. Once
entered into the various "Prepare" menu forms, clicking 'Save' saves the
configuration as a 'codified design.' Basically, that means the information
is saved in a YAML file as a set of parameters or, more commonly Ansible
variables. 

Once the chaperone-admin-ui Prepare menu forms are complete and saved, the
next step is clicking on the Install menu and thereafter "Saving the Configuration."
That is a button on the Install menu that generates the second web interface,
the chaperone-ui site. 

The chaperone-ui site is the site used to configure the SDDC installations.
That process is the same as chaperone-admin-ui, wherein the user fills out the
Prepare forms and saves them. Thereafter, the Install menu provides buttons for
the various tasks that must be done to complete the SDDC install. To perform
the various installations and configurations, Chaperone generally runs Ansible
plays as a result of clicking on one of the Install menu buttons. The plays
configure and deploy the environment, pursuant to the saved Prepare values.
Standard configurations we work on currently include:

- Chaperone for VIO (Open Stack Integration)
- Chaperone for CNA (Cloud Native Application Platform)
- Chaperone for CMP (Hybrid Cloud Management Platform)

##Developer's Guide
###Prerequisites
The assumption Chaperone makes for developers is not something one would propose is
light, but not out of the norm for many. We assume reasonable competence in the
following:

-  VMware technologies
-  [Google Repo](https://code.google.com/p/git-repo/)
-  git
-  [gerrit](https://gerrit-review.googlesource.com/Documentation/install-quick.html)
-  Python
-  [Ansible](http://www.ansible.com)

###Contributing
Committers (those with rights to merge code) will also need credentials to our Gerrit
server. For the time being, this is an internal process at VMware as all committers
are currently at VMware.

With that said, the Chaperone team welcomes contributions from the community.
If you wish to contribute code, we require that you first sign our
[Contributor License Agreement](https://vmware.github.io/photon/assets/files/vmware_cla.pdf)
and return a copy to [osscontributions@vmware.com](mailto:osscontributions@vmware.com)
before you submit a [Pull Request](https://help.github.com/articles/creating-a-pull-request)
for review and potential merge into the code base.

###Getting the code
[Instructions to download](docs/setup.md), install and deploy the Chaperone UI
tools and underlying Ansible plays, Python modules and other required code
bases are [here](docs/setup.md)

###Running Chaperone
[Information on initial environments and running](docs/run.md) the Chaperone tools against
an appropriate SDDC environment are [here](docs/run.md)

###Structure and Standards
*TODO* - coming soon . . .

###Development Workflow
*TODO* - coming soon. . .

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

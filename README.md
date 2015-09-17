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

###Running Confuence
TODO Add link to run.md

###Structure and Standards
*TODO Add README describing the components of the code, what standards to adhere to, etc*

###Development Workflow
*TODO Add README to descrbe standards on how to start and commit a change*

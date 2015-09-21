Running Chaperone
=================
Once one or more of the Chaperone package tools has been [deployed](setup.md)
to a Chaperone Deployment Server, a vCenter Server environment will be needed
for the Chaperone tool to configure.

##Setting up the vCenter Server Environment
The Chaperone tools require some initial setup in the vCenter server
environment. While the state of the setup may vary, for a development
environment the typical configuration is:

- A router that is exposed on an external ip address *artifact of nested environment
- A set of ESXi hosts
- A vCenter server and vSphere application managing the ESXi hosts
- An internal network to which all VM are connected
- A Windows Control Center acting as the primary DNS *artifact of nested environment

Note: The Chaperone playbooks progressively set up and configure the vCenter
server environment. In some instances when later stage playbooks are to be
developed, it may be more efficient to use a vCenter developer environment that
is more fully configured.

###Connectivity for Chaperone-UI
For a development environment, there are two deployment configurations (see [Environments](env.md)).

If the Chaperone Deployment Server is external to the vCenter Server
environment, the vCenter server https port must be exposed externally through
the router.
TODO: are there other ports/VM's that need to be exposed?

If the CDS is deployed within the vCenter Server environment, the ssh port of
Chaperone Deployment Server must be exposed through the router.

###Running Chaperone
The Chaperone UI exposes Prepare and Install sections. The Prepare section
accepts configurations to be used in configuring the Data Center. This may be
populated manually or can be preloaded (TODO: describe process)

The Install section exposes scripts that will actually set up the Data Center
using the configurations in the Prepare section.

Some of components install steps are prerequisites for later installs, so the
initial order in which the scripts are run is important:

Data Center Deploy
NSX Deploy
TODO: Add others







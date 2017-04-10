Running Chaperone
=================
Chaperone, as a general tool, can be used to automate most any process. With
that said, though, the tools currently taint their view a bit towards a
VMware setup where a vCenter Server is available. Therefore we have a number
of examples that might make the tools seem purely VMware, but do not let the
samples fool -- it is a general purpose tool set as you will see when setting
up UI forms and getting those to call on various processes.

With the 'taint' noted above, once one or more of the Chaperone package tools
has been [deployed](setup.md) to a Chaperone Deployment Server, a vCenter
Server environment will be needed for the Chaperone tool to configure.

## Setting up a management environment: vCenter Servers
When dealing with a SDDC utilizing VMware products, Chaperone requires some
initial setup in a vCenter server environment. While the state of the setup may
vary, for a development environment the typical configuration is:

- A router that is exposed on an external IP address of the (possibly nested ESXi) environment;
- A set of ESXi hosts;
- A vCenter server and vSphere application managing the ESXi hosts;
- An internal network to which all VM are connected;
- A validly operating primary DNS server within the (nested) environment that can serve up the local (e.g., corp.local) names.

Note: The Chaperone playbooks progressively set up and configure the vCenter
server environment. In some instances when later stage playbooks are to be
developed, it may be more efficient to use a vCenter developer environment that
is more fully configured.

### Connectivity for Chaperone-UI
For a development environment, there are two deployment configurations (see [Environments](env.md)).

If the Chaperone Deployment Server is external to the vCenter Server
environment, the vCenter server https port must be exposed externally through
the any intermediary firewalls. It may also be useful to have a 'jump' server
(VM) alongside the CDS so that you can start the vCenter web client as necessary
to review vCenter. Such a jump server would use the DNS server above as its
primary name server, thus would know any local domains (e.g., corp.local).

If the CDS is deployed within the vCenter Server environment, a SSH port for
the Chaperone Deployment Server must also be exposed through the router.

### Running Chaperone
The Chaperone UI exposes (via a left-hand side menu system) 'Prepare' and
'Install' sections. The 'Prepare' section presents forms that accept configurations
to be used in configuring the Data Center. This may be populated manually, or
or the population can be preloaded by using an answerfile. (This is an advanced
topic for which documentation is forthcoming).

The 'Install' section exposes scripts that will actually set up the Data Center
using the configurations in the Prepare section.

Some of components install steps are prerequisites for later installs, so the
initial order in which the scripts are run is important, for example:

1. Deploy vCenter Servers
1. Perform logical build (generate Datacenter, clusters, vDS/Portgroups, add ESXi hosts, etc.)
1. Data Center Deploy
1. Deploy NSX
1. Deploy vRLI
1. Deploy vROps
1. Deploy VIO
1. etc.

To be sure, the operations available are quite flexible, and tuning Chaperone
to a particular scenario is both encouraged and well supported given the
entirety of the Prepare and Install menus are defined by YAML files. The
project that implements the web interfaces and thus interprets and renders the
YAML markup is [chaperone-ui](https://github.com/vmware/chaperone-ui.git).


### Web Based User Interfaces

There are two interfaces with which users of Chaperone
interact:

- chaperone-admin-ui (e.g., 'http://chaperone-admin-ui.corp.local')
- chaperone-ui (e.g., 'http://chaperone-ui.corp.local')

*Note the use of internal domains in the URLs above. This is common where
developers or users do not have rights to create new domains in their DNS
servers, and thus make use of locally defined domains. More on that in the
[setup documentation](setup.md).*

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

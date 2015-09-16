Chaperone Setup
============== 

Development and deployment of Chaperone tools require two [Ubuntu Linux 64-bit](http://www.ubuntu.com/download/server) instances:

- **Development Environment (DE)** is the environment where the source code is downloaded, modified and built. 
- **Chaperone Deployment Server (CDS)** is the build target for the development environment. 

###Note on environments
To simply build and deploy the Chaperone GUI(s), any Ubuntu 64-bit instance is sufficient. However, in order to run the Chaperone and to set up the vCenter environment, the CDS must have access to, or be installed within, the vCenter Server environment. Additional information on deployment options and vCenter Server requirements is availabe [here](README.env.md)

Getting Started
---------------

## Setting up the Chaperone Deployment Server
###Assumptions
- User has downloaded and installed a Ubuntu Linux 64-bit server.

###Install a vmware user 
    sudo adduser vmware
### Get the IP address of the CDS:
If the CDS is running in the same environment as the DE, simply get the ip address:

    ip address

If the CDS is running in a vCenter environment and the DE is not, the CDS will need to be exposed through an external ip (TODO: link to this). 

## Setting up the Development Environment

###Assumptions
- User has an account on the Charerone gerrit project
- User has downloaded and installed a Ubuntu Linux 64-bit server.

###Install a vmware user 
    sudo adduser vmware

### Setup For Gerrit Access
Install [google repo](https://source.android.com/source/downloading.html) in the development environment

*Begin to be removed when gerrit is no longer local:*

Add the following to /etc/hosts file:

    IP-ADDR-OF-GERRIT-SERVER gerrit.cloudbuilders.vmware.local
    
where IP-ADDR-OF-GERRIT-SERVER is the current ip address of the gerrit server documented [here](https://wiki.eng.vmware.com/PSO/MSI_CloudBuilders/SuperVIO) 

*End to be removed when gerrit is no longer local:*


On your development host, your ~/.ssh/config file should have
something similar to the following so you can more easily access
Gerrit:


    Host *
    StrictHostKeyChecking no
    UserKnownHostsFile=/dev/null

    Host gerrit.cloudbuilders.vmware.local
    Hostname gerrit.cloudbuilders.vmware.local
    User MYUSERID
    IdentityFile ~/.ssh/cloudbuilders/id_rsa
    Port 29418


Change the "MYUSERID" to your own gerrit userid and make sure the
~/.ssh/cloudbuilders/id_rsa contains your private key, the public key of
which you registered with the Gerrit server.

### Pull the Chaperone Code
Once Gerrit access is working, you can pull the code base on to your
development host:

    mkdir workspace
    cd workspace
    repo init -u http://gerrit.cloudbuilders.vmware.local:8080/supervio -b master -g supervio
    repo sync

### Setup the DE using any VM

For a non-X11 based, pure terminal VM with vim installed:

    cd ansible/playbooks/ansible
    ansible-playbook --ask-sudo-pass -i inventory ansible.yml

For a setup with LXDE (X11) and the Geany editor:

    cd ansible/playbooks/ansible
    ansible-playbook --ask-sudo-pass -i inventory ansible-lxde.yml

### Setup the DE /etc/hosts with the CVM IP address
For each Chaperone tool to be deployed, add an line in the DE /etc/hosts file with the following

    CVM_IP_ADDRESS supervio-ui.corp.local
    CVM_IP_ADDRESS supersddc-ui.corp.local
    CVM_IP_ADDRESS supercna-ui.corp.local

where CVM_IP_ADDRESS is the actual dotted quad address of the CVM. Note: All three applications may run on the same CVM.

If the CDS is exposed on a port other the 22, add the port to the inventory file the the playbook project that will be built:

Ex. :~/work/ansible/playbooks/supervio-ui/inventory becomes

    [supervio-ui]
    supervio-ui.corp.local:8422

#### Special Note about Domains:

The default domain name for most things Chaperone is "vmware.local" for
development VMs or containers. However, at times (arguably often) work
will occur on remote vCenter server environments, which generally use a other domain names (such as 
"corp.local").

Given that note, take care to understand the actual domain name the DNS
server you use uses in the event it is providing names, for example,
as supervio-ui.corp.local.

There are variables in some of the playbooks, and inventory files, that
require care and attention if the target environment's domain is different from the default.


## Deploy the CVM guis and tools
To setup the Chaperone UI on the CVM, run one or more of the the UI-generating playbooks
from the DE. The playbooks install and configure the CVM automatically
with commands similar to the following:

    # be on the DE as vmware
    # builds chaperone vio application
    cd ~/workspace/ansible/playbooks/supervio-ui
    # be sure to update the inventory and /etc/hosts files to
    # the right network adress of the supervio-ui deploy
    ansible-playbook --ask-pass --ask-sudo-pass -i inventory base.yml
    ansible-playbook -i inventory ui.yml

    # builds chaperone sddc application
    cd ~/workspace/ansible/playbooks/supervio-ui
    # be sure to update the inventory and /etc/hosts files to
    # the right network adress of the supersddc-ui deploy
    ansible-playbook --ask-pass --ask-sudo-pass -i inventory base.yml
    ansible-playbook -i inventory ui.yml

    # builds chaperone cna application
    cd ~/workspace/ansible/playbooks/supercna-ui
    # be sure to update the inventory and /etc/hosts files to
    # the right network adress of the supercna-ui deploy
    ansible-playbook --ask-pass --ask-sudo-pass -i inventory base.yml
    ansible-playbook -i inventory ui.yml


## Configure and deploy
Each Chaperone tool is accessed through a descriptive DNS name in the format "super(XXX)-ui.corp.local" where XXX is vio, sddc or cna to denote the tool. Entries for each tool deployed need to either be added to the /etc/hosts or in the dns table of the system running the browser that accesses the application.

Open a browser to http://super(XXX)-ui.corp.local, and you should see the gui.
Fill in the gui with environment specific data, and 'save' will write the answers.yml.

Alternatively, you can create an answers.yml via some other process.

Either run the deploy via the gui, or ssh into the SVM, and run
manually from /opt/super(XXX)-ansible/

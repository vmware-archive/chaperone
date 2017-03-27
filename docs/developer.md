# Developer's Guide
## Prerequisites
The assumption Chaperone makes for developers is not something one would propose is
light, but not out of the norm for many. We assume reasonable competence in the
following:

-  VMware technologies
-  [Google Repo](https://code.google.com/p/git-repo/)
-  [git](https://git-scm.com/)
-  [gerrit](https://gerrit-review.googlesource.com/Documentation/install-quick.html)
-  [Python](https://www.python.org)
-  [Ansible](http://www.ansible.com)

## Contributing
The Chaperone team welcomes contributions from the community. 

Submit issues and PRs through github.

If you wish to contribute code and you have not signed our contributor license agreement
(CLA), our bot will update the issue when you open a 
[Pull Request](https://help.github.com/articles/creating-a-pull-request). 
For any questions about the CLA process, please refer to our [FAQ](https://cla.vmware.com/faq).

## Getting the code
[Instructions to setup](docs/setup.md), install and deploy the Chaperone UI
tools and underlying Ansible plays, Python modules and other required code
bases are [here](docs/setup.md)

## Structure and Standards
*TODO*

## Development Workflow

### General public enhancements or fixes on individual code repositories 

#### Use case:
You've found bug found in a single role or playbook, you would like to submit a fix,
and you don't have push privileges to the original repository.

#### the steps
1. Use an existing Chaperone base or run a typical `repo init` as described
   in the [setup docs](docs/setup.md) to pull original Chaperone sources down
1. fork the original role or playbook repository in Github under your own account
1. add your remote in the source tree (` cd ansible/roles/role-to-fix; git remote add myfork https://github.com/myaccount/myrepo` )
1. make edits in the role/playbook, commit them
1. push your work to your fork: `git push myfork`
1. in github make a Pull Request from your fork to the origin repo

*new contributors will need to fill out the [CLA](https://cla.vmware.com/faq).*


### Long Running Project

In some cases, we need to do work for customers or for specific projects
that will require long running divergence of the repo manifest.  These manifest changes
are may not intended to be pushed back to origin/master for public consumption, but
must be available to other people working on the same project.

#### Some examples of this use case:

* Isolated environments, where access to public repositories is blocked by firewall
* Team working on a feature not ready or intended for public release

#### the steps

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

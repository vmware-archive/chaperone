#!/bin/sh
set -x

if grep Ubuntu /etc/lsb-release; then
	sudo apt-get update -y
	sudo apt-get upgrade -y
	sudo apt-get install -y curl virt-what git build-essential python python-dev sshpass
	sudo apt-get -y autoremove
	sudo apt-get clean
	sudo apt-get autoclean

	# setup vagrant and ssh keys
	if id -u vagrant; then
		mkdir -p ~vagrant/.ssh
		chmod 700 ~vagrant/.ssh
		curl -Lk 'https://raw.github.com/mitchellh/vagrant/master/keys/vagrant.pub' -o ~vagrant/.ssh/authorized_keys
		chmod 600 ~vagrant/.ssh/authorized_keys
		chown -R vagrant ~vagrant/.ssh
	fi

	getent group admin || sudo groupadd -r admin
	getent passwd vagrant || sudo useradd -m vagrant
	sudo usermod -a -G admin vagrant
	sudo cp /etc/sudoers /etc/sudoers.orig
	sudo sed -i -e '/Defaults\s\+env_reset/a Defaults\texempt_group=admin' /etc/sudoers
	sudo sed -i -e 's/%admin ALL=(ALL) ALL/%admin ALL=NOPASSWD:ALL/g' /etc/sudoers

	getent passwd vmware || sudo useradd -m vmware
	sudo usermod -a -G admin vmware
	echo -e 'VMware1!\nVMware1!' | passwd vmware
fi

# install easy_install on the way to ansible
curl https://bootstrap.pypa.io/ez_setup.py | sudo python
sudo easy_install pip
sudo pip install ansible

# install repo
curl https://storage.googleapis.com/git-repo-downloads/repo > /tmp/repo
sudo mv /tmp/repo /bin/repo
sudo chmod a+x /bin/repo

[ -d /opt/chaperone ] || sudo mkdir -p /opt/chaperone
sudo chown root:vagrant /opt/chaperone
sudo chmod 775 /opt/chaperone
cd /opt/chaperone
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
repo init -u https://github.com/vmware/chaperone -b master -g chaperone
repo sync

cd /opt/chaperone/ansible/playbooks/ansible
ansible-playbook -i inventory ansible.yml
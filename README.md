OMERO server examples
=====================

This repository contains example playbooks for installing OMERO with [Ansible](https://www.ansible.com/).
You can copy these and modify them for your own use.


Quick start
===========

- Install `ansible`: e.g. `pip install ansible`
- Install roles: `ansible-galaxy install -r requirements.yml -p roles`
- Install OMERO.server and OMERO.web using one of these playbooks:


Public user
-----------

This recreates the configuration documented under https://www.openmicroscopy.org/site/support/omero/sysadmins/public.html

- `cd public-user; ansible-playbook playbook.yml`


Three nodes
-----------

This is an example of installing PostgreSQL, OMERO.server and OMERO.web on separate nodes.

- `cd three-nodes; ansible-playbook playbook.yml`

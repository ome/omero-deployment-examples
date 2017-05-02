OMERO with Public User
----------------------

This repository recreates the configuration documented under
https://www.openmicroscopy.org/site/support/omero/sysadmins/public.html

Playbooks and the associated requirements.yml files can be used for
creating a basic OMERO configuration with a public user `public`. Most
likely you will want to copy the configuration into your own playbooks.

### Quick start ###

- Install `ansible` and `ansible-galaxy`: e.g. `pip install ansible ansible-galaxy`
- Install roles: `ansible-galaxy install -r requirements.yml -p roles`
- Install OMERO server and setup public user: `ansible-playbook playbook.yml`

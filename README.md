OMERO server examples
=====================

This repository contains example playbooks for installing OMERO with [Ansible](https://www.ansible.com/).
You can copy these and modify them for your own use.


Quick start
===========

- Install Ansible: e.g. `pip install ansible>=2.6.16,<2.7`. Other versions of Ansible may work but are not routinely tested by us.
- Install OMERO.server and OMERO.web using one of these playbooks:


Basics
------

    cd ansible-example-omero-onenode
    ansible-galaxy install -r requirements.yml
    ansible-playbook playbook.yml

<img src="images/one-node.png" alt="One-node OMERO" width="40%" align="left"/>

The above diagram represents the most basic OMERO installation with OMERO.web, OMERO.server, and
PostgreSQL all installed on the same physical node. This repository includes ansible and docker
installation blueprints for this configuration as well as more advanced ones:

 * [Public user](#public-user): allow public access to selected data without the need to log in
 * [Three nodes](#three-nodes): use more physical or virtual hardware to scale up your installation

Public user
-----------

This recreates the configuration documented under https://docs.openmicroscopy.org/latest/omero/sysadmins/public.html


    cd ansible-role-omero-public-user
    ansible-galaxy install -r requirements.yml
    ansible-playbook playbook.yml

<img src="images/public-user.png" alt="OMERO with public user" width="40%" align="left"/>

Three nodes
-----------

This is an example of installing PostgreSQL, OMERO.server and OMERO.web on separate nodes.

    cd ansible-role-omero-three-nodes
    ansible-galaxy install -r requirements.yml
    ansible-playbook playbook.yml

Alternatively, use docker-compose to run a similar configuration in Docker:

    cd docker-example-omero
    docker-compose up

<img src="images/three-nodes.png" alt="Three-nodes OMERO" width="40%" align="left"/>

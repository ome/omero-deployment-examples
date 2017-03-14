### ansible playbooks & requirements for installing basic OMERO + public web

- playbooks set up to run from localhost rather than remotely

- after installing ansible and ansible-galaxy,
    ansible-galaxy install -r requirements.yml -p roles

- install OMERO server
    ansible-playbook neubias-basic-omero-install.yml

- set up Public web user
    ansible-playbook neubias-omero-publicweb.yml

import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('omero-server')

OMERO = '/opt/omero/server/OMERO.server/bin/omero'


def test_services_running_and_enabled(host):
    service = host.service('omero-server')
    assert service.is_running
    assert service.is_enabled


def test_postgres_not_installed(host):
    service = host.service('postgresql-9.6')
    assert not service.is_running
    assert not service.is_enabled


def test_omero_login(host):
    with host.sudo('omero-server'):
        host.check_output(
            '%s login -C -s localhost -u root -w omero' % OMERO)

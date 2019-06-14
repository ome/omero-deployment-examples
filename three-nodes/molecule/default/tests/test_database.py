import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('omero-database')


def test_services_running_and_enabled(host):
    service = host.service('postgresql-9.6')
    assert service.is_running
    assert service.is_enabled

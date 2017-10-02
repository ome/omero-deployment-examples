import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('omero-database')


def test_services_running_and_enabled(Service):
    service = Service('postgresql-9.6')
    assert service.is_running
    assert service.is_enabled

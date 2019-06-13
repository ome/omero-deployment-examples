import json
import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


OMERO = '/opt/omero/server/OMERO.server/bin/omero'


def test_omero_web_public(host):
    out = host.check_output(
        'curl -f http://localhost/webclient/api/containers/')
    r = json.loads(out)
    assert r['screens'] == []
    assert r['plates'] == []
    assert r['projects'] == []
    assert r['datasets'] == []

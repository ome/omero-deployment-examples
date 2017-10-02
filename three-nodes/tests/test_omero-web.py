import testinfra.utils.ansible_runner
import pytest
from time import sleep

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('omero-web')


@pytest.mark.parametrize('name', ['omero-web', 'nginx'])
def test_services_running_and_enabled(Service, name):
    service = Service(name)
    assert service.is_running
    assert service.is_enabled


def test_omero_web_first_page(Command):
    out = Command.check_output('curl -fsL http://localhost/')
    assert 'omero:4064' in out


def get_cookie(cookietxt, name):
    for line in cookietxt.splitlines():
        tokens = line.split()
        try:
            if tokens[5] == name:
                return tokens[6]
        except IndexError:
            pass


# https://github.com/openmicroscopy/omero-grid-docker/blob/0.1.0/test_login.sh
def test_omero_web_login(Command, File):
    LOGIN_URL = 'http://localhost/webclient/login/'
    CURL = 'curl -f -i -k -s -c cookies.txt -b cookies.txt -e %s' % LOGIN_URL

    for i in xrange(60):
        sleep(2)
        Command.check_output('%s %s' % (CURL, LOGIN_URL))
        csrf = get_cookie(File('cookies.txt').content_string, 'csrftoken')
        if csrf:
            break
    assert csrf

    data = '&'.join([
        'csrfmiddlewaretoken=%s' % csrf,
        'username=root',
        'password=omero',
        'server=1',
        'url=%2Fwebclient%2F',
        ])

    for i in xrange(60):
        sleep(2)
        Command.check_output('%s -d "%s" -X POST %s' % (
            CURL, data, LOGIN_URL))
        sessionid = get_cookie(
            File('cookies.txt').content_string, 'sessionid')
        if sessionid:
            break
    assert sessionid

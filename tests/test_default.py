import testinfra.utils.ansible_runner
import pytest


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


@pytest.fixture()
def config_file():
    config_f = '/usr/local/kafka-manager/application.conf'
    return config_f


def test_kafka_manager_config_state(File, config_file):
    c_file = File(config_file)
    assert c_file.exists
    assert c_file.is_file
    assert c_file.mode == 436


def test_kafka_manager_service(Service):
    ntp_daemon = "kafka-manager"
    s = Service(ntp_daemon)
    assert s.is_running
    assert s.is_enabled


def test_kafka_manager_systemd(File):
    c_file = File('/etc/systemd/system/kafka-manager.service')
    assert c_file.contains('/usr/local/kafka-manager/bin/kafka-manager')


@pytest.mark.parametrize("teststring", [
    ("basicAuthentication.enabled=false"),
    ('kafka-manager.zkhosts="127.0.0.1:2181"'),
    ('application.features=\[' +
     '"KMClusterManagerFeature","KMTopicManagerFeature' +
     '","KMPreferredReplicaElectionFeature","KMReassignPartitionsFeature"\]'),
    ('basicAuthentication.username="admin"'),
    ('basicAuthentication.password="password"'),
    ('play\.crypto.secret="/HeV^GoZV00N=ov8`IRL3:iTDX3\[WNgS1hMMPl/3Y0' +
     '\[qfKCncDspHaNSYNyoB3XA"')
])
def test_kafka_manager_config_sources(File, config_file, teststring):
    c_file = File(config_file)
    assert c_file.contains(teststring)


def test_kafka_manager_listener(Command):
    listener = Command("netstat -ant")
    assert '8080' in listener.stdout

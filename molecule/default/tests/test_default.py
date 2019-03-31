import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_repositories(host):
    odoo_repository = host.file(
        '/etc/apt/sources.list.d/nightly_odoo_com_11_0_nightly_deb.list')
    assert odoo_repository.exists

    ruby_repository = host.file(
        '/etc/apt/sources.list.d/ppa_brightbox_ruby_ng_xenial.list')
    assert ruby_repository.exists


def test_packages(host):
    odoo = host.package("odoo")
    assert odoo.is_installed
    assert odoo.version.startswith("11")


def test_services(host):
    odoo = host.service("odoo")
    assert odoo.is_running
    assert odoo.is_enabled


def test_log(host):
    odoo_log = host.file('/var/log/odoo/odoo-server.log')
    assert odoo_log.exists
    assert not odoo_log.contains('ERROR')

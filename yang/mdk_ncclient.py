from ncclient import manager
from pyangbind.lib.serialise import pybindIETFXMLEncoder
from lxml import etree
from huawei_ifm import *
from utils import *

def connect(ip, user, password):
    netconf_conn = manager.connect(host = ip, username = user,password = password,port = 830,hostkey_verify = False)
    return netconf_conn

def modify_yang_obj():
    huawei_ifm_obj = huawei_ifm()
    interface_obj = huawei_ifm_obj.ifm.interfaces.interface.add("GigabitEthernet 3/0/1")
    addr_obj = interface_obj.ipv4.addresses.address.add("192.0.0.1")
    addr_obj.mask = "255.255.255.255"
    addr_obj.type = "main"
    return pybindIETFXMLEncoder.serialise(huawei_ifm_obj.ifm)

def add_configNode(xml):
    configNode = etree.Element("config", nsmap={None: "urn:ietf:params:xml:ns:netconf:base:1.0"})
    root = etree.fromstring(xml)
    xpath = "/a:ifm/a:interfaces/a:interface[a:name='GigabitEthernet 3/0/1']"
    ns = {'a': 'urn:huawei:yang:huawei-ifm'}
    operation = 'create'
    root = add_netconf_operation(root, xpath, ns, operation)
    configNode.append(root)
    return etree.tostring(configNode, pretty_print=True).decode("utf8")

def get_config():
    huawei_ifm_obj = huawei_ifm()
    interface_obj = huawei_ifm_obj.ifm.interfaces.interface.add("GigabitEthernet 3/0/1")
    xml = pybindIETFXMLEncoder.serialise(huawei_ifm_obj.ifm)
    root = etree.fromstring(xml)
    configNode = etree.Element("filter", nsmap={None: "urn:ietf:params:xml:ns:netconf:base:1.0"})
    configNode.append(root)
    return etree.tostring(configNode, pretty_print=True).decode("utf8")

if __name__ == '__main__':
    ip = "localhost"
    user = "netconf"
    password = "netconf"
    netconf_conn = connect(ip, user, password)
    #xml = modify_yang_obj()
    #configNode = add_configNode(xml)
    #print(configNode)
    #res = netconf_conn.edit_config(target='running',config=configNode)
    res = netconf_conn.get_config(source='running',filter=get_config())
    print(res)

from utils import *
# note:Each time a yang binding file is added, you need to add import.Pay attention to "_" not "-"
from huawei_ifm import *

# this is function that ncclient connection
def connect(ip, user, password):
    netconf_conn = manager.connect(host = ip, username = user,password = password,port = 830,hostkey_verify = False)
    return netconf_conn

# this is function that modify edit-config packets.add interface,set ip address,mask and type
def modify_yang_obj():
    huawei_ifm_obj = huawei_ifm()
    interface_obj = huawei_ifm_obj.ifm.interfaces.interface.add("GigabitEthernet 3/0/1")
    addr_obj = interface_obj.ipv4.addresses.address.add("192.0.0.1")
    addr_obj.mask = "255.255.255.255"
    addr_obj.type = "main"
    return pybindIETFXMLEncoder.serialise(huawei_ifm_obj.ifm)

# this is function that add configNode.Serialize an object into a NETCONF packet and add Operation Attributes to Specified XML Nodes
def add_configNode(xml):
    configNode = etree.Element("config", nsmap={None: "urn:ietf:params:xml:ns:netconf:base:1.0"})
    root = etree.fromstring(xml)
    xpath = "/a:ifm/a:interfaces/a:interface[a:name='GigabitEthernet 3/0/1']"
    ns = {'a': 'urn:huawei:yang:huawei-ifm'}
    operation = 'create'
    root = add_netconf_operation(root, xpath, ns, operation)
    configNode.append(root)
    return etree.tostring(configNode, pretty_print=True).decode("utf8")

# this function that get_config.Serialize an object into a NETCONF packet and add filter to XML Nodes
def get_config():
    huawei_ifm_obj = huawei_ifm()
    interface_obj = huawei_ifm_obj.ifm.interfaces.interface.add("GigabitEthernet 3/0/1")
    xml = pybindIETFXMLEncoder.serialise(huawei_ifm_obj.ifm)
    root = etree.fromstring(xml)
    configNode = etree.Element("filter", nsmap={None: "urn:ietf:params:xml:ns:netconf:base:1.0"})
    configNode.append(root)
    return etree.tostring(configNode, pretty_print=True).decode("utf8")

if __name__ == '__main__':

  #------------------------set ncclent connection --------------------
  ip = "localhost"
  user = "netconf"
  password = "netconf"
  netconf_conn = connect(ip, user, password)

  #------------------------exit_config-------------------------------
  #xml = modify_yang_obj()
  #configNode = add_configNode(xml)
  #print(configNode)
  #res = netconf_conn.edit_config(target='running', config=configNode)

  #------------------------get_config-------------------------------
  res = netconf_conn.get_config(source='running', filter=get_config())

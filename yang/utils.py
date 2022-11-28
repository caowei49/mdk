from lxml import etree
from lxml.etree import QName
from ncclient import manager
from pyangbind.lib.serialise import pybindIETFXMLEncoder, pybindIETFXMLDecoder


class XMLNamespaces:
  xc = 'urn:ietf:params:xml:ns:netconf:base:1.0'

def connect(ip, user, password):
  netconf_conn = manager.connect(host=ip, username=user, password=password, port=830, hostkey_verify=False)
  return netconf_conn

def add_netconf_operation(root, xpath, ns, operation):
  target_node = root.xpath(xpath, namespaces=ns)[0]
  target_node.attrib[QName(XMLNamespaces.xc, 'operation')] = operation
  return root

def netconf_edit(python_obj, ip, user, password, xpath=None, ns=None, operation=None):
  xml = pybindIETFXMLEncoder.serialise(python_obj)
  configNode = etree.Element("config", nsmap={None: "urn:ietf:params:xml:ns:netconf:base:1.0"})
  root = etree.fromstring(xml)
  if xpath is not None and ns is not None and operation is not None:
    root = add_netconf_operation(root, xpath, ns, operation)
  configNode.append(root)
  edit_xml = etree.tostring(configNode, pretty_print=True).decode("utf8")
  print(edit_xml)
  netconf_conn = connect(ip, user, password)
  res = netconf_conn.edit_config(target='running', config=edit_xml)
  return res

def netconf_get(python_obj, ip, user, password, binding, entrance_name):
  xml = pybindIETFXMLEncoder.serialise(python_obj)
  root = etree.fromstring(xml)
  configNode = etree.Element("filter", nsmap={None: "urn:ietf:params:xml:ns:netconf:base:1.0"})
  configNode.append(root)
  get_xml = etree.tostring(configNode, pretty_print=True).decode("utf8")
  netconf_conn = connect(ip, user, password)
  res = netconf_conn.get_config(source='running', filter=get_xml)
  rpc_reply = etree.fromstring(str(res))
  ns = {"nc": "urn:ietf:params:xml:ns:netconf:base:1.0"}
  path = "/nc:rpc-reply/nc:data"
  data = rpc_reply.xpath(path, namespaces=ns)
  py_obj = pybindIETFXMLDecoder.decode(etree.tostring(data[0]), binding, entrance_name)
  return py_obj

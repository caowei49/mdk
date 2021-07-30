from lxml.etree import QName


class XMLNamespaces:
  xc = 'urn:ietf:params:xml:ns:netconf:base:1.0'


def add_netconf_operation(root, xpath, ns, operation):
  target_node = root.xpath(xpath, namespaces=ns)[0]
  target_node.attrib[QName(XMLNamespaces.xc, 'operation')] = operation
  return root

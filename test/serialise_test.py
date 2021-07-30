from lxml import etree

from pyangbind.lib.serialise import pybindIETFXMLEncoder,pybindIETFXMLDecoder
from test.yang_bindings import ietf_interfaces_binding
import pyangbind.lib.pybindJSON as pybindJSON
from test.yang_bindings.huawei_ifm_binding import *
from test.utils import *

from test.yang_bindings.ietf_interfaces_binding import ietf_interfaces


def modify_yang_obj():
    hw_ifm_obj = huawei_ifm()
    instance1_obj = hw_ifm_obj.ifm.interfaces.interface.add("test1")
    address1_obj = instance1_obj.ipv4.addresses.address.add("192.0.0.1")
    address1_obj.mask = "255.255.255.255"
    address1_obj.type = "main"
    instance2_obj = hw_ifm_obj.ifm.interfaces.interface.add("test2")
    address2_obj = instance2_obj.ipv4.addresses.address.add("192.0.0.2")
    address2_obj.mask = "255.255.255.255"
    address2_obj.type = "main"
    address3_obj = instance2_obj.ipv4.addresses.address.add("192.0.0.3")
    address3_obj.mask = "255.255.255.255"

    return hw_ifm_obj.ifm

ietf_interfaces_xml = """
<config>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
      <interface>
          <name>GigabitEthernet 3/0/1</name>
          <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
          <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
             <address>
                <ip>192.0.1.1</ip>
                <prefix-length>32</prefix-length>
             </address>
          </ipv4>
       </interface>
       <interface>
          <name>GigabitEthernet 3/0/2</name>
          <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
          <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
             <address>
                <ip>192.0.2.1</ip>
                <prefix-length>28</prefix-length>
             </address>
          </ipv4>
          <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
             <address>
                <ip>192.0.2.2</ip>
                <prefix-length>24</prefix-length>
             </address>
          </ipv4>
       </interface>
    </interfaces>
</config>
"""

def test_deserialise_xml():
    res = pybindIETFXMLDecoder.decode(ietf_interfaces_xml, ietf_interfaces_binding, "ietf_interfaces")
    print(res)

def test_serialise_python_obj(py_obj):
    xml = pybindIETFXMLEncoder.serialise(py_obj)
    # add operation in xml
    xpath = '/a:ifm/a:interfaces/a:interface[a:name="test1"]'
    ns = {'a': 'urn:huawei:yang:huawei-ifm', 'xc': 'urn:ietf:params:xml:ns:netconf:base:1.0'}
    operation = 'merge'
    root = add_operation(xml, xpath, ns, operation)
    return root

def add_operation(xml, xpath, ns, operation):
  root = etree.fromstring(xml)
  add_netconf_operation(root, xpath, ns, operation)
  return etree.tostring(root, pretty_print=True).decode()

if __name__ == "__main__":
    # yangobj = test_decoder_yang_obj()
    # translated_obj = _translate_ietf_interfaces_obj._translate__ietf_interfaces(yangobj)
    py_obj = modify_yang_obj()
    xml = test_serialise_python_obj(py_obj)
    print(xml)
    # test_deserialise_xml()

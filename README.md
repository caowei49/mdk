# **MDK-huawei-gen**

## **Overview**

**PyangBind** is a plugin for [Pyang][pyang] that generates a Python class hierarchy from a YANG data model. The resulting classes can be directly interacted with in Python. Particularly, **PyangBind** will allow you to:

 * Create new data instances - through setting values in the Python class hierarchy.
 * Load data instances from external sources - taking input data from an external source and allowing it to be addressed through the Python classes.
 * Serialise populated objects into formats that can be stored, or sent to another system (e.g., a network element).

Development of **PyangBind** has been motivated by consuming the  [OpenConfig][openconfig] data models; and is intended to be well-tested against these models. The Python classes generated, and serialisation methods are intended to provide network operators with a starting point for loading data instances from network elements, manipulating them, and sending them to a network device. **PyangBind** classes also have functionality which allows additional methods to be associated with the classes, such that it can be used for the foundation of a NMS.

## **Installation**
### **Prerequisites**

OS: Ubuntu, CentOS, Suse  
Python: 3.7  
Required Python package:pyang,bitarray,lxml,regex,six,enum34,ncclient,pyangbind

### Build From Source  

1.Clone the mdk repository:
 ```
 git clone https://github.com/HuaweiDatacomm/mdk.git
 ```
2.Install required Python package:
```
 pip3 install pyangbind
 pip3 install ncclient
 pip3 install -r requirments.txt
 python3 setup.py install
 pip3 list
```

## Getting Used

### use Yang model generation python class:
To generate your first set of classes, you will need a YANG module, and its dependencies. A number of simple modules can be found in the tests directory (e.g., tests/base-test.yang).
To generate a set of Python classes, Pyang needs to be provided a pointer to where PyangBind's plugin is installed. This location can be found by running:

```
$ export PYBINDPLUGIN=`/usr/bin/env python3 -c \
'import pyangbind; import os; print ("{}/plugin".format(os.path.dirname(pyangbind.__file__)))'`
$ echo $PYBINDPLUGIN
```
Once this path is known, it can be provided to the --plugin-dir argument to Pyang. Here is an example of huawei-ifm.yang:
```
$ pyang --plugindir $PYBINDPLUGIN -f pybind -o huawei_ifm.py yang/huawei-ifm.yang
```
Note:if you want to generating Python Classes in batches:(put yang models in dir yang)
```
cd mdk
mkdir python-gen
mkdir translate-gen
cd yang
chmod +x generate_py.sh
./generate_py.sh
```
### generate a Python class for a Yang model with schema-mount.
put yang model with schema-mount in dir test-ietf.	--schema-mount: sm2_correct.json (schema mount configuration file)

```
cd mdk
mkdir test-ietf
cd test-ietf
$ export PYBINDPLUGIN=`/usr/bin/env python3 -c \
'import pyangbind; import os; print ("{}/plugin".format(os.path.dirname(pyangbind.__file__)))'`
$ pyang --plugindir $PYBINDPLUGIN --schema-mount sm2_correct.json -f pybind -o ietf_network_instance.py ietf-network-instance\@2018-03-20.yang ietf-yang-schema-mount\@2019-01-14.yang ietf-interfaces.yang
```

### Operate the Python class to generate NETCONF packets and deliver them to the device.
Here is an example of huawei-ifm.yang.First use Yang models generation python classes(have been told how to use) 

```
cd mdk
cd python-gen
vi mdk_ncclient.py
```

```
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
```





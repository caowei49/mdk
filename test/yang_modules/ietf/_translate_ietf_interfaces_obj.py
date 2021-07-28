
def _translate__interfaces_interface_statistics(input_yang_obj: yc_statistics_ietf_interfaces__interfaces_interface_statistics, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /interfaces/interface/statistics

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.discontinuity_time._changed():
        input_yang_obj.discontinuity_time = input_yang_obj.discontinuity_time
        
    if input_yang_obj.in_octets._changed():
        input_yang_obj.in_octets = input_yang_obj.in_octets
        
    if input_yang_obj.in_unicast_pkts._changed():
        input_yang_obj.in_unicast_pkts = input_yang_obj.in_unicast_pkts
        
    if input_yang_obj.in_broadcast_pkts._changed():
        input_yang_obj.in_broadcast_pkts = input_yang_obj.in_broadcast_pkts
        
    if input_yang_obj.in_multicast_pkts._changed():
        input_yang_obj.in_multicast_pkts = input_yang_obj.in_multicast_pkts
        
    if input_yang_obj.in_discards._changed():
        input_yang_obj.in_discards = input_yang_obj.in_discards
        
    if input_yang_obj.in_errors._changed():
        input_yang_obj.in_errors = input_yang_obj.in_errors
        
    if input_yang_obj.in_unknown_protos._changed():
        input_yang_obj.in_unknown_protos = input_yang_obj.in_unknown_protos
        
    if input_yang_obj.out_octets._changed():
        input_yang_obj.out_octets = input_yang_obj.out_octets
        
    if input_yang_obj.out_unicast_pkts._changed():
        input_yang_obj.out_unicast_pkts = input_yang_obj.out_unicast_pkts
        
    if input_yang_obj.out_broadcast_pkts._changed():
        input_yang_obj.out_broadcast_pkts = input_yang_obj.out_broadcast_pkts
        
    if input_yang_obj.out_multicast_pkts._changed():
        input_yang_obj.out_multicast_pkts = input_yang_obj.out_multicast_pkts
        
    if input_yang_obj.out_discards._changed():
        input_yang_obj.out_discards = input_yang_obj.out_discards
        
    if input_yang_obj.out_errors._changed():
        input_yang_obj.out_errors = input_yang_obj.out_errors
        
    return translated_yang_obj

def _translate__interfaces_interface_ipv4_address(input_yang_obj: yc_address_ietf_interfaces__interfaces_interface_ipv4_address, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /interfaces/interface/ipv4/address

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.prefix_length._changed():
        translated_yang_obj.mask = input_yang_obj.prefix_length
        
    if input_yang_obj.netmask._changed():
        input_yang_obj.netmask = input_yang_obj.netmask
        
    if input_yang_obj.origin._changed():
        input_yang_obj.origin = input_yang_obj.origin
        
    return translated_yang_obj

def _translate__interfaces_interface_ipv4_neighbor(input_yang_obj: yc_neighbor_ietf_interfaces__interfaces_interface_ipv4_neighbor, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /interfaces/interface/ipv4/neighbor

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.link_layer_address._changed():
        input_yang_obj.link_layer_address = input_yang_obj.link_layer_address
        
    if input_yang_obj.origin._changed():
        input_yang_obj.origin = input_yang_obj.origin
        
    return translated_yang_obj

def _translate__interfaces_interface_ipv4(input_yang_obj: yc_ipv4_ietf_interfaces__interfaces_interface_ipv4, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /interfaces/interface/ipv4

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.enabled._changed():
        input_yang_obj.enabled = input_yang_obj.enabled
        
    if input_yang_obj.forwarding._changed():
        input_yang_obj.forwarding = input_yang_obj.forwarding
        
    if input_yang_obj.mtu._changed():
        input_yang_obj.mtu = input_yang_obj.mtu
        
    for k, listInst in input_yang_obj.address.iteritems():
        innerobj = translated_yang_obj.ifm.interfaces.interface.ipv4.addresses.address.add(k)
        _translate__interfaces_interface_ipv4_address(listInst, innerobj)
          
    for k, listInst in input_yang_obj.neighbor.iteritems():
        innerobj = _translate__interfaces_interface_ipv4_neighbor(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__interfaces_interface_ipv6_address(input_yang_obj: yc_address_ietf_interfaces__interfaces_interface_ipv6_address, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /interfaces/interface/ipv6/address

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.prefix_length._changed():
        input_yang_obj.prefix_length = input_yang_obj.prefix_length
        
    if input_yang_obj.origin._changed():
        input_yang_obj.origin = input_yang_obj.origin
        
    if input_yang_obj.status._changed():
        input_yang_obj.status = input_yang_obj.status
        
    return translated_yang_obj

def _translate__interfaces_interface_ipv6_neighbor(input_yang_obj: yc_neighbor_ietf_interfaces__interfaces_interface_ipv6_neighbor, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /interfaces/interface/ipv6/neighbor

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.link_layer_address._changed():
        input_yang_obj.link_layer_address = input_yang_obj.link_layer_address
        
    if input_yang_obj.origin._changed():
        input_yang_obj.origin = input_yang_obj.origin
        
    if input_yang_obj.is_router._changed():
        input_yang_obj.is_router = input_yang_obj.is_router
        
    if input_yang_obj.state._changed():
        input_yang_obj.state = input_yang_obj.state
        
    return translated_yang_obj

def _translate__interfaces_interface_ipv6_autoconf(input_yang_obj: yc_autoconf_ietf_interfaces__interfaces_interface_ipv6_autoconf, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /interfaces/interface/ipv6/autoconf

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.create_global_addresses._changed():
        input_yang_obj.create_global_addresses = input_yang_obj.create_global_addresses
        
    if input_yang_obj.create_temporary_addresses._changed():
        input_yang_obj.create_temporary_addresses = input_yang_obj.create_temporary_addresses
        
    if input_yang_obj.temporary_valid_lifetime._changed():
        input_yang_obj.temporary_valid_lifetime = input_yang_obj.temporary_valid_lifetime
        
    if input_yang_obj.temporary_preferred_lifetime._changed():
        input_yang_obj.temporary_preferred_lifetime = input_yang_obj.temporary_preferred_lifetime
        
    return translated_yang_obj

def _translate__interfaces_interface_ipv6(input_yang_obj: yc_ipv6_ietf_interfaces__interfaces_interface_ipv6, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /interfaces/interface/ipv6

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.enabled._changed():
        input_yang_obj.enabled = input_yang_obj.enabled
        
    if input_yang_obj.forwarding._changed():
        input_yang_obj.forwarding = input_yang_obj.forwarding
        
    if input_yang_obj.mtu._changed():
        input_yang_obj.mtu = input_yang_obj.mtu
        
    for k, listInst in input_yang_obj.address.iteritems():
        innerobj = _translate__interfaces_interface_ipv6_address(listInst, translated_yang_obj)
        
    for k, listInst in input_yang_obj.neighbor.iteritems():
        innerobj = _translate__interfaces_interface_ipv6_neighbor(listInst, translated_yang_obj)
        
    if input_yang_obj.dup_addr_detect_transmits._changed():
        input_yang_obj.dup_addr_detect_transmits = input_yang_obj.dup_addr_detect_transmits
        
    innerobj = _translate__interfaces_interface_ipv6_autoconf(input_yang_obj.autoconf, translated_yang_obj)
        
    return translated_yang_obj

def _translate__interfaces_interface(input_yang_obj: yc_interface_ietf_interfaces__interfaces_interface, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /interfaces/interface

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.description._changed():
        input_yang_obj.description = input_yang_obj.description
        
    if input_yang_obj.type._changed():
        input_yang_obj.type = input_yang_obj.type
        
    if input_yang_obj.enabled._changed():
        input_yang_obj.enabled = input_yang_obj.enabled
        
    if input_yang_obj.link_up_down_trap_enable._changed():
        input_yang_obj.link_up_down_trap_enable = input_yang_obj.link_up_down_trap_enable
        
    if input_yang_obj.admin_status._changed():
        input_yang_obj.admin_status = input_yang_obj.admin_status
        
    if input_yang_obj.oper_status._changed():
        input_yang_obj.oper_status = input_yang_obj.oper_status
        
    if input_yang_obj.last_change._changed():
        input_yang_obj.last_change = input_yang_obj.last_change
        
    if input_yang_obj.if_index._changed():
        input_yang_obj.if_index = input_yang_obj.if_index
        
    if input_yang_obj.phys_address._changed():
        input_yang_obj.phys_address = input_yang_obj.phys_address
        
    if input_yang_obj.higher_layer_if._changed():
        input_yang_obj.higher_layer_if = input_yang_obj.higher_layer_if
        
    if input_yang_obj.lower_layer_if._changed():
        input_yang_obj.lower_layer_if = input_yang_obj.lower_layer_if
        
    if input_yang_obj.speed._changed():
        input_yang_obj.speed = input_yang_obj.speed
        
    innerobj = _translate__interfaces_interface_statistics(input_yang_obj.statistics, translated_yang_obj)
        
    innerobj = _translate__interfaces_interface_ipv4(input_yang_obj.ipv4, translated_yang_obj)
        
    innerobj = _translate__interfaces_interface_ipv6(input_yang_obj.ipv6, translated_yang_obj)
        
    return translated_yang_obj

def _translate__interfaces(input_yang_obj: yc_interfaces_ietf_interfaces__interfaces, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /interfaces

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.interface.iteritems():
        innerobj = translated_yang_obj.ifm.interfaces.interface.add(k)
        _translate__interfaces_interface(listInst, innerobj)
          
    return translated_yang_obj

def _translate__interfaces_state_interface_statistics(input_yang_obj: yc_statistics_ietf_interfaces__interfaces_state_interface_statistics, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /interfaces-state/interface/statistics

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.discontinuity_time._changed():
        input_yang_obj.discontinuity_time = input_yang_obj.discontinuity_time
        
    if input_yang_obj.in_octets._changed():
        input_yang_obj.in_octets = input_yang_obj.in_octets
        
    if input_yang_obj.in_unicast_pkts._changed():
        input_yang_obj.in_unicast_pkts = input_yang_obj.in_unicast_pkts
        
    if input_yang_obj.in_broadcast_pkts._changed():
        input_yang_obj.in_broadcast_pkts = input_yang_obj.in_broadcast_pkts
        
    if input_yang_obj.in_multicast_pkts._changed():
        input_yang_obj.in_multicast_pkts = input_yang_obj.in_multicast_pkts
        
    if input_yang_obj.in_discards._changed():
        input_yang_obj.in_discards = input_yang_obj.in_discards
        
    if input_yang_obj.in_errors._changed():
        input_yang_obj.in_errors = input_yang_obj.in_errors
        
    if input_yang_obj.in_unknown_protos._changed():
        input_yang_obj.in_unknown_protos = input_yang_obj.in_unknown_protos
        
    if input_yang_obj.out_octets._changed():
        input_yang_obj.out_octets = input_yang_obj.out_octets
        
    if input_yang_obj.out_unicast_pkts._changed():
        input_yang_obj.out_unicast_pkts = input_yang_obj.out_unicast_pkts
        
    if input_yang_obj.out_broadcast_pkts._changed():
        input_yang_obj.out_broadcast_pkts = input_yang_obj.out_broadcast_pkts
        
    if input_yang_obj.out_multicast_pkts._changed():
        input_yang_obj.out_multicast_pkts = input_yang_obj.out_multicast_pkts
        
    if input_yang_obj.out_discards._changed():
        input_yang_obj.out_discards = input_yang_obj.out_discards
        
    if input_yang_obj.out_errors._changed():
        input_yang_obj.out_errors = input_yang_obj.out_errors
        
    return translated_yang_obj

def _translate__interfaces_state_interface_ipv4_address(input_yang_obj: yc_address_ietf_interfaces__interfaces_state_interface_ipv4_address, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /interfaces-state/interface/ipv4/address

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.prefix_length._changed():
        input_yang_obj.prefix_length = input_yang_obj.prefix_length
        
    if input_yang_obj.netmask._changed():
        input_yang_obj.netmask = input_yang_obj.netmask
        
    if input_yang_obj.origin._changed():
        input_yang_obj.origin = input_yang_obj.origin
        
    return translated_yang_obj

def _translate__interfaces_state_interface_ipv4_neighbor(input_yang_obj: yc_neighbor_ietf_interfaces__interfaces_state_interface_ipv4_neighbor, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /interfaces-state/interface/ipv4/neighbor

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.link_layer_address._changed():
        input_yang_obj.link_layer_address = input_yang_obj.link_layer_address
        
    if input_yang_obj.origin._changed():
        input_yang_obj.origin = input_yang_obj.origin
        
    return translated_yang_obj

def _translate__interfaces_state_interface_ipv4(input_yang_obj: yc_ipv4_ietf_interfaces__interfaces_state_interface_ipv4, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /interfaces-state/interface/ipv4

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.forwarding._changed():
        input_yang_obj.forwarding = input_yang_obj.forwarding
        
    if input_yang_obj.mtu._changed():
        input_yang_obj.mtu = input_yang_obj.mtu
        
    for k, listInst in input_yang_obj.address.iteritems():
        innerobj = _translate__interfaces_state_interface_ipv4_address(listInst, translated_yang_obj)
        
    for k, listInst in input_yang_obj.neighbor.iteritems():
        innerobj = _translate__interfaces_state_interface_ipv4_neighbor(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__interfaces_state_interface_ipv6_address(input_yang_obj: yc_address_ietf_interfaces__interfaces_state_interface_ipv6_address, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /interfaces-state/interface/ipv6/address

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.prefix_length._changed():
        input_yang_obj.prefix_length = input_yang_obj.prefix_length
        
    if input_yang_obj.origin._changed():
        input_yang_obj.origin = input_yang_obj.origin
        
    if input_yang_obj.status._changed():
        input_yang_obj.status = input_yang_obj.status
        
    return translated_yang_obj

def _translate__interfaces_state_interface_ipv6_neighbor(input_yang_obj: yc_neighbor_ietf_interfaces__interfaces_state_interface_ipv6_neighbor, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /interfaces-state/interface/ipv6/neighbor

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.link_layer_address._changed():
        input_yang_obj.link_layer_address = input_yang_obj.link_layer_address
        
    if input_yang_obj.origin._changed():
        input_yang_obj.origin = input_yang_obj.origin
        
    if input_yang_obj.is_router._changed():
        input_yang_obj.is_router = input_yang_obj.is_router
        
    if input_yang_obj.state._changed():
        input_yang_obj.state = input_yang_obj.state
        
    return translated_yang_obj

def _translate__interfaces_state_interface_ipv6(input_yang_obj: yc_ipv6_ietf_interfaces__interfaces_state_interface_ipv6, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /interfaces-state/interface/ipv6

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.forwarding._changed():
        input_yang_obj.forwarding = input_yang_obj.forwarding
        
    if input_yang_obj.mtu._changed():
        input_yang_obj.mtu = input_yang_obj.mtu
        
    for k, listInst in input_yang_obj.address.iteritems():
        innerobj = _translate__interfaces_state_interface_ipv6_address(listInst, translated_yang_obj)
        
    for k, listInst in input_yang_obj.neighbor.iteritems():
        innerobj = _translate__interfaces_state_interface_ipv6_neighbor(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__interfaces_state_interface(input_yang_obj: yc_interface_ietf_interfaces__interfaces_state_interface, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /interfaces-state/interface

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    if input_yang_obj.type._changed():
        input_yang_obj.type = input_yang_obj.type
        
    if input_yang_obj.admin_status._changed():
        input_yang_obj.admin_status = input_yang_obj.admin_status
        
    if input_yang_obj.oper_status._changed():
        input_yang_obj.oper_status = input_yang_obj.oper_status
        
    if input_yang_obj.last_change._changed():
        input_yang_obj.last_change = input_yang_obj.last_change
        
    if input_yang_obj.if_index._changed():
        input_yang_obj.if_index = input_yang_obj.if_index
        
    if input_yang_obj.phys_address._changed():
        input_yang_obj.phys_address = input_yang_obj.phys_address
        
    if input_yang_obj.higher_layer_if._changed():
        input_yang_obj.higher_layer_if = input_yang_obj.higher_layer_if
        
    if input_yang_obj.lower_layer_if._changed():
        input_yang_obj.lower_layer_if = input_yang_obj.lower_layer_if
        
    if input_yang_obj.speed._changed():
        input_yang_obj.speed = input_yang_obj.speed
        
    innerobj = _translate__interfaces_state_interface_statistics(input_yang_obj.statistics, translated_yang_obj)
        
    innerobj = _translate__interfaces_state_interface_ipv4(input_yang_obj.ipv4, translated_yang_obj)
        
    innerobj = _translate__interfaces_state_interface_ipv6(input_yang_obj.ipv6, translated_yang_obj)
        
    return translated_yang_obj

def _translate__interfaces_state(input_yang_obj: yc_interfaces_state_ietf_interfaces__interfaces_state, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /interfaces-state

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    for k, listInst in input_yang_obj.interface.iteritems():
        innerobj = _translate__interfaces_state_interface(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__ietf_interfaces(input_yang_obj: ietf_interfaces, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ietf-interfaces

    Most of the times, for each yang list instance in the source, we may need to create
    a yang list instance in the translated-yang-object. Use the "add" API to create the yang list
    instance.
    For ex:
        To add a srv6 locator instance:
            loc1 = segripv6.srv6Locators.srv6Locator.add(locatorName=listInst.name)

        To iterate over list instances:
            for k, listInst in segripv6.srv6Locators.srv6Locator.iteritems():
                -- Use this for APP business logic.

    We need to add translation logic only for non-key leaves.
    Keys are already added as part of yang list instance creation
    """
    
    innerobj = _translate__interfaces(input_yang_obj.interfaces, translated_yang_obj)
        
    innerobj = _translate__interfaces_state(input_yang_obj.interfaces_state, translated_yang_obj)
        
    return translated_yang_obj

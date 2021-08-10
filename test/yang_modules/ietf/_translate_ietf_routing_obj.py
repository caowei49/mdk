
def _translate__routing_interfaces(input_yang_obj: yc_interfaces_ietf_routing__routing_interfaces, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/interfaces

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
    
    if input_yang_obj.interface._changed():
        input_yang_obj.interface = input_yang_obj.interface
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols_control_plane_protocol(input_yang_obj: yc_control_plane_protocol_ietf_routing__routing_control_plane_protocols_control_plane_protocol, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols/control-plane-protocol

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
        
    return translated_yang_obj

def _translate__routing_control_plane_protocols(input_yang_obj: yc_control_plane_protocols_ietf_routing__routing_control_plane_protocols, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/control-plane-protocols

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
    
    for k, listInst in input_yang_obj.control_plane_protocol.iteritems():
        innerobj = _translate__routing_control_plane_protocols_control_plane_protocol(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_ribs_rib_routes_route_next_hop_next_hop_list_next_hop(input_yang_obj: yc_next_hop_ietf_routing__routing_ribs_rib_routes_route_next_hop_next_hop_list_next_hop, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/ribs/rib/routes/route/next-hop/next-hop-list/next-hop

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
    
    if input_yang_obj.outgoing_interface._changed():
        input_yang_obj.outgoing_interface = input_yang_obj.outgoing_interface
        
    return translated_yang_obj

def _translate__routing_ribs_rib_routes_route_next_hop_next_hop_list(input_yang_obj: yc_next_hop_list_ietf_routing__routing_ribs_rib_routes_route_next_hop_next_hop_list, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/ribs/rib/routes/route/next-hop/next-hop-list

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
    
    for k, listInst in input_yang_obj.next_hop.iteritems():
        innerobj = _translate__routing_ribs_rib_routes_route_next_hop_next_hop_list_next_hop(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_ribs_rib_routes_route_next_hop(input_yang_obj: yc_next_hop_ietf_routing__routing_ribs_rib_routes_route_next_hop, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/ribs/rib/routes/route/next-hop

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
    
    if input_yang_obj.outgoing_interface._changed():
        input_yang_obj.outgoing_interface = input_yang_obj.outgoing_interface
        
    if input_yang_obj.special_next_hop._changed():
        input_yang_obj.special_next_hop = input_yang_obj.special_next_hop
        
    innerobj = _translate__routing_ribs_rib_routes_route_next_hop_next_hop_list(input_yang_obj.next_hop_list, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_ribs_rib_routes_route(input_yang_obj: yc_route_ietf_routing__routing_ribs_rib_routes_route, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/ribs/rib/routes/route

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
    
    if input_yang_obj.route_preference._changed():
        input_yang_obj.route_preference = input_yang_obj.route_preference
        
    innerobj = _translate__routing_ribs_rib_routes_route_next_hop(input_yang_obj.next_hop, translated_yang_obj)
        
    if input_yang_obj.source_protocol._changed():
        input_yang_obj.source_protocol = input_yang_obj.source_protocol
        
    if input_yang_obj.active._changed():
        input_yang_obj.active = input_yang_obj.active
        
    if input_yang_obj.last_updated._changed():
        input_yang_obj.last_updated = input_yang_obj.last_updated
        
    return translated_yang_obj

def _translate__routing_ribs_rib_routes(input_yang_obj: yc_routes_ietf_routing__routing_ribs_rib_routes, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/ribs/rib/routes

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
    
    for k, listInst in input_yang_obj.route.iteritems():
        innerobj = _translate__routing_ribs_rib_routes_route(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_ribs_rib_active_route_output_route_next_hop_next_hop_list_next_hop(input_yang_obj: yc_next_hop_ietf_routing__routing_ribs_rib_active_route_output_route_next_hop_next_hop_list_next_hop, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/ribs/rib/active-route/output/route/next-hop/next-hop-list/next-hop

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
    
    if input_yang_obj.outgoing_interface._changed():
        input_yang_obj.outgoing_interface = input_yang_obj.outgoing_interface
        
    return translated_yang_obj

def _translate__routing_ribs_rib_active_route_output_route_next_hop_next_hop_list(input_yang_obj: yc_next_hop_list_ietf_routing__routing_ribs_rib_active_route_output_route_next_hop_next_hop_list, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/ribs/rib/active-route/output/route/next-hop/next-hop-list

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
    
    for k, listInst in input_yang_obj.next_hop.iteritems():
        innerobj = _translate__routing_ribs_rib_active_route_output_route_next_hop_next_hop_list_next_hop(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_ribs_rib_active_route_output_route_next_hop(input_yang_obj: yc_next_hop_ietf_routing__routing_ribs_rib_active_route_output_route_next_hop, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/ribs/rib/active-route/output/route/next-hop

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
    
    if input_yang_obj.outgoing_interface._changed():
        input_yang_obj.outgoing_interface = input_yang_obj.outgoing_interface
        
    if input_yang_obj.special_next_hop._changed():
        input_yang_obj.special_next_hop = input_yang_obj.special_next_hop
        
    innerobj = _translate__routing_ribs_rib_active_route_output_route_next_hop_next_hop_list(input_yang_obj.next_hop_list, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_ribs_rib_active_route_output_route(input_yang_obj: yc_route_ietf_routing__routing_ribs_rib_active_route_output_route, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/ribs/rib/active-route/output/route

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
    
    innerobj = _translate__routing_ribs_rib_active_route_output_route_next_hop(input_yang_obj.next_hop, translated_yang_obj)
        
    if input_yang_obj.source_protocol._changed():
        input_yang_obj.source_protocol = input_yang_obj.source_protocol
        
    if input_yang_obj.active._changed():
        input_yang_obj.active = input_yang_obj.active
        
    if input_yang_obj.last_updated._changed():
        input_yang_obj.last_updated = input_yang_obj.last_updated
        
    return translated_yang_obj

def _translate__routing_ribs_rib_active_route_output(input_yang_obj: yc_output_ietf_routing__routing_ribs_rib_active_route_output, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/ribs/rib/active-route/output

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
    
    innerobj = _translate__routing_ribs_rib_active_route_output_route(input_yang_obj.route, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_ribs_rib_active_route(input_yang_obj: yc_active_route_ietf_routing__routing_ribs_rib_active_route, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/ribs/rib/active-route

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
    
    if input_yang_obj.output._changed():
        input_yang_obj.output = input_yang_obj.output
        
    return translated_yang_obj

def _translate__routing_ribs_rib(input_yang_obj: yc_rib_ietf_routing__routing_ribs_rib, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/ribs/rib

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
    
    if input_yang_obj.address_family._changed():
        input_yang_obj.address_family = input_yang_obj.address_family
        
    if input_yang_obj.default_rib._changed():
        input_yang_obj.default_rib = input_yang_obj.default_rib
        
    innerobj = _translate__routing_ribs_rib_routes(input_yang_obj.routes, translated_yang_obj)
        
    if input_yang_obj.active_route._changed():
        input_yang_obj.active_route = input_yang_obj.active_route
        
    if input_yang_obj.description._changed():
        input_yang_obj.description = input_yang_obj.description
        
    return translated_yang_obj

def _translate__routing_ribs(input_yang_obj: yc_ribs_ietf_routing__routing_ribs, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing/ribs

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
    
    for k, listInst in input_yang_obj.rib.iteritems():
        innerobj = _translate__routing_ribs_rib(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing(input_yang_obj: yc_routing_ietf_routing__routing, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing

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
    
    if input_yang_obj.router_id._changed():
        input_yang_obj.router_id = input_yang_obj.router_id
        
    innerobj = _translate__routing_interfaces(input_yang_obj.interfaces, translated_yang_obj)
        
    innerobj = _translate__routing_control_plane_protocols(input_yang_obj.control_plane_protocols, translated_yang_obj)
        
    innerobj = _translate__routing_ribs(input_yang_obj.ribs, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_state_interfaces(input_yang_obj: yc_interfaces_ietf_routing__routing_state_interfaces, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing-state/interfaces

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
    
    if input_yang_obj.interface._changed():
        input_yang_obj.interface = input_yang_obj.interface
        
    return translated_yang_obj

def _translate__routing_state_control_plane_protocols_control_plane_protocol(input_yang_obj: yc_control_plane_protocol_ietf_routing__routing_state_control_plane_protocols_control_plane_protocol, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing-state/control-plane-protocols/control-plane-protocol

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
    
    return translated_yang_obj

def _translate__routing_state_control_plane_protocols(input_yang_obj: yc_control_plane_protocols_ietf_routing__routing_state_control_plane_protocols, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing-state/control-plane-protocols

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
    
    for k, listInst in input_yang_obj.control_plane_protocol.iteritems():
        innerobj = _translate__routing_state_control_plane_protocols_control_plane_protocol(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_state_ribs_rib_routes_route_next_hop_next_hop_list_next_hop(input_yang_obj: yc_next_hop_ietf_routing__routing_state_ribs_rib_routes_route_next_hop_next_hop_list_next_hop, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing-state/ribs/rib/routes/route/next-hop/next-hop-list/next-hop

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
    
    if input_yang_obj.outgoing_interface._changed():
        input_yang_obj.outgoing_interface = input_yang_obj.outgoing_interface
        
    return translated_yang_obj

def _translate__routing_state_ribs_rib_routes_route_next_hop_next_hop_list(input_yang_obj: yc_next_hop_list_ietf_routing__routing_state_ribs_rib_routes_route_next_hop_next_hop_list, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing-state/ribs/rib/routes/route/next-hop/next-hop-list

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
    
    for k, listInst in input_yang_obj.next_hop.iteritems():
        innerobj = _translate__routing_state_ribs_rib_routes_route_next_hop_next_hop_list_next_hop(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_state_ribs_rib_routes_route_next_hop(input_yang_obj: yc_next_hop_ietf_routing__routing_state_ribs_rib_routes_route_next_hop, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing-state/ribs/rib/routes/route/next-hop

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
    
    if input_yang_obj.outgoing_interface._changed():
        input_yang_obj.outgoing_interface = input_yang_obj.outgoing_interface
        
    if input_yang_obj.special_next_hop._changed():
        input_yang_obj.special_next_hop = input_yang_obj.special_next_hop
        
    innerobj = _translate__routing_state_ribs_rib_routes_route_next_hop_next_hop_list(input_yang_obj.next_hop_list, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_state_ribs_rib_routes_route(input_yang_obj: yc_route_ietf_routing__routing_state_ribs_rib_routes_route, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing-state/ribs/rib/routes/route

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
    
    if input_yang_obj.route_preference._changed():
        input_yang_obj.route_preference = input_yang_obj.route_preference
        
    innerobj = _translate__routing_state_ribs_rib_routes_route_next_hop(input_yang_obj.next_hop, translated_yang_obj)
        
    if input_yang_obj.source_protocol._changed():
        input_yang_obj.source_protocol = input_yang_obj.source_protocol
        
    if input_yang_obj.active._changed():
        input_yang_obj.active = input_yang_obj.active
        
    if input_yang_obj.last_updated._changed():
        input_yang_obj.last_updated = input_yang_obj.last_updated
        
    return translated_yang_obj

def _translate__routing_state_ribs_rib_routes(input_yang_obj: yc_routes_ietf_routing__routing_state_ribs_rib_routes, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing-state/ribs/rib/routes

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
    
    for k, listInst in input_yang_obj.route.iteritems():
        innerobj = _translate__routing_state_ribs_rib_routes_route(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_state_ribs_rib_active_route_output_route_next_hop_next_hop_list_next_hop(input_yang_obj: yc_next_hop_ietf_routing__routing_state_ribs_rib_active_route_output_route_next_hop_next_hop_list_next_hop, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing-state/ribs/rib/active-route/output/route/next-hop/next-hop-list/next-hop

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
    
    if input_yang_obj.outgoing_interface._changed():
        input_yang_obj.outgoing_interface = input_yang_obj.outgoing_interface
        
    return translated_yang_obj

def _translate__routing_state_ribs_rib_active_route_output_route_next_hop_next_hop_list(input_yang_obj: yc_next_hop_list_ietf_routing__routing_state_ribs_rib_active_route_output_route_next_hop_next_hop_list, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing-state/ribs/rib/active-route/output/route/next-hop/next-hop-list

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
    
    for k, listInst in input_yang_obj.next_hop.iteritems():
        innerobj = _translate__routing_state_ribs_rib_active_route_output_route_next_hop_next_hop_list_next_hop(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_state_ribs_rib_active_route_output_route_next_hop(input_yang_obj: yc_next_hop_ietf_routing__routing_state_ribs_rib_active_route_output_route_next_hop, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing-state/ribs/rib/active-route/output/route/next-hop

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
    
    if input_yang_obj.outgoing_interface._changed():
        input_yang_obj.outgoing_interface = input_yang_obj.outgoing_interface
        
    if input_yang_obj.special_next_hop._changed():
        input_yang_obj.special_next_hop = input_yang_obj.special_next_hop
        
    innerobj = _translate__routing_state_ribs_rib_active_route_output_route_next_hop_next_hop_list(input_yang_obj.next_hop_list, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_state_ribs_rib_active_route_output_route(input_yang_obj: yc_route_ietf_routing__routing_state_ribs_rib_active_route_output_route, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing-state/ribs/rib/active-route/output/route

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
    
    innerobj = _translate__routing_state_ribs_rib_active_route_output_route_next_hop(input_yang_obj.next_hop, translated_yang_obj)
        
    if input_yang_obj.source_protocol._changed():
        input_yang_obj.source_protocol = input_yang_obj.source_protocol
        
    if input_yang_obj.active._changed():
        input_yang_obj.active = input_yang_obj.active
        
    if input_yang_obj.last_updated._changed():
        input_yang_obj.last_updated = input_yang_obj.last_updated
        
    return translated_yang_obj

def _translate__routing_state_ribs_rib_active_route_output(input_yang_obj: yc_output_ietf_routing__routing_state_ribs_rib_active_route_output, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing-state/ribs/rib/active-route/output

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
    
    innerobj = _translate__routing_state_ribs_rib_active_route_output_route(input_yang_obj.route, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_state_ribs_rib_active_route(input_yang_obj: yc_active_route_ietf_routing__routing_state_ribs_rib_active_route, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing-state/ribs/rib/active-route

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
    
    if input_yang_obj.output._changed():
        input_yang_obj.output = input_yang_obj.output
        
    return translated_yang_obj

def _translate__routing_state_ribs_rib(input_yang_obj: yc_rib_ietf_routing__routing_state_ribs_rib, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing-state/ribs/rib

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
    
    if input_yang_obj.address_family._changed():
        input_yang_obj.address_family = input_yang_obj.address_family
        
    if input_yang_obj.default_rib._changed():
        input_yang_obj.default_rib = input_yang_obj.default_rib
        
    innerobj = _translate__routing_state_ribs_rib_routes(input_yang_obj.routes, translated_yang_obj)
        
    if input_yang_obj.active_route._changed():
        input_yang_obj.active_route = input_yang_obj.active_route
        
    return translated_yang_obj

def _translate__routing_state_ribs(input_yang_obj: yc_ribs_ietf_routing__routing_state_ribs, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing-state/ribs

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
    
    for k, listInst in input_yang_obj.rib.iteritems():
        innerobj = _translate__routing_state_ribs_rib(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__routing_state(input_yang_obj: yc_routing_state_ietf_routing__routing_state, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /routing-state

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
    
    if input_yang_obj.router_id._changed():
        input_yang_obj.router_id = input_yang_obj.router_id
        
    innerobj = _translate__routing_state_interfaces(input_yang_obj.interfaces, translated_yang_obj)
        
    innerobj = _translate__routing_state_control_plane_protocols(input_yang_obj.control_plane_protocols, translated_yang_obj)
        
    innerobj = _translate__routing_state_ribs(input_yang_obj.ribs, translated_yang_obj)
        
    return translated_yang_obj

def _translate__ietf_routing(input_yang_obj: ietf_routing, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ietf-routing

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
    
    innerobj = _translate__routing(input_yang_obj.routing, translated_yang_obj)
        
    innerobj = _translate__routing_state(input_yang_obj.routing_state, translated_yang_obj)
        
    return translated_yang_obj

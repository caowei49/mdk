
def _translate__network_instances_network_instance_vrf_root(input_yang_obj: yc_vrf_root_ietf_network_instance__network_instances_network_instance_vrf_root, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instances/network-instance/vrf-root

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
    
    innerobj = _translate__network_instances_network_instance_vrf_root(input_yang_obj.interfaces, translated_yang_obj)
        
    innerobj = _translate__network_instances_network_instance_vrf_root(input_yang_obj.interfaces_state, translated_yang_obj)
        
    innerobj = _translate__network_instances_network_instance_vrf_root(input_yang_obj.routing, translated_yang_obj)
        
    innerobj = _translate__network_instances_network_instance_vrf_root(input_yang_obj.routing_state, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instances_network_instance(input_yang_obj: yc_network_instance_ietf_network_instance__network_instances_network_instance, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instances/network-instance

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
        
    if input_yang_obj.description._changed():
        input_yang_obj.description = input_yang_obj.description
        
    innerobj = _translate__network_instances_network_instance_vrf_root(input_yang_obj.vrf_root, translated_yang_obj)
        
    innerobj = _translate__network_instances_network_instance_vsi_root(input_yang_obj.vsi_root, translated_yang_obj)
        
    innerobj = _translate__network_instances_network_instance_vv_root(input_yang_obj.vv_root, translated_yang_obj)
        
    return translated_yang_obj

def _translate__network_instances(input_yang_obj: yc_network_instances_ietf_network_instance__network_instances, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /network-instances

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
    
    for k, listInst in input_yang_obj.network_instance.iteritems():
        innerobj = _translate__network_instances_network_instance(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__ietf_network_instance(input_yang_obj: ietf_network_instance, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ietf-network-instance

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
    
    innerobj = _translate__network_instances(input_yang_obj.network_instances, translated_yang_obj)
        
    return translated_yang_obj

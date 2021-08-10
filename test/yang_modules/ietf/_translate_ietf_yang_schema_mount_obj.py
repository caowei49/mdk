
def _translate__schema_mounts_namespace(input_yang_obj: yc_namespace_ietf_yang_schema_mount__schema_mounts_namespace, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /schema-mounts/namespace

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
    
    if input_yang_obj.uri._changed():
        input_yang_obj.uri = input_yang_obj.uri
        
    return translated_yang_obj

def _translate__schema_mounts_mount_point_shared_schema(input_yang_obj: yc_shared_schema_ietf_yang_schema_mount__schema_mounts_mount_point_shared_schema, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /schema-mounts/mount-point/shared-schema

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
    
    if input_yang_obj.parent_reference._changed():
        input_yang_obj.parent_reference = input_yang_obj.parent_reference
        
    return translated_yang_obj

def _translate__schema_mounts_mount_point(input_yang_obj: yc_mount_point_ietf_yang_schema_mount__schema_mounts_mount_point, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /schema-mounts/mount-point

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
    
    if input_yang_obj.config._changed():
        input_yang_obj.config = input_yang_obj.config
        
    innerobj = _translate__schema_mounts_mount_point_shared_schema(input_yang_obj.shared_schema, translated_yang_obj)
        
    return translated_yang_obj

def _translate__schema_mounts(input_yang_obj: yc_schema_mounts_ietf_yang_schema_mount__schema_mounts, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /schema-mounts

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
    
    for k, listInst in input_yang_obj.namespace.iteritems():
        innerobj = _translate__schema_mounts_namespace(listInst, translated_yang_obj)
        
    for k, listInst in input_yang_obj.mount_point.iteritems():
        innerobj = _translate__schema_mounts_mount_point(listInst, translated_yang_obj)
        
    return translated_yang_obj

def _translate__ietf_yang_schema_mount(input_yang_obj: ietf_yang_schema_mount, translated_yang_obj=None):
    """
    Translate method. This can only be called after object pointing to "self" is instantiated.
    This is mapped to Yang variable /ietf-yang-schema-mount

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
    
    innerobj = _translate__schema_mounts(input_yang_obj.schema_mounts, translated_yang_obj)
        
    return translated_yang_obj

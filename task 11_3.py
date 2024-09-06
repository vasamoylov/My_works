def introspection_info(obj):
    obj_type = type(obj)
    attr = dir(obj)
    methods = [x for x in attr if callable(getattr(obj, x))]
    attrributes = [x for x in attr if not callable(getattr(obj, x))]
    module = obj.classmodule if hasattr(obj, 'class') else None

    info = {'type': obj_type.__name__, 'attributes': attrributes, 'methods': methods, 'module': module}
    return info


print(introspection_info(42))

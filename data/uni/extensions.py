# -*- coding: utf-8 -*-

def check_tasas_type(value, rule_obj, path):

    type_1 = 'precio_por_crédito'
    type_2= 'cantidad_fija'

    data_1 = 'cantidades'
    data_2 = 'cantidad'

    if (not 'tipo' in value):
        raise Exception("No 'tipo' defined in %s" % path)

    if ('cantidades' in value and 'cantidad' in value):
        raise Exception("'%s' and '%s' can't be together in %s" % (data_1, data_2, path))

    if (not 'cantidades' in value and not 'cantidad' in value):
        raise Exception("Must exist '%s' or '%s' in %s" % (data_1, data_2, path))

    if (value['tipo'] == type_1 and data_2 in value):
        raise Exception("For type '%s' must not exist '%s' in %s" % (type_1, data_2, path))

    if (value['tipo'] == type_2 and data_1 in value):
        raise Exception("For type '%s' must not exist '%s' in %s" % (type_2, data_1, path))

    return True

def check_tasas_exists(value, rule_obj, path):
    if any(elem is None for elem in value.values()):
        raise Exception("Empty values not allowed in %s" % path)

    return True
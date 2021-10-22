"""Examples of using jsonpath with apidoc"""


def jsonpath_ng_example(apidoc_data):
    from jsonpath_ng.ext import parse as parse_ng
    method_parameters = parse_ng("$[*].parameter.fields.Parameter[?(@.field=='method')].allowedValues")
    return [match.value for match in method_parameters.find(apidoc_data)]


def jsonpath_example(apidoc_data):
    from jsonpath import jsonpath
    method_parameters = jsonpath(apidoc_data, '$[*].parameter.fields.Parameter[*]')
    method_names = []
    for parameter in method_parameters:
        if parameter.get('field') == 'method':
            method_name = parameter.get('allowedValues')
            method_names.append(method_name)
    return method_names
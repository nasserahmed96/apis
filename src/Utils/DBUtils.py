def build_conditions(self, conditions):
    """
    This function builds conditions for the SELECT query, based on whether the required widget has something in it
    or not
    :return:
    """
    return ' WHERE ' + ' '.join([self.get_condition_string(condition) for condition in conditions]) if any(
        conditions) else ""


def build_condition(self, column, value, operator, options='', logic=''):
    return {
        'column': column,
        'value': value,
        'operator': operator,
        'options': options,
        'logic': logic
    }


def extract_values_from_conditions(self, conditions):
    placeholder = dict()
    for condition in conditions:
        placeholder[condition['column'].replace('.', '_')] = condition['value']
    return placeholder


def get_condition_string(self, condition):
    """
    Get a condition string out of a condition object
    :param condition: A condition object contains the required parameters for the condition
    :return: A condition string to be used in SQL query
    """
    return f"{condition['column']} {condition['operator']} :{condition['column'].replace('.', '_')} {condition['options']} {condition['logic']}"

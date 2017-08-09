from expects import *


with description('diffing dictionaries'):
    with it('shows different values for the same key'):
        a_dict = {'a': 0, 'key': 0}
        another_dict = {'a': 0, 'key': 1}

        expect(differences(a_dict, another_dict)).to(equal([{'key': 0}, {'key': 1}]))

    with it('shows extra keys'):
        a_dict = {'key': 0}
        another_dict = {'key': 0, 'extra_key': 0}

        expect(differences(a_dict, another_dict)).to(equal([{}, {'extra_key': 0}]))

    with it('shows extra keys and different values for the same key'):
        a_dict = {'key': 0, 'key_with_different_value': 0}
        another_dict = {'key': 0, 'key_with_different_value': 1, 'extra_key': 0}

        expect(differences(a_dict, another_dict)).to(equal([
            {'key_with_different_value': 0},
            {'key_with_different_value': 1, 'extra_key': 0}
        ]))

    with it('shows no differences for equal dictionaries'):
        a_dict = {'key': 0, 'another_key': 1}
        another_dict = {'key': 0, 'another_key': 1}

        expect(differences(a_dict, another_dict)).to(equal([{}, {}]))




def differences(left_dict, right_dict):
    common_keys = common_keys_between(left_dict, right_dict)
    left_differences = exclude_keys_in(left_dict, common_keys)
    right_differences = exclude_keys_in(right_dict, common_keys)

    for key in common_keys:
        if left_dict[key] != right_dict[key]:
            left_differences[key] = left_dict[key]
            right_differences[key] = right_dict[key]

    return [left_differences, right_differences]

def exclude_keys_in(a_dict, keys_to_exclude):
    return { key: a_dict[key] for key in a_dict.keys() if key not in keys_to_exclude }

def common_keys_between(left_dict, right_dict):
    left_keys = set(left_dict.keys())
    right_keys = set(right_dict.keys())
    return left_keys.intersection(right_keys)

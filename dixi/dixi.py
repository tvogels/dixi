from collections import OrderedDict

class Dixi:
    def __init__(self, data=None, ordered=False):
        self.dict_type = OrderedDict if ordered else dict
        if data:
            self.data = data
        else:
            self.data = self.dict_type()
    
    def __getitem__(self, key):
        if isinstance(key, tuple):
            def get(data_pointer, key_list):
                key_head = key_list[0]
                if key_head == slice(None, None, None):# :
                    return Dixi({
                        key: get(value, key_list[1:])
                        for key, value in data_pointer.items()
                    })
                elif isinstance(key_head, tuple) or isinstance(key_head, list):
                    return Dixi({
                        key: get(data_pointer[key], key_list[1:])
                        for key in key_head
                    })
                else:
                    if len(key_list) == 1:
                        return data_pointer[key_head]
                    else:
                        return get(data_pointer[key_head], key_list[1:])

            return get(self.data, key)
        else:
            return self.data[key]
    
    def __setitem__(self, key, value):
        if isinstance(value, Dixi):
            value = self.dict_type(value.data)
        if not isinstance(key, tuple):
            self.data[key] = value
        else:
            data_pointer = self.data
            for key_part in key[:-1]:
                if not key_part in data_pointer:
                    data_pointer[key_part] = self.dict_type()
                data_pointer = data_pointer[key_part]
            if not isinstance(data_pointer, dict):
                raise Exception('Trying to assign to a non-dict')
            data_pointer[key[-1]] = value
    
    def __delitem__(self, key):
        if isinstance(key, tuple):
            data_pointer = self.data
            for key_part in key[:-1]:
                data_pointer = data_pointer[key_part]
            del data_pointer[key[-1]]
        else:
            del self.data[key]

    def __contains__(self, key):
        if isinstance(key, tuple):
            data_pointer = self.data
            for key_part in key:
                if not isinstance(data_pointer, self.dict_type) or not key_part in data_pointer:
                    return False
                data_pointer = data_pointer[key_part]
            return True
        else:
            return key in self.data

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return hash(self.data)

    def __iter__(self):
        return self.leavekeys()

    def __eq__(self, other):
        if isinstance(other, Dixi):
            return self.data == other.data
        elif isinstance(other, self.dict_type):
            return self.data == other
        else:
            raise ValueError('Cannot compare a Dixi to something of type {}'.format(type(other)))

    def iterleaves(self):
        def iterate(data_pointer, key_prefix):
            for key, value in data_pointer.items():
                current_key = key_prefix + (key, )
                if isinstance(value, self.dict_type):
                    for (child_key, child_val) in iterate(value, current_key):
                        yield child_key, child_val
                else:
                    yield current_key, value
        return iterate(self.data, tuple())
        
    def leafkeys(self):
        for key, value in self.iterleaves():
            yield key
        
    def pop(self, key):
        value = self[key]
        del self[key]
        return value
    
    def keys(self):
        return self.data.keys()

    def values(self):
        return self.data.values()
    
    def items(self):
        return self.data.items()

    def iteritems(self, key):
        return self.data.iteritems()

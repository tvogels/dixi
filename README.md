# Dixi - Deep Dictionaries for Python

## Installation
```bash
pip install dixi
```

## Examples
```python
from dixi import Dixi

data = Dixi({
    'Chris': {
        'age': 25,
        'address': {
            'city': 'Amsterdam',
            'country': 'Netherlands',
        },
    },
    'Anna': {
        'age': 19,
        'address': {
            'city': 'Zürich',
            'country': 'Switzerland',
        },
    },
    'John': {
        'age': 44,
        'address': {
            'city': 'London',
            'country': 'United Kingdom',
        },
    },
})
```

### Deep indexing
```python
data['John', 'age']
# >> 44
```

### Partial indexing
```python
data['Chris', 'address']
# >> {'city': 'Amsterdam', 'country': 'Netherlands'}
```

### NumpPy style slicing
```python
data[:, 'address', 'country']
# >> Dixi({'Chris': 'Netherlands', 'Anna': 'Switzerland', 'John': 'United Kingdom'})
data[['Chris', 'Anna'], 'age']
# >> {'Chris': 25, 'Anna': 19}
```

### Setting
```python
data['Derek', 'hobbies'] = ['Sewing', 'Archery']
```

### Iteration
```python
for key in data: # or key in data.leafkeys()
    print(key)
# >> ('Chris', 'age')
# >> ('Anna', 'age')
# >> ('Anna', 'address', 'city')
# >> ('Anna', 'address', 'country')
# >> ('John', 'age')
# >> ('John', 'address', 'city')
# >> ('John', 'address', 'country')
# >> ('Derek', 'hobbies')
```
```python
for key in data.keys():
    print(key)
# >> Chris
# >> Anna
# >> John
# >> Derek
```
```python
for key, value in data.items():
    print(key, value)
# >> Chris {'age': 25}
# >> Anna {'age': 19, 'address': {'city': 'Zürich', 'country': 'Switzerland'}}
# >> John {'age': 44, 'address': {'city': 'London', 'country': 'United Kingdom'}}
# >> Derek {'hobbies': ['Sewing', 'Archery']}
```
```python
data = Dixi({
    0: {  0: 'a', 1: 'b' },
    1: { 0: 'c', 1: 'd' },
})
for keys, value in data.iterleaves():
    print(keys, value)
# >> (0, 0) a
# >> (0, 1) b
# >> (1, 0) c
# >> (1, 1) d
```

### Deletion
```python
del data['Chris', 'address']
```

## Todo
* Allow indexing for arrays

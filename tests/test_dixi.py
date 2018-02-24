import unittest
from dixi import Dixi

class TestDixi(unittest.TestCase):
    def test_assign_and_read(self):
        d = Dixi()
        d['a'] = 3
        self.assertEqual(d['a'], 3)

    def test_delete(self):
        d = Dixi()
        d['a'] = 3
        del d['a']
        with self.assertRaises(KeyError):
            d['a']
        with self.assertRaises(KeyError):
            d['a']

    def test_assign_deep(self):
        d = Dixi()
        d['my', 'a'] = 3
        self.assertEqual(d['my', 'a'], 3)
        self.assertEqual(d['my'], {'a': 3})
    
    def test_deep_delete(self):
        d = Dixi()
        d['my', 'a'] = 3
        d['my', 'b'] = 4
        d['your', 'a'] = 3
        d['your', 'b'] = 4

        del d['my']
        with self.assertRaises(KeyError):
            d['my']
        with self.assertRaises(KeyError):
            d['my', 'a']

        del d['your', 'b']
        with self.assertRaises(KeyError):
            d['your', 'b']
        self.assertEqual(d['your', 'a'], 3)

    def test_contains(self):
        d = Dixi()
        d['my', 'a'] = 1
        d['my', 'b'] = 2
        d['your'] = 3
        self.assertTrue(('my', 'a') in d)
        self.assertTrue('my' in d)
        self.assertTrue(('my',) in d)
        self.assertTrue('your' in d)
        self.assertFalse(('my', 'c') in d)
        self.assertFalse(('your', 'q') in d)
        self.assertFalse('x' in d)
    
    def test_pop(self):
        d = Dixi()
        d['your', 'bike'] = 12
        d['my', 'bike'] = d.pop(('your', 'bike'))
        
        with self.assertRaises(KeyError):
            d['your', 'bike']
        self.assertEqual(d['my', 'bike'], 12)
        self.assertEqual(d['your'], {})

        d.pop('your')
        with self.assertRaises(KeyError):
            d['your']
        
    def test_iterleaves(self):
        d = Dixi()
        d['a', 'b'] = 1
        d['c'] = 2
        leaves = list(d.iterleaves())
        expected_leaves = [
            (('a', 'b'), 1),
            (('c',), 2),
        ]
        self.assertEqual(leaves, expected_leaves)

    def test_slice(self):
        data = {
            'John': {'age': 4},
            'Bertha': {'age': 6},
            'Chris': {'age': 10},
        }
        d = Dixi(data)

        ages = d[:, 'age']

        expected_ages = Dixi({
            'John': 4,
            'Bertha': 6,
            'Chris': 10,
        })

        self.assertEqual(ages.data, expected_ages.data)

    def test_subset_slice(self):
        data = {
            'John': {'age': 4},
            'Bertha': {'age': 6},
            'Chris': {'age': 10},
        }
        d = Dixi(data)

        ages = d[['John', 'Bertha'], 'age']

        expected_ages = Dixi({
            'John': 4,
            'Bertha': 6,
        })

        self.assertEqual(ages.data, expected_ages.data)


if __name__ == '__main__':
    unittest.main()

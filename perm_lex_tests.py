import unittest
import perm_lex


class TestAssign1(unittest.TestCase):

    def test_perm_gen_lex(self):
        self.assertEqual(perm_lex.perm_gen_lex(''), [])
        self.assertEqual(perm_lex.perm_gen_lex('a'), ['a'])
        self.assertEqual(perm_lex.perm_gen_lex('x'), ['x'])
        self.assertEqual(perm_lex.perm_gen_lex('ab'), ['ab', 'ba'])
        self.assertEqual(perm_lex.perm_gen_lex('xy'), ['xy', 'yx'])
        self.assertEqual(perm_lex.perm_gen_lex('abc'), ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(perm_lex.perm_gen_lex('xyz'), ['xyz', 'xzy', 'yxz', 'yzx', 'zxy', 'zyx'])
        self.assertEqual(perm_lex.perm_gen_lex('abcd'), ['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb',
                                                         'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca',
                                                         'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba',
                                                         'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba'])
        self.assertEqual(perm_lex.perm_gen_lex('xyz!'), ['xyz!', 'xy!z', 'xzy!', 'xz!y', 'x!yz', 'x!zy',
                                                         'yxz!', 'yx!z', 'yzx!', 'yz!x', 'y!xz', 'y!zx',
                                                         'zxy!', 'zx!y', 'zyx!', 'zy!x', 'z!xy', 'z!yx',
                                                         '!xyz', '!xzy', '!yxz', '!yzx', '!zxy', '!zyx'])


if __name__ == "__main__":
    unittest.main()

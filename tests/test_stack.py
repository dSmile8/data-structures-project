"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Stack, Node


class TestStack(unittest.TestCase):
    def test_push(self):

        self.assertEqual(Stack().push('DaTa1'), None)

        node = Node('DaTa1', 'DaTa2')
        self.assertEqual(node.next_node, 'DaTa2')
        self.assertEqual(node.data, 'DaTa1')

        stack = Stack()

        stack.push('111111')
        self.assertEqual(stack.top.data, '111111')

        stack.push('2222')
        self.assertEqual(stack.top.data, '2222')
        self.assertEqual(stack.top.next_node.data, '111111')


if __name__ == '__main__':
    unittest.main()

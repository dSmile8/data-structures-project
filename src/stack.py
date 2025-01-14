class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node
        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return f'{self.data}, {self.next_node}'


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""

        self.top = None

    def push(self, data) -> None:
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """

        # next_node = self.top
        # new_top = Node(data, next_node)
        # self.top = new_top

        if self.top is None:
            self.top = Node(data, None)
        else:
            self.top = Node(data, self.top)

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """

        return_element = self.top
        self.top = self.top.next_node
        return return_element.data

    def __repr__(self):
        return f'{self.top}'




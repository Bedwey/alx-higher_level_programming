class Node:
    """
    A class that defines a node of a singly linked list.

    Attributes:
        data (int): The data to be stored in the node.
        next_node (Node): A reference to the next node in the linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new instance of the Node class.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node, optional): A reference to the
                next node in the linked list. Defaults to None.

        Raises:
            TypeError: If data is not an integer
                or next_node is not a Node object.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        The data stored in the node.

        Returns:
            int: The data stored in the node.
        """
        return self._data

    @data.setter
    def data(self, value):
        """
        Sets the data stored in the node.

        Args:
            value (int): The data to be stored in the node.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """
        The next node in the linked list.

        Returns:
            Node: The next node in the linked list.
        """
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next node in the linked list.

        Args:
            value (Node): The next node in the linked list.

        Raises:
            TypeError: If value is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    """
    A class that defines a singly linked list.

    Attributes:
        head (Node): The first node in the linked list.
    """

    def __init__(self):
        """
        Initializes a new instance of the SinglyLinkedList class.
        """
        self.head = None

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            str: A string representation of the linked list.
        """
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted
            position in the linked list (increasing order).

        Args:
            value (int): The data to be stored in the new node.
        """
        new_node = Node(value)
        if self.head is None or self.head.data > value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None \
                    and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

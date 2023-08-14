class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head: Node | None):
        if not head:
            head = None
        self.head = head

    def append(self, new_node):
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def delete(self, value: str):
        current = self.head
        if not current:
            return
        if current.value == value:
            self.head = current.next
            return True
        else:
            while current:
                if current.value == value:
                    break
                prev = current
                current = current.next
                return True
            if current is None:
                return False
            prev.next = current.next  # type: ignore
            current = None
            return True

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "0".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        count = 0
        current = self.head
        """
        if the position is 0 then move the current head to next
        and make the new element as head
        """
        if position == 0:
            new_element.next = self.head
            self.head = new_element
        """
        1. loop as long as current exists
        2. This will break as soon as new element is inserted
        """
        while current:
            if count + 1 == position:
                new_element.next = current.next
                current.next = new_element
                return
            else:
                count += 1
                current = current.next
        """void out the end of the statment"""
        pass


mainList = LinkedList(None)


def addNode(node: str):
    mainList.append(Node(node))


def getNode(position: int):
    print('position', position)
    current = mainList.head
    count = 0
    while current:
        if count == position:
            print('stopping')
            return current.value
        else:
            count += 1
            current = current.next
    print('i should not reach this')
    return None


def deleteNode(node: str):
    mainList.delete(node)


def insertNode(node: str, position: int):
    mainList.insert(Node(node), position)


def makeList():
    node1 = Node('a')
    node2 = Node('b')
    node3 = Node('c')
    node4 = Node('d')
    ll = LinkedList(node1)
    ll.append(node2)
    ll.append(node3)
    ll.append(node4)
    ll.insert(Node('b2'), 1)
    ll.delete('b2')

    return str(ll.head.next.value if ll.head else None)

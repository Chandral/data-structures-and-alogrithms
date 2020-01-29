import inspect


class Link:
    def __init__(self, data):
        self.data = data
        self._next_link = None

    @property
    def next_link(self):
        return self._next_link

    @next_link.setter
    def next_link(self, link):
        caller = inspect.stack()[1].function
        if hasattr(LinkedList, caller):
            self._next_link = link
        else:
            raise AttributeError("Can't set value of link from class Link")


class LinkedList:
    def __init__(self):
        self.head = None

    def append_link(self, link):
        if not self.head:
            self.head = Link(link)
        else:
            tail = self.head
            while tail.next_link:
                tail = tail.next_link
            tail.next_link = Link(link)


ll = LinkedList()
ll.append_link(10)
ll.append_link(20)
ll.append_link(30)
ll.append_link(40)
print(ll.head.next_link.next_link.next_link.next_link)
ll.head.next_link.next_link.next_link.next_link = Link(2)
print(ll.head.next_link.next_link.next_link.next_link)
import inspect


class Link:

    def __init__(self, value=None, link=None):
        self.value = value
        self._link = link

    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, value):
        caller = inspect.stack()[1].function
        if hasattr(LinkedList, caller):
            self._link = value
        else:
            raise AttributeError("Can't set value of link from class Link")


class LinkedList:

    def __init__(self):
        self.head = None
    def append_link(self, value):
        if not self.head:
            self.head = Link(value)
        else:
            t = self.head
            while t.link != None:
                t = t.link
            t.link = Link(value)
    def __repr__(self):
        t = self.head
        list_values = []
        while t != None:
            list_values.append(str(t.value))
            t = t.link
        return f'[{", ".join(list_values)}]'


ll = LinkedList()
print(ll)
ll.append_link(10)
ll.append_link(20)
ll.append_link(30)
ll.append_link(40)
print(ll)

l = Link()
l.link = 'value'
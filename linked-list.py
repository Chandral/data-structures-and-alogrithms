class Link(object):
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def get_data(self):
        return self.data

    def change_data(self, new_data):
        self.data = new_data


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def add_link(self, link):
        if self.head:
            current_link = self.head
            while current_link.next_node:
                current_link = current_link.next_node
            current_link.next_node = link
        else:
            self.head = link

    def remove_link_at(self, position):
        pass

    def get_data_at(self, position):
        pass


ll = LinkedList()
n1 = Link(1)
n2 = Link(2)
n3 = Link(3)
ll.add_link(n1)
ll.add_link(n2)
ll.add_link(n3)

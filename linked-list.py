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
        if isinstance(link, Link):
            if self.head:
                current_link = self.head
                while current_link.next_node:
                    current_link = current_link.next_node
                current_link.next_node = link
            else:
                self.head = link
            self.size += 1
        else:
            print("Please provide a Link object")

    def insert_link_at(self, position):
        try:
            position = int(position)
        except ValueError:
            print("Please provide an integer")

    def remove_link_at(self, position):
        try:
            position = int(position)
        except ValueError:
            print("Please provide an integer")

    def get_data_at(self, position):
        try:
            position = int(position)
        except ValueError:
            print("Please provide an integer")

    def remove_link_with_data(self, data):
        pass

    def remove_all_links_with_data(self, data):
        pass


ll = LinkedList()
n1 = Link(1)
n2 = Link(2)
n3 = Link(3)
ll.add_link(n1)
ll.add_link(n2)
ll.add_link(n3)
ll.add_link("asdfasd")


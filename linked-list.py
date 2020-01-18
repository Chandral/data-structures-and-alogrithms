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

    def insert_link_at(self, position, link):
        if isinstance(link, Link):
            try:
                position = int(position)
                if 0 < position <= self.size:
                    preceding_link = self.head
                    for pos in range(0, position-2):
                        preceding_link = preceding_link.next_node
                    link.next_node = preceding_link.next_node
                    preceding_link.next_node = link
                    self.size += 1
                else:
                    print("No existing link at this position. Try add_link() method")
            except ValueError:
                print("Please provide an integer")
        else:
            print("Please provide a Link object")

    def remove_link_at(self, position):
        try:
            position = int(position)
            if 0 < position <= self.size:
                current_node = self.head
                for pos in range(0, position - 1):
                    current_node = current_node.next_node
                print(current_node.data)
            else:
                print("No link found at this position to remove")
        except ValueError:
            print("Please provide an integer")

    def get_data_at(self, position):
        try:
            position = int(position)
            if 0 < position <= self.size:
                current_node = self.head
                for pos in range(0, position - 1):
                    current_node = current_node.next_node
                return current_node.data
            return "No link found at this position"
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
n4 = Link(4)


ll.add_link(n1)
ll.add_link(n2)
ll.add_link(n3)
ll.add_link(n4)

print(ll.head.data)
print(ll.head.next_node.data)
print(ll.head.next_node.next_node.data)
print(ll.head.next_node.next_node.next_node.data)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

ll.insert_link_at(3, n4)

print(ll.head.data)
print(ll.head.next_node.data)
print(ll.head.next_node.next_node.data)
print(ll.head.next_node.next_node.next_node.data)
print(ll.head.next_node.next_node.next_node.next_node.data)

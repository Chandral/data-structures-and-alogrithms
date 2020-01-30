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
        self.size = 0

    def append_link(self, link_data):
        if not self.head:
            self.head = Link(link_data)
        else:
            tail = self.head
            while tail.next_link:
                tail = tail.next_link
            tail.next_link = Link(link_data)
        self.size += 1

    def insert_link_at(self, position, link_data):
        try:
            position = int(position)
            if 0 < position <= self.size:
                if position == 1:
                    temp = self.head
                    self.head = Link(link_data)
                    self.head.next_link = temp
                else:
                    preceding_link = self.head
                    for _ in range(1, position-1):
                        preceding_link = preceding_link.next_link
                    new_link = Link(link_data)
                    new_link.next_link = preceding_link.next_link
                    preceding_link.next_link = new_link
                self.size += 1
            else:
                print("No existing link at position: {}. Try appending it.".format(position))
        except ValueError:
            print("Please provide an integer")

    def delete_link_at(self, position):
        try:
            position = int(position)
            if 0 < position <= self.size:
                if position == 1:
                    if self.head.next_link:
                        self.head = self.head.next_link
                    else:
                        self.head = None
                else:
                    preceding_link = self.head
                    for _ in range(1, position - 1):
                        preceding_link = preceding_link.next_link
                    preceding_link.next_link = preceding_link.next_link.next_link
                self.size -= 1
            else:
                print("No link found at position: {}".format(position))
        except ValueError:
            print("Please provide an integer")

    def break_link_at(self, position):
        try:
            position = int(position)
            if 0 < position <= self.size:
                link = self.head
                for _ in range(1, position):
                    link = link.next_link
                link.next_link = None
                self.size = position
            else:
                print("No link found at position: {}".format(position))
        except ValueError:
            print("Please provide an integer")

    def read_data_at(self, position):
        try:
            position = int(position)
            if 0 < position <= self.size:
                link = self.head
                for _ in range(1, position):
                    link = link.next_link
                return link.data
            else:
                print("No link found at position: {}".format(position))
        except ValueError:
            print("Please provide an integer")

    def count_instances_of(self, link_data):
        num_of_links = 0
        link = self.head
        while link:
            if link.data == link_data:
                num_of_links += 1
            link = link.next_link
        return num_of_links

    def delete_link_with_data(self, link_data):
        link = self.head
        position = 1
        found = False
        while link:
            if link.data == link_data:
                found = True
                break
            link = link.next_link
            position += 1
        if found:
            self.delete_link_at(position)

    def delete_links_with_data(self, link_data):
        count = self.count_instances_of(link_data)
        if count > 0:
            for _ in range(0, count):
                self.delete_link_with_data(link_data)

    def get_positions_of(self, link_data):
        positions = []
        link = self.head
        p = 1
        while link:
            if link.data == link_data:
                positions.append(p)
            link = link.next_link
            p += 1
        if positions:
            return positions
        return link_data, "Not found"


ll = LinkedList()
[ll.append_link(i) for i in ("A", "A", "A", "B", "C", "C", "D")]

def show():
    L = ll.head
    s = ""
    while L:
        s += str(L.data)
        L = L.next_link
    print(s)

show()
ll.delete_links_with_data("D")
show()
print(ll.get_positions_of("D"))
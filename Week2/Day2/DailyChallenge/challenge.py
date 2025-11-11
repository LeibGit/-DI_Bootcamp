from math import ceil as c
class Pagination:
    def __init__(self, items=None, page_size=10):
        if items == None:
            self.items = []
        self.items = items
        self.page_size = page_size
        self.current_idx = 0
        self.total_pages = c(len(self.items) / self.page_size)
    
    def get_visible_items(self):
        start = self.current_idx * self.page_size
        end = start + self.page_size
        print(self.items[start:end])
        return self.items[start:end]

    def go_to_page(self, page_num):
        if 1 <= page_num <= self.total_pages:
                self.current_idx = page_num - 1
                print(f"You are on page: {page_num}")
                return self.get_visible_items()
        else:
            raise ValueError(f"Enter a page that exists. There are only {self.total_pages} pages.")
        
    def first_page(self):
        self.current_idx = 0
        print(f"You are on page: 1")
        return self.get_visible_items()

    def last_page(self):
        self.current_idx = self.total_pages -1
        print(f"You are on page: {self.total_pages}")
        return self.get_visible_items()

    def next_page(self):
        if self.current_idx == 0:
            self.current_idx = 2
            print(f"You are now on page: {self.current_idx}")
            return self.get_visible_items()
        elif self.current_idx + 1 > 1 and self.current_idx + 1 < self.total_pages:
            self.current_idx += 1
            print(f"You are now on page: {self.current_idx + 1}")
            return self.get_visible_items()
        else:
            raise ValueError("You are already on the last page.")


        
    def previous_page(self):
        if self.current_idx == 0:
            print("You are already on the first page.")

test = Pagination(["a", "b", "c", "d", "e", "f"], 2)
"""
test.get_visible_items()
test.go_to_page(3)
test.first_page()
test.last_page()
"""
test.go_to_page(1)
test.next_page()
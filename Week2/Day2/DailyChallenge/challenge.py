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
                return self
        else:
            raise ValueError(f"Enter a page that exists. There are only {self.total_pages} pages.")
        
    def first_page(self):
        self.current_idx = 0
        return self

    def last_page(self):
        self.current_idx = self.total_pages-1
        return self

    def next_page(self):  
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
            return self
        else:
            raise ValueError("You are already on the last page.")
        
    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
            return self
        else:
            raise ValueError("No more previous pages.")
    
    def __str__(self):
        return f"Page {self.current_idx + 1} of {self.total_pages}"

if __name__=='__main__':
    test = Pagination(["a", "b", "c", "d", "e", "f"], 2)

    print(test)  # Page 1 of 3
    print(test.get_visible_items())  # ['a', 'b']

    test.next_page()
    print(test)  # Page 2 of 3
    print(test.get_visible_items())  # ['c', 'd']

    test.last_page()
    print(test)  # Page 3 of 3
    print(test.get_visible_items())  # ['e', 'f']
# 第一题 面向对象的海盗
class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
    def is_worth_it(self):
        return self.draft > 20 + (1.5 * self.crew)
    
# 第二题 搭建积木
class Block(object):
    def __init__(self, wlh):
        self.w, self.l, self.h = w,l,h = wlh
        self.v = w*h*l
        self.a = 2 * (w*l + w*h + l*h)
    
    def get_width(self):        return self.w
    def get_length(self):       return self.l
    def get_height(self):       return self.h
    def get_volume(self):       return self.v
    def get_surface_area(self): return self.a
    
# 第三题 分页助手
class PaginationHelper:
    def __init__(self, collection, items_per_page):
        self._item_count = len(collection)
        self.items_per_page = items_per_page

    def item_count(self):
        return self._item_count

    def page_count(self):
        return -(self._item_count // -self.items_per_page)

    def page_item_count(self, page_index):
        return min(self.items_per_page, self._item_count - page_index * self.items_per_page) \
            if 0 <= page_index < self.page_count() else -1

    def page_index(self, item_index):
        return item_index // self.items_per_page \
            if 0 <= item_index < self._item_count else -1

# 第四题 向量（Vector）类

import numpy as np

class Vector(np.ndarray):
    def __new__(cls, input_array, info=None):
        return np.asarray(input_array).view(cls)

    def add(self, vector):
        return self + vector

    def subtract(self, vector):
        return self - vector

    def norm(self):
        return np.linalg.norm(self)
    
    def equals(self, vector):
        return np.all(self == vector)

    def __str__(self):
        return "({})".format(",".join([str(i) for i in self]))
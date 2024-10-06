from math import ceil
from typing import List


class PhotoAlbum:
    PHOTOS_PER_PAGE: int = 4
    DASHES_TO_COUNT = 11
    SYMBOL_TO_DISPLAY = "-"

    def __init__(self, pages: int):
        self.pages = pages
        self.photos: List[List[str]] = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / cls.PHOTOS_PER_PAGE))

    def add_photo(self, label: str):
        for page in range(self.pages):
            if len(self.photos[page]) < 4:
                slot = len(self.photos[page]) + 1
                self.photos[page].append(label)

                return f"{label} photo added successfully on page {page + 1} slot {slot}"

        return "No more free slots"

    def display(self):
        display_result = [
            self.DASHES_TO_COUNT * self.SYMBOL_TO_DISPLAY
        ]

        for page in self.photos:
            display_result.append(("[] " * len(page)).rstrip())
            display_result.append(self.DASHES_TO_COUNT * self.SYMBOL_TO_DISPLAY)

        return '\n'.join(display_result)


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
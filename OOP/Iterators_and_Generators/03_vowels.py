class vowels:
    def __init__(self, string: str):
        self.string = string
        self.vowels = ['a', 'e', 'i', 'o', 'u', 'y']
        self.all_vowels = [el for el in self.string if el.lower() in self.vowels]
        self.current_index = - 1

    def __iter__(self):
        return self


    def __next__(self):
        self.current_index += 1
        if self.current_index == len(self.all_vowels):
            raise StopIteration
        return self.all_vowels[self.current_index]

    # def __next__(self):
    #     self.current_index += 1
    #     if self.current_index == len(self.string):
    #         raise StopIteration
    #
    #     if self.string[self.current_index].lower() in self.vowels:
    #         return self.string[self.current_index]
    #     else:
    #         return self.__next__()

my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
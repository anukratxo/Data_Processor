class data_processor:
    def __init__ (self, list, dict, string):
        self.list = list
        self.dict = dict
        self.string = string

    def rev_func (self):
        (self.list).reverse()
        b = self.string[::-1]
        return self.list,b
    
    def capital(self):
        a = (self.string).upper()
        for i in range(0,len(self.list)):
            if type(self.list[i]) == str:
                (self.list[i]) = (self.list[i]).upper()
        for i in self.dict:
            if type(self.dict[i]) == str:
                self.dict[i] = (self.dict[i]).upper()
        return a, self.list, self.dict
    
    def summary_list (self):
        a = b = c = 0
        for i in self.list:
            if type(i) == str:
                a = a+1
            elif type(i) == int:
                b = b+1
            else:
                c = c+1
        print(f"the stats of list is: str = {a} | int = {b} | other = {c}")
        
#FOR TESTING I USED AI FOLLOW UP:
# Sample inputs
my_list = ["apple", 42, "banana", 3.14, "cat"]
my_dict = {"name": "anukrat", "city": "jaipur", "age": 22}
my_string = "helloWorld"

# Create an object of data_processor
processor = data_processor(my_list, my_dict, my_string)

# Test rev_func
rev_list, rev_string = processor.rev_func()
print("Reversed list:", rev_list)
print("Reversed string:", rev_string)

# Test capital
cap_string, cap_list, cap_dict = processor.capital()
print("Capitalized string:", cap_string)
print("Capitalized list:", cap_list)
print("Capitalized dict:", cap_dict)

# Test summary_list

processor.summary_list()

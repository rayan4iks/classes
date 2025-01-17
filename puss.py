# Task 1
# class Book:
#     def __init__(self, title, author, year):
#         self._title = title
#         self._author = author
#         self._year = year

#     def info(self):
#         return self._title, self._author, self._year
    
# book1 = Book('Kolobok', 'Russian national fairytale', '1873')
# print(book1.info())

# Task 2
# class Point:
#     def __init__(self, x_coordinate, y_coordinate):
#         self._x_coordinate = x_coordinate
#         self._y_coordinate = y_coordinate

#     def distance_to_zero(self):
#         distance = (self._x_coordinate ** 2 + self._y_coordinate ** 2) ** 0.5
#         return distance
    
# point1 = Point(6, 8)
# print(point1.distance_to_zero())

# Task 3
# class Counter:
#     def __init__(self):
#         self.value = 0

#     def increment(self):
#         self.value += 1

#     def decrement(self):
#         self.value -= 1

#     def reset(self):
#         self.value = 0

# counter = Counter()

# counter.increment()
# print(counter.value)

# counter.decrement()
# print(counter.value)

# counter.reset()
# print(counter.value)

# Task 4
# class Animal():
#     def __init__(self, name, sound):
#         self.name = name
#         self.sound = sound

# class Dog(Animal):
#     def __init__(self, name, sound):
#         super().__init__(name, sound)

# class Cat(Animal):
#     def __init__(self, name, sound):
#         super().__init__(name, sound)

# dog = Dog('Bobik', 'gav')
# cat = Cat('Murzik', 'meow')
# print(dog.name, dog.sound)
# print(cat.name, cat.sound)

# Task 5
# class BankAccount():
#     def __init__(self):
#         self.__balance = 0

#     def deposit(self, amount):
#         self.__balance += amount

#     def withdraw(self, amount):
#         if self.__balance - amount >= 0:
#             self.__balance -= amount
#         else:
#             return 'unavailable'
        
#     def get_balance(self):
#         return self.__balance

# acc = BankAccount()
# acc.deposit(10000)
# print(acc.get_balance())
# acc.withdraw(3000)
# print(acc.get_balance())
# print(acc.get_balance())

# Task 6
# class Store():
#     def __init__(self, name):
#         self.name = name
#         self.items = []

#     def add_items(self, item):
#         self.items.append(item)

#     def remove_items(self, item):
#         if item in self.items:
#             self.items.remove(item)
#             print(f"Item '{item}' removed.")
#         else:
#             print(f"Item '{item}' does not exist.")

#     def display(self):
#         return self.items
    
# def main():
#     store = Store(input('Enter store name: '))
    
#     while True:
#         print('1. Add item')
#         print('2. Remove item')
#         print('3. See all items')

#         choice = input('Choose an option: ')

#         if choice == '1':
#             item_name = input('Enter item: ')
#             store.add_items(item_name)

#         elif choice == '2':
#             item_name = input('Enter item to remove: ')
#             store.remove_items(item_name)

#         elif choice == '3':
#             print(store.display())

#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == '__main__':
#     main()


# Task 7
# class Shape():
#     def __init__(self):
#         pass

#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__()
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2

# class Square(Shape):
#     def __init__(self, length):
#         super().__init__()
#         self.length = length

#     def area(self):
#         return self.length ** 2

# circle = Circle(7)
# square = Square(13)

# print(circle.area(), square.area())


# Task 8
class User():
    def __init__(self, username, email):
        self.username = username
        self.email = email

        if '@' not in self.email:
            raise ValueError
        
user1 = User('Rayana', 'Rayanaemail.com')
print(user1.email, user1.username)
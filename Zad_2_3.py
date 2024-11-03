class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"{self.city}, {self.street}, Kod pocztowy: {self.zip_code}, Otwarte: {self.open_hours}, Telefon: {self.phone}"

class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"Pracownik: {self.first_name} {self.last_name}, Data zatrudnienia: {self.hire_date}, Data urodzenia: {self.birth_date}, Adres: {self.street}, {self.city}, {self.zip_code}, Telefon: {self.phone}"

class Student:
    def __init__(self, first_name, last_name, id):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    def __str__(self):
        return f"{self.first_name} {self.last_name}, ID: {self.id}"

class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"\nAutor: {self.author_name} {self.author_surname}, Data publikacji: {self.publication_date}, Liczba stron: {self.number_of_pages}, Biblioteka: {self.library}"

class Order:
    def __init__(self, id, employee, student, books, order_date):
        self.id=id
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_str = ', '.join([str(book) for book in self.books])
        return f"Zamówienie numer {self.id}:\n{self.employee}, \nStudent: {self.student}, \nKsiążki: {books_str}, \nData: {self.order_date}"


library1 = Library("Katowice", "Bankowa", "40-007", "8-18", "123456789")
library2 = Library("Rybnik", "Rudzka", "44-200", "9-17", "987654321")

book1 = Book(library1, "2022-01-01", "George", "Orwell", 300)
book2 = Book(library1, "2021-05-05", "Mark", "Twain", 250)
book3 = Book(library2, "2020-03-03", "Colleen", "Hoover", 150)
book4 = Book(library2, "2019-12-12", "John", "Green", 400)
book5 = Book(library1, "2018-08-08", "Ewa", "Nowak", 500)

employee1 = Employee("Anna", "Nowak", "2020-01-01", "1980-05-05", "Katowice", "Bogucicka", "40-215", "111222333")
employee2 = Employee("Jan", "Kowalski", "2019-03-01", "1975-04-04", "Katowice", "Bankowa", "40-007", "444555666")
employee3 = Employee("Maria", "Wiśniewska", "2021-07-01", "1985-06-06", "Rybnik", "Rudzka", "40-200", "777888999")

student1 = Student("Katarzyna", "Wysoka",  1)
student2 = Student("Tomasz", "Miły",  2)
student3 = Student("Mariusz", "Kowal",  3)

order1 = Order(1, employee1, student1, [book1, book2], "2024-01-01")
order2 = Order(2, employee2, student2, [book3, book4, book5], "2024-10-28")

print(order1)
print(order2)
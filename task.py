from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value: str):
        if not isinstance(value, str) or not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must be exactly 10 digits.")
        super().__init__(value)


class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones: list[Phone] = []

    def add_phone(self, phone_number: str):
        phone = Phone(phone_number)
        self.phones.append(phone)

    def remove_phone(self, phone_number: str):
        self.phones = [p for p in self.phones if p.value != phone_number]

    def edit_phone(self, old_number: str, new_number: str):
        for p in self.phones:
            if p.value == old_number:
                p_new = Phone(new_number)
                p.value = p_new.value
                return
        raise ValueError("Old phone not found or new phone invalid")

    def find_phone(self, phone_number: str):
        for p in self.phones:
            if p.value == phone_number:
                return p
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str):
        return self.data.get(name)

    def delete(self, name: str):
        if name in self.data:
            del self.data[name]

    def __str__(self):
        if not self.data:
            return ""
        return "\n".join(str(rec) for rec in self.data.values())

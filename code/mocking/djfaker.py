'''
    example faker script
'''
from faker import Faker
from faker.config import AVAILABLE_LOCALES
import dumper

fake = Faker('en_GB')
print(f"name: {fake.name()}")
print(f"date of birth: {fake.date_of_birth()}")
print(f"address: {fake.address()}")
print(f"country: {fake.country()}")
print(f"email: {fake.email()}")

localelist = list(AVAILABLE_LOCALES)

print(f"text: {fake.text()}")
print(f"paragraph: {fake.paragraph()}")
print(f"paragraphs: {fake.paragraphs()}")
print(f"word: {fake.word()}")
print(f"words: {fake.words(6)}")
words = ['one', 'two', 'three', 'four', 'five']
print(f'currency: {fake.currency()}')
print(f'currency name: {fake.currency_name()}')

print(f'currency code: {fake.currency_code()}')

profile1 = fake.simple_profile()
profile2 = fake.simple_profile('M')
profile3 = fake.simple_profile('F')
print('-------------------------')
dumper.dump(profile1)
print('-------------------------')
dumper.dump(profile2)
print('-------------------------')
dumper.dump(profile3)
print('-------------------------')

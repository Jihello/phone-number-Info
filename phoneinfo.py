import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone

a = input("Enter phone number: ")
phone_number = phonenumbers.parse(a)
print("Reigion")
print(geocoder.description_for_number (phone_number, "en"))
print("Service provider")
print(carrier.name_for_number(phone_number, "en"))
valid = phonenumbers.is_valid_number(phone_number)
  
# Checking possibility of a number
possible = phonenumbers.is_possible_number(phone_number)
  
# Printing the output
print("valid")
print(valid)
print("possible")
print(possible)

print(timezone.
time_zones_for_number)
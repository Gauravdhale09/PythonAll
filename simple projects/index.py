import phonenumbers
#from text import number1
from phonenumbers import geocoder
number1 = input("Input the number with country code=")
ch_number = phonenumbers.parse(number1, "CH")
print(geocoder.description_for_number(ch_number,"en"))
from phonenumbers import carrier
service_provider = phonenumbers.parse(number1, "RO")
print(carrier.name_for_number(service_provider, "en"))

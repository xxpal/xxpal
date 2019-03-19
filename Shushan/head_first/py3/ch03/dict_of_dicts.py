# pprint can take any data structure and display it in a easier-to-read format
# pprint is a shorthand for "pretty print"
import pprint


people = {}

people['Ford'] = {'Name': 'Ford Prefect',
                  'Gender': 'Male',
                  'Occupation': 'Researcher',
                  'Home Planet': 'Betelgeuse Seven'}

people['Arthur'] = {'Name': 'Arthur Dent',
                    'Gender': 'Male',
                    'Occupation': 'Sandwich-Maker',
                    'Home Planet': 'Earth'}

people['Trillian'] = {'Name': 'Tricia McMillan',
                      'Gender': 'Female',
                      'Occupation': 'Mathematician',
                      'Home Planet': 'Earth'}

people['Robot'] = {'Name': 'Marvin',
                   'Gender': 'Unknown',
                   'Occupation': 'Paranoid Android',
                   'Home Planet': 'Unknown'}

print(people)
pprint.pprint(people)

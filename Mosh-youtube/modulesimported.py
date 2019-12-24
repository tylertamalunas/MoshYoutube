# imports the entire module from converters.py
from modules import converters

print(converters.kg_to_lbs(70))

# imports just the function/class from the module
from modules.converters import lbs_to_kg

print(lbs_to_kg(100))

import converters  # import the WHOLE MODULE !!
from converters import kg_to_lbs  # import only functions we need

import utils # import MODULE

print(kg_to_lbs(100))

print(converters.kg_to_lbs(int(input("Weight: "))))


numbers = [10,3,6,2]
maximum = utils.find_max(numbers)

print(maximum)

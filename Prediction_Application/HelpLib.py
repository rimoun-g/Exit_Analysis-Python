import numpy as np
class convert():
    pass
	# converting dictionary to list
    def list_to_dict(lst):
        """This function enumerates a list and return enumerated list in form of dictionary
        input: list
        output: dictionary
		example:
		>>list_to_dict(['a','b','c'])
		>>{'a':0,'b':1,'c':2}
        """
        dictionary = {}
        for value, key in enumerate(lst):
            dictionary[key] = value
        return dictionary

    # converting decimal number as years and months
    def dec_to_year(dec):
        """This function converts the decimal to years and month
        input: float
        output: int, int
		example:
		>>dec_to_year(1.5)
		>>1 , 6 
        one year and six months
        """
        year = int(dec)
        month = ((dec - year) * 365)/30
        mnth = int(month)
        return year, mnth
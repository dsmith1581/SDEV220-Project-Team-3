# Project Team 3 (Alexander Smith, Daniel Smith, John Sharp)
# Ivy Tech Asset Manager - Validation Functions
# Implements various validation functions which can be shared across class setter methods

import re


# Checks if each character in a string is in the allowed character list
# Does not allow for empty string
def has_valid_characters(input):
	allowed_chars = r" !$%&()*+-.,'/:[<=>?@[\]^_{|}~abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
	pattern = f'^[{re.escape(allowed_chars)}]+$'

	return bool(re.match(pattern, input))

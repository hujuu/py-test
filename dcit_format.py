example_dict = {
	'float_number':1324.212312,
	'very_large_integer':4380549834,
	'percentage': .324,
}

string_print = "float: {float_number:.4f}\n"
string_print += "integer: {very_large_integer: ,}\n"
string_print += "percentage: {percentage: .2%}"

print(string_print.format(**example_dict))
def verify_orders(register1, register2, served_orders):
	
  # returns False if there are any excess completed orders or missing orders
	if len(served_orders) != len(register1) + len(register2):
		return False
	
	r1_index = 0
	r2_index = 0
	
  # returns False if an element in served_orders is not the "next" element in register1 or register2 
  # else increments pointer for relevent register
	for order in served_orders:
		if r1_index < len(register1) and order == register1[r1_index]:
			r1_index += 1
		elif r2_index < len(register2) and order == register2[r2_index]:
			r2_index += 1
		else:
			return False
	
  # returns True if no above failure conditions are found
	return True

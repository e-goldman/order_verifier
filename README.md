# order_verifier
Simple exercise 2 - Verify that customer orders were completed in the correct order

Source: Interview Cake

Premise:

A cafe is concerned that their customers are not correctly being served on a first-come, first-served basis. Write a function
that verifies this based on daily records of orders placed and orders completed. It should return boolean T/F to indicate
whether or not a day's orders were done correctly.

It is also possible that orders are being missed altogether, or that the kitchen is completing orders that do not exist. 
The function should account for these cases by also treating them as failure.

It should return True only if all purchases were accounted for and completed in the correct order.

The function must complete in O(n) time and require only O(1) additional space.

Additional details:

The orders come from two registers. For each function call, the cafe will provide two lists of order numbers, one for each 
of the registers. They are sorted from least to most recently ordered and stored as arbitrary unique integers. 

The cafe will also provide a third list containing orders completed by the kitchen.

Sample data:

register1 = [1, 3, 5]
register2 = [2, 4, 6]
served_orders = [1, 2, 4, 6, 5, 3]

This dataset returns False because order 5 was served before order 3.

register1 = [17, 8, 24]
register2 = [12, 19, 2]
served_orders = [17, 8, 12, 19, 24, 2]

This dataset returns True because the orders from each register were completed first-come, first-served. As noted above,
the order numbers are arbitrary. They may or may not be in ascending order.

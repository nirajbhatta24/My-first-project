#price of a house is $1M. IF buyer has good credit, they need to put down 10% otherwise they need to put down 20%.
# print the down payment.


price_of_house=1000000
good_credit=False
if good_credit:
    down_payment=0.1*price_of_house
else:
    down_payment=0.2*price_of_house
print(f"Down Payment : ${down_payment}")


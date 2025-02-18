star20 = '*' * 20
print(star20)
print('My Coffee and Muffin Shop')

# prints beginning text ^

print("Number of coffees bought?: ")
coffee = int(input(""))
print("Number of muffins bought?: ")
muffin = int(input(""))
print(star20 , '\n')
print(star20) 

# prints input from user^

print('My Coffee and Muffin Shop Reciept')
print(coffee, ' Coffee at $5 each: ', end='')
coTotal = coffee * 5
print('$ ', coTotal, '.00' )
print(muffin, ' Muffin at $4 each: ', end='')
muTotal = muffin * 4
print('$ ', muTotal, '.00')

# prints everything before tax^

tax = float(0.06 * (coTotal + muTotal))
def tot_products(sum):
    sum = coTotal + muTotal + tax
    return sum

# a function that returns the total of everything^

print('6% tax: $', f'{tax:.02f}')
total = tot_products (coTotal + muTotal + tax)
print('---------')
print('Total: $', total)
print(star20, '\n')

# returns the total of the order^

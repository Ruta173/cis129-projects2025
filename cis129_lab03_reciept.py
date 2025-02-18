star20 = '*' * 20
print(star20)
print('My Coffee Shop')

# prints beginning text ^

print("Number of coffees bought?: ")
coffee = int(input(""))
print("Number of muffins bought?: ")
muffin = int(input(""))
print("Number of cake pops bought?: ")
cakePop = int(input(""))
print("Number of special waters bought?: ")
specWat = int(input(""))
print(star20 , '\n')
print(star20)

# prints input from user^

print('My Coffee Shop Receipt')
if coffee > 1:
    print(coffee, 'Coffees at $5 each: ', end='')
    coTotal = coffee * 5
    print('$', coTotal, '.00')
else:
    print(coffee, ' Coffee at $5 each: ', end='')
    coTotal = coffee * 5
    print('$', coTotal, '.00')
if muffin > 1:
    print(muffin, ' Muffins at $4 each: ', end='')
    muTotal = muffin * 4
    print('$', muTotal, '.00')
else:
    print(muffin, ' Muffin at $4 each: ', end='')
    muTotal = muffin * 4
    print('$', muTotal, '.00')
if cakePop > 1:
    print(cakePop, ' Cake Pops at $1 each: ', end='')
    popTotal = cakePop * 1
    print('$', popTotal, '.00')
else:
    print(cakePop, ' Cake Pop at $1 each: ', end='')
    popTotal = cakePop * 1
    print('$', popTotal, '.00')
if specWat > 1:
    print(specWat, ' Special waters at $8 each: ', end='')
    watTotal = specWat * 8
    print('$', watTotal, '.00')
else:
    print(specWat, ' Special water at $8 each: ', end='')
    watTotal = specWat * 8
    print('$', watTotal, '.00')

# displays totals before tax^

sum = (coTotal + muTotal + popTotal + watTotal)
tax = (sum * .06)
def tot_products(sum):
    sum = coTotal + muTotal + popTotal + watTotal + tax
    return sum

# a function that returns the total of everything^

print('6% tax: $', f'{tax:.02f}')
total = tot_products(coTotal + muTotal + popTotal + watTotal + tax)
print('---------')
print('Total: $', f"{total:.2f}")
print(star20, '\n')

# displays the total of the order^

print(star20, '\n')
if total >= 50:
    print('Wow! Big spender, huh? Thank you so much for your business!')
    print('We hope to see you again!', '\n')
else:
    print('Thank you for Shopping here. Come again.', '\n')

# a very nice thank you message^

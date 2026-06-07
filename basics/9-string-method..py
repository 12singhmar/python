name = "alpha beta"
phone = "123-456-789"

#result = len(name)
#result = name.find(" ")    - blank space exists at 5th place
#result = name.rfind(" ")   - finds from backside (reverse)
#result = name.capitalise() - ouput = Alpha beta
#reesult = name.upper()     - output = ALPHA BETA
#result = name.lower()      - output = alpha beta
#result = phone.isdigit()   - FALSE as it contains -
#result = name.isalpha()    - FALSE as it contains " " too
#result = phone.replace("-"," ")  - replaces - with blanks
#result = name.count("a")   - count only used when str
#print(result)

print(help(str))


#----------------------------------------------------------------------------

#indexing
#credit card number = ccno

ccno = "1234 5678"

print(ccno[0])

#the way it works is start:end(not included):step
# so 1:5:2 states start from 1 to 4 in steps of 2
print(ccno[1:5:2])

# :5 means from start to 4
# 0: means from 0 to end
# ::2 means from start to end in steps of 2

#reversing-
print(ccno[::-1])

#-x means xth from the end
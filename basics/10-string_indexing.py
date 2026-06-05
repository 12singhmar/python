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
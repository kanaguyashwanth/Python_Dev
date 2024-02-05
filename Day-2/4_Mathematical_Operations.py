# MATHEMATICAL OPERATIONS

print (3+5)
print (7-4)
print (3*2)
print (type(6 / 3))
print (2**2) # 2 power 2 = 4

# When there are more than one operation on same line:
# ORDER PRIORITY
'''
ORDER: [Same line = Equally important, Most left = More priority(Calculation goes from left to right]
()
**
* /
+ -

PEMDASLR:
() - Paranthesis
** - Exponents
*  - Multiplication
/  - Division
+  - Addition
-  - Subtraction
LR - Left to Right
'''


print (3 * 3 + 3 / 3 - 3) # OUTPUT: 7.0, here, the * and the / are equally important and thus, they both happen once!
                          # 3*3 + 3/3 - 3 (Calculates from LEFT to RIGHT)
                          # 9 + 1.0 - 3
                          # 10.0 - 3
                          # 7.0 (USE DEBUGGER TO CHECK STEP-BY-STEP)
                          
print (3 * (3 + 3) / 3 - 3) # OUTPUT: 3.0

from arraystack import ArrayStack

#function to define if the character is an operand from A to Z
def isOperand(c):
    return c.isalpha()
    #this is a pythin built in method which returns true if its a letter of the alphabet, either capital or small

operators="=+-*/^"

#function to chech is the character is an operator +*-/^
def isOperator(c):
    return c in operators

def getPrecedence(c):
    result = 0

    for char in operators:
        result += 1

        if char == c:
            if c in '-/':
                result -= 1
            break

    return result

def inToPost(expression):
    #creating a stack
    stack1 = ArrayStack()    
    #having a empty string for the result
    postfix = "" 
               
    #loop
    for char in expression:
        if isOperand(char):
            postfix += char
        elif isOperator(char):
            while True:
                if stack1.isEmpty() or stack1.peek() == '(':
                    stack1.push(char)
                    break
                else:
                    topChar = stack1.peek()
                    pC = getPrecedence(char)
                    pTC = getPrecedence(topChar)

                    if pC > pTC:
                        stack1.push(char)
                        break
                    else:
                        postfix += stack1.pop()
        elif char == '(':
            stack1.push(char)
        elif char == ')':
            cpop = stack1.pop()
            while cpop != '(':
                postfix += cpop
                cpop = stack1.pop()

    # Pop remaining operators
    while not stack1.isEmpty():
        postfix += stack1.pop()

    return postfix


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# test
infixexpression= input("please enter a infix expression: ")

postfix = inToPost(infixexpression)
print(f'Infix: {infixexpression} -> Postfix: {postfix}')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#code for evaluating postfix evaluation

def evaluatePostfix(postfix):
    stack2=ArrayStack()
    #will use a dictionary to hold the values of the operands, e.g: A:10
    dictValues={}
    for char in postfix:
        if char.isalpha():
            if char not in dictValues:
                values=float(input(f"please enter the value for {char}: "))
                dictValues[char]=values
            stack2.push(dictValues[char])
        elif char in operators:
            right=stack2.pop()
            left=stack2.pop()

            if char == '+':
                result=left+right
            elif char =='-':
                result=left-right
            elif char =='*':
                result=left*right
            elif char =='/':
                result=left/right
            elif char =='^':
                result=left**right
            
            stack2.push(result)

    return stack2.pop()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# test
evaluation=evaluatePostfix(postfix)
print("evaluation result:",evaluation)

def brackets(expression):
    OP_EXPR = ['(', '[', '{']
    CL_EXPR = [')', ']', '}']
    CORR_HT = {OP_EXPR[i]: CL_EXPR[i] for i in range(len(OP_EXPR))}
    stack = []
    for char in expression:
        if char in OP_EXPR:
            stack.append(char)
        elif char in CL_EXPR and stack != [] and CORR_HT[stack[-1]] == char:
            stack.pop()
        elif char in CL_EXPR:
            return False

    return stack == []

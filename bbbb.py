def arithmetic_arranger(problems, show_answers=True):
    if len(problems)>5:
        return("Error: Too many problems.")
    operations = list(map(lambda x: x.split()[1], problems))
    if set(operations) != {'+', '-'} and len(set(operations)) != 2:
        return ("Error: Operator must be '+' or '-'.")
    l1 = ""
    l2 = ""
    l3 = ""
    l4 = ""
    for eq in problems:
        num1 = eq[ : eq.find(' ')]
        num2 = eq[ eq.rfind(' ')+1:]
         
        op = eq[[eq.find(char) for char in ['+','-'] if char in eq][0]]
        if op=='+':
            result = str(int(num1)+int(num2))
        elif op=='-':
            result = str(int(num1)-int(num2))
        width = max(len(num1),len(num2))+2
        l1 = l1+" " * (width - len(num1)) + num1+' '*3
        l2 = l2+op + " " * (width - len(num2) - 1) + num2+' '*3
        l3 = l3+"-" * width +' '*3
        l4 = l4 + " "*(width-len(result))+result+' '*3
    p = l1 + "\n" + l2 + "\n" + l3 + "\n" + l4
    print(p)
    
arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49","151 + 20","201 + 25"], True)

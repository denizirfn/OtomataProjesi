def polishNotasyonu(ifade):  # operatörler sayının önüne alınır
    yigin = []
    operatörler = ['+', '-', '*', '/']

    def operatorSecim(operatör, operand1, operand2):
        if operatör == '+':
            return operand1 + operand2
        elif operatör == '-':
            return operand1 - operand2
        elif operatör == '*':
            return operand1 * operand2
        elif operatör == '/':
            return operand1 / operand2

    semboller = ifade.split()
    for sembol in reversed(semboller):
        if sembol in operatörler:
            operand1 = yigin.pop()
            operand2 = yigin.pop()
            result = operatorSecim(sembol, operand1, operand2)
            yigin.append(result)

        else:
            yigin.append(int(sembol))  # 4 işlem sonucu istediği için int cevrildi
    return yigin[0]


print("lutfen bir ifade giriniz:")
ifade = input()
result = polishNotasyonu(ifade)
print(result)



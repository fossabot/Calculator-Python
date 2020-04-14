import re
import math

class CommandList():
    def check(inputValue):
        value = inputValue.get()
        if inputValue is not None:
            return(value)
        else:
            retun(0)
    def nthRoot(inputValue):
        value = CommandList.check(inputValue)
        if value is not "":
            inputValue.set("√("+value+")")
    def secondPower(inputValue):
        value = CommandList.check(inputValue)
        print(value)
        if value is not "":
            inputValue.set("("+value+")^2")
    def inverseMultiplicative(inputValue):
        value = CommandList.check(inputValue)
        if value is not "":
            value = "1/("+value+")"
        inputValue.set(value)
    def clear(inputValue):
        inputValue.set("")
    def delete(inputValue):
        value = CommandList.check(inputValue)
        inputValue.set(value[:len(value)-1])
    def divide(inputValue):
        inputValue.set(CommandList.check(inputValue)+"/")
    def multiply(inputValue):
        inputValue.set(CommandList.check(inputValue)+"*")
    def minus(inputValue):
        inputValue.set(CommandList.check(inputValue)+"-")
    def plus(inputValue):
        inputValue.set(CommandList.check(inputValue)+"+")
    def plusMinusInversion(inputValue):
        value = CommandList.check(inputValue)

        if value is not 0:
            reValue = re.search("[0-9]+$", value)

            if reValue:
                # získání první pozice
                reValueStart = reValue.start()

                if value[reValueStart-1:reValueStart] == "+":
                    value = value[:reValueStart-1]+"-"+value[reValueStart:]
                elif value[reValueStart-1:reValueStart] == "-":
                    value = value[:reValueStart-1]+"+"+value[reValueStart:]
                else:
                    value = value[:reValueStart] + "(-" + value[reValueStart:] + ")"
            elif re.search("[)]$", value):
                # spočítání počtu závorek
                start = re.search("[^(]+$", value).start()
                bracketsCount = len(re.findall("[)]+", value[start:]))
                i = 0
                while True:
                    if value[start-1:start] == "(":
                        i = i + 1
                        start = start - 1
                    elif bracketsCount == i and value[start-1:start] == "-":
                        value = value[:start-1] + "+" + value[start:]
                        break
                    elif bracketsCount == i and value[start-1:start] == "+":
                        value = value[:start-1] + "-" + value[start:]
                        break
                    elif bracketsCount == i:
                        value = value[:start] + "(-" + value[start:] + ")"
                        break
                    else:
                        start = start - 1
        inputValue.set(value)
    def decimalSeparator(inputValue):
        value = CommandList.check(inputValue)
        if (value is not None or value is not "") and len(value) >= 1:
            if re.search("[0-9]", value[len(value)-1]):
                value = value+","
        inputValue.set(value)
    def result(inputValue):
        value = CommandList.check(inputValue)

        # python používá jako desetinné znaménko ".", ne české ","
        value = value.replace(",", ".")

        # python má odmocninu jako **, ne ^
        value = value.replace("^", "**")

        # nahrazení odmocniny za python funkci squared (druhá odmocnina)
        value = value.replace("√", "math.sqrt")

        print(value)

        try:
            result = eval(value)
        except:
            result = "ERROR"

        inputValue.set(result)
    def number_nine(inputValue):
        inputValue.set(CommandList.check(inputValue)+"9")
    def number_eight(inputValue):
        inputValue.set(CommandList.check(inputValue)+"8")
    def number_seven(inputValue):
        inputValue.set(CommandList.check(inputValue)+"7")
    def number_six(inputValue):
        inputValue.set(CommandList.check(inputValue)+"6")
    def number_five(inputValue):
        inputValue.set(CommandList.check(inputValue)+"5")
    def number_four(inputValue):
        inputValue.set(CommandList.check(inputValue)+"4")
    def number_three(inputValue):
        inputValue.set(CommandList.check(inputValue)+"3")
    def number_two(inputValue):
        inputValue.set(CommandList.check(inputValue)+"2")
    def number_one(inputValue):
        inputValue.set(CommandList.check(inputValue)+"1")
    def number_zero(inputValue):
        inputValue.set(CommandList.check(inputValue)+"0")

import time

import nsii

# Nsii setup
nsii = nsii.Nsii()

nsii.fps_target = 'max'
nsii.font = ('Consolas', (12, 6))


def resizeX(val):
    """Resize the image to the size of the window"""
    return int(val / 900 * nsii.size[0])


def resizeY(val):
    """Resize the image to the size of the window"""
    return int(val / 1100 * nsii.size[1])


def isClicked(iPosX, iPosY, iSizeX=163, iSizeY=177):
    """
    Function that returns True or False if the mouse is hovering inside defined coordinates
    :param iPosX: Position X of the upper-left pixel of the image
    :param iPosY: Position Y of the upper-left pixel of the image
    :param iSizeX: Size in X axis of the image
    :param iSizeY: Size in Y axis of the image
    :return: True | False
    """
    mPosX, mPosY = nsii.m_pos  # Get the mouse coords
    iSizeX = resizeX(iSizeX)
    iSizeY = resizeY(iSizeY)
    iPosX = resizeX(iPosX)
    iPosY = resizeY(iPosY)
    return iPosX <= mPosX < iPosX + iSizeX and iPosY <= mPosY < iPosY + iSizeY


def calculate(calc):
    """
    Function that calculates a problem told by the user using the PEMDAS technique :
    - Parenthesis
    - Exponents & Square roots
    - Multiply & Divide
    - Add & Subtract
    :param calc: The problem of the user
    :return: str - Solution to the problem
    """
    indMinNum1 = 0
    indMaxNum2 = len(calc)
    num1 = ''
    num2 = ''
    if "(" in calc:  # Parenthesis case
        for ind in range(len(calc)):
            char = calc[ind]
            if char == "(":
                indMinNum1 = ind + 1
            elif char == ")":
                indMaxNum2 = ind
                break
        return calculate(calc[:indMinNum1 - 1] + calculate(calc[indMinNum1:indMaxNum2]) + calc[indMaxNum2 + 1:])

    elif "^" in calc:  # Exponent case
        for ind in range(calc.find('^')):  # Find the first number
            char = calc[ind]
            if char == '^':
                break
            elif char in '+*_/':
                num1 = ''
                indMinNum1 = ind + 1
            else:
                num1 += str(char)

        if calc[calc.find("^") + 1] == "_":
            num2 += "-"
            pos = 2
        else:
            pos = 1

        for ind in range(calc.find('^') + pos, len(calc)):  # Find the second number
            char = calc[ind]
            if char in '+_/*':
                indMaxNum2 = ind - 1
                break
            else:
                num2 += str(char)
        return calculate(calc[:indMinNum1] + str(float(num1) ** float(num2)) + calc[indMaxNum2:])  # calculate the result

    elif "*" in calc:  # Multiply case
        for ind in range(calc.find('*')):
            char = calc[ind]
            if char == '*':
                break
            elif char in '+_/':
                num1 = ''
                indMinNum1 = ind + 1
            else:
                num1 += str(char)

        if calc[calc.find("*") + 1] == "_":
            num2 += "-"
            pos = 2
        else:
            pos = 1

        for ind in range(calc.find('*') + pos, len(calc)):
            char = calc[ind]
            if char in '+_/*':
                indMaxNum2 = ind - 1
                break
            else:
                num2 += str(char)
        return calculate(calc[:indMinNum1] + str(float(num1) * float(num2)) + calc[indMaxNum2:])

    elif "/" in calc:  # Divide case
        for ind in range(calc.find('/')):
            char = calc[ind]
            if char == '/':
                break
            elif char in '+_':
                num1 = ''
                indMinNum1 = ind + 1
            else:
                num1 += str(char)

        if calc[calc.find("/") + 1] == "_":
            num2 += "-"
            pos = 2
        else:
            pos = 1

        for ind in range(calc.find('/') + pos, len(calc)):
            char = calc[ind]
            if char in '+_/':
                indMaxNum2 = ind - 1
                break
            else:
                num2 += str(char)

        if float(num2) != float(0):
            return calculate(calc[:indMinNum1] + str(float(num1) / float(num2)) + calc[indMaxNum2:])
        else:
            print("Error")

    elif "+" in calc:  # Add case
        for ind in range(calc.find('+')):
            char = calc[ind]
            if char == '+':
                break
            elif char in '*_':
                num1 = ''
                indMinNum1 = ind + 1
            else:
                num1 += str(char)

        if calc[calc.find("+") + 1] == "_":
            num2 += "-"
            pos = 2
        else:
            pos = 1

        for ind in range(calc.find('+') + pos, len(calc)):
            char = calc[ind]
            if char in '+_':
                indMaxNum2 = ind - 1
                break
            else:
                num2 += str(char)

        return calculate(calc[:indMinNum1] + str(float(num1) + float(num2)) + calc[indMaxNum2:])

    elif "_" in calc:  # Subtract case
        for ind in range(calc.find('_')):
            char = calc[ind]
            if char == '_':
                break
            else:
                num1 += str(char)

        if calc[calc.find("_") + 1] == "_":
            num2 += "-"
            pos = 2
        else:
            pos = 1

        for ind in range(calc.find('_') + pos, len(calc)):
            char = calc[ind]
            if char == "_":
                indMaxNum2 = ind - 1
                break
            else:
                num2 += str(char)
        if num1 == '':
            num1 = '0'
        return calculate(calc[:indMinNum1] + str(float(num1) - float(num2)) + calc[indMaxNum2:])

    else:  # Return the result
        return f"{float(calc):.3f}"


class Calculator:
    def __init__(self):
        """
        Main function
        """
        self.screen = ''
        self.background = nsii.new_image('image/background.ppm')
        self.numbers = [nsii.new_image('image/0.ppm'), nsii.new_image('image/1.ppm'), nsii.new_image('image/2.ppm'),
                        nsii.new_image('image/3.ppm'), nsii.new_image('image/4.ppm'), nsii.new_image('image/5.ppm'),
                        nsii.new_image('image/6.ppm'), nsii.new_image('image/7.ppm'), nsii.new_image('image/8.ppm'),
                        nsii.new_image('image/9.ppm')]
        self.symbols = [nsii.new_image('image/divide.ppm'), nsii.new_image('image/exp.ppm'),
                        nsii.new_image('image/minus.ppm'), nsii.new_image('image/multiply.ppm'),
                        nsii.new_image('image/parenthesisIn.ppm'), nsii.new_image('image/parenthesisOut.ppm'),
                        nsii.new_image('image/plus.ppm'), nsii.new_image('image/point.ppm')]

    def showChar(self, char, ind):
        """
        Shows the specified character on the screen
        :param char: Character
        :param ind: Index of the character on the screen
        """
        if char.isdigit():
            self.numbers[int(char)].pos = (resizeX(48 + (resizeX(82) + 50) * ind), resizeY(65))
            self.numbers[int(char)].size = (resizeX(82), resizeY(132))
            self.numbers[int(char)].show(hide=(255, 255, 255))
        elif char == '/':
            self.symbols[0].pos = (resizeX(48 + (resizeX(82) + 50) * ind), resizeY(65))
            self.symbols[0].size = (resizeX(82), resizeY(132))
            self.symbols[0].show(hide=(255, 255, 255))
        elif char == '^':
            self.symbols[1].pos = (resizeX(48 + (resizeX(82) + 50) * ind), resizeY(65))
            self.symbols[1].size = (resizeX(82), resizeY(132))
            self.symbols[1].show(hide=(255, 255, 255))
        elif char == '_':
            self.symbols[2].pos = (resizeX(48 + (resizeX(82) + 50) * ind), resizeY(65))
            self.symbols[2].size = (resizeX(82), resizeY(132))
            self.symbols[2].show(hide=(255, 255, 255))
        elif char == '-':
            self.symbols[2].pos = (resizeX(48 + (resizeX(82) + 50) * ind), resizeY(65))
            self.symbols[2].size = (resizeX(82), resizeY(132))
            self.symbols[2].show(hide=(255, 255, 255))
        elif char == '*':
            self.symbols[3].pos = (resizeX(48 + (resizeX(82) + 50) * ind), resizeY(65))
            self.symbols[3].size = (resizeX(82), resizeY(132))
            self.symbols[3].show(hide=(255, 255, 255))
        elif char == '(':
            self.symbols[4].pos = (resizeX(48 + (resizeX(82) + 50) * ind), resizeY(65))
            self.symbols[4].size = (resizeX(82), resizeY(132))
            self.symbols[4].show(hide=(255, 255, 255))
        elif char == ')':
            self.symbols[5].pos = (resizeX(48 + (resizeX(82) + 50) * ind), resizeY(65))
            self.symbols[5].size = (resizeX(82), resizeY(132))
            self.symbols[5].show(hide=(255, 255, 255))
        elif char == '+':
            self.symbols[6].pos = (resizeX(48 + (resizeX(82) + 50) * ind), resizeY(65))
            self.symbols[6].size = (resizeX(82), resizeY(132))
            self.symbols[6].show(hide=(255, 255, 255))
        elif char == '.':
            self.symbols[7].pos = (resizeX(48 + (resizeX(82) + 50) * ind), resizeY(65))
            self.symbols[7].size = (resizeX(82), resizeY(132))
            self.symbols[7].show(hide=(255, 255, 255))

    def showImages(self):
        """
        Manages the things that are shown on the terminal
        """
        self.background.size = nsii.size
        self.background.show()

        maxScreenLen = 10
        if len(self.screen) >= maxScreenLen:
            for ind in range(0, maxScreenLen):
                char = self.screen[-(maxScreenLen - ind)]
                self.showChar(char, ind)
        else:
            for ind in range(0, len(self.screen) % maxScreenLen):
                char = self.screen[-(len(self.screen) % maxScreenLen - ind)]
                self.showChar(char, ind)

        nsii.draw()

    def buttonManagement(self):
        """
        Manages all the button presses
        """
        if nsii.m_click('left'):
            time.sleep(0.1)  # Protection against long mouse press
            if not nsii.m_click('left'):
                if isClicked(9, 280):
                    self.screen += '7'
                elif isClicked(190, 280):
                    self.screen += '8'
                elif isClicked(370, 280):
                    self.screen += '9'
                elif isClicked(550, 280):
                    self.screen += '('
                elif isClicked(730, 280):
                    self.screen += ')'

                elif isClicked(9, 490):
                    self.screen += '4'
                elif isClicked(190, 490):
                    self.screen += '5'
                elif isClicked(370, 490):
                    self.screen += '6'
                elif isClicked(550, 490):
                    self.screen += '*'
                elif isClicked(730, 490):
                    self.screen += '/'

                elif isClicked(9, 705):
                    self.screen += '1'
                elif isClicked(190, 705):
                    self.screen += '2'
                elif isClicked(370, 705):
                    self.screen += '3'
                elif isClicked(550, 705):
                    self.screen += '+'
                elif isClicked(730, 705):
                    self.screen += '_'

                elif isClicked(9, 913):
                    self.screen = self.screen[:-1]
                elif isClicked(190, 913):
                    self.screen += '0'
                elif isClicked(370, 913):
                    self.screen += '.'
                elif isClicked(550, 913):
                    self.screen += '^'
                elif isClicked(730, 913):
                    if self.screen:
                        temp = calculate(self.screen)
                        if '.' in temp:
                            while True:
                                nb = temp[-1]
                                if nb == '.':
                                    temp = temp[:-1]
                                    break
                                elif nb == '0':
                                    temp = temp[:-1]
                                else:
                                    break

                        self.screen = temp

                elif isClicked(8, 8, 884, 262):
                    self.screen = ''


if __name__ == '__main__':
    pass
    c = Calculator()
    while True:
        c.showImages()
        c.buttonManagement()
        nsii.name = "Calculatrice"

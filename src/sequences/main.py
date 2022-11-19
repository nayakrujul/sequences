from math import *
from string import *
import statistics
from sequences.List import List

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

def run(code, _stack=(), _lst=(), u=None, _inputs=()):
    index = 0
    stack = List(_stack)
    lst = List(_lst)
    inputs = List(_inputs)
    while index < len(code):
        char = code[index]
        if char in '0123456789.':
            string = char
            index += 1
            try:
                while code[index] in '0123456789.':
                    string += code[index]
                    index += 1
            except:
                pass
            index -= 1
            while string[0] == '0':
                stack.push(0)
                try:
                    string = string[1:]
                except:
                    break
            stack.push(eval(string))
        elif char == '"':
            string = char
            index += 1
            try:
                while code[index] != '"':
                    string += code[index]
                    index += 1
            except:
                pass
            string += code[index]
            stack.push(eval(string))
        elif char == 'i':
            stack.push(int(input()))
            inputs.push(stack[0])
        elif char == 'I':
            stack.push(list(map(int, input().split())))
            inputs.push(stack[0])
        elif char == 't':
            stack.push(input())
            inputs.push(stack[0])
        elif char == 'T':
            stack.push(input().split())
            inputs.push(stack[0])
        elif char == 's':
            stack.push(list(stack).copy())
        elif char == 'S':
            stack.push(List(stack.first(list)).sum)
        elif char == 'P':
            stack.push(List(stack.first(list)).product)
        elif char == 'M':
            stack.push(max(stack.first(list)))
        elif char == 'm':
            stack.push(min(stack.first(list)))
        elif char == 'G':
            stack.push(gcd(stack.first(list)))
        elif char == 'L':
            stack.push(lcm(stack.first(list)))
        elif char == 'k':
            stack.push(statistics.mean(stack.first(list) or [0]))
        elif char == 'l':
            stack.push([])
        elif char == 'A':
            stack.push(stack.first(list) + [stack.first(list, False)])
        elif char == 'C':
            a, b = stack.first(list, n=2)
            stack.push(a + b)
        elif char == 'R':
            a = stack.first((list, str))
            if isinstance(a, list):
                stack.push(list(reversed(a)))
            else:
                stack.push(''.join(reversed(a)))
        elif char == 'D':
            stack.push(list(set(stack.first(list))))
        elif char == 'r':
            a, b = stack.first(str, n=2)
            stack.push(b.split(a))
        elif char == 'J':
            stack.push(stack.first(str).join(stack.first(list)))
        elif char == 'w':
            stack.push(str(stack[0]))
        elif char == 'W':
            stack.push(list(map(str, stack.first(list))))
        elif char == 'n':
            stack.push(int(stack[0]))
        elif char == 'N':
            stack.push(list(map(int, stack.first(list))))
        elif char == 'c':
            stack.push(list(str(stack[0])))
        elif char == 'o':
            a = stack.first(list).copy()
            a.remove(stack.first(list, False))
            stack.push(a)
        elif char == 'O':
            a = stack.first(list).copy()
            b = stack.first(list, False)
            while b in a:
                a.remove(b)
            stack.push(a)
        elif char == 'x':
            stack.push(list(range(stack.first(int))))
        elif char == 'X':
            stack.push(list(range(len(stack.first((list, str))))))
        elif char == 'z':
            stack.push(len(stack.first((list, str))))
        elif char == 'e':
            stack.push(stack.first((list, str))[stack.first(int)])
        elif char == '+':
            b, a = stack.first((int, float), n=2)
            stack.remove(a)
            stack.remove(b)
            stack.push(a + b)
        elif char == '-':
            b, a = stack.first((int, float), n=2)
            stack.remove(a)
            stack.remove(b)
            stack.push(a - b)
        elif char == '*':
            b, a = stack.first((int, float), n=2)
            stack.remove(a)
            stack.remove(b)
            stack.push(a * b)
        elif char == '/':
            b, a = stack.first((int, float), n=2)
            stack.remove(a)
            stack.remove(b)
            stack.push(a / b)
        elif char == '^':
            b, a = stack.first((int, float), k=2)
            stack.remove(a)
            stack.remove(b)
            stack.push(a ** b)
        elif char == '%':
            b, a = stack.first((int, float), n=2)
            stack.push(a % b)
        elif char == 'K':
            b, a = stack.first((int, float), n=2)
            stack.remove(a)
            stack.remove(b)
            stack.push(list(divmod(a, b)))
        elif char == '>':
            b, a = stack.first((int, float), n=2)
            stack.remove(a)
            stack.remove(b)
            stack.push(a > b)
        elif char == 'q':
            b, a = stack.first((int, float), n=2)
            stack.remove(a)
            stack.remove(b)
            stack.push(a >= b)
        elif char == '<':
            b, a = stack.first((int, float), n=2)
            stack.remove(a)
            stack.remove(b)
            stack.push(a < b)
        elif char == 'Q':
            b, a = stack.first((int, float), n=2)
            stack.remove(a)
            stack.remove(b)
            stack.push(a <= b)
        elif char == '=':
            stack.push(stack[0] == stack[1])
        elif char == 'p':
            stack.push(stack[0] != stack[1])
        elif char == '&':
            stack.push(stack[0] and stack[1])
        elif char == '|':
            stack.push(stack[0] or stack[1])
        elif char == '@':
            stack.push(bool(stack[0]) ^ bool(stack[1]))
        elif char == '~':
            stack.push(not stack[0])
        elif char == '?':
            if_true = ''
            index += 1
            while code[index] != ':':
                if_true += code[index]
                index += 1
            index += 1
            try:
                if_false = ''
                while code[index] != ';':
                    if_false += code[index]
                    index += 1
            except:
                pass
            if stack[0]:
                stack, lst = run(if_true, stack, lst, u, inputs)
            else:
                stack, lst = run(if_false, stack, lst, u, inputs)
        elif char == '{':
            string = ''
            index += 1
            try:
                while code[index] != '}':
                    string += code[index]
                    index += 1
            except:
                pass
            a = stack.first(str)
            for i in a:
                stack, lst = run(string, [i] + stack, lst, u, inputs)
        elif char == '[':
            string = ''
            index += 1
            try:
                while code[index] != ']':
                    string += code[index]
                    index += 1
            except:
                pass
            a = stack.first(list)
            for i in a:
                stack, lst = run(string, [i] + stack, lst, u, inputs)
        elif char == '\\':
            index += 1
            if isinstance(stack[0], str):
                stack[0] += code[index]
            else:
                stack.push(code[index])
        elif char == 'a':
            stack.push(ascii_lowercase)
        elif char == 'Z':
            stack.push(ascii_uppercase)
        elif char == 'j':
            a, b = stack.first(str, n=2)
            stack.push(b.ljust(stack.first(int), a))
        elif char == 'y':
            a, b = stack.first(str, n=2)
            stack.push(b.rjust(stack.first(int), a))
        elif char == 'Y':
            a, b = stack.first(str, n=2)
            stack.push(a.index(b))
        elif char == 'B':
            a, b = stack.first(int, n=2)
            if b <= 64:
                alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/'
                stack.push(''.join(map(alphabet.__getitem__, numberToBase(a, b))))
        elif char == 'b':
            a = stack.first(str)
            b = stack.first(int)
            stack.push(''.join(map(a.__getitem__, numberToBase(b, len(a)))))
        elif char == 'd':
            a, b = stack.first(int, n=2)
            stack.push(int(a, b))
        elif char == 'f':
            print(stack[0], end='')
        elif char == 'F':
            print(stack[0])
        elif char == '$':
            string = ''
            index += 1
            try:
                while code[index] != '$':
                    string += code[index]
                    index += 1
            except:
                pass
            a = stack.first((list, str))
            l = []
            for i in a:
                stack, lst = run(string, [i] + stack, lst, u, inputs)
                l.append(stack[0])
            stack.push(l)
        elif char == 'E':
            while 1:
                stack, lst = run(code[index+1:], stack, lst, u, inputs)
                print(stack[0])
        elif char == 'g':
            stack.push(list(lst).copy())
        elif char == 'h':
            stack.push(lst[-1])
        elif char == 'H':
            lst.append(stack[0])
        elif char == 'v':
            stack.push(ord(stack.first(str)))
        elif char == 'V':
            stack.push(chr(stack.first(int)))
        elif char == 'U':
            u = stack[0]
        elif char == 'u':
            stack.push(u)
        elif char == '(':
            stack.push(list(inputs).copy())
        elif char == ')':
            stack.push(inputs[0])
        else:
            if isinstance(stack[0], str):
                stack[0] += code[index]
            else:
                stack.push(code[index])
        index += 1
    return stack, lst

def from_cmdline():
    code = input('Code: ')
    s, l = run(code)
    print('\nOutput:')
    print(s[0])
    print(l)

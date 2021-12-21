from sympy import *
import numpy as np
import math

# f(x1) * f(x2) < 0
# Ex.: Encontre um intervalo, de amplitude no máximo igual a 1, que contenha uma raiz da
#função: f(x) = x^3 − 9x + 3
def bolzano(function, searchInterval, printCondition):
  functionResults = []
  intervalRange = 1
  intervalResult = []

  for x in range(searchInterval[0], searchInterval[1]):
    functionResults.append(eval(function.replace('x', str(x))))
  
  #print(functionResults)

  for index, x in enumerate(functionResults):
    for y in range(intervalRange):
      if index <= len(functionResults)-2:
        if x*functionResults[index+(y+1)] < 0:
          intervalResult.append(index)
          intervalResult.append(index+(y+1))

  splitedIntervalResult = splitArray(intervalResult, 2)

  if printCondition:
    print('Bolzano Method')
    print('There are roots in the following intervals:')
    splitedIntervalResult = splitArray(intervalResult, 2)

    for x in splitedIntervalResult:
      print([(x[0]-10), (x[1]-10)])

  return [splitedIntervalResult,functionResults]


# x = a + b /2
# if f(a) x f(x) < 0 -> new interval will be [a, x]
# if f(a) x f(x) > 0 -> new interval will be [x, b]
# stop criteria b − a < ε
#Ex.: Calcule a raiz da equação f(x) = x2 − 5sen(x), com ε ≤ 0,01 utilizando o método da bisseção. Use o intervalo [1,3]
def bisection():
  function = 'x**2-5*math.sin(x)'
  searchInterval = [1,3]
  stopCriteria = 0.01
  resultA = 0
  resultB = 0
  xk = 0
  resultXk = 0

  stopCondition = True

  while(stopCondition):
    resultA = eval(function.replace('x', str(searchInterval[0])))
    resultB = eval(function.replace('x', str(searchInterval[1])))

    xk = (searchInterval[0] + searchInterval[1])/2

    resultXk = resultB = eval(function.replace('x', str(xk)))

    if resultXk*resultA < 0:
      searchInterval[1] = xk
    else:
      searchInterval[0] = xk

    if searchInterval[1]-searchInterval[0] <= stopCriteria:
      stopCondition = False
  
  print()
  print()
  print('Bisection Method')
  print('There is a root when x is approximately '+str(xk))

# xk+1 = xk − f(xk)/f′(xk)
# Ex.: Calcule f(x)= x^5-26 pelo método de Newton-Raphson. Considere ε = 10^-5
def NewtonRaphson():
  function = 'x**5-26'
  x = Symbol('x')
  derivative = str((x**5-26).diff(x))
  stopCriteria = 0.00001
  bolzanoResult = bolzano(function, [0,3], False)
  AtualX = 0
  
  if bolzanoResult[1][bolzanoResult[0][0][0]] < 0 and bolzanoResult[1][bolzanoResult[0][0][1]] > 0:
    testCondition = bolzanoResult[1][bolzanoResult[0][0][0]]*(-1)

    if testCondition > bolzanoResult[1][bolzanoResult[0][0][1]]:
      AtualX = bolzanoResult[0][0][1]
    else:
      AtualX = bolzanoResult[0][0][0]
  
  elif bolzanoResult[1][bolzanoResult[0][0][0]] > 0 and bolzanoResult[1][bolzanoResult[0][0][1]] < 0:

    testCondition = bolzanoResult[1][bolzanoResult[0][0][1]]*(-1)

    if testCondition > bolzanoResult[1][bolzanoResult[0][0][0]]:
      AtualX = bolzanoResult[0][0][0]
    else:
      AtualX = bolzanoResult[0][0][1]

  else:
    if bolzanoResult[1][bolzanoResult[0][0][1]] > bolzanoResult[1][bolzanoResult[0][0][0]]:
      AtualX = bolzanoResult[0][0][0]
    else:
      AtualX = bolzanoResult[0][0][1]

  #print(AtualX)
  stopCondition = True

  while(stopCondition):
    functionResult = eval(function.replace('x', str(AtualX)))
    derivativeResult = eval(derivative.replace('x', str(AtualX)))

    if functionResult < 0:
      if (functionResult * (-1)) < stopCriteria:
        stopCondition = False
        break
    elif functionResult < stopCriteria:
      stopCondition = False
      break

    AtualX = AtualX - (functionResult / derivativeResult)

  print()
  print()
  print('Newton-Raphson Method')
  print('There is a root when x is approximately '+str(AtualX))
    

#f(x) = g(x) − h(x)
# 0 = g(x) − h(x)
#g(x) = h(x)
# Ex.: Encontre, pelo método gráfico, as raízes da função: f(x) = e^x − 3x
def graphical():
  function = 'math.e**x-3*x'
  convergenceResult = convergence(function)
  searchInterval = [-3,3]
  finalResult = []
  resultArray = []

  #print(convergenceResult)
  for x in convergenceResult[0]:
    #for y * 0,01 in range(searchInterval[0], searchInterval[1]):
    result = []
    i = searchInterval[0]
    while i <= searchInterval[1]:
      result.append(eval(x.replace('x', str(i))))
      i += 0.01
    finalResult.append(result)
  
  #print(finalResult)
  for index, x in enumerate(finalResult):
    for i, y in enumerate(x):
      if index <= len(finalResult)-2:
        for z in finalResult[index+1]:
          if y - z <= 0.001:
            resultArray.append(y)
      break

  print()
  print()
  print('Graphical Method')
  print('There is a root when x is approximately '+str(resultArray[0]))  
    



def convergence(function):
  newFunc = function.split('+')
  finalFunc = []
  for x in newFunc:
    if x.find('-') != -1:
      splitFunc = x.split('-')
      for y in splitFunc:
        finalFunc.append(x.split('-'))
    else:
      finalFunc.append(x.split('-'))

  return finalFunc

# https://stackoverflow.com/a/23148997
def splitArray(arr, size):
     arrs = []
     while len(arr) > size:
         pice = arr[:size]
         arrs.append(pice)
         arr   = arr[size:]
     arrs.append(arr)
     return arrs


bolzano('x**3-9*x+3', [-10,10], True)
bisection()
NewtonRaphson()
graphical()
#convergence('x**3-9*x+3')


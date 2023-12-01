# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 09:47:43 2023

@author: jsingh
"""

def main():
    lines = readFile("input.txt")
    calvalues1 = getCalibrationValuesPart1(lines)
    print(sum(calvalues1))
    calvalues2 = getCalibrationValuesPart2(lines)
    print(sum(calvalues2))

def readFile(fileName):
    f = open(fileName, "r")
    lines = f.readlines()
    f.close()
    
    return lines

def getCalibrationValuesPart1(lines):
    calvalues = []
    for line in lines:
        for index in range(len(line)):
            if line[index].isnumeric():
                fDigit = int(line[index])
                break
        for index in range(len(line)-1, -1, -1):
            if line[index].isnumeric():
                sDigit = int(line[index])
                break
        calvalues.append(fDigit*10 + sDigit)
    
    return calvalues

def getCalibrationValuesPart2(lines):
    nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    calvalues = []
    for line in lines:
        for index in range(len(line)):
            if line[index].isnumeric():
                fDigit = int(line[index])
                break
            elif index < len(line)-3 and line[index:index+3] in nums:
                fDigit = nums.index(line[index:index+3]) + 1
                break
            elif index < len(line)-4 and line[index:index+4] in nums:
                fDigit = nums.index(line[index:index+4]) + 1
                break
            elif index < len(line)-5 and line[index:index+5] in nums:
                fDigit = nums.index(line[index:index+5]) + 1
                break
        for index in range(len(line)-1, -1, -1):
            if line[index].isnumeric():
                sDigit = int(line[index])
                break
            elif index > 2 and line[index-3:index] in nums:
                sDigit = nums.index(line[index-3:index]) + 1
                break
            elif index > 3 and line[index-4:index] in nums:
                sDigit = nums.index(line[index-4:index]) + 1
                break
            elif index > 4 and line[index-5:index] in nums:
                sDigit = nums.index(line[index-5:index]) + 1
                break
            
        calvalues.append(fDigit*10 + sDigit)
    
    return calvalues

main()
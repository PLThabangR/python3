#An algorithm is a set of instructions that is completed in a step-by-step way to solve a particular problem
#***1.WWite pseudocode, English-like syntax that resembles code, to explain the problem in a series of steps
#**2.Another approach is to use a flow chart that provides a graphical representation of the series of steps
#palihndrome

str="racecer"
startIndex=0
endIndex=len(str)-1

for i in str:
    if str[startIndex] != str[endIndex]:
        print("False")
    else:
        print("True")

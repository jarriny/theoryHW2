import xml.etree.ElementTree as ET
import sys
import itertools
from dfa import dfa
from transition import transition
from runRead import run

input = sys.stdin.read()
testTree = ET.parse(input)
tree = ET.parse(input)

test = testTree.getroot()

states = set()
start = 'NOTFOUND'
accept = set()
alphabet = set()
allTransitions = set()
fromTransitions = []
toTransitions = []
readTransitions = []

idToState = {}

namesFinal = ""
startFinal = ""
finalFinal = ""

if test.tag != 'automaton':
    root = tree.getroot().find('automaton')
else:
    root = tree.getroot()

for state in root.findall('state'):
    idToState.update({state.get('id') : state.get('name')})
    states.add(state.get('name'))
    for subtag in state.findall('initial'):
        if start == 'NOTFOUND':
            start = state.get('name')
    for subtag2 in state.findall('final'):
        accept.add(state.get('name'))
for transitionObj in root.findall('transition'):
    fromVar = 0
    toVar = 0
    readVar = 0
    for subtag3 in transitionObj.findall('from'):
        #fromTransitions.append(subtag3.text)
        fromVar = subtag3.text
    for subtag4 in transitionObj.findall('to'):
        #toTransitions.append(subtag4.text)
        toVar = subtag4.text
    for subtag5 in transitionObj.findall('read'):
        #readTransitions.append(subtag5.text)
        readVar = subtag5.text
        alphabet.add(subtag5.text)
    allTransitions.add(transition(idToState.get(fromVar), readVar, idToState.get(toVar)))


for name in states:
    namesFinal += name
    namesFinal += " "

for st in start:
    startFinal += st
    startFinal += " "

for fi in accept:
    finalFinal += fi
    finalFinal += " "

dfa_object = dfa(states, alphabet, allTransitions, start, accept)

one = itertools.product(alphabet, repeat = 1)
two = itertools.product(alphabet, repeat = 2)
three = itertools.product(alphabet, repeat = 3)
four = itertools.product(alphabet, repeat = 4)
five = itertools.product(alphabet, repeat = 5)

total = []
totalFinal = []

for m in one:
    total.append(m)

for m in two:
    total.append(m)

for m in three:
    total.append(m)

for m in four:
    total.append(m)

for m in five:
    total.append(m)


for i in total:
    k = ""
    for j in i:
        k = k + j
    totalFinal.append(k)

totalFinalFinal = []

for j in totalFinal:
    if run(j, dfa_object):
        totalFinalFinal.append(j)

#CHANGE WHEN READY
for k in totalFinal:
    print(k)



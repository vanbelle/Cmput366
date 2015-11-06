# This module takes in a string of 0's, 1's, and -1's.
# These values represent the outcomes of a betting game.
# And we can make bets on the outcome. 

from __future__ import division
import sys

currentCash = 2500
currentBet = 500

maxBet = 1000
minBet = 100

maxCash = 0

wentBroke = 0

percentage = 0
maxPercentage = 0
minPercentage = 0

lineNumber = 0

blockSize = 10

class Run(object):

	maxCash = 0
	runLength = 0

	def __init__(self):
		self.maxCash = 0
		self.runLength = 0

runs = []

run = Run()
for line in sys.stdin:
	lineNumber += 1
	outcome = int(line.strip())
	currentCash += (currentBet*outcome)
	maxCash = max(currentCash, maxCash)
	run.maxCash = max(currentCash, run.maxCash)
	run.runLength += 1

	if outcome > 0:
		currentBet -= 100
		currentBet = max(currentBet, minBet)
	elif outcome < 0:
		currentBet += 100
		currentBet = min(currentBet, maxBet)
	
	if currentCash <= 0:
		wentBroke += 1
		currentCash = 2500
		runs.append(run)
		run = Run()


#	if lineNumber % 1 == 0:
#		print ""
#		print "Line: " + str(lineNumber) 
#		print "Current Cash: $" + str(currentCash)
#		print "Max Cash: $" + str(maxCash)
#		print "Went Broke: " + str(wentBroke) + " times"


	if lineNumber % 10000 == 0:
		numberLostMoney = 0
		numberDoubledMoney = 0

#		print "========== Runs so far ============="
#		for i in runs:
#			print "Max: " + str(i.maxCash)
#			print "Length: " + str(i.runLength)
#			print ""


#		print ""
#		print "===========Stats============="
		print ""

		for i in runs:
			if i.maxCash == 2500:
				numberLostMoney += 1
			elif i.maxCash >= 5000:
				numberDoubledMoney += 1

		print "Lost Money: " + str(numberLostMoney) + " times"
		print "Doubled Money: " + str(numberDoubledMoney) + " times"


#	if lineNumber % 1000 == 0:
#		print "========== Runs so far ============="
#		for i in runs:
#			print "Max: " + str(i.maxCash)
#			print "Length: " + str(i.runLength)
#			print ""







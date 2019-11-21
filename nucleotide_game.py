import random
import sys
from Bio import SeqIO

for seq_record1 in SeqIO.parse("liver.fasta", "fasta"):
	chromosome1 = seq_record1.seq
	
for seq_record2 in SeqIO.parse("muscle.fasta", "fasta"):
	chromosome2 = seq_record2.seq
	


chromosome1 = len(seq_record1)
chromosome2 = len(seq_record2)

print chromosome1, chromosome2

player = 0

while player!=-1:

	if player==0 and not(chromosome1 ==0 and chromosome2 == 1) and not(chromosome1 ==1 and chromosome2 ==0):
		print "Player 1 is playing \n"
		print "Which chromosome do you choose to delete? \n 1. chromosome1 = ", chromosome1, "\n 2. chromosome2= ", chromosome2
		print "Pick between the chromosome 1 and 2"
		choice = input()
		while choice != 1 and choice != 2:
			print "Wrong input. Pick between the chromosome 1 and 2"
			choice = input()
		if choice == 1:
			chromosome1 =0
			if chromosome2 !=1:
				print "Split chromosome 2 into two non empty parts, give one of the parts"
				part = input()
				while part <= 0 or part>=chromosome2:
					print "Input must be not a negative number and smaller than chromosome 2 length"
					meros = input()
				chromosome1 = part
				chromosome2 = chromosome2 - part
		else:
			chromosome2 = 0
			if chromosome1 !=1:				
				print "Split chromosome 1 into two non empty parts, give one of the parts"
				part = input()
				while part <= 0 or part>=chromosome1:
					print "Input must be not a negative number and smaller than chromosome 1 length"
					part = input()				
				chromosome1 = chromosome1 - part
				chromosome2 = part
				
		
		player = 1		
	elif player ==1 and  not(chromosome1 ==0 and chromosome2 == 1) and not(chromosome1 ==1 and chromosome2 ==0):
		print "Player 2 is playing \n" 
		print "Which chromosome do you choose to delete? \n 1. chromosome1 = ", chromosome1, "\n 2. chromosome2= ", chromosome2
		print "Pick between the chromosome 1 and 2"
		choice = input()
		while choice != 1 and choice != 2:
			print "Wrong input. Pick between the chromosome 1 and 2" 
			choice = input()
		if choice == 1:
			chromosome1 =0
			if chromosome2 !=1:
				print "Split chromosome 2 into two non empty parts, give one of the parts" 
				part = input()
				while part <= 0 or part>=chromosome2:
					print "Input must be not a negative number and smaller than chromosome 2 length"
					part = input()
				chromosome1 = part
				chromosome2 = chromosome2 - part
		else: 
			chromosome2 = 0
			if chromosome1 !=1:
				print "Split chromosome 1 into two non empty parts, give one of the parts"
				part = input()
				while part <= 0 or part>=chromosome1:
					print "Input must be not a negative number and smaller than chromosome 1 length" 
					part = input()
				chromosome1 = chromosome1 - part
				chromosome2 = part
		
		player = 0
			
	elif (chromosome1 ==0 and chromosome2 == 1) or (chromosome1 ==1 and chromosome2 ==0):
		if player==0:
			print "Player 1 won" 
		elif player==1:
			print "Player 2 won"
		player = -1
			
			
			


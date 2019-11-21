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
		print "Paizei o 1os paixtis \n"
		print "Poio chromosoma epilegeis na diagrapseis? \n 1. chromosome1 = ", chromosome1, "\n 2. chromosome2= ", chromosome2
		print "Epelekse metaksu tou 1 kai tou 2"
		choice = input()
		while choice != 1 and choice != 2:
			print "Lathos eisodos.Dialekse metaksu tou 1 i tou 2"
			choice = input()
		if choice == 1:
			chromosome1 =0
			if chromosome2 !=1:
				print "Xwrise to chromosome2 se 2 mh kena merh, dwse to ena meros"
				meros = input()
				while meros <= 0 or meros>=chromosome2:
					print "Prepei na valeis mh arnhtikh timh kai mikroterh apo to idio to chromosome2"
					meros = input()
				chromosome1 = meros
				chromosome2 = chromosome2 - meros
		else:
			chromosome2 = 0
			if chromosome1 !=1:				
				print "Xwrise to chromosome1 se 2 mh kena merh, dwse to ena meros"
				meros = input()
				while meros <= 0 or meros>=chromosome1:
					print "Prepei na valeis mh arnhtikh timh kai mikroterh apo to idio to chromosome1"
					meros = input()				
				chromosome1 = chromosome1 - meros
				chromosome2 = meros
				
		
		player = 1		
	elif player ==1 and  not(chromosome1 ==0 and chromosome2 == 1) and not(chromosome1 ==1 and chromosome2 ==0):
		print "Paizei o 2os paixtis \n" 
		print "Poio chromosoma epilegeis na diagrapseis? \n 1. chromosome1 = ", chromosome1, "\n 2. chromosome2= ", chromosome2
		print "Epelekse metaksu tou 1 kai tou 2"
		choice = input()
		while choice != 1 and choice != 2:
			print "Lathos eisodos. Dialekse metaksu tou 1 i tou 2" 
			choice = input()
		if choice == 1:
			chromosome1 =0
			if chromosome2 !=1:
				print "Xwrise to chromosome2 se 2 mh kena merh, dwse to ena meros" 
				meros = input()
				while meros <= 0 or meros>=chromosome2:
					print "Prepei na valeis mh arnhtikh timh kai mikroterh apo to idio to chromosome2"
					meros = input()
				chromosome1 = meros
				chromosome2 = chromosome2 - meros
		else: 
			chromosome2 = 0
			if chromosome1 !=1:
				print "Xwrise to chromosome1 se 2 mh kena merh, dwse to ena meros"
				meros = input()
				while meros <= 0 or meros>=chromosome1:
					print "Prepei na valeis mh arnhtikh timh kai mikroterh apo to idio to chromosome1" 
					meros = input()
				chromosome1 = chromosome1 - meros
				chromosome2 = meros
		
		player = 0
			
	elif (chromosome1 ==0 and chromosome2 == 1) or (chromosome1 ==1 and chromosome2 ==0):
		if player==0:
			print "o paixtis 1 nikise" 
		elif player==1:
			print "o paixtis 2 nikise"
		player = -1
			
			
			


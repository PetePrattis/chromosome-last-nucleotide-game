# A Python Program / Project

**This is a Python project from my early days as a Computer Science student**

_This programm was created for the sixth semester class Bioinformatics
and is one of the final projects for the class_

> #### Description of project
>
>>A Python script that implements a two player strategic game with two chromosomes having length n and m of nucleotides respectively. In each Round of the game a player can destroy one of the chromosomes and split the other into two non-empty parts. The player who deletes the last nucleotide wins.

> #### Strategy explanation
>
> In this exercise we used homo sapiens chromosome 14 and homo sapiens chromosome 11. The first chromosome has a length of 39,314 and the second has a length of 14,327.
The player who reaches the length of the 2 chromosomes in chromosome 1 = length 1 and chromosome 2 = length 2 should delete chromosome 1 with length 1 to reach chromosome 1 = length 1 and chromosome 2 = length 1. 
So we leave no choice to the other player and as a result we win winners.
Initially, we enter our data from the NCBI database, and then we define the player with 0 which equals player 1. 
Assuming that the terminal condition is for the player to be -1, we enter the main loop. 
There, we define the variable choice, according to which the player chooses which chromosome he wishes to delete. 
The first condition we come across is one where the player must be 1 in order for the player to be valid and in addition the chromosome in each chromosome is not 0 or 1 in length.

> #### About this project
>
> - The comments to make the code understandable, are within the .py archive
> - This project was written in IDLE, Python’s Integrated Development and Learning Environment.
> - Biological data used from https://www.ncbi.nlm.nih.gov/gene/ (genes 5836, 5837)
> - This program runs for Python version 2.7
> - This repository was created to show the variety of the work I did and experience I gained as a student
>

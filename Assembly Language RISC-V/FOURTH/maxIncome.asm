maxIncome:
#finds the max income from the file
#arguments:	a0 contains the file record pointer array location (0x10040000 in our example) But your code MUST handle any address value
#		a1:the number of records in the file
#return value a0: heap memory pointer to actual  location of the record stock name in the file buffer

	#if empty file, return 0 for both a0, a1
	bnez a1, maxIncome_fileNotEmpty
	li a0, 0
	ret

 maxIncome_fileNotEmpty:
	
	# Start your coding from here!

	li a0, 0x10040010
	#if no student code entered, a0 just returns 0x10040010 always :(
	lwu t0, 0(a0)
	li t1, 0
	li t3, 0
	
	loopmax:
		lwu t2, 0(t0)
		bge t2, t3, max
		max:
			addi t3, t2, 0
			j b2loopmax
	b2loopmax:
		bgt t1, a1, endmax
		addi t0, t0, 1
		addi t1, t1, 1
		j loopmax
	endmax:
	
# End your  coding  here!
	
		ret
#######################end of maxIncome###############################################

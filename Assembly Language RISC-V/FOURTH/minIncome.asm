minIncome:
#finds the min income from the file
#arguments:	a0 contains the file record pointer array location (0x10040000 in our example) But your code MUST handle any address value
#		a1:the number of records in the file
#return value a0: heap memory pointer to actual  location of the record stock name in the file buffer

	#if empty file, return 0 for both a0, a1
	bnez a1, minIncome_fileNotEmpty
	li a0, 0
	ret

 minIncome_fileNotEmpty:
	
	# Start your coding from here!

	li a0, 0x10040010
	#if no student code entered, a0 just returns 0x10040010 always :(
	lwu t0, 0(a0)
	li t1, 0
	li t3, 0
	
	loopmin:
		lwu t2, 0(t0)
		ble t2, t3, min
		min:
			addi t3, t2, 0
			j b2loopmin
	b2loopmin:
		bgt t1, a1, endmin
		addi t0, t0, 1
		addi t1, t1, 1
		j loopmin
	endmin:
	
	
# End your  coding  here!
	
		ret
#######################end of minIncome###############################################

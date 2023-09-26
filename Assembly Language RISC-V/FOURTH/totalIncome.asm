totalIncome:
#finds the total income from the file
#arguments:	a0 contains the file record pointer array location (0x10040000 in our example) But your code MUST handle any address value
#		a1:the number of records in the file
#return value a0:the total income (add up all the record incomes)

	#if empty file, return 0 for  a0
	bnez a1, totalIncome_fileNotEmpty
	li a0, 0
	ret

totalIncome_fileNotEmpty:
	
	# Start your coding from here!
	
	li a0, 0x10040010
	li t0, 0
	li t1, 0
	#lwu t2, 4(a0)
	
	loop:
		lwu t2, 4(a0)
		#lbu t3, (t2)
		bgt t1, a1, end
		#addi a0, t3, 0
		jal income_from_record
		addi t0, a0, 0
		addi t1, t1, 1
		addi a0, a0, 4
		j loop
	end:
	
	#if no student code entered, a0 just returns 0 always :(
	
		
	
# End your  coding  here!
	
		ret
#######################end of nameOfMaxIncome_totalIncome###############################################

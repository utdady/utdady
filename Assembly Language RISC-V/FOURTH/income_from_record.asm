income_from_record:
#function to return numerical income from a specific record
#e.g. for record "Microsoft,34\r\n", income to return is 34(for which name is Microsoft)

#arguments:	a0 contains pointer to start of numerical income in record 

#function RETURNS income numerical value of the asci income in a0 (34 in our example)
	
# Start your coding from here!

	#if no student code entered, a0 just returns 0 always :(
# .data
# incomeStr: .asciz "365\r"

# .text
# li a0, 0x10040004
# la t1, incomeStr
# sw t1, (a0)

sw t1, (a0)
addi a2, a0, 0

li t2, 13
li t3, 0

	loop1:
		lbu t0, (a2)
		beq t0, t2, end1
		addi a2, a2, 1
		addi t3, t3, 1
		j loop1
	end1:
		j parttwo
#t2, t3, t1, t0 cannot be used as variables
	parttwo:
		sw t1, (a0)
	
		addi t3, t3, -1

		loop2:
			lbu t0, (t1)
			beq t0, t2, end2
	
			addi t0, t0, -48
			addi t5, t3, 0
		
			li t4, 10
			li t6, 1
			power:
				beqz t5, endpower
				mul t6, t6, t4
				addi t5, t5, -1
				j power
			endpower:
				mul t0, t0, t6
				j update
		update:	
			addi t3, t3, -1	
			add a1, a1, t0
			addi t1, t1, 1
			j loop2
		end2:
			addi a0, a1, 0

# End your  coding  here!
			ret
	
#######################end of income_from_record###############################################	

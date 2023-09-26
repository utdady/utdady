length_of_file:
#function to find length of data read from file
#arguments: a1=bufferAdress holding file data
#return file length in a0
	
#Start your coding here

li a0, 0
li t0, 0

loop_start:
	lbu t1, (a1)
	
	beqz t1, loop_end

	addi a1, a1, 1
	addi t0, t0, 1
	b loop_start
loop_end:
	addi a0, t0, 0
	
#if no student code provided, this function just returns 0 in a0
	
#End your coding here
	
	ret
#######################end of length_of_file###############################################	

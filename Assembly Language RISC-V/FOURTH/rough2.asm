.data
incomeStr: .asciz "365\r"

.text
li a0, 0x10040004
la t1, incomeStr
sw t1, (a0)

lb t0, (t1) #init
addi t1, t1, 1 #increament
lb t0, (t1) #init
addi t1, t1, 1 #increament
lb t0, (t1) #init
addi t1, t1, 1 #increament
lb t0, (t1) #init
addi t1, t1, 1 #increament
lb t0, (t1) #init
addi t1, t1, 1 #increament

loop:
	lb t0
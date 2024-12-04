.data
    menu: .asciiz "\nM E N U\n1, Enter Number 1\n2, Enter Number 2\n3, Display num1 and num2\n4, Display sum or subtraction of num1 and num2\n5, Display product of num1 and num2\n6, Divide num1 by num2\n7, Exchange numbers 1 and 2\n8, Display numbers between num1 and num2\n9, Sum numbers between num1 and num2\n10, Raise num1 to the power of num2\n11, Display prime numbers between num1 and num2\n12, Toggle Option 4 between addition and subtraction\n13, Quit\n\nChoose an Option: "
    prompt1: .asciiz "Enter Number 1: "
    prompt2: .asciiz "Enter Number 2: "
    message: .asciiz "\nThe numbers selected are:\n"
    num1Label: .asciiz "Number 1 is: "
    num2Label: .asciiz "Number 2 is: "
    sumLabel: .asciiz "\nSum of num1 and num2 is: "
    subLabel: .asciiz "\nSubtraction of num1 and num2 is: "
    productLabel: .asciiz "\nProduct of num1 and num2 is: "
    divisionResult: .asciiz "\nQuotient is: "
    remainderResult: .asciiz "\nRemainder is: "
    swappedMessage: .asciiz "\nNumbers have been swapped.\n"
    invalidChoice: .asciiz "Invalid choice. Please select again.\n"
    rangeMessage: .asciiz "\nNumbers between num1 and num2 inclusive: "
    errorGreaterEqual: .asciiz "Error: num1 is greater than or equal to num2.\n"
    comma: .asciiz ", "
    newline: .asciiz "\n"
    sumRangeLabel: .asciiz "\nSum of numbers between num1 and num2 is: "
    powerResultLabel: .asciiz "\nResult of num1 raised to the power of num2 is: "
    errorNegativePowerMsg: .asciiz "Error: Negative exponents are not supported.\n"
    primeLabel: .asciiz "\nPrime numbers between num1 and num2: "
    errorDivideByZero: .asciiz "Error: Division by zero.\n"
    optionChangedToAddMessage: .asciiz "Option 4 has been changed to addition.\n"
    optionChangedToSubMessage: .asciiz "Option 4 has been changed to subtraction.\n"
    sumFlag: .word 1     # Flag to indicate addition (1) or subtraction (0)

.text
    .globl main

main:
    # Initialize variables
    li $t0, 0           # num1
    li $t1, 0           # num2

menu_loop:
    # Display menu
    li $v0, 4
    la $a0, menu
    syscall

    # Read user choice
    li $v0, 5
    syscall
    move $t3, $v0        # Store user choice in $t3

    # Handle menu options
    beq $t3, 1, input_num1
    beq $t3, 2, input_num2
    beq $t3, 3, display_numbers
    beq $t3, 4, display_sum
    beq $t3, 5, display_product
    beq $t3, 6, divide_numbers
    beq $t3, 7, exchange_numbers
    beq $t3, 8, display_range
    beq $t3, 9, sum_range
    beq $t3, 10, raise_power
    beq $t3, 11, display_primes
    beq $t3, 12, toggle_option4_operation
    beq $t3, 13, exit_program
    j invalid_choice

# Option 1: Input num1
input_num1:
    li $v0, 4
    la $a0, prompt1
    syscall
    li $v0, 5
    syscall
    move $t0, $v0  # Store input in num1
    j menu_loop

# Option 2: Input num2
input_num2:
    li $v0, 4
    la $a0, prompt2
    syscall
    li $v0, 5
    syscall
    move $t1, $v0  # Store input in num2
    j menu_loop

# Option 3: Display num1 and num2
display_numbers:
    li $v0, 4
    la $a0, message
    syscall

    li $v0, 4
    la $a0, num1Label
    syscall
    li $v0, 1
    move $a0, $t0  # Display num1
    syscall

    li $v0, 4
    la $a0, newline
    syscall

    li $v0, 4
    la $a0, num2Label
    syscall
    li $v0, 1
    move $a0, $t1  # Display num2
    syscall

    li $v0, 4
    la $a0, newline
    syscall
    j menu_loop

# Option 4: Display sum or subtraction of num1 and num2
display_sum:
    lw $t4, sumFlag
    beq $t4, 1, do_addition
    j do_subtraction

do_addition:
    li $v0, 4
    la $a0, sumLabel
    syscall
    add $t2, $t0, $t1  # t2 = num1 + num2
    j display_result

do_subtraction:
    li $v0, 4
    la $a0, subLabel
    syscall
    sub $t2, $t0, $t1  # t2 = num1 - num2

display_result:
    li $v0, 1
    move $a0, $t2  # Display result
    syscall
    j menu_loop

# Option 5: Display product of num1 and num2
display_product:
    mul $t2, $t0, $t1  # t2 = num1 * num2
    li $v0, 4
    la $a0, productLabel
    syscall
    li $v0, 1
    move $a0, $t2  # Display product
    syscall
    j menu_loop

# Option 6: Divide num1 by num2
divide_numbers:
    beqz $t1, errorDivide  # Check if num2 is zero
    div $t0, $t1
    mflo $t2             # Quotient
    mfhi $t3             # Remainder
    li $v0, 4
    la $a0, divisionResult
    syscall
    li $v0, 1
    move $a0, $t2  # Display quotient
    syscall
    li $v0, 4
    la $a0, remainderResult
    syscall
    li $v0, 1
    move $a0, $t3  # Display remainder
    syscall
    j menu_loop

errorDivide:
    li $v0, 4
    la $a0, errorDivideByZero
    syscall
    j menu_loop

# Option 7: Exchange numbers 1 and 2
exchange_numbers:
    move $t4, $t0
    move $t0, $t1
    move $t1, $t4
    li $v0, 4
    la $a0, swappedMessage
    syscall
    j menu_loop

# Option 8: Display numbers between num1 and num2
display_range:
    bgt $t0, $t1, display_errorGreaterEqual
    beq $t0, $t1, display_errorGreaterEqual

    li $v0, 4
    la $a0, rangeMessage
    syscall

    move $t2, $t0
range_loop:
    ble $t2, $t1, display_num
    j end_range_loop
display_num:
    li $v0, 1
    move $a0, $t2
    syscall
    li $v0, 4
    la $a0, comma
    syscall
    addi $t2, $t2, 1
    j range_loop
end_range_loop:
    li $v0, 4
    la $a0, newline
    syscall
    j menu_loop

display_errorGreaterEqual:
    li $v0, 4
    la $a0, errorGreaterEqual
    syscall
    j menu_loop

# Option 9: Sum numbers between num1 and num2
sum_range:
    bgt $t0, $t1, display_errorGreaterEqual
    beq $t0, $t1, display_errorGreaterEqual

    add $t2, $zero, $zero
    move $t3, $t0
sum_loop:
    ble $t3, $t1, add_num #Branch if Less Than or Equal
    j display_sum_range
add_num:
    add $t2, $t2, $t3
    addi $t3, $t3, 1
    j sum_loop
display_sum_range:
    li $v0, 4
    la $a0, sumRangeLabel
    syscall
    li $v0, 1
    move $a0, $t2
    syscall
    j menu_loop

# Option 10: Raise num1 to the power of num2
raise_power:
    bltz $t1, errorNegativePower  # Error if num2 < 0
    li $t2, 1
    move $t3, $t1
power_loop:
    beqz $t3, power_done #Branch if Equal to Zero
    mul $t2, $t2, $t0
    addi $t3, $t3, -1
    j power_loop
power_done:
    li $v0, 4
    la $a0, powerResultLabel
    syscall
    li $v0, 1
    move $a0, $t2
    syscall
    j menu_loop

errorNegativePower:
    li $v0, 4
    la $a0, errorNegativePowerMsg
    syscall
    j menu_loop

# Option 11: Display prime numbers between num1 and num2
display_primes:
    bgt $t0, $t1, display_errorGreaterEqual
    beq $t0, $t1, display_errorGreaterEqual

    li $v0, 4
    la $a0, primeLabel
    syscall
    move $t2, $t0
prime_loop:
    ble $t2, $t1, check_prime
    j end_prime_loop
check_prime:
    li $t3, 2
    li $t4, 1
prime_check_loop:
    div $t2, $t3
    mfhi $t5
    beqz $t5, not_prime
    addi $t3, $t3, 1
    blt $t3, $t2, prime_check_loop
    j display_prime
not_prime:
    addi $t2, $t2, 1
    j prime_loop
display_prime:
    li $v0, 1
    move $a0, $t2
    syscall
    li $v0, 4
    la $a0, comma
    syscall
    addi $t2, $t2, 1
    j prime_loop
end_prime_loop:
    li $v0, 4
    la $a0, newline
    syscall
    j menu_loop

# Option 12: Toggle Option 4 between addition and subtraction
toggle_option4_operation:
    lw $t4, sumFlag
    xori $t4, $t4, 1 #Performs a bitwise XOR between the value in register $t4 and the immediate value 1
    sw $t4, sumFlag
    beq $t4, 1, show_add_message
    li $v0, 4
    la $a0, optionChangedToSubMessage
    syscall
    j menu_loop
show_add_message:
    li $v0, 4
    la $a0, optionChangedToAddMessage
    syscall
    j menu_loop

# Option 13: Exit program
exit_program:
    li $v0, 10
    syscall

# Invalid choice handling
invalid_choice:
    li $v0, 4
    la $a0, invalidChoice
    syscall
    j menu_loop

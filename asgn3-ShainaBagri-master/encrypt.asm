; Encrypts a string using a Caesar cipher.
; CSC 225, Assignment 3
; Given code, Winter '20

; TODO: Complete this program.

      .ORIG x3000        ;Initializes LC-3 to x3000
      AND R1, R1, #0     ;Resets R1 ("Enter")
      ADD R1, R1, x0A    ;Puts ASCII code for "Enter" into R1
      NOT R1, R1         ;Makes R1 negative
      ADD R1, R1 #1      ;Makes R1 negative
      LEA R3, MEM        ;Loads memory addresses dedicated to storing chars
      LEA R0, P1         ;Loads prompt 1 address into R0
      PUTS               ;Prints prompt 1
      GETC               ;Gets user int
      OUT                ;Prints out user int
      ADD R2, R0, #-16   ;Puts int into R2 (key)
      ADD R2, R2, #-16
      ADD R2, R2, #-16
      GETC               ;Gets user char "Enter"
      OUT                ;Prints out user char "Enter"
      LEA R0, P2         ;Loads prompt 2 address into R0
      PUTS               ;Prints prompt 2
LOOP  GETC               ;Loops through user string and gets each char
      STR R0, R3, #0     ;Stores char in new memory address
      OUT                ;Prints out user char so can see what typing
      ADD R3, R3, #1     ;increments memory address at which next char will be stored
      ADD R0, R0, R1     ;Checks if user char is "Enter"
      BRnp LOOP          ;Loop ends if user char is "Enter"
      AND R0, R0, #0     ;Resets R0
      ADD R0, R0, #1     ;Ensures loop will run (R0 != 0)
      LEA R3, MEM        ;Loads memory addresses dedicated to storing chars
      AND R4, R4, #0     ;Resets R4
      LEA R0, P3         ;Loads prompt 3 address into R0
      PUTS               ;Prints prompt 3
LOOP2 LDR R0, R3, #0     ;Loads char from memory address
      ADD R4, R0, R1     ;Checks if char is "Enter"
      BRz DONE           ;If char is "Enter", end loop
      ADD R0, R0, R2     ;Encodes char
      OUT                ;Prints out user char so can see what typing
      ADD R3, R3, #1     ;Increments memory address at which next char will be stored
      BRnzp LOOP2        ;Always loops back
DONE  HALT
MEM   .BLKW #32          ;Reserves 32 memory locations for chars in user string
P1    .STRINGZ "Encryption key (0-9): "
P2    .STRINGZ "Unencrypted string: "
P3    .STRINGZ "Encrypted string: "
      .END
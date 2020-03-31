; Recursively computes Fibonacci numbers.
; CSC 225, Assignment 6
; Given code, Winter '20

        .ORIG x4000

; int fib(int)
; TODO: Implement this function.
FIBFN
        ;Callee setup
        ADD R6, R6, #-1     ;Push space for return value
        ADD R6, R6, #-1     ;Push return address
        STR R7, R6, #0
        ADD R6, R6, #-1     ;Push dynamic link
        STR R5, R6, #0
        ADD R5, R6, #-1     ;Sets frame pointer to first local variable
        ADD R6, R6, #-1     ;Push space for local: a
        ADD R6, R6, #-1     ;Push space for local: b
        
        LDR R0, R5, #4      ;load n into R0
        BRp ELIF            ;If <= 0...
        ;Base case
        AND R0, R0, #0       ;Set return value to 0
        STR R0, R5, #3
        BRnzp FIBRET
        
ELIF    ADD R0, R0, #-1
        BRp ELSE            ;Else if == 1...
        ;Base case
        AND R0, R0, #0      ;Set return value to 1
        ADD R0, R0, #1
        STR R0, R5, #3
        BRnzp FIBRET
        
ELSE    ADD R0, R0, #1      ;Resets else if check

        ;Recursive case
        ;Caller setup n-1
        ADD R0, R0, #-1     ;Compute n-1
        ADD R6, R6, #-1     ;Push n-1
        STR R0, R6, #0
        JSR FIBFN           ;f(n-1)
        
        ;Caller teardown n-1
        LDR R1, R6, #0      ;Pop f(n-1) into R1
        ADD R6, R6, #1
        STR R1, R5, #0     ;Stores f(n-1) in local a of f(n)
        ADD R6, R6, #1     ;Pop arguments
        
        ;Caller setup n-2
        LDR R0, R5, #4       ;Reload n
        ADD R0, R0, #-2     ;Compute n-2
        ADD R6, R6, #-1     ;Push n-2
        STR R0, R6, #0
        JSR FIBFN           ;f(n-2)
        
        ;Caller teardown n-2
        LDR R1, R6, #0      ;Pop f(n-2) into R1
        ADD R6, R6, #1
        STR R1, R5, #-1     ;Stores f(n-2) in local b of f(n)
        ADD R6, R6, #1     ;Pop arguments
        
        LDR R0, R5, #0     ;Loads f(n-1) in R0
        LDR R1, R5, #-1     ;Loads f(n-2) in R1
        ADD R0, R0, R1
        STR R0, R5, #3     ;Sets return value to f(n-1) + f(n-2)
        
FIBRET  ;Callee teardown
        ADD R6, R6, #1     ;Pop locals
        ADD R6, R6, #1
        LDR R5, R6, #0      ;Pop dynamic link
        ADD R6, R6, #1
        LDR R7, R6, #0      ;Pop return address
        ADD R6, R6, #1
        
        RET
        .END

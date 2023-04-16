; file: product.asm

; product function.
; Realiza el producto de dos valores DOUBLE.
;
; C prototype:
;   double product(double first_value, double second_value)
; Parameters:
;   first_value.
;   second_value.
; Return value:
;   first_value * second_value

; Macros
%define first_value   qword  [ebp+8]
%define second_value  qword  [ebp+16]

segment .data

segment .bss

segment .text
        global product

product:
        ; Prolog
        push    ebp                 ; Se guarda el EBP original.
        mov     ebp, esp            ; EBP = ESP.
        ; Implementation
        fld     first_value         ; stack: first_value.
        fmul    second_value        ; stack: first_value * second_value.
        ; Epilog
        mov     esp, ebp            ; Se actualiza el valor original de ESP.
        pop     ebp                 ; Se saca el valor original guardado en el prólogo.
        ; Retorno resultado
        ret


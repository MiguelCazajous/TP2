; file: converter.asm

; function converter
; convierte un valor double de origen (USD) a un valor double de destino (ARS o EUR). 
;
; C prototype:
;   int converter( double source_currency, double convertion_factor)
; Parameters:
;   source_currency   - valor de criptomoneda en USD
;   convertion_factor - factor de conversión
; Return value:
;   double  dest_currency - valor de criptomoneda en ARS o EUR

; Macros
%define source_currency     qword  [ebp+8]
%define convertion_factor   qword  [ebp+16]

segment .data

segment .bss

segment .text
        global converter

converter:
        push    ebp                 ; Se guarda el EBX original
        mov     ebp, esp            ; EBP = ESP

        fld     source_currency;    ; stack: source_currency
        fmul    convertion_factor   ; stack: source_currency * convertion_factor 

        pop     ebp
        ret
        

;
; file: converter.asm

; function converter
; convierte un valor float de origen (USD) a un valor float de destino (ARS o EUR). 
;
; C prototype:
;   float converter_float( float source_currency, float convertion_factor)
; Parameters:
;   source_currency   - valor de criptomoneda en USD
;   convertion_factor - factor de conversión
; Return value:
;   float  dest_currency - valor de criptomoneda en ARS o EUR

; Macros
%define source_currency     dword  [ebp+8]
%define convertion_factor   dword  [ebp+12]

segment .data

segment .bss

segment .text
        global converter_float

converter_float:
        push    ebp                     ; Se guarda el EBX original
        mov     ebp, esp                ; EBP = ESP

        fld     source_currency;        ; stack: source_currency
        fmul    convertion_factor       ; stack: source_currency * convertion_factor 

        pop     ebp
        ret
        

             

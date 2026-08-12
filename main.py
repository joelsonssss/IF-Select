import flet as ft
import json
import os
import sys
from pathlib import Path

lista_aplicacao_geral = ("Bobinadeira", "Bomba deslocamento positivo", "Compressor", "Centrifugadora", "Elevador de carga c/ cremalheira", "Elevador de carga c/ contrapeso","Guindaste", "Extrusora", "Lavadora industrial", "Máquina operatriz", "Misturador", "Ponte rolante", "Bomba centrífuga", "Ventilador e Exaustor", "Esteira transportadora", "Outros")
lista_aplicacao_if20 = ("Bobinadeira", "Bomba deslocamento positivo", "Compressor", "Centrfugadora", "Elevador de carga c/ cremalheira","Elevador de carga c/ contrapeso", "Guindaste", "Extrusora", "Lavadora industrial", "Máquina operatriz", "Misturador", "Ponte rolante")
lista_aplicacao_if10 = ("Bomba centrífuga","Ventilador e Exaustor", "Esteira transportadora")
lista_aplicacao_if10_20 = ("Bobinadeira", "Bomba deslocamento positivo", "Compressor", "Centrifugadora", "Elevador de carga c/ cremalheira", "Elevador de carga c/ contrapeso","Guindaste", "Extrusora", "Lavadora industrial", "Máquina operatriz", "Misturador", "Ponte rolante", "Bomba centrífuga", "Ventilador e Exaustor", "Esteira transportadora")
lista_aplicacao_if20_pot = ("Misturador", "Máquina operatriz", "Bomba deslocamento positivo")
lista_aplicacao_if20_mais1 = ("Bobinadeira", "Bomba deslocamento positivo", "Compressor", "Centrifugadora", "Elevador de carga c/ cremalheira","Elevador de carga c/ contrapeso", "Guindaste", "Extrusora", "Lavadora industrial", "Ponte rolante")
lista_aplicacao_if20_resistor = ("Elevador de carga c/ cremalheira", "Elevador de carga c/ contrapeso","Guindaste", "Ponte rolante", "Centrifugadora", "Lavadora industrial")
lista_if10_potencia_220 = ("1 cv", "2 cv", "3 cv", "5 cv")
lista_if10_potencia_380 = ("1 cv", "2 cv", "3 cv", "5 cv", "7,5 cv", "10 cv")
lista_if20_potencia_220 = ("1 cv", "2 cv", "3 cv", "5 cv", "7,5 cv","10 cv", "15 cv", "20 cv", "25 cv", "30 cv", "40 cv", "50 cv", "60 cv", "75 cv")
lista_if20_potencia_380 = ("1 cv", "2 cv", "3 cv", "5 cv", "7,5 cv","10 cv", "15 cv", "20 cv", "25 cv", "30 cv", "40 cv", "50 cv", "60 cv", "75 cv")
lista_if20_potencia_220_troca = ("100 cv", "125 cv", "150 cv", "175 cv", "200 cv", "250 cv", "300 cv", "350 cv")
lista_if20_potencia_380_480 = ("5 cv", "7,5 cv", "10 cv", "15 cv", "20 cv", "25 cv", "30 cv", "40 cv","50 cv", "60 cv", "75 cv", "100 cv", "125 cv", "150 cv", "175 cv", "200 cv", "250 cv", "300 cv", "350 cv")
lista_if20_mais1_potencia_380_480 = ("5 cv", "7,5 cv", "10 cv", "15 cv", "20 cv", "25 cv", "30 cv", "40 cv","50 cv", "60 cv", "75 cv", "100 cv", "125 cv", "150 cv", "175 cv", "200 cv", "250 cv", "300 cv")
lista_if30_potencia_220 = ("1 cv", "2 cv", "3 cv", "5 cv", "7,5 cv","10 cv", "15 cv", "20 cv", "25 cv", "30 cv", "40 cv")
lista_if30_mais1_potencia_220 = ("1 cv", "2 cv", "3 cv", "5 cv", "7,5 cv", "10 cv", "15 cv", "20 cv", "25 cv", "30 cv", "30 cv")
lista_if30_potencia_380_480 = ("1 cv", "2 cv", "3 cv", "5 cv", "7,5 cv", "10 cv", "15 cv", "20 cv", "25 cv", "30 cv", "40 cv", "50 cv")
lista_if30_mais1_potencia_380_480 = ("1 cv", "2 cv", "3 cv", "5 cv", "7,5 cv", "10 cv", "15 cv", "20 cv", "25 cv", "30 cv", "40 cv")
lista_potencia_geral = ("1 cv", "2 cv", "3 cv", "5 cv", "7,5 cv", "10 cv", "15 cv", "20 cv", "25 cv", "30 cv","40 cv", "50 cv", "60 cv", "75 cv", "100 cv", "125 cv", "150 cv", "175 cv", "200 cv", "250 cv", "300 cv", "350 cv")
lista_tensao = ("220V", "380V", "380V-440V")
lista_if20_mais1_potencia_220 = ("1 cv", "2 cv", "3 cv", "5 cv", "7,5 cv", "10 cv", "15 cv", "20 cv", "25 cv", "30 cv", "40 cv", "50 cv", "60 cv")
lista_if30_comunicacao = ("COMUNICAÇÃO CANOPEN", "COMUNICAÇÃO ETHERCAT","COMUNICAÇÃO MODBUS-TCP", "COMUNICAÇÃO PROFINET")
lista_if30_adicionais = ("EXPANSÃO IO", "EXPANSÃO P/ ENCODER 5V","EXPANSÃO P/ ENCODER PUSH-PULL 24V", "SEGURANÇA STO (NR12)")
lista_if30_recursos_adicionais = ("COMUNICAÇÃO CANOPEN", "COMUNICAÇÃO ETHERCAT", "COMUNICAÇÃO MODBUS-TCP", "COMUNICAÇÃO PROFINET","EXPANSÃO IO", "EXPANSÃO P/ ENCODER 5V", "EXPANSÃO P/ ENCODER PUSH-PULL 24V", "SEGURANÇA STO (NR12)")
lista_if30_tensao = ("220V", "380V-440V")





def main(page: ft.Page):
    page.title = "Aplicações IF"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 400
    page.window_height = 700
    page.padding = 0
    page.spacing = 0
    page.bgcolor = ft.Colors.GREY_100
    page.window_max_height = 500
    page.window_maximized = True
    page.window_resizable = True
    page.window_maximizable =False
    
    
    def fechar_dialogo(e):
        ad1.open = False
        page.update()





    ad1 = ft.AlertDialog(
        bgcolor="#FFFFFF",
        title=ft.Text(
            value="Atenção",
            text_align=ft.TextAlign.CENTER,
        ),
        content=ft.Text(
            value=(
                "Selecione os campos de “Aplicação”, "
                "“Tensão” e “Potência” para visualizar os resultados."
            ),
            text_align=ft.TextAlign.CENTER,
            size=20,
        ),
        content_padding=ft.padding.all(30),
        inset_padding=ft.padding.all(10),
        modal=True,
        shape=ft.RoundedRectangleBorder(radius=0),
        actions=[
            ft.ElevatedButton(
                text="Fechar",
                on_click=fechar_dialogo,
                style=ft.ButtonStyle(
                    bgcolor="#0A2D42",
                    color=ft.Colors.WHITE,
                    shape=ft.RoundedRectangleBorder(radius=0),
                ),
            ),
        ],
        actions_alignment=ft.MainAxisAlignment.CENTER,
    )


  


    # Adiciona o AlertDialog à camada superior da página
    page.overlay.append(ad1)

    # Abre o diálogo automaticamente
    ad1.open = True
    page.update()
    

    def buscar(e):
        
        aplicacao = str(aplicacao_dropdown.value)
        tensao = str(alimentacao_dropdown.value)
        potencia = str(potencia_dropdown.value)
        comunicacao = str(comunicacao_dropdown.value)
        adcional = str(adicional_dropdown.value)

# DEFINE QUAL MODELO USAR IF10 OU IF20 ou IF30
    # ==============================
        # IF10
        if  (aplicacao in lista_aplicacao_if10 and 
                tensao == "220V" and 
                potencia in lista_if10_potencia_220 and 
                not comunicacao in lista_if30_recursos_adicionais and not 
                adcional in lista_if30_recursos_adicionais):
            f1 = "IF10"

        elif    (aplicacao in lista_aplicacao_if10 and 
                tensao == "380V" and 
                potencia in lista_if10_potencia_380 and 
                not comunicacao in lista_if30_recursos_adicionais and 
                not adcional in lista_if30_recursos_adicionais):
            f1 = "IF10"

        # IF20
        elif    ((aplicacao in lista_aplicacao_if20 or 
                aplicacao in lista_aplicacao_if10) and 
                tensao == "220V" and 
                potencia in lista_if20_mais1_potencia_220 and 
                not comunicacao in lista_if30_comunicacao and 
                not adcional in lista_if30_recursos_adicionais):
            f1 = "IF20"

        elif    ((aplicacao in lista_aplicacao_if10) and 
                tensao == "220V" and 
                potencia in lista_if20_potencia_220 and 
                not comunicacao in lista_if30_comunicacao and 
                not adcional in lista_if30_recursos_adicionais):
            f1 = "IF20"

        elif    ((aplicacao in lista_aplicacao_if20 or 
                  aplicacao in lista_aplicacao_if10) and 
                  tensao == "380V" and 
                  potencia in lista_if20_potencia_380 and 
                  not comunicacao in lista_if30_comunicacao and 
                  not adcional in lista_if30_recursos_adicionais):
            f1 = "IF20"

        elif    (aplicacao in lista_aplicacao_if10 and 
                  tensao == "380V-440V" and 
                  potencia in lista_if20_potencia_380_480 and 
                  not comunicacao in lista_if30_comunicacao and 
                  not adcional in lista_if30_recursos_adicionais):
            f1 = "IF20"

        elif    (aplicacao in lista_aplicacao_if20_mais1  and 
                  tensao == "380V-440V" and 
                  potencia in lista_if20_mais1_potencia_380_480 and 
                  not comunicacao in lista_if30_comunicacao and 
                  not adcional in lista_if30_recursos_adicionais):
            f1 = "IF20"


# OUTROS  220V
        elif    (aplicacao == "Outros" and 
                 tensao == "220V" and 
                 potencia in lista_if20_potencia_220 and 
                 not comunicacao in lista_if30_recursos_adicionais and 
                 not adcional in lista_if30_recursos_adicionais):
            f1 = "IF20"

# OUTROS 380v
        elif    (aplicacao == "Outros" and 
                 tensao == "380V" and 
                 potencia in lista_if20_potencia_380 and 
                 not comunicacao in lista_if30_recursos_adicionais and 
                 not adcional in lista_if30_recursos_adicionais):
            f1 = "IF20"

# OUTROS  380V-440V
        elif    (aplicacao == "Outros" and 
                 tensao == "380V-440V" and 
                 potencia in lista_if20_potencia_380_480 and 
                 not comunicacao in lista_if30_comunicacao and 
                 not adcional in lista_if30_recursos_adicionais):
            f1 = "IF20"

        elif    (aplicacao == "Outros" and 
                tensao == "380V-440V" and 
                potencia in lista_if30_potencia_380_480 and 
                (comunicacao in lista_if30_comunicacao or 
                adcional in lista_if30_adicionais)):
            f1 = "IF30"

        elif    (aplicacao == "Outros" and 
                tensao == "380V-440V" and 
                potencia in lista_if30_potencia_380_480 and 
                (not comunicacao in lista_if30_comunicacao or 
                not adcional in lista_if30_adicionais)):
            f1 = "IF30"

        # IF30
        elif    (aplicacao in lista_aplicacao_if10_20 and 
                tensao == "220V" and 
                potencia in lista_if30_mais1_potencia_220):
            f1 = "IF30"

        elif    (aplicacao in lista_aplicacao_if10 and 
                tensao == "220V" and 
                potencia in lista_if30_potencia_220 and 
                (comunicacao in lista_if30_comunicacao or 
                adcional in lista_if30_adicionais)):
            f1 = "IF30"

        elif    (aplicacao == "Outros" and 
                tensao == "220V" and 
                potencia in lista_if30_potencia_220 and 
                (comunicacao in lista_if30_comunicacao or 
                 adcional in lista_if30_recursos_adicionais)):
            f1 = "IF30"

        elif    (aplicacao in lista_aplicacao_if10_20 and 
                tensao == "220V" and 
                potencia in lista_if10_potencia_220 and 
                (comunicacao in lista_if30_comunicacao or 
                adcional in lista_if30_recursos_adicionais)):
            f1 = "IF30"

        elif    (aplicacao in lista_aplicacao_if10_20 and 
                tensao == "380V" and 
                potencia in lista_if10_potencia_220 and 
                (not comunicacao in lista_if30_comunicacao and 
                not adcional in lista_if30_recursos_adicionais)):
            f1 = "IF30"

        elif    (aplicacao in lista_aplicacao_if10_20 and 
                tensao == "380V-440V" and 
                potencia in lista_if30_mais1_potencia_380_480 and 
                (comunicacao in lista_if30_comunicacao or 
                adcional in lista_if30_recursos_adicionais)):
            f1 = "IF30"

        elif    (aplicacao in lista_aplicacao_if10_20 and 
                tensao == "380V-440V" and 
                potencia in lista_if30_mais1_potencia_380_480 and 
                (not comunicacao in lista_if30_comunicacao or 
                not adcional in lista_if30_recursos_adicionais)):
            f1 = "IF30"

        elif    (aplicacao in lista_aplicacao_if10 and 
                tensao == "380V-440V" and 
                potencia in lista_if30_potencia_380_480 and 
                (not comunicacao in lista_if30_comunicacao or 
                not adcional in lista_if30_recursos_adicionais)):
            f1 = "IF30"

        else:
            f1 = "xxx"

# COMPARAÇÃO PARA DEFINIR SE ADICIONA UMA POTÊNCIA ACIMA

        if aplicacao in lista_aplicacao_if20_mais1:
            soma1 = "0"  # valor 0 adiciona mais 1 na potência

        else:
            soma1 = "1"  # valor 1 não adiciona mais 1 na potência

# DEFINE A TENSAO DO INVERSOR
    # ==============================

        if  (tensao == "220V" and 
            aplicacao in lista_aplicacao_if10_20 and 
            potencia in lista_if20_mais1_potencia_220 and 
            (not comunicacao in lista_if30_comunicacao and 
            not adcional in lista_if30_adicionais)):
            f9 = "2"

        elif    (tensao == "220V" and 
                aplicacao in lista_aplicacao_if10_20 and 
                potencia in lista_if30_mais1_potencia_220 and 
                (comunicacao in lista_if30_comunicacao or 
                adcional in lista_if30_adicionais)):
            f9 = "2"

        elif    (tensao == "220V" and 
                aplicacao in lista_aplicacao_if10 and 
                potencia in lista_if20_potencia_220 and 
                (not comunicacao in lista_if30_comunicacao and 
                not adcional in lista_if30_adicionais)):
            f9 = "2"

        elif    (tensao == "220V" and 
                aplicacao in lista_aplicacao_if10_20 and 
                potencia in lista_if30_mais1_potencia_220 and 
                (comunicacao in lista_if30_comunicacao or 
                adcional in lista_if30_adicionais)):
            f9 = "2"

        elif    (tensao == "220V" and 
                aplicacao in lista_aplicacao_if10 and 
                potencia in lista_if30_potencia_220 and 
                (comunicacao in lista_if30_comunicacao or 
                adcional in lista_if30_adicionais)):
            f9 = "2"

        elif    (tensao == "220V" 
                and aplicacao == "Outros" and 
                potencia in lista_if20_potencia_220 and 
                not comunicacao in lista_if30_comunicacao and 
                not adcional in lista_if30_adicionais):
            f9 = "2"

        elif    (tensao == "220V" and 
                aplicacao == "Outros" and 
                potencia in lista_if30_potencia_220 and 
                (comunicacao in lista_if30_comunicacao or 
                adcional in lista_if30_adicionais)):
            f9 = "2"

        elif    (tensao == "380V" and 
                aplicacao in lista_aplicacao_if10_20 and 
                potencia in lista_if20_potencia_380 and 
                (not comunicacao in lista_if30_comunicacao and 
                not adcional in lista_if30_adicionais)):
            f9 = "4"

        elif    (tensao == "380V" and 
                aplicacao == "Outros" and 
                potencia in lista_if20_potencia_380 and 
                not comunicacao in lista_if30_comunicacao and 
                not adcional in lista_if30_adicionais):
            f9 = "4"


        elif    (aplicacao in lista_aplicacao_if20_mais1 and
                tensao == "380V-440V" and
                (potencia in lista_if20_mais1_potencia_380_480 or
                 potencia in lista_if30_potencia_380_480) and
                not comunicacao in lista_if30_comunicacao and
                not adcional in lista_if30_adicionais):
            f9 = "5"
            
        elif    (aplicacao in lista_aplicacao_if20_mais1 and
                tensao == "380V-440V" and
                potencia in lista_if30_mais1_potencia_380_480 and
                (comunicacao in lista_if30_comunicacao or
                adcional in lista_if30_adicionais)):
            f9 = "5"
            
        elif    ((aplicacao == "Outros" or
                aplicacao in lista_aplicacao_if10) and                  
                tensao == "380V-440V" and
                potencia in lista_potencia_geral and
                not comunicacao in lista_if30_comunicacao and
                not adcional in lista_if30_adicionais):
            f9 = "5"
            
# OUTRO E IF
        elif    ((aplicacao == "Outros" or
                aplicacao in lista_aplicacao_if10) and                  
                tensao == "380V-440V" and
                potencia in lista_if30_potencia_380_480 and
                (comunicacao in lista_if30_comunicacao or
                adcional in lista_if30_adicionais)):
            f9 = "5"

        else:
            f9 = "xxx"

    # ==============================

#   CONDIÇÃO MODELO 1CV

        # CONDIÇÃO PARA IF20
        if potencia == "1 cv" and tensao == "220V" and soma1 == "0" and aplicacao in lista_aplicacao_if20_mais1:
            pot = "02-1"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 2CV - 7A - 220V MONOFÁSICO"
            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF30 - 2CV - 7,2A - 220V MONOFÁSICO"

        elif potencia == "1 cv" and tensao == "220V" and soma1 == "0" and aplicacao in lista_aplicacao_if10_20:
            pot = "01-1"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 2CV - 7A - 220V MONOFÁSICO"
            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF30 - 2CV - 7,2A - 220V MONOFÁSICO"

        # CONDIÇÃO PARA IF10

        elif potencia == "1 cv" and tensao == "220V" and soma1 == "1" and aplicacao in lista_aplicacao_if10_20:
            pot = "01-1"
            var_inf_inversor = "INV. ESCALAR IF10 - 1CV - 5A - 220V MONOFÁSICO"

        elif potencia == "1 cv" and tensao == "220V" and aplicacao == "Outros":
            pot = "01-1"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 1CV - 5A - 220V MONOFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF30 - 1CV - 3,8A - 220V MONOFÁSICO"

#   CONDIÇÃO MODELO 2CV

        # CONDIÇÃO PARA IF20

         # CONDIÇÃO PARA IF20 + 1
        elif potencia == "2 cv" and tensao == "220V" and soma1 == "0" and aplicacao in lista_aplicacao_if20_mais1:
            pot = "03-1"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 3CV - 11A - 220V MONOFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF30 - 3CV - 9A - 220V MONOFÁSICO"

        elif potencia == "2 cv" and tensao == "220V" and soma1 == "0" and aplicacao in lista_aplicacao_if10_20:
            pot = "02-1"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 2CV - 7A - 220V MONOFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF30 - 2CV - 7,2A - 220V MONOFÁSICO"

        elif potencia == "2 cv" and tensao == "220V" and soma1 == "1" and aplicacao in lista_aplicacao_if10_20:
            pot = "02-1"
            var_inf_inversor = "INV. ESCALAR IF10 - 2CV - 7A - 220V MONOFÁSICO"

        elif potencia == "2 cv" and tensao == "220V" and aplicacao == "Outros":
            pot = "02-1"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 2CV - 7A - 220V MONOFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF30 - 2CV - 7,2A - 220V MONOFÁSICO"

        # ==============================

#   CONDIÇÃO MODELO 3CV
    # ==============================
        # CONDIÇÃO PARA IF20 +1
        elif potencia == "3 cv" and tensao == "220V" and soma1 == "0" and aplicacao in lista_aplicacao_if20_mais1:
            pot = "05-1"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 5CV - 16,5A - 220V MONOFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF30 - 5CV - 13A - 220V MONOFÁSICO"

        # CONDIÇÃO PARA IF20
        elif potencia == "3 cv" and tensao == "220V" and soma1 == "0" and aplicacao in lista_aplicacao_if10_20:
            pot = "03-1"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 3CV - 11A - 220V MONOFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF30 - 3CV - 9A - 220V MONOFÁSICO"

        # CONDIÇÃO PARA IF10
        elif potencia == "3 cv" and tensao == "220V" and soma1 == "1" and aplicacao in lista_aplicacao_if10_20:
            pot = "03-1"
            var_inf_inversor = "INV. ESCALAR IF10 - 3CV - 11A - 220V MONOFÁSICO"

        elif potencia == "3 cv" and tensao == "220V" and aplicacao == "Outros":
            pot = "03-1"

            if f1 == "IF20":
                var_inf_inversor = "INV. ESCALAR IF20 - 3CV - 11A - 220V MONOFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. ESCALAR IF30 - 3CV - 9A - 220V MONOFÁSICO"

        # CONDIÇÃO PARA IF20 + 1

#   CONDIÇÃO MODELO 5CV
    # ==============================
        # CONDIÇÃO PARA IF20

        # CONDIÇÃO PARA IF20 +1
        elif potencia == "5 cv" and tensao == "220V" and soma1 == "0" and aplicacao in lista_aplicacao_if20_mais1:
            pot = "08-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 7,5CV - 25A -220V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF30 - 7,5CV - 25A -220V TRIFÁSICO"

# ==============================

        elif potencia == "5 cv" and tensao == "220V" and soma1 == "0" and aplicacao in lista_aplicacao_if10_20:
            pot = "05-1"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 5CV - 16,5A - 220V MONOFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF30 - 5CV - 13A - 220V MONOFÁSICO"

        elif potencia == "5 cv" and tensao == "220V" and soma1 == "1" and aplicacao in lista_aplicacao_if10_20:
            pot = "05-1"
            var_inf_inversor = "INV. ESCALAR IF10 - 5CV - 16,5A - 220V MONOFÁSICO"

        elif potencia == "5 cv" and tensao == "220V" and aplicacao == "Outros":
            pot = "05-1"

            if f1 == "IF20":
                var_inf_inversor = "INV. ESCALAR IF20 - 5CV - 16,5A - 220V MONOFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. ESCALAR IF30 - 5CV - 13A - 220V MONOFÁSICO"

#   CONDIÇÃO MODELO 7,5CV
    # ==============================
        # CONDIÇÃO PARA IF20 + 1
        elif potencia == "7,5 cv" and tensao == "220V" and soma1 == "0" and aplicacao in lista_aplicacao_if20_mais1:
            pot = "10-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 10CV - 32A - 220V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF30 - 10CV - 32A - 220V TRIFÁSICO"

        # CONDIÇÃO PARA IF20
        elif potencia == "7,5 cv" and tensao == "220V" and soma1 == "1" and aplicacao in lista_aplicacao_if10_20:
            pot = "08-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 7,5CV - 25A -220V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF30 - 7,5CV - 25A -220V TRIFÁSICO"

        elif potencia == "7,5 cv" and tensao == "220V" and aplicacao == "Outros":
            pot = "08-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 7,5CV - 25A -220V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF30 - 7,5CV - 25A -220V TRIFÁSICO"

    # ==============================

#   CONDIÇÃO MODELO 10CV
        elif potencia == "10 cv" and tensao == "220V" and soma1 == "0" and aplicacao in lista_aplicacao_if20_mais1:
            pot = "15-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 15CV - 45A - 220V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF30 - 15CV - 45A - 220V TRIFÁSICO"

#   CONDIÇÃO MODELO 10CV
        elif potencia == "10 cv" and tensao == "220V" and soma1 == "1" and aplicacao in lista_aplicacao_if10_20:
            pot = "10-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 10CV - 32A - 220V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF30 - 10CV - 32A - 220V TRIFÁSICO"

        elif potencia == "10 cv" and tensao == "220V" and aplicacao == "Outros":
            pot = "10-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 10CV - 32A - 220V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF30 - 10CV - 32A - 220V TRIFÁSICO"

    # ==============================

#   CONDIÇÃO MODELO 15CV
        elif potencia == "15 cv" and tensao == "220V" and aplicacao in lista_aplicacao_if20_mais1:
            pot = "20-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 20CV - 60A - 220V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF20 - 30CV - 60A - 220V TRIFÁSICO"

#   CONDIÇÃO MODELO 15CV
        elif potencia == "15 cv" and tensao == "220V" and aplicacao in lista_aplicacao_if10_20:
            pot = "15-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 15CV - 45A - 220V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF30 - 15CV - 45A - 220V TRIFÁSICO"

#   CONDIÇÃO MODELO 15CV
        elif potencia == "15 cv" and tensao == "220V" and aplicacao == "Outros":
            pot = "15-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 15CV - 45A - 220V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF30 - 15CV - 45A - 220V TRIFÁSICO"

    # ==============================

#   CONDIÇÃO MODELO 20CV +1
        elif potencia == "20 cv" and tensao == "220V" and aplicacao in lista_aplicacao_if20_mais1:
            pot = "25-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 25CV - 75A - 220V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF30 - 25CV - 75A - 220V TRIFÁSICO"

#   CONDIÇÃO MODELO 20CV
        elif potencia == "20 cv" and tensao == "220V" and aplicacao in lista_aplicacao_if10_20:
            pot = "20-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 20CV - 60A - 220V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF30 - 20CV - 60A - 220V TRIFÁSICO"

#   CONDIÇÃO MODELO 20CV
        elif potencia == "20 cv" and tensao == "220V" and aplicacao == "Outros":
            pot = "20-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 20CV - 60A - 220V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF30 - 20CV - 60A - 220V TRIFÁSICO"

      # ==============================

#   CONDIÇÃO MODELO 25CV +1
        elif potencia == "25 cv" and tensao == "220V" and aplicacao in lista_aplicacao_if20_mais1:
            pot = "30-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 30CV - 90A - 220V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF30 - 30CV - 90A - 220V TRIFÁSICO"

#   CONDIÇÃO MODELO 25CV
        elif potencia == "25 cv" and tensao == "220V" and aplicacao in lista_aplicacao_if10_20:
            pot = "25-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 25CV - 75A - 220V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF30 - 25CV - 75A - 220V TRIFÁSICO"

#   CONDIÇÃO MODELO 25CV
        elif potencia == "25 cv" and tensao == "220V" and aplicacao == "Outros":
            pot = "25-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 25CV - 75A - 220V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF30 - 25CV - 75A - 220V TRIFÁSICO"

        # ==============================

#   CONDIÇÃO MODELO 30CV +1
        elif potencia == "30 cv" and tensao == "220V" and aplicacao in lista_aplicacao_if20_mais1:
            pot = "40-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 40CV - 110A - 220V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF30 - 40CV - 110A - 220V TRIFÁSICO"

#   CONDIÇÃO MODELO 30CV
        elif potencia == "30 cv" and tensao == "220V" and aplicacao in lista_aplicacao_if10_20:
            pot = "30-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 30CV - 90A - 220V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF30 - 30CV - 90A - 220V TRIFÁSICO"

#   CONDIÇÃO MODELO 30CV
        elif potencia == "30 cv" and tensao == "220V" and aplicacao == "Outros":
            pot = "30-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 30CV - 90A - 220V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF30 - 30CV - 90A - 220V TRIFÁSICO"

    # ==============================

#   CONDIÇÃO MODELO 40CV +1
        elif    (potencia == "40 cv" and 
                tensao == "220V" and 
                aplicacao in lista_aplicacao_if20_mais1 and 
                (not comunicacao in lista_if30_comunicacao and 
                not adcional in lista_if30_adicionais)):
            pot = "50-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 50CV - 150A - 220V TRIFÁSICO"

#   CONDIÇÃO MODELO 40CV
        elif potencia == "40 cv" and tensao == "220V" and aplicacao in lista_aplicacao_if10_20 and (not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais):
            pot = "40-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 40CV - 110A - 220V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF30 - 40CV - 110A - 220V TRIFÁSICO"

#   CONDIÇÃO MODELO 40CV
        elif potencia == "40 cv" and tensao == "220V" and aplicacao in lista_aplicacao_if10 and (comunicacao in lista_if30_comunicacao or adcional in lista_if30_adicionais):
            pot = "40-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 40CV - 110A - 220V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF30 - 40CV - 110A - 220V TRIFÁSICO"

#   CONDIÇÃO MODELO 40CV
        elif potencia == "40 cv" and tensao == "220V" and aplicacao == "Outros":
            pot = "40-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 40CV - 110A - 220V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF30 - 40CV - 110A - 220V TRIFÁSICO"

      # ==============================

#   CONDIÇÃO MODELO 50CV +1
        elif potencia == "50 cv" and tensao == "220V" and aplicacao in lista_aplicacao_if20_mais1 and (not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais):
            pot = "60-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 60CV - 176A - 220V TRIFÁSICO"

#   CONDIÇÃO MODELO 50CV
        elif    (potencia == "50 cv" and 
                tensao == "220V" and 
                aplicacao in lista_aplicacao_if10_20 and 
                (not comunicacao in lista_if30_comunicacao and 
                not adcional in lista_if30_recursos_adicionais)):
            pot = "50-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 50CV - 150A - 220V TRIFÁSICO"

#   CONDIÇÃO MODELO 50CV
        elif potencia == "50 cv" and tensao == "220V" and aplicacao == "Outros" and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais:
            pot = "50-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 50CV - 150A - 220V TRIFÁSICO"

      # ==============================

#   CONDIÇÃO MODELO 60CV +1
        elif potencia == "60 cv" and tensao == "220V" and aplicacao in lista_aplicacao_if20_mais1 and (not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais):
            pot = "75-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 75CV - 210A - 220V TRIFÁSICO"

#   CONDIÇÃO MODELO 60CV
        elif potencia == "60 cv" and tensao == "220V" and aplicacao in lista_aplicacao_if10_20 and (not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_recursos_adicionais):
            pot = "60-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 60CV - 176A - 220V TRIFÁSICO"

#   CONDIÇÃO MODELO 60CV
        elif potencia == "60 cv" and tensao == "220V" and aplicacao == "Outros" and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais:
            pot = "60-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 60CV - 176A - 220V TRIFÁSICO"

  #####################################

#   CONDIÇÃO MODELO 75CV +1
        elif potencia == "75 cv" and tensao == "220V" and aplicacao in lista_aplicacao_if20_mais1 and (not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais):
            pot = "xxx"
            var_inf_inversor = ""  # "** INV. VETORIAL IF20 - 100CV - 150A - 380V TRIFÁSICO **"

#   CONDIÇÃO MODELO 75CV
        elif potencia == "75 cv" and tensao == "220V" and aplicacao in lista_aplicacao_if10_20 and (not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_recursos_adicionais):
            pot = "75-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 75CV - 210A - 220V TRIFÁSICO"

#   CONDIÇÃO MODELO 75CV
        elif potencia == "75 cv" and tensao == "220V" and aplicacao == "Outros" and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais:
            pot = "75-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 75CV - 210A - 220V TRIFÁSICO"

#####################################################################

#   CONDIÇÃO MODELO 1CV +1
    # ==============================
        elif (potencia == "1 cv" and tensao == "380V" and soma1 == "0" and aplicacao in lista_aplicacao_if20_mais1 and (not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais)):
            pot = "02-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 2CV - 3,7A - 380V TRIFÁSICO"

#   CONDIÇÃO MODELO 1CV
        elif (potencia == "1 cv" and tensao == "380V" and soma1 == "0" and aplicacao in lista_aplicacao_if10_20 and (not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais)):
            pot = "01-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 1CV - 2,5A - 380V TRIFÁSICO"

        elif potencia == "1 cv" and tensao == "380V" and soma1 == "1" and aplicacao in lista_aplicacao_if10_20 and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais:
            pot = "01-3"
            var_inf_inversor = "INV. ESCALAR IF10 - 1CV - 2.7A - 380V TRIFÁSICO"

        elif potencia == "1 cv" and tensao == "380V" and aplicacao == "Outros":
            pot = "01-3"
            var_inf_inversor = "INV. ESCALAR IF20 - 1CV - 2,5A - 380V TRIFÁSICO"

    # ==============================

#   CONDIÇÃO MODELO 2CV +1

        elif potencia == "2 cv" and tensao == "380V" and soma1 == "0" and aplicacao in lista_aplicacao_if20_mais1 and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais:
            pot = "03-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 3CV - 5A - 380V TRIFÁSICO"

#   CONDIÇÃO MODELO 2CV

        elif potencia == "2 cv" and tensao == "380V" and soma1 == "0" and aplicacao in lista_aplicacao_if10_20 and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais:
            pot = "02-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 2CV - 3,7A - 380V TRIFÁSICO"

        elif potencia == "2 cv" and tensao == "380V" and soma1 == "1" and aplicacao in lista_aplicacao_if10_20 and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais:
            pot = "02-3"
            var_inf_inversor = "INV. ESCALAR IF10 - 2CV - 4A - 380V TRIFÁSICO"

        elif potencia == "2 cv" and tensao == "380V" and aplicacao == "Outros" and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais:
            pot = "02-3"
            var_inf_inversor = "INV. ESCALAR IF20 - 2CV - 3.7A - 380V TRIFÁSICO"

    # ==============================

#   CONDIÇÃO MODELO 3CV +1
        elif potencia == "3 cv" and tensao == "380V" and soma1 == "0" and aplicacao in lista_aplicacao_if20_mais1 and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais:
            pot = "05-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 5CV - 9A - 380V TRIFÁSICO"

#   CONDIÇÃO MODELO 3CV
        elif potencia == "3 cv" and tensao == "380V" and soma1 == "0" and aplicacao in lista_aplicacao_if10_20 and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais:
            pot = "03-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 3CV - 5A - 380V TRIFÁSICO"

        elif potencia == "3 cv" and tensao == "380V" and soma1 == "1" and aplicacao in lista_aplicacao_if10_20 and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais:
            pot = "03-3"
            var_inf_inversor = "INV. ESCALAR IF10 - 3CV - 5A - 380V TRIFÁSICO"

        elif potencia == "3 cv" and tensao == "380V" and aplicacao == "Outros" and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais:
            pot = "03-3"
            var_inf_inversor = "INV. ESCALAR IF20 - 3CV - 5A - 380V TRIFÁSICO"

    # ==============================

#   CONDIÇÃO MODELO 5CV +1
        elif potencia == "5 cv" and tensao == "380V" and soma1 == "0" and aplicacao in lista_aplicacao_if20_mais1 and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais:
            pot = "08-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 7,5CV - 13A - 380V TRIFÁSICO"

#   CONDIÇÃO MODELO 5CV
        elif potencia == "5 cv" and tensao == "380V" and soma1 == "0" and aplicacao in lista_aplicacao_if10_20 and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais:
            pot = "05-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 5CV - 9A - 380V TRIFÁSICO"

        elif potencia == "5 cv" and tensao == "380V" and soma1 == "1" and aplicacao in lista_aplicacao_if10_20 and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais:
            pot = "05-3"
            var_inf_inversor = "INV. ESCALAR IF10 - 5CV - 8,6 - 380V TRIFÁSICO"

        elif potencia == "5 cv" and tensao == "380V" and aplicacao == "Outros" and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais:
            pot = "05-3"
            var_inf_inversor = "INV. ESCALAR IF20 - 5CV - 9A - 380V TRIFÁSICO"

    # ==============================

#   CONDIÇÃO MODELO 7,5CV +1
        elif potencia == "7,5 cv" and tensao == "380V" and soma1 == "0" and aplicacao in lista_aplicacao_if20_mais1 and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais:
            pot = "10-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 10CV - 17A - 380V TRIFÁSICO"

#   CONDIÇÃO MODELO 7,5CV
        elif potencia == "7,5 cv" and tensao == "380V" and soma1 == "0" and aplicacao in lista_aplicacao_if10_20 and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais:
            pot = "08-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 7,5CV - 13A - 380V TRIFÁSICO"

        elif potencia == "7,5 cv" and tensao == "380V" and soma1 == "1" and aplicacao in lista_aplicacao_if10_20 and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais:
            pot = "08-3"
            var_inf_inversor = "INV. ESCALAR IF10 - 7,5CV - 12,5 - 380V TRIFÁSICO"

        elif potencia == "7,5 cv" and tensao == "380V" and aplicacao == "Outros" and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais:
            pot = "08-3"
            var_inf_inversor = "INV. ESCALAR IF20 - 7,5CV - 13A - 380V TRIFÁSICO"

    # ==============================

#   CONDIÇÃO MODELO 10CV +1
        elif potencia == "10 cv" and tensao == "380V" and soma1 == "0" and aplicacao in lista_aplicacao_if20_mais1 and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais:
            pot = "15-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 15CV - 25A - 380V TRIFÁSICO"

#   CONDIÇÃO MODELO 10CV
        elif potencia == "10 cv" and tensao == "380V" and soma1 == "0" and aplicacao in lista_aplicacao_if10_20 and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais:
            pot = "10-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 10CV - 17A - 380V TRIFÁSICO"

        elif potencia == "10 cv" and tensao == "380V" and soma1 == "1" and aplicacao in lista_aplicacao_if10_20 and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais:
            pot = "10-3"
            var_inf_inversor = "INV. ESCALAR IF10 - 10CV - 17,5A - 380V TRIFÁSICO"

        elif potencia == "10 cv" and tensao == "380V" and aplicacao == "Outros" and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais:
            pot = "10-3"
            var_inf_inversor = "INV. ESCALAR IF10 - 20CV - 17A - 380V TRIFÁSICO"

    # ==============================

#   CONDIÇÃO MODELO 15CV +1
        elif potencia == "15 cv" and tensao == "380V" and aplicacao in lista_aplicacao_if20_mais1 and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais:
            pot = "20-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 20CV - 32A - 380V TRIFÁSICO"

#   CONDIÇÃO MODELO 15CV
        elif potencia == "15 cv" and tensao == "380V" and aplicacao in lista_aplicacao_if10_20 and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais:
            pot = "15-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 15CV - 25A - 380V TRIFÁSICO"

        elif potencia == "15 cv" and tensao == "380V" and aplicacao == "Outros" and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais:
            pot = "15-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 15CV - 25A - 380V TRIFÁSICO"

    # ==============================

#   CONDIÇÃO MODELO 20CV +1
        elif potencia == "20 cv" and tensao == "380V" and aplicacao in lista_aplicacao_if20_mais1 and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais:
            pot = "30-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 30CV - 45A - 380V TRIFÁSICO"

#   CONDIÇÃO MODELO 20CV
        elif potencia == "20 cv" and tensao == "380V" and aplicacao in lista_aplicacao_if10_20 and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais:
            pot = "20-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 20CV - 32A - 380V TRIFÁSICO"

#   CONDIÇÃO MODELO 20CV
        elif potencia == "20 cv" and tensao == "380V" and aplicacao == "Outros" and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais:
            pot = "20-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 20CV - 32A - 380V TRIFÁSICO"

    # ==============================

#   CONDIÇÃO MODELO 25CV +1
        elif potencia == "25 cv" and tensao == "380V" and aplicacao in lista_aplicacao_if20_mais1 and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais:
            pot = "30-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 30CV - 45A - 380V TRIFÁSICO"

#   CONDIÇÃO MODELO 25CV
        elif potencia == "25 cv" and tensao == "380V" and aplicacao in lista_aplicacao_if10_20 and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais:
            pot = "25-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 25CV - 380V TRIFÁSICO"

#   CONDIÇÃO MODELO 25CV
        elif potencia == "25 cv" and tensao == "380V" and aplicacao == "Outros" and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais:
            pot = "25-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 25CV - 380V TRIFÁSICO"

    # ==============================

#   CONDIÇÃO MODELO 30CV +1
        elif potencia == "30 cv" and tensao == "380V" and aplicacao in lista_aplicacao_if20_mais1 and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais:
            pot = "40-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 40CV - 60A - 380V TRIFÁSICO"

#   CONDIÇÃO MODELO 30CV
        elif potencia == "30 cv" and tensao == "380V" and aplicacao in lista_aplicacao_if10_20 and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais:
            pot = "30-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 30CV - 45A - 380V TRIFÁSICO"

#   CONDIÇÃO MODELO 30CV
        elif potencia == "30 cv" and tensao == "380V" and aplicacao == "Outros" and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais:
            pot = "30-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 30CV - 45A - 380V TRIFÁSICO"

    # ==============================

#   CONDIÇÃO MODELO 40CV +1
        elif potencia == "40 cv" and tensao == "380V" and aplicacao in lista_aplicacao_if20_mais1 and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais:
            pot = "50-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 50CV - 75A - 380V TRIFÁSICO"

#   CONDIÇÃO MODELO 40CV
        elif potencia == "40 cv" and tensao == "380V" and aplicacao in lista_aplicacao_if10_20 and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais:
            pot = "40-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 40CV - 60A - 380V TRIFÁSICO"

#   CONDIÇÃO MODELO 40CV
        elif potencia == "40 cv" and tensao == "380V" and aplicacao == "Outros" and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais:
            pot = "40-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 40CV - 60A - 380V TRIFÁSICO"

    # ==============================

#   CONDIÇÃO MODELO 50CV +1
        elif potencia == "50 cv" and tensao == "380V" and aplicacao in lista_aplicacao_if20_mais1 and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais:
            pot = "75-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 75CV - 110A - 380V TRIFÁSICO"

#   CONDIÇÃO MODELO 50CV
        elif potencia == "50 cv" and tensao == "380V" and aplicacao in lista_aplicacao_if10_20 and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais:
            pot = "50-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 50CV - 75A - 380V TRIFÁSICO"

#   CONDIÇÃO MODELO 50CV
        elif potencia == "50 cv" and tensao == "380V" and aplicacao == "Outros" and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais:
            pot = "50-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 50CV - 75A - 380V TRIFÁSICO"

    # ==============================

#   CONDIÇÃO MODELO 75CV +1
        elif potencia == "60 cv" and tensao == "380V" and aplicacao in lista_aplicacao_if20_mais1 and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais:
            pot = "75-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 75CV - 110A - 380V TRIFÁSICO"

#   CONDIÇÃO MODELO 75CV
        elif potencia == "60 cv" and tensao == "380V" and aplicacao in lista_aplicacao_if10_20 and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais:
            pot = "75-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 75CV - 110A - 380V TRIFÁSICO"

#   CONDIÇÃO MODELO 75CV                            '
        elif potencia == "60 cv" and tensao == "380V" and aplicacao == "Outros" and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais:
            pot = "75-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 75CV - 110A - 380V TRIFÁSICO"

    # ==============================

#   CONDIÇÃO MODELO 75CV +1
        elif potencia == "75 cv" and tensao == "380V" and aplicacao in lista_aplicacao_if20_mais1 and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais:
            pot = "100-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 100CV - 150A - 380V TRIFÁSICO"

#   CONDIÇÃO MODELO 75CV
        elif potencia == "75 cv" and tensao == "380V" and aplicacao in lista_aplicacao_if10_20 and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais:
            pot = "75-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 75CV - 110A - 380V TRIFÁSICO"

#   CONDIÇÃO MODELO 75CV
        elif potencia == "75 cv" and tensao == "380V" and aplicacao == "Outros" and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais:
            pot = "75-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 75CV - 110A - 380V TRIFÁSICO"

    # ==============================

#   CONDIÇÃO MODELO 100CV +1
        elif (potencia == "100 cv" and 
              tensao == "380V" and 
              aplicacao in lista_aplicacao_if20_mais1 and 
              f1 == "IF20" and
              not comunicacao in lista_if30_comunicacao and 
              not adcional in lista_if30_adicionais):
            pot = "125-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 125CV - 176A - 380V"

#   CONDIÇÃO MODELO 100CV
        elif (potencia == "100 cv" and 
              tensao == "380V" and 
              aplicacao in lista_aplicacao_if10_20 and 
              f1 == "IF20" and
              not comunicacao in lista_if30_comunicacao and 
              not adcional in lista_if30_adicionais):
            pot = "100-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 100CV - 150A - 380V TRIFÁSICO"

#   CONDIÇÃO MODELO 100CV
        elif (potencia == "100 cv" and 
                tensao == "380V" and 
                aplicacao == "Outros" and 
                f1 == "IF20" and
                not comunicacao in lista_if30_comunicacao and 
                not adcional in lista_if30_adicionais):
            pot = "100-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 100CV - 150A - 380V TRIFÁSICO"

    # ==============================

#   CONDIÇÃO MODELO 125V +1
        elif (potencia == "125 cv" and 
                tensao == "380V" and 
                aplicacao in lista_aplicacao_if20_mais1 and 
                f1 == "IF20" and
                not comunicacao in lista_if30_comunicacao and 
                not adcional in lista_if30_adicionais):
            pot = "150-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 150CV - 210A - 380V TRIFÁSICO"

#   CONDIÇÃO MODELO 125V
        elif (potencia == "125 cv" and 
                tensao == "380V" and 
                aplicacao in lista_aplicacao_if10_20 and 
                f1 == "IF20" and
                not comunicacao in lista_if30_comunicacao and 
                not adcional in lista_if30_adicionais):
            pot = "125-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 125CV - 176A - 380V"

#   CONDIÇÃO MODELO 125V
        elif (potencia == "125 cv" and 
                tensao == "380V" and 
                aplicacao == "Outros" and 
                f1 == "IF20" and
                not comunicacao in lista_if30_comunicacao and 
                not adcional in lista_if30_adicionais):
            pot = "125-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 125CV - 176A - 380V"

    # ==============================

#   CONDIÇÃO MODELO 150CV +1
        elif (potencia == "150 cv" and 
              tensao == "380V" and 
              aplicacao in lista_aplicacao_if20_mais1 and 
              f1 == "IF20" and
              not comunicacao in lista_if30_comunicacao and 
              not adcional in lista_if30_adicionais):
            pot = "175-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 175CV - 253A - 380 A 480V TRIFÁSICO"

#   CONDIÇÃO MODELO 150CV
        elif (potencia == "150 cv" and 
              tensao == "380V" and 
              aplicacao in lista_aplicacao_if10_20 and 
              f1 == "IF20" and
              not comunicacao in lista_if30_comunicacao and 
              not adcional in lista_if30_adicionais):
            pot = "150-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 150CV - 210A - 380V TRIFÁSICO"

#   CONDIÇÃO MODELO 150CV
        elif (potencia == "150 cv" and 
              tensao == "380V" and 
              aplicacao == "Outros" and 
              f1 == "IF20" and
              not comunicacao in lista_if30_comunicacao and 
              not adcional in lista_if30_adicionais):
            pot = "150-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 150CV - 210A - 380V TRIFÁSICO"

    # ==============================

#   CONDIÇÃO MODELO 5CV +1
        elif potencia == "5 cv" and tensao == "380V-440V" and aplicacao in lista_aplicacao_if20_mais1:
            pot = "08-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 7,5CV - 13A - 380 A 460V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF20 - 7,5CV - 13A - 380 A 460V TRIFÁSICO"

#   CONDIÇÃO MODELO IF30 380-480

#   CONDIÇÃO MODELO 1CV +1
        elif (potencia == "1 cv" and tensao == "380V-440V" and aplicacao in lista_aplicacao_if20_mais1 and (comunicacao in lista_if30_comunicacao or adcional in lista_if30_adicionais)):
            pot = "02-3"
            var_inf_inversor = "INV. VETORIAL IF30 - 2CV - 3,8A - 380 A 480V TRIFÁSICO"

        elif (potencia == "1 cv" and tensao == "380V-440V" and aplicacao in lista_aplicacao_if20_mais1 and (not comunicacao in lista_if30_comunicacao or not adcional in lista_if30_adicionais)):
            pot = "02-3"
            var_inf_inversor = "INV. VETORIAL IF30 - 2CV - 3,8A - 380 A 480V TRIFÁSICO"

        elif (potencia == "1 cv" and tensao == "380V-440V" and aplicacao in lista_aplicacao_if10 and (not comunicacao in lista_if30_comunicacao or not adcional in lista_if30_adicionais)):
            pot = "01-3"
            var_inf_inversor = "INV. VETORIAL IF30 - 1CV - 2,1A - 380 A 480V TRIFÁSICO"

        elif (potencia == "1 cv" and tensao == "380V-440V" and aplicacao == "Outros"):
            pot = "01-3"
            var_inf_inversor = "INV. VETORIAL IF30 - 1CV - 2,1A - 380 A 480V TRIFÁSICO"

#   CONDIÇÃO MODELO 2CV +1
        elif potencia == "2 cv" and tensao == "380V-440V" and aplicacao in lista_aplicacao_if20_mais1:
            pot = "03-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 3CV - 5,1A - 380 A 480V TRIFÁSICO"

        elif (potencia == "2 cv" and tensao == "380V-440V" and (aplicacao in lista_aplicacao_if10_20 or aplicacao == "Outros")):
            pot = "02-3"
            var_inf_inversor = "INV. VETORIAL IF30 - 2CV - 3,8A - 380 A 480V TRIFÁSICO"

#   CONDIÇÃO MODELO 3CV +1
        elif potencia == "3 cv" and tensao == "380V-440V" and aplicacao in lista_aplicacao_if20_mais1:
            pot = "05-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 5CV - 9A - 380 A 480V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF30 - 5CV - 9A - 380 A 480V TRIFÁSICO"

        elif (potencia == "3 cv" and tensao == "380V-440V" and (aplicacao in lista_aplicacao_if10_20 or aplicacao == "Outros")):
            pot = "03-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 3CV - 5,1A - 380 A 480V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF30 - 3CV - 5,1A - 380 A 480V TRIFÁSICO"

#   CONDIÇÃO MODELO 5CV
        elif potencia == "5 cv" and tensao == "380V-440V" and aplicacao in lista_aplicacao_if10_20:
            pot = "05-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 5CV - 9A - 380 A 460V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF30 - 5CV - 9A - 380 A 460V TRIFÁSICO"

        elif potencia == "5 cv" and tensao == "380V-440V" and aplicacao == "Outros":
            pot = "05-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 5CV - 9A - 380 A 460V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF30 - 5CV - 9A - 380 A 460V TRIFÁSICO"

    # ==============================

#   CONDIÇÃO MODELO 7,5CV +1
        elif potencia == "7,5 cv" and tensao == "380V-440V" and aplicacao in lista_aplicacao_if20_mais1:
            pot = "10-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 10CV - 17A - 380 A 460V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF30 - 10CV - 17A - 380 A 460V TRIFÁSICO"

#   CONDIÇÃO MODELO 7,5CV
        elif potencia == "7,5 cv" and tensao == "380V-440V" and aplicacao in lista_aplicacao_if10_20:
            pot = "08-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 7,5CV - 13A - 380 A 460V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF30 - 7,5CV - 13A - 380 A 460V TRIFÁSICO"

        elif potencia == "7,5 cv" and tensao == "380V-440V" and aplicacao == "Outros":
            pot = "08-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 7,5CV - 13A - 380 A 460V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF30 - 7,5CV - 13A - 380 A 460V TRIFÁSICO"

    # ==============================

#   CONDIÇÃO MODELO 10CV +1
        elif potencia == "10 cv" and tensao == "380V-440V" and aplicacao in lista_aplicacao_if20_mais1:
            pot = "15-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 15CV - 25A - 380 A 460V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF30 - 15CV - 25A - 380 A 460V TRIFÁSICO"

#   CONDIÇÃO MODELO 10CV
        elif potencia == "10 cv" and tensao == "380V-440V" and aplicacao in lista_aplicacao_if10_20:
            pot = "10-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 10CV - 17A - 380 A 460V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF30 - 10CV - 17A - 380 A 460V TRIFÁSICO"

#   CONDIÇÃO MODELO 10CV
        elif potencia == "10 cv" and tensao == "380V-440V" and aplicacao == "Outros":
            pot = "10-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 10CV - 17A - 380 A 460V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF30 - 10CV - 17A - 380 A 460V TRIFÁSICO"

    # ==============================

#   CONDIÇÃO MODELO 15CV +1
        elif potencia == "15 cv" and tensao == "380V-440V" and aplicacao in lista_aplicacao_if20_mais1:
            pot = "20-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 20CV - 32A - 380 A 460V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF30 - 20CV - 32A - 380 A 460V TRIFÁSICO"

#   CONDIÇÃO MODELO 15CV
        elif potencia == "15 cv" and tensao == "380V-440V" and aplicacao in lista_aplicacao_if10_20:
            pot = "15-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 15CV - 25A - 380 A 460V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF20 - 15CV - 25A - 380 A 460V TRIFÁSICO"

#   CONDIÇÃO MODELO 15CV
        elif potencia == "15 cv" and tensao == "380V-440V" and aplicacao == "Outros":
            pot = "15-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 15CV - 25A - 380 A 460V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF20 - 15CV - 25A - 380 A 460V TRIFÁSICO"

    # ==============================

#   CONDIÇÃO MODELO 20CV +1
        elif ((potencia == "20 cv") and (tensao == "380V-440V")) and aplicacao in lista_aplicacao_if20_mais1:
            pot = "30-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 30CV - 45A - 380 A 460V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF20 - 30CV - 45A - 380 A 460V TRIFÁSICO"

#   CONDIÇÃO MODELO 20CV
        elif ((potencia == "20 cv") and (tensao == "380V-440V")) and aplicacao in lista_aplicacao_if10_20:
            pot = "20-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 20CV - 32A - 380 A 460V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF20 - 20CV - 32A - 380 A 460V TRIFÁSICO"

#   CONDIÇÃO MODELO 20CV
        elif ((potencia == "20 cv") and (tensao == "380V-440V")) and aplicacao == "Outros":
            pot = "20-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 20CV - 32A - 380 A 460V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF20 - 20CV - 32A - 380 A 460V TRIFÁSICO"

    # ==============================

#   CONDIÇÃO MODELO 30CV +1
        elif ((potencia == "25 cv") and (tensao == "380V-440V")) and aplicacao in lista_aplicacao_if20_mais1:
            pot = "30-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 30CV - 45A - 380 A 460V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF20 - 30CV - 45A - 380 A 460V TRIFÁSICO"

#   CONDIÇÃO MODELO 30CV
        elif ((potencia == "25 cv") and (tensao == "380V-440V")) and aplicacao in lista_aplicacao_if10_20:
            pot = "30-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 30CV - 45A - 380 A 460V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF20 - 30CV - 45A - 380 A 460V TRIFÁSICO"

#   CONDIÇÃO MODELO 30CV
        elif ((potencia == "25 cv") and (tensao == "380V-440V")) and aplicacao == "Outros":
            pot = "30-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 30CV - 45A - 380 A 460V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF20 - 30CV - 45A - 380 A 460V TRIFÁSICO"

    # ==============================

#   CONDIÇÃO MODELO 30CV +1
        elif ((potencia == "30 cv") and (tensao == "380V-440V")) and aplicacao in lista_aplicacao_if20_mais1:
            pot = "40-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 40CV - 60A - 380 A 460V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF20 - 40CV - 60A - 380 A 460V TRIFÁSICO"

#   CONDIÇÃO MODELO 30CV
        elif ((potencia == "30 cv") and (tensao == "380V-440V")) and aplicacao in lista_aplicacao_if10_20:
            pot = "30-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 30CV - 45A - 380 A 460V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF20 - 30CV - 45A - 380 A 460V TRIFÁSICO"

#   CONDIÇÃO MODELO 30CV
        elif ((potencia == "30 cv") and (tensao == "380V-440V")) and aplicacao == "Outros":
            pot = "30-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 30CV - 45A - 380 A 460V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF20 - 30CV - 45A - 380 A 460V TRIFÁSICO"

    # ==============================

#   CONDIÇÃO MODELO 40CV +1
        elif ((potencia == "40 cv") and (tensao == "380V-440V")) and aplicacao in lista_aplicacao_if20_mais1:
            pot = "50-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 50CV - 75A - 380 A 460V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF20 - 50CV - 75A - 380 A 460V TRIFÁSICO"

#   CONDIÇÃO MODELO 40CV
        elif ((potencia == "40 cv") and (tensao == "380V-440V")) and aplicacao in lista_aplicacao_if10_20:
            pot = "40-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 40CV - 60A - 380 A 460V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF20 - 40CV - 60A - 380 A 460V TRIFÁSICO"

#   CONDIÇÃO MODELO 40CV
        elif ((potencia == "40 cv") and (tensao == "380V-440V")) and aplicacao == "Outros":
            pot = "40-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 40CV - 60A - 380 A 460V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF20 - 40CV - 60A - 380 A 460V TRIFÁSICO"

    # ==============================

#   CONDIÇÃO MODELO 50CV +1
        elif (potencia == "50 cv" and tensao == "380V-440V" and aplicacao in lista_aplicacao_if20_mais1 and (not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais)):
            pot = "60-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 75CV - 110A - 380 A 460V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF20 - 75CV - 110A - 380 A 460V TRIFÁSICO"

#   CONDIÇÃO MODELO 50CV
        elif ((potencia == "50 cv") and (tensao == "380V-440V")) and (aplicacao == "Outros" or aplicacao in lista_aplicacao_if10)              :
            pot = "50-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 50CV - 75A - 380 A 460V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF20 - 50CV - 75A - 380 A 460V TRIFÁSICO"

    # ==============================

#   CONDIÇÃO MODELO 60CV +1
        elif (potencia == "60 cv" and tensao == "380V-440V" and aplicacao in lista_aplicacao_if20_mais1 and (not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais)):
            pot = "75-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 75CV - 110A - 380 A 460V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF20 - 75CV - 110A - 380 A 460V TRIFÁSICO"

#   CONDIÇÃO MODELO 75CV
        elif (potencia == "60 cv" and tensao == "380V-440V" and aplicacao in lista_aplicacao_if10_20 and (not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais)):
            pot = "75-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 75CV - 110A - 380 A 460V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF20 - 75CV - 110A - 380 A 460V TRIFÁSICO"

#   CONDIÇÃO MODELO 75CV
        elif (potencia == "60 cv" and tensao == "380V-440V" and aplicacao == "Outros"):
            pot = "xxx"
            var_inf_inversor = ""

    # ==============================

#   CONDIÇÃO MODELO 75CV +1
        elif (potencia == "75 cv" and tensao == "380V-440V" and aplicacao in lista_aplicacao_if20_mais1 and (not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais)):
            pot = "100-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 100CV - 150A - 380 A 480V TRIFÁSICO"

#   CONDIÇÃO MODELO 75CV
        elif (potencia == "75 cv" and tensao == "380V-440V" and aplicacao in lista_aplicacao_if10_20 and (not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais)):
            pot = "75-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 75CV - 110A - 380 A 460V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF20 - 75CV - 110A - 380 A 460V TRIFÁSICO"

#   CONDIÇÃO MODELO 75CV
        elif ((potencia == "75 cv") and (tensao == "380V-440V")) and aplicacao == "Outros" and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_recursos_adicionais:
            pot = "75-3"

            if f1 == "IF20":
                var_inf_inversor = "INV. VETORIAL IF20 - 75CV - 110A - 380 A 460V TRIFÁSICO"

            elif f1 == "IF30":
                var_inf_inversor = "INV. VETORIAL IF20 - 75CV - 110A - 380 A 460V TRIFÁSICO"

    # ==============================

#   CONDIÇÃO MODELO 100CV +1
        elif (potencia == "100 cv" and tensao == "380V-440V" and aplicacao in lista_aplicacao_if20_mais1 and (not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais)):
            pot = "125-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 125CV - 176A - 380 A 480V TRIFÁSICO"

#   CONDIÇÃO MODELO 100CV
        elif (potencia == "100 cv" and tensao == "380V-440V" and aplicacao in lista_aplicacao_if10_20 and (not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais)):
            pot = "100-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 100CV - 150A - 380 A 480V TRIFÁSICO"

#   CONDIÇÃO MODELO 100CV
        elif ((potencia == "100 cv") and (tensao == "380V-440V")) and aplicacao == "Outros" and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_recursos_adicionais:
            pot = "100-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 100CV - 150A - 380 A 480V TRIFÁSICO"

# ==============================

#   CONDIÇÃO MODELO 125CV +1
        elif (potencia == "125 cv" and tensao == "380V-440V" and aplicacao in lista_aplicacao_if20_mais1 and (not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais)):
            pot = "150-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 150CV - 210A - 380 A 480V TRIFÁSICO"

#   CONDIÇÃO MODELO 125CV
        elif (potencia == "125 cv" and tensao == "380V-440V" and aplicacao in lista_aplicacao_if10_20 and (not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais)):
            pot = "125-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 125CV - 176A - 380 A 480V TRIFÁSICO"

#   CONDIÇÃO MODELO 125CV
        elif ((potencia == "125 cv") and (tensao == "380V-440V")) and aplicacao == "Outros" and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_recursos_adicionais:
            pot = "125-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 125CV - 176A - 380 A 480V TRIFÁSICO"

    # ==============================

#   CONDIÇÃO MODELO 150CV +1
        elif (potencia == "150 cv" and tensao == "380V-440V" and aplicacao in lista_aplicacao_if20_mais1 and (not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais)):
            pot = "175-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 175CV - 253A - 380 A 480V TRIFÁSICO"

#   CONDIÇÃO MODELO 150CV
        elif (potencia == "150 cv" and tensao == "380V-440V" and aplicacao in lista_aplicacao_if10_20 and (not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais)):
            pot = "150-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 150CV - 210A - 380 A 480V TRIFÁSICO"

#   CONDIÇÃO MODELO 150CV
        elif ((potencia == "150 cv") and (tensao == "380V-440V")) and aplicacao == "Outros" and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_recursos_adicionais:
            pot = "150-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 150CV - 210A - 380 A 480V TRIFÁSICO"

    # ==============================

#   CONDIÇÃO MODELO 175CV +1
        elif (potencia == "175 cv" and tensao == "380V-440V" and aplicacao in lista_aplicacao_if20_mais1 and (not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais)):
            pot = "200-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 200CV - 300A - 380 A 480V TRIFÁSICO"

#   CONDIÇÃO MODELO 175CV
        elif (potencia == "175 cv" and tensao == "380V-440V" and aplicacao in lista_aplicacao_if10_20 and (not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais)):
            pot = "175-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 175CV - 253A - 380 A 480V TRIFÁSICO"

#   CONDIÇÃO MODELO 175CV
        elif ((potencia == "175 cv") and (tensao == "380V-440V")) and aplicacao == "Outros" and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_recursos_adicionais:
            pot = "175-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 175CV - 253A - 380 A 480V TRIFÁSICO"

    # ==============================

#   CONDIÇÃO MODELO 200CV +1
        elif (potencia == "200 cv" and tensao == "380V-440V" and aplicacao in lista_aplicacao_if20_mais1 and (not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais)):
            pot = "250-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 250CV - 340A - 380 A 480V TRIFÁSICO"

#   CONDIÇÃO MODELO 200CV
        elif (potencia == "200 cv" and tensao == "380V-440V" and aplicacao in lista_aplicacao_if10_20 and (not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais)):
            pot = "200-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 200CV - 300A - 380 A 480V TRIFÁSICO"

#   CONDIÇÃO MODELO 200CV
        elif ((potencia == "200 cv") and (tensao == "380V-440V")) and aplicacao == "Outros" and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_recursos_adicionais:
            pot = "200-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 200CV - 300A - 380 A 480V TRIFÁSICO"

    # ==============================

#   CONDIÇÃO MODELO 250CV +1
        elif (potencia == "250 cv" and tensao == "380V-440V" and aplicacao in lista_aplicacao_if20_mais1 and (not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais)):
            pot = "300-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 300CV - 420A - 380 A 460V TRIFÁSICO"

#   CONDIÇÃO MODELO 250CV
        elif (potencia == "250 cv" and tensao == "380V-440V" and aplicacao in lista_aplicacao_if10_20 and (not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais)):
            pot = "250-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 250CV - 340A - 380 A 480V TRIFÁSICO"

#   CONDIÇÃO MODELO 250CV
        elif ((potencia == "250 cv") and (tensao == "380V-440V")) and aplicacao == "Outros" and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_recursos_adicionais:
            pot = "250-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 250CV - 340A - 380 A 480V TRIFÁSICO"

    # ==============================

#   CONDIÇÃO MODELO 300CV +1
        elif (potencia == "300 cv" and tensao == "380V-440V" and aplicacao in lista_aplicacao_if20_mais1 and (not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais)):
            pot = "350-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 350CV - 470A - 380 A 460V TRIFÁSICO"

#   CONDIÇÃO MODELO 300CV
        elif (potencia == "300 cv" and tensao == "380V-440V" and aplicacao in lista_aplicacao_if10_20 and (not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais)):
            pot = "300-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 300CV - 420A - 380 A 460V TRIFÁSICO"

#   CONDIÇÃO MODELO 300CV
        elif ((potencia == "300 cv") and (tensao == "380V-440V")) and aplicacao == "Outros" and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_recursos_adicionais:
            pot = "300-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 300CV - 420A - 380 A 460V TRIFÁSICO"

    # ==============================

#   CONDIÇÃO MODELO 350CV +1
        elif (potencia == "350 cv" and tensao == "380V-440V" and aplicacao in lista_aplicacao_if20_mais1 and (not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais)):
            pot = "xxx"
            var_inf_inversor = ""

#   CONDIÇÃO MODELO 350CV
        elif (potencia == "350 cv" and tensao == "380V-440V" and aplicacao in lista_aplicacao_if10_20 and (not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_adicionais)):
            pot = "350-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 350CV - 470A - 380 A 460V TRIFÁSICO"

#   CONDIÇÃO MODELO 350CV
        elif ((potencia == "350 cv") and (tensao == "380V-440V")) and aplicacao == "Outros" and not comunicacao in lista_if30_comunicacao and not adcional in lista_if30_recursos_adicionais:
            pot = "350-3"
            var_inf_inversor = "INV. VETORIAL IF20 - 350CV - 470A - 380 A 460V TRIFÁSICO"

    # ==============================

#   CONDIÇÃO ELSE
        else:
            pot = "xxx"
            var_inf_inversor = ""
#   CONDIÇÃO SUB DIMESSIONAMENTO
        # and potencia < "350"   :
#        if aplicacao in lista_aplicacao_if20_resistor and potencia in lista_if20_potencia_380 and tensao in lista_tensao:
#            ate = "Aplicação Eventualmente Requer o uso de Resistor de Frenagem, Consulte a Tabela de Valores no Manual do Produto"
#            ate2 = "ATENÇÃO" 

        if (aplicacao in lista_aplicacao_if20_resistor and 
            (potencia in lista_if20_mais1_potencia_380_480 or potencia in lista_if20_potencia_220) and 
            tensao in lista_tensao):
            var_inf_resistor_frenagem = "Aplicação eventualmente requer o uso de resistor de frenagem, Consulte a Tabela de Valores no manual do produto."
            ate2 = "ATENÇÃO" 

        else:
            var_inf_resistor_frenagem = ""
            ate2 = ""

        ate0 = "Guia de seleção rápida de inversores, não possui efeito de especificação definitiva. Consulte sempre a Engenharia de Aplicações da Metaltex."
        ate5 = "© Todos os direitos reservado - Metaltex  (versão 1.02)"


        if (comunicacao == "COMUNICAÇÃO CANOPEN" and (f1 == "IF20" or f1 == "IF30")): 
            f5 = "+ Módulo"
            f6 = "IF30-CAN"

        elif (comunicacao == "COMUNICAÇÃO ETHERCAT" and (f1 == "IF20" or f1 == "IF30")): 
            f5 = "+ Módulo"
            f6 = "IF30-ECAT"

        elif (comunicacao == "COMUNICAÇÃO MODBUS-TCP" and (f1 == "IF20" or f1 == "IF30")): 
            f5 = "+ Módulo"
            f6 = "IF30-MTCP"

        elif (comunicacao == "COMUNICAÇÃO PROFINET" and (f1 == "IF20" or f1 == "IF30")): 
            f5 = "+ Módulo"
            f6 = "IF30-PROF"

        elif (adcional == "EXPANSÃO IO" and (f1 == "IF20" or f1 == "IF30")): 
            f5 = "+ Módulo"
            f6 = "IF30-IO-1"

        elif (adcional == "EXPANSÃO P/ ENCODER 5V" and (f1 == "IF20" or f1 == "IF30")): 
            f5 = "+ Módulo"
            f6 = "IF30-E5"

        elif (adcional == "EXPANSÃO P/ ENCODER PUSH-PULL 24V" and (f1 == "IF20" or f1 == "IF30")): 
            f5 = "+ Módulo"
            f6 = "IF30-E24"

        elif (adcional == "SEGURANÇA STO (NR12)" and (f1 == "IF20" or f1 == "IF30")): 
            f5 = ""
            f6 = ""

        else:
            f5 = ""
            f6 = ""                    

        #if not aplicacao in lista_aplicacao_geral or not tensao in lista_tensao or not potencia in lista_potencia_geral:
            



        valor_resultado_inversor = f"Inversor: {f1}-{f9}{pot} {f5} {f6}"
        
        resultado_texto_modelo_inversor.value = valor_resultado_inversor
        resultado_texto_inf_modelo.value = var_inf_inversor
        resultado_texto_atencao_resistor_frenagem.value = ate2  
        resultado_texto_resistor_frenagem.value = var_inf_resistor_frenagem
        resultado_texto_guia_selecao.value = ate0
        
        
        page.update() 
         
    ss_imagem_topo = ft.Container(
        alignment=ft.alignment.center,
        content=ft.Image(
            src="images/topo.jpg",
            height=70,
            fit=ft.ImageFit.CONTAIN,
        ),
    )
    # Título com espaço abaixo
    
    ss_aplicacao = ft.Container(
        alignment=ft.alignment.center,
        padding=ft.padding.only(left=15, right=15, top=5, bottom=10),
        content=ft.Column(
            controls=[
                ft.Text(value="APLICAÇÃO",color="#0A2D42"),
                aplicacao_dropdown := ft.Dropdown(
                    width=400,
                    label="Selecione a aplicação",
                    label_style=ft.TextStyle(size=12),
                    leading_icon=ft.Icons.SETTINGS_APPLICATIONS_SHARP,
                    options=[
                        ft.dropdown.Option("Outros"),
                        ft.dropdown.Option("Bobinadeira"),
                        ft.dropdown.Option("Bomba centrífuga"),
                        ft.dropdown.Option("Bomba deslocamento positivo"),
                        ft.dropdown.Option("Compressor"),
                        ft.dropdown.Option("Centrifugadora"),
                        ft.dropdown.Option("Elevador de carga c/ cremalheira"),
                        ft.dropdown.Option("Elevador de carga c/ contrapeso"),
                        ft.dropdown.Option("Esteira transportadora"),
                        ft.dropdown.Option("Guindaste"),
                        ft.dropdown.Option("Ventilador e Exaustor"),
                        ft.dropdown.Option("Extrusora"),
                        ft.dropdown.Option("Lavadora industrial"),
                        ft.dropdown.Option("Máquina operatriz"),
                        ft.dropdown.Option("Misturador"),
                        ft.dropdown.Option("Ponte rolante"),

                        ]
                    )
                ]
            )
        )

    
    ss_alimentacao = ft.Container(
        alignment=ft.alignment.center,
        padding=ft.padding.only(left=15, right=15, top=0, bottom=10),
        content=ft.Column(
            controls=[
                ft.Text(value="ALIMENTAÇÃO",color="#0A2D42"),
                alimentacao_dropdown := ft.Dropdown(
                    width=400,
                    label="Selecione a tensão do motor",
                    label_style=ft.TextStyle(size=12),
                    leading_icon=ft.Icons.FLASH_AUTO,
                    options=[
                        ft.dropdown.Option("220V"),
                        ft.dropdown.Option("380V"),
                        ft.dropdown.Option("380V-440V"),                        
                    ]
                )            
            ]      
        )  
    )
    

    ss_potencia = ft.Container(
        alignment=ft.alignment.center,
        padding=ft.padding.only(left=15, right=15, top=0, bottom=10),
        content=ft.Column(
            controls=[
                ft.Text(value="POTÊNCIA DO MOTOR",color="#0A2D42"),
                potencia_dropdown := ft.Dropdown(
                    width=400,
                    label="Selecione a potência do motor",
                    label_style=ft.TextStyle(size=12),
                    leading_icon=ft.Icons.EXPOSURE,
                    options=[
                          ft.dropdown.Option("1 cv"),
                          ft.dropdown.Option("2 cv"),
                          ft.dropdown.Option("3 cv"),
                          ft.dropdown.Option("5 cv"),
                          ft.dropdown.Option("7,5 cv"),
                          ft.dropdown.Option("10 cv"),
                          ft.dropdown.Option("15 cv"),
                          ft.dropdown.Option("20 cv"),
                          ft.dropdown.Option("25 cv"),
                          ft.dropdown.Option("30 cv"),
                          ft.dropdown.Option("40 cv"),
                          ft.dropdown.Option("50 cv"),
                          ft.dropdown.Option("60 cv"),
                          ft.dropdown.Option("75 cv"),
                          ft.dropdown.Option("100 cv"),
                          ft.dropdown.Option("125 cv"),
                          ft.dropdown.Option("150 cv"),
                          ft.dropdown.Option("175 cv"),
                          ft.dropdown.Option("200 cv"),
                          ft.dropdown.Option("250 cv"),
                          ft.dropdown.Option("300 cv"),
                          ft.dropdown.Option("350 cv"),
                        
                    ]
                )            
            ]      
        )  
    )
    
    ss_comunicacao = ft.Container(
        alignment=ft.alignment.center,
        padding=ft.padding.only(left=15, right=15, top=0, bottom=10),
        content=ft.Column(
            controls=[
                ft.Text(value="MÓDULO DE COMUNICAÇÃO (OPCIONAL)",color="#0A2D42"),
                comunicacao_dropdown := ft.Dropdown(
                    width=400,
                    label="Todos já possuem Modbus-RTU RS485",
                    label_style=ft.TextStyle(size=12),
                    leading_icon=ft.Icons.SETTINGS_ETHERNET_SHARP,
                    options=[
                        ft.dropdown.Option("--"),
                        ft.dropdown.Option("COMUNICAÇÃO CANOPEN"),
                        ft.dropdown.Option("COMUNICAÇÃO ETHERCAT"),
                        ft.dropdown.Option("COMUNICAÇÃO MODBUS-TCP"),
                        ft.dropdown.Option("COMUNICAÇÃO PROFINET"),
                        ft.dropdown.Option("MODBUS-RTU RS485"),

                    ]
                )            
            ]      
        )  
    )
    
    ss_adicionais = ft.Container(
        alignment=ft.alignment.center,
        padding=ft.padding.only(left=15, right=15, top=0, bottom=10),
        content=ft.Column(
            controls=[
                ft.Text(value="MÓDULO ADICIONAIS (OPCIONAL)",color="#0A2D42"),
                adicional_dropdown := ft.Dropdown(
                    width=400,
                    label="Selecione recursos adicionais",
                    label_style=ft.TextStyle(size=12),
                    leading_icon=ft.Icons.ADD_CIRCLE_OUTLINE,
                    options=[
                        ft.dropdown.Option("--"),
                        ft.dropdown.Option("EXPANSÃO IO"),
                        ft.dropdown.Option("EXPANSÃO P/ ENCODER 5V"),
                        ft.dropdown.Option("EXPANSÃO P/ ENCODER PUSH-PULL 24V"),
                        ft.dropdown.Option("SEGURANÇA STO (NR12)"),

                    ]
                )            
            ]      
        )  
    )
    
    ss_botao_consulta = ft.Container(
        alignment=ft.alignment.center,
        padding=ft.padding.only(left=15, right=15, top=10, bottom=5),
        border=ft.border.only(
                    top=ft.BorderSide(width=2, color=ft.Colors.with_opacity(1, 'PRIMARY'))),
        content=ft.ElevatedButton(
            width=700,
            text="Consultar",
            on_click=buscar,
            icon=ft.Icons.SEARCH_SHARP,
            color=ft.Colors.WHITE,
            bgcolor="#0A2D42",
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=6)
            ) 
        ) 
    )
    
    resultado_texto_modelo_inversor = ft.Text(value="",size=20,color="#0A2D42")
    resultado_texto_inf_modelo = ft.Text(value="",size=13,color="#0A2D42")
    resultado_texto_atencao_resistor_frenagem = ft.Text(value="",size=10,color="#FF0505")
    resultado_texto_resistor_frenagem = ft.Text(value="",size=10,color="#FF0505")
    resultado_texto_guia_selecao = ft.Text(value="",size=11,color="#0A2D42")
    resultado_texto_link_inversor = ft.Text(value="",size=11,color="#0A2D42")
    
    ss_texto_modelo_inversor = ft.Container(
        alignment=ft.alignment.center,
        padding=ft.padding.only(left=5, right=5, top=5, bottom=5),
        content=ft.Column(
            controls=[
              resultado_texto_modelo_inversor,  
            ]
        )    
    )                           
    
    ss_texto_inf_modelo = ft.Container(
        alignment=ft.alignment.center,
        padding=ft.padding.only(left=15, right=15, top=0, bottom=10),
        content=ft.Column(
            controls=[
              resultado_texto_inf_modelo,  
            ]
        )    
    )                           
    
    
    ss_texto_atencao_resitor_frenagem = ft.Container(
        alignment=ft.alignment.center,
        padding=ft.padding.only(left=15, right=15, top=0, bottom=0),
        content=ft.Column(
            controls=[
                resultado_texto_atencao_resistor_frenagem,
             
            ]
        )    
    )                           
    
    ss_texto_resitor_frenagem = ft.Container(
        alignment=ft.alignment.center,
        padding=ft.padding.only(left=15, right=15, top=0, bottom=10),
        content=ft.Column(
            controls=[
              resultado_texto_resistor_frenagem,  
            ]
        )    
    )                           

    ss_texto_guia_selecao = ft.Container(
        alignment=ft.alignment.center,
        padding=ft.padding.only(left=15, right=15, top=0, bottom=10),
        content=ft.Column(
            controls=[
              resultado_texto_guia_selecao,  
            ]
        )    
    )                           

    ss_texto_link_inversor = ft.Container(
        alignment=ft.alignment.center,
        padding=ft.padding.only(left=15, right=15, top=0, bottom=10),
        bgcolor=ft.Colors.WHITE,
        content=ft.Column(
            controls=[
                ft.Text(
                    text_align=ft.TextAlign.CENTER,
                    spans=[
                        ft.TextSpan(
                            text="Conheça toda a linha de Inversores de Frequência Metaltex",
                            url="https://metaltex.com.br/collections/mtx-cat-inversores-de-frequencia",
                            style=ft.TextStyle(
                                color="#0A2D42", decoration=ft.TextDecoration.UNDERLINE,size=12,),
                                

                        )])]))   

    rodape = ft.Container(
        alignment=ft.alignment.center,
        height=20,
        bgcolor="#0A2D42",
        content=ft.Text("© Todos os direitos reservado - Metaltex  (versão 1.03)",
        color=ft.Colors.WHITE,
        size=9,
        text_align=ft.TextAlign.CENTER,
    ),
)
    
    conteudo_app = ft.Container(
    width=800,
    expand=False,
    bgcolor=ft.Colors.WHITE,
    content=ft.Column(
        expand=True,
        spacing=0,
        controls=[
            # Área que rola
            ft.Column(
                expand=True,
                scroll=ft.ScrollMode.AUTO,
                spacing=0,
                controls=[
                    ss_imagem_topo,
                    ss_aplicacao,
                    ss_alimentacao,
                    ss_potencia,
                    ss_comunicacao,
                    ss_adicionais,
                    ss_botao_consulta,
                    ss_texto_modelo_inversor,
                    ss_texto_inf_modelo,
                    ss_texto_atencao_resitor_frenagem,
                    ss_texto_resitor_frenagem,
                    ss_texto_guia_selecao,
                    ss_texto_link_inversor,
                ],
            ),  # fecha a Column interna

            rodape,  
        ], 
    ),  
)  
    
    def ajustar_layout(e=None):
        largura_disponivel = page.width if page.width else 400
        largura_final = min(max(largura_disponivel - 12, 280), 400)
        conteudo_app.width = largura_final
        page.update()

    page.on_resize = ajustar_layout
    page.add(
        ft.Row(
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[conteudo_app],
        )
    )
    ajustar_layout()
    


ft.app(target=main, assets_dir="assets")
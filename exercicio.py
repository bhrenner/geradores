import funcao_gr

with open('geradores/reccrimepfa-210901-151708.csv', 'r') as file_name:
    lines = (line for line in file_name) #é lida em cada linha do arquivo.
    list_line = (s.rstrip().split(",") for s in lines) #divide cada linha em valores e coloca os valores em uma lista.
    cols = next(list_line)#usa para armazenar os nomes das colunas em uma lista
    #company_dicts = map(funcao_gr.dicio(cols, l) for l in list_line)
    company_dicts = (dict(zip(cols, d)) for d in list_line) #cria dicionários e os une com uma chamada/ As chaves são os nomes das colunas/ Os valores são as linhas na forma de lista
    funding = ( #recebe os valores de number offences de cada regiao.Também filtra qualquer outra quantidade levantada.
        int(company_dict["Rolling year total number of offences"])
        for company_dict in company_dicts
        #if company_dict["Offence"] == "Bicycle theft"
        if company_dict["Offence"] == "Homicide"
    )
    total_series_a = sum(funding) #inicia o processo de iteração ligando para obter o valor total
    print(f"Total series A fundraising: ${total_series_a}")

# FORMATAÇÃO DE DATA
from datetime import datetime

first_date = "30/11/2020"
second_date = "12/10/2019"

formatted_date1 = datetime.strptime(first_date, "%d/%m/%Y").date()
formatted_date2 = datetime.strptime(second_date, "%d/%m/%Y").date()
form = formatted_date1.year
print(formatted_date1.year > 2015,formatted_date2, form)
import xml.etree.ElementTree as ET

import pandas as pd
import requests
import os

def get_data(url, params, headers):
    response = requests.get(url, params=params, headers=headers)
    '''if response.status_code == 200:
        print("Data retrieved successfully")
    else:
        print(f"Error: {response.status_code}")'''
    return response

def data_to_df(response):
    # Parse XML
    root = ET.fromstring(response.text)
    proposicoes = root.findall('proposicao')

    # Colocar dados em listas de dicionários
    lista_dados = []

    for p in proposicoes:
        dados = {}
        for child in p:
            if len(child) > 0: # Check if the child has subchilds
                for subchild in child:
                    dados[f"{child.tag}_{subchild.tag}"] = subchild.text
                
            else:
                dados[child.tag] = child.text
        lista_dados.append(dados)

    # Criar DataFrame
    df = pd.DataFrame(lista_dados)
    return df

def save_csv(df, filename):
    if not os.path.exists('data'):
        os.makedirs('data')
    
    full_path = os.path.join('data', filename)
    df.to_csv(full_path, index=False)
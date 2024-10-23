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

def data_to_df(response, ObterProposicaoPorID=None):
    # Parse XML
    root = ET.fromstring(response.text)

    # Colocar dados em listas de dicionários
    lista_dados = []

    if ObterProposicaoPorID == None:
        proposicoes = root.findall('proposicao')

        
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

    else:
        proposicoes = root

        dados = {}
        for child in proposicoes:
            if len(child) > 0: # Check if the child has subchilds
                for subchild in child:
                    dados[f"{child.tag}_{subchild.tag}"] = subchild.text
                
            else:
                dados[child.tag] = child.text

        df = pd.DataFrame([dados])
        
    return df

def save_csv(df, filename, ObterProposicaoPorID=None):

    if ObterProposicaoPorID != None:
        if not os.path.exists('data/proposicoes'):
            os.makedirs('data/proposicoes')
        full_path = os.path.join('data/proposicoes', filename)

    else:
        if not os.path.exists('data'):
            os.makedirs('data')
        
        full_path = os.path.join('data', filename)
    
    df.to_csv(full_path, index=False)
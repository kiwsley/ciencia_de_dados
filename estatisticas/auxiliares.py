import pandas as pd

def tabela_distribuicao_frequencias(dataframe,coluna,coluna_frequencia = False):

    df_estatistica = pd.DataFrame()

    if coluna_frequencia:
        df_estatistica['Frequencia']=dataframe[coluna]
        df_estatistica['frequencia_relativa']=df_estatistica['Frequencia']/df_estatistica['Frequencia'].sum()


    else:
        # quantidade de ocorrencia
        df_estatistica['Frequencia']= dataframe[coluna].value_counts().sort_index()
        # %
        df_estatistica['frequencia_relativa']= dataframe[coluna].value_counts(normalize=True).sort_index()
        
    #soma dos valores    
    df_estatistica['frequencia_acumulada']= df_estatistica['Frequencia'].cumsum()   
    #soma da frenquencia relativa  
    df_estatistica['frequencia_relativa_acumulada']= df_estatistica['frequencia_relativa'].cumsum()


    return df_estatistica
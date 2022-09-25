#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import joblib
import streamlit as st


# In[11]:


#criando dicionários para cada tipo de dado

features_numericas = {'host_listings_count': 0, 'latitude': 0, 'longitude': 0, 'accommodates': 0, 'bathrooms': 0, 'bedrooms': 0,
                      'beds': 0, 'extra_people': 0, 'minimum_nights': 0, 'mes': 0, 'ano': 0, 'num_amenities': 0}

features_true_or_false = {'host_is_superhost': 0}

features_texto = {'property_type': ['Apartment', 'Bed and breakfast', 'Condominium', 'Guest suite', 'Guesthouse', 'Hostel',
                                   'House', 'Loft', 'Others', 'Serviced apartment'],
                 'room_type': ['Entire home/apt', 'Hotel room', 'Private room', 'Shared room'],
                 'cancellation_policy':['flexible', 'moderate', 'strict', 'strict_14_with_grace_period']
                 }

dicionario_dummies = {}

for item in features_texto:
    for valor in features_texto[item]:
        dicionario_dummies[f'{item}_{valor}'] = 0

#criando os campos para o usuário preencher/selecionar

for item in features_numericas:
    if item == 'latitude' or item == 'longitude':
        valor = st.number_input(f'{item}', step = 0.00001, value = 0.0, format = '%.5f')
        features_numericas[item] = valor
    elif item == 'extra_people':
        valor = st.number_input(f'{item}', step = 0.01, value = 0.0, format = '%.2f')
        features_numericas[item] = valor
    else:
        valor = st.number_input(f'{item}', step = 1, value = 0)
        features_numericas[item] = valor
        
    
for item in features_true_or_false:
    valor = st.selectbox(f'{item}', ('Sim', 'Não'))
    if valor == 'Sim':
        features_true_or_false[item] = 1
    else:
        features_true_or_false[item] = 0
        
    
for item in features_texto:
    valor = st.selectbox(f'{item}', features_texto[item])
    dicionario_dummies[f'{item}_{valor}'] = 1
    
    
botao = st.button('Prever diária do imóvel')

#colocando uma função no botão

if botao:
    dicionario_final = {}
    dicionario_final.update(features_numericas)
    dicionario_final.update(features_true_or_false)
    dicionario_final.update(dicionario_dummies)
    dataframe_features = pd.DataFrame(dicionario_final, index = [0])
    ordem_das_colunas = ['host_listings_count', 'host_is_superhost', 'latitude', 'longitude', 'accommodates', 'bathrooms', 'bedrooms', 'beds', 'extra_people', 'minimum_nights', 'mes', 'ano', 'num_amenities', 'property_type_Apartment', 'property_type_Bed and breakfast', 'property_type_Condominium', 'property_type_Guest suite', 'property_type_Guesthouse', 'property_type_Hostel', 'property_type_House', 'property_type_Loft', 'property_type_Others', 'property_type_Serviced apartment', 'room_type_Entire home/apt', 'room_type_Hotel room', 'room_type_Private room', 'room_type_Shared room', 'cancellation_policy_flexible', 'cancellation_policy_moderate', 'cancellation_policy_strict', 'cancellation_policy_strict_14_with_grace_period']
    dataframe_features = dataframe_features.loc[:, ordem_das_colunas]


    modelo = joblib.load('modelo.joblib')
    preco_diaria = modelo.predict(dataframe_features)
    st.write(f'Preço sugerido para a diária: R$ {preco_diaria[0]}')
   



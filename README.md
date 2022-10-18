# Projeto Airbnb Rio - Ferramenta de Previsão de Preço de Imóvel para pessoas comuns

<div align = 'center'>
 <img src = 'https://airbnblover.com/wp-content/uploads/2017/02/airbnb-refugees-1.png' width = '45%'/>
</div>

### Contexto

No Airbnb, qualquer pessoa que tenha um quarto ou um imóvel de qualquer tipo (apartamento, casa, chalé, pousada, etc.) pode ofertar o seu imóvel para ser alugado por diária.

Você cria o seu perfil de host (pessoa que disponibiliza um imóvel para aluguel por diária) e cria o anúncio do seu imóvel.

Nesse anúncio, o host deve descrever as características do imóvel da forma mais completa possível, de forma a ajudar os locadores/viajantes a escolherem o melhor imóvel para eles (e de forma a tornar o seu anúncio mais atrativo)

Existem dezenas de personalizações possíveis no seu anúncio, desde quantidade mínima de diária, preço, quantidade de quartos, até regras de cancelamento, taxa extra para hóspedes extras, exigência de verificação de identidade do locador, etc.

<div align = 'center'>
 <img src = 'https://images.unsplash.com/photo-1504639725590-34d0984388bd?ixlib=rb-1.2.1&q=80&cs=tinysrgb&fm=jpg&crop=entropy' width = '35%' />
</div>

### Nosso objetivo

Construir um modelo de previsão de preço que permita uma pessoa comum que possui um imóvel possa saber quanto deve cobrar pela diária do seu imóvel.

Ou ainda, para o locador comum, dado o imóvel que ele está buscando, ajudar a saber se aquele imóvel está com preço atrativo (abaixo da média para imóveis com as mesmas características) ou não.

### O que temos disponível

As bases de dados foram retiradas do site kaggle: [https://www.kaggle.com/allanbruno/airbnb-rio-de-janeiro](https://www.kaggle.com/allanbruno/airbnb-rio-de-janeiro)

- As bases de dados são os preços dos imóveis obtidos e suas respectivas características em cada mês.
- Os preços são dados em reais (R$)
- Temos bases de abril de 2018 a maio de 2020, com exceção de junho de 2018 que não possui base de dados

### Resultados

- Conseguimos criar um modelo que consegue prever bem aproximadamente 97% dos preços
- Analisando os 3 modelos testados, o ExtraTrees mostrou ser mais eficaz
- Dentre as features analisadas, foi possível observar que a localidade (latitude e longitude), quantidade de quartos e número de amenities (comodidades) tem grande impacto no cálculo da diária pelo modelo.
- Foi feito um deploy local no computador para facilitar o usuário a inserir as informações do imóvel e conseguir prever a diária que deve cobrar

### Mapa de calor com os preços x localização

<div align = 'center'>
 <img src = 'https://user-images.githubusercontent.com/114163919/196525598-4f65cc54-92c0-4e78-bd4b-94281dc728b2.png' width = '50%' />
</div>


### Resultado do Deploy / Modelo Funcionando

<div align = 'center'>
 <img src = 'https://user-images.githubusercontent.com/114163919/196525692-46fe6809-6b31-4e35-840e-1a54d3658585.png' width = '50%' />
</div>

Obs: não foi possível colocar no github a pasta com o dataset e nem o modelo salvo no joblib devido ao tamanho dos arquivos.

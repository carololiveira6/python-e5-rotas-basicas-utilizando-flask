## **Table of Contents**
- [E5 - Rotas básicas útilizando Flask](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2a_e_01_rotas-basicas-flask.html&ref=master#e5---rotas-k%C3%A1sicas-%C3%BAltilizando-flask) 
  - [Objetivo](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2a_e_01_rotas-basicas-flask.html&ref=master#mcetoc_1f362b6b10)
  - [Preparativos](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2a_e_01_rotas-basicas-flask.html&ref=master#mcetoc_1f362b6b11)
  - [Rota Home](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2a_e_01_rotas-basicas-flask.html&ref=master#mcetoc_1eg6l938o6l) 
    - [Exemplo](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2a_e_01_rotas-basicas-flask.html&ref=master#mcetoc_1f3bcepvk0)
  - [Rota Current Datetime](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2a_e_01_rotas-basicas-flask.html&ref=master#mcetoc_1f3bcepvk1) 
    - [Exemplo](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2a_e_01_rotas-basicas-flask.html&ref=master#mcetoc_1f3bcf5ei2)
- [Entregáveis](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2a_e_01_rotas-basicas-flask.html&ref=master#mcetoc_1f362b6b12) 
  - [Repositório](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2a_e_01_rotas-basicas-flask.html&ref=master#mcetoc_1egvrpv6k1l4)
- [Critérios de aceitação](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2a_e_01_rotas-basicas-flask.html&ref=master#mcetoc_1eh146n6m3)
# **E5 - Rotas básicas utilizando Flask**
Nesta entrega você irá criar duas rotas com retornos específicos.
## **Objetivo**
Essa atividade foi elaborada para trabalhar o que você aprendeu sobre requisições com Flask.
## **Preparativos**
Você deve criar um arquivo chamado **flask\_routes.py,** nele você irá criar as suas rotas.

**Nota: Utilize a documentação do [datetime](https://docs.python.org/pt-br/3/library/datetime.html "https://docs.python.org/pt-br/3/library/datetime.html") para pegar a data e siga essa [tabela de formatação](https://docs.python.org/pt-br/3/library/datetime.html#strftime-and-strptime-format-codes "https://docs.python.org/pt-br/3/library/datetime.html") para te dar a resposta do seu servidor e também utilize o [insomnia](https://insomnia.rest/download "https://insomnia.rest/download") para fazer as requisições.**
## **Rota Home**
- Endpoint da rota -> /
- Retorno da rota deve ser um dicionário.
### **Exemplo**
![](Aspose.Words.782911e4-1b7f-4774-9eab-93d3a606f7ae.001.png)


## **Rota Current Datetime**
- Endpoint da rota -> **/current\_datetime**
- Retorno da rota deve ser o seguinte formato de dicionário: 
  - **current\_datetime**: informando o dia, a hora e qual o período,
  - **message**: entre meia noite e meio dia deve retornar **"Bom dia!"**, entre o meio dia às seis da tarde deve retornar **"Boa tarde!"** e a partir das seis deve retornar **"Boa noite!"**, **dependendo do horário da requisição**:
### **Exemplo**
![](Aspose.Words.782911e4-1b7f-4774-9eab-93d3a606f7ae.002.png)

-----
# **Entregáveis**
## **Repositório**
- Link do **repositório** do **GitLab**
- **Código fonte:** 
  - arquivo **flask\_routes.py**.
- **Privacidade** 
  - Incluir **ka-br-out-2020-correcoes** como reporter.
-----
# **Critérios de aceitação**

|**pts**|**Dado**|**Quando**|**É esperado**|
| :-: | :-: | :-: | :-: |
|2.5|Rota **/**|Fazer a requisição na rota|Retornar um dicionário seguindo o pedido|
|2.5|Rota **/current\_datetime**|Fazer a requisição na rota|Retornar um dicionário seguindo o pedido|
**Boa diversão, devs! 🧪**











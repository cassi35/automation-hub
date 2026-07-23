# descricao

tento ler textos em ingles com noticias do techcrunch , crunchbase, hbr ,businer insider ,pándo , venture beat para:

## objetivo

- aprimorar vocabulario no ingles
- me atualizar das noticias
- entender novos mercados de como se realciona no que estou fazendo estudando agora
- descobrir palavras novas no ingles para
- aplicar anotar as palavras novas no meu cotidiano

# repeticao

abro borweer --> rolo a scolbar dos meus sites de notica salvo --> abro em janelas diferentes

# problemas

## procrastinacao

- acumolo de tarefas que como é muito (ingles , programacao , envio de curriculo) gasto tempo que poderia ser automatizado
- como é chato ler e selecionar acabo lendo qualquer coisa que nao me interresa
- preciso exercitar a lingua com ia apartir dessas noticias mas acabo nao fazendo por ter muita coisa pra fazer por ter muita coisa
- as vezes é muito extenso o texto e acabo nao lendo todo

## ansiedade

- como tenho tdah fico ansioso pra acabar o texto por que sei que tenho 30 minutos a uma hora pra fazer essa leitura
- gasto um tempo procurando textos que sejam relevantes navegando em abas pra saber e ler
- nao sei qais topicos to disposto a ler

## dificuldade de encaixar as ideias por falta de tempo e disposicao

- quero pegar esses textos e encaixar na minhya realidade como conmversar com a ia em ingles
- nao sei com o texto da pode ser falado , escrito
- quero pegar esse texto e gerar questinarios em ingles mas gastaria um tempo
- nao é todo dia que eu quero ler e tambem alguns assuntos chatos

## travamento

- muitas abas consumindo memoria ram
- travamento que com muitas abas abertas tambem por causa que ja tenho da minha rotina de programacao

## atraso

sou uma pessoa que gosto de rotina produzo 5 a 6 horas dia acordo as 8 da manha comeco as 9

- como escolho as noticias de tudo de uma vez de manha é mais trabalho e tempo + leitura

# solucao

## porque

evitar

# ideas

1. filtrando as melhores noticias via scraping tech crunch , havard busines revirew , crunchbase , venture com as ideias que eu quero

- caracter textos pequenos
- topicos especificos
- caculo de tempo que vou gastar lendo com o conjunto dos textos eescolhidos
- classificar qual o potencial de cada texto de acordo com criterios (que vou escolher)

2. mudar o microsoft todo nas observacoes com link das melhores noticias
3. geracao de prompt deterministicos so copiar e copar para comecar a comversar com chat ia
4. geracao de questinarios (atividades) personalizados sobre sentenses no ingles com asuntos dos textos personalizados
5. calcular tempo que vou ler com cada texto para fechar exatamentoe vou proximo
6. abrir dinamicamente com seleniom no brower

# pensar

antes de criar preciso entender o fluxo de dados ,

1. **separar camadas**

- agendador/ trigger (disparador): o que inicia o processo (coron/botao/webhook)
- engine backend (automacao) Scripts de Scraping, Filtros, Processamento LLM, APIs (MS To-Do).
- Usuário (Interface/Consumo): Onde você interage (Navegador, Leitura, Chat com IA).

2. **Simbologia Padrão (Notação BPMN / Flowchart):**

- Elipse/Círculo (Início/Fim): Eventos que iniciam ou encerram a rotina.

- Retângulo (Ação/Processo): Uma tarefa executada pelo sistema (ex: Fazer scraping do TechCrunch).

- Losango (Decisão/Condicional): Um ponto de checagem com saídas Sim/Não (ex: Tempo total de leitura > 45 min?).

- Paralelogramo (Entrada/Saída de Dados): Envio/recebimento de dados externos (ex: Payload enviado para API do MS To-Do).

- Cilindro (Banco de Dados/Persistência): Armazenamento de estado (ex: PostgreSQL ou JSON cache).

3. **Determinismo:**

- Cada etapa deve ter uma regra clara de entrada e saída. Não pode haver nós "soltos" sem destino.

# fluxo

1. ## **camadas**

- **trigger**:
- **automacao**:
- **interface**:

2. ## **flowchart**

- **(Início/Fim)**:

3. ## **Determinismo:**

- **etapas**:

# fluxograma mermied

```
flowchart TD
    %% --- INÍCIO E TRIGGER ---
    Start([Início: Cron Job - 08:30 AM]) --> Scraping[1. Executar Scraping de Notícias]

    subgraph Scraping_Step [Fase 1: Coleta de Dados]
        Scraping --> Sources[/TechCrunch, HBR, Crunchbase, VentureBeat/]
        Sources --> ExtractText[Extrair Título, Corpo, URL e Categoria]
    end

    subgraph Processing_Step [Fase 2: Processamento e Filtragem]
        ExtractText --> CalcWordCount[Calcular quantidade de palavras]
        CalcWordCount --> EstReadTime[Estimar tempo de leitura: palavras / 150 wpm]
        EstReadTime --> LLMFilter[LLM: Classificar tópicos e descartar textos irrelevantes]
        LLMFilter --> ScoreFilter{Texto atende aos critérios?}

        ScoreFilter -- Não --> Discard[Descartar Notícia]
        ScoreFilter -- Sim --> Rank[Ordernar por Relevância/Pontuação]
    end

    subgraph Time_Constraint [Fase 3: Limite de Tempo]
        Rank --> SelectTop[Selecionar Notícias acumulando até 45 min de leitura]
    end

    subgraph Content_Gen [Fase 4: Geração de Conteúdo Complementar]
        SelectTop --> LLMPrompt[LLM: Gerar Prompts Determinísticos para Conversação]
        SelectTop --> LLMQuiz[LLM: Extrair Vocabulário e Gerar Questionário em Inglês]
    end

    subgraph Integration_Step [Fase 5: Integração com Plataformas]
        LLMPrompt --> MSToDo[/Enviar Tarefas + Links + Prompts para API do MS To-Do/]
        LLMQuiz --> MSToDo
        MSToDo --> SaveDB[(PostgreSQL: Registrar Execução e URLs lidas)]
    end

    subgraph User_Action [Fase 6: Consumo pelo Usuário - 09:00 AM]
        SaveDB --> UserLogin([Usuário abre a rotina às 09:00])
        UserLogin --> OpenTask[Abre a lista do MS To-Do do dia]
        OpenTask --> OpenSelenium[Dispara script/Selenium para abrir apenas as 2-3 abas selecionadas]
        OpenSelenium --> Read[Realiza Leitura Cronometrada]
        Read --> ExecuteQuiz[Aplica o Questionário / Pratica no Chat de IA]
        ExecuteQuiz --> CompleteTask[Marca Tarefa como Concluída no MS To-Do]
        CompleteTask --> End([Fim da Rotina])
```

# stack

- scrapy
- pytest
- rabbitmq
- timer

# processo codigo

1. descrever ideia
2. esboco inicial (rascunho fluxograa)
3. comecar a codar
4. conforme eu descubro os problemas reais eu atualizo o fluxograma e o readme

---

## 4. Dúvidas de Conceito: Regras de Negócio, Requisitos e Observabilidade

### A) O que são Regras de Negócio x Requisitos Funcionais x Não-Funcionais?

- **Regras de Negócio (Domain Rules):** São as fórmulas, limites e políticas que regem a lógica.
  - _Exemplo:_ _"A leitura diária não pode passar de 45 minutos"_ ou _"Considerar velocidade de 150 palavras/min"_.
- **Requisitos Funcionais (O que o sistema FAZ):**
  - _Exemplo:_ _"O sistema deve buscar artigos no TechCrunch"_, _"O sistema deve criar uma tarefa no MS To-Do"_.
- **Requisitos Não-Funcionais (COMO o sistema se comporta em termos de qualidade/performance):**
  - _Exemplo:_ _"O banco de dados deve ser PostgreSQL"_, _"O token da API do Jira deve ser armazenado em variável de ambiente (`.env`)"_, _"Se um site falhar, o script não pode quebrar"_.

---

### B) Como fazer o processamento sem LLM (100% Determinístico)?

Se você não quer usar LLMs (OpenAI, Ollama, etc.), a filtragem precisa ser baseada em **algoritmos e regras estáticas**:

1. **Cálculo de Tempo:**
   ```python
   words = len(article_body.split())
   estimated_minutes = round(words / 150)
   ```

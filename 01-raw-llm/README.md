# Creating an LLM Model Based on BERT from Scratch  

## Project Objective  

This project aims to create a Large Language Model (LLM) based on the BERT architecture from scratch, exploring every fundamental step of its development. The process encompasses tasks ranging from data loading and preparation, building an optimized vocabulary, and defining special tokens to implementing the complete model architecture. This architecture includes modules such as Embedding, Multi-Head Attention, and Encoder Layers. Additionally, the project covers hyperparameter configuration, training strategies, model evaluation, and generating predictions. By following this step-by-step approach, the goal is not only to reproduce the effectiveness of BERT but also to gain a deep understanding of the principles and mechanisms that make this architecture so powerful in natural language processing.  

1. **Data Loading**  
   Prepare and load the text corpus that will be used to train the model, ensuring its quality and relevance to the application domain.  

2. **Vocabulary Construction and Special Token Definition**  
   Build the set of tokens that the model will use, including special tokens ([CLS], [SEP], [MASK], and [PAD]) essential for tasks such as classification, sentence separation, and masking.  

3. **Hyperparameter Definition**  
   Configure the parameters that control the model’s training and architecture, such as the number of layers, attention heads, vocabulary size, and learning rate.  

4. **Batch Creation for Training**  
   Split the data into smaller batches to optimize training efficiency and enable the model to process large data volumes incrementally.  

5. **Model Construction**  
   - **Embedding Module:** Converts tokens into high-dimensional vectors, incorporating both token and positional information.  
   - **Scaled Dot Product Attention:** Implements the attention mechanism, enabling the model to focus on relevant parts of the text.  
   - **Multi-Head Attention Module:** Enhances the model's attention capability, allowing it to analyze different aspects of the text simultaneously.  
   - **Positional Feedforward Module:** Adds a non-linear layer to improve the model's expressiveness.  
   - **Encoder Layer Module:** Combines multi-head attention and feedforward components, forming the foundation of the BERT model.  
   - **Final Architecture:** Integrates all layers to create the complete BERT model structure.  

6. **Model Training and Evaluation**  
   Train the model with the data and evaluate its performance on specific tasks, fine-tuning parameters to improve results.  

7. **Generating Predictions with the Model**  
   Use the trained model to infer results on new data, demonstrating its practical application and predictive capabilities.  

---

## **Conceito de IA Generativa**

A Inteligência Artificial Generativa, especialmente no contexto dos Large Language Models (LLMs), refere-se à capacidade desses modelos de criar conteúdo novo e original, baseado nos padrões  e  informações  aprendidos  durante  o  treinamento  em  grandes  volumes de  dados textuais. Este aspecto generativo destaca-se por várias razões:

**Geração de Texto**: Os LLMs podem gerar textos coerentes e contextualmente relevantes. Isso  inclui  a  escrita  de  artigos,  histórias,  scripts  de  código,  poesia  e  até  respostas  a  perguntas específicas. A geração é feita processando a entrada do usuário e construindo uma resposta que segue logicamente a partir dessa entrada.

**Criatividade e Inovação**: Uma das características mais notáveis dos modelos generativos é a capacidade de combinar informações de maneiras novas e criativas. Eles podem, por exemplo, criar histórias com enredos originais ou sugerir soluções inovadoras para problemas.

**Personalização**: Estes modelos podem ser adaptados para gerar conteúdo específico para certos  contextos  ou  necessidades  do  usuário.  Isso  significa  que  podem  ser  usados  para  criar conteúdo personalizado em uma ampla gama de estilos e formatos.

**Interatividade**: Os modelos generativos  permitem  uma  interação  bidirecional,  onde  o modelo não apenas responde a entradas, mas também pode fazer perguntas, sugerir tópicos ou guiar uma conversa.

**Tradução  e  Adaptação  Linguística**: Podem  ser  usados  para  traduzir  textos  entre  idiomas ou adaptar conteúdo para diferentes dialetos ou estilos linguísticos.

É importante ressaltar  que, apesar de sua capacidade avançada, os modelos generativos têm limitações, como a possibilidade de gerar informações incorretas ou tendenciosas, e a falta de  entendimento  real  do  mundo  ou  de  consciência.  Além  disso,  o  uso  responsável  desses modelos é um tema de constante debate, envolvendo questões éticas e de direitos autorais.

---

## Aplicações de IA Generativa

A  IA  Generativa  tem  encontrado  aplicações  em  uma  variedade  de  campos  e  contextos, seguem abaixo alguns exemplos:

* **Arte e Design:**
    
    * **Geração  de  Imagens**: Modelos  como  DALL·E  da  OpenAI  podem  criar  imagens  originais  a partir de descrições textuais.
    
    * **Música**: Existem   modelos   que   podem   compor   músicas   originais   ou   emular   estilos específicos de artistas.
    
    * **Design de Produtos**: IA Generativa pode ser usada para criar designs de produtos, como móveis ou roupas, otimizados para certos critérios.
    
* **Entretenimento e Mídia:**
    
    * **Criação  de  Personagens  para  Jogos**: Modelos  generativos  podem  criar  personagens, cenários e objetos para jogos.
    
    * **Filmes e Animações**: IA pode ser usada para gerar animações ou até mesmo roteiros.
    
* **Ciência e Pesquisa**:
    
    * **Descoberta  de  Drogas**: Modelos  podem  gerar  estruturas  moleculares  para  novas  drogas potenciais.
    
    * **Simulação  de  Dados**: Em  áreas  onde  os  dados  são  escassos,  a  IA  Generativa  pode  criar conjuntos de dados simulados para pesquisa
    

* **Negócios e Comércio**
    
    * **Design de Websites**: Modelos podem propor designs de sites com base em certos critérios ou tendências.
    
    * **Publicidade  Personalizada**: Anúncios  gráficos  podem  ser  gerados  especificamente  para atender aos interesses de um usuário individual
    

* **Moda**
    
    * **Design de Roupas**: Modelos generativos podem criar designs de roupas ou padrões têxteis inovadores.
    
* **Falsificações e Deepfakes**
    
    Infelizmente, a IA Generativa também tem um lado sombrio. Ela pode ser usada para criar "deepfakes", que são vídeos ou áudios manipulados onde pessoas parecem dizer ou fazer coisas que nunca fizeram. Isso levanta sérias preocupações éticas e de segurança.
    

Estes são apenas alguns exemplos e a lista continua crescendo à medida que a tecnologia avança e encontra novas aplicações em diversos setores.

---

## O que é Processamento de Linguagem Natural?

Processamento de Linguagem Natural (PLN) é um campo de estudo e aplicação que se situa na interseção da ciência da computação, inteligência artificial e linguística. O objetivo do PLN é capacitar  os  computadores para  entender,  interpretar,  manipular  e  responder  a  linguagem humana de uma forma útil e significativa. Aqui estão os principais aspectos do PLN:

- **Compreensão  de  Linguagem**: PLN  envolve  o  desenvolvimento  de  algoritmos  e  sistemas que permitem aos computadores compreender texto e fala humanos. Isso inclui a capacidade de entender gramática, semântica, contexto e nuances da linguagem.
- **Geração  de  Linguagem**: Além  de  compreender  a  linguagem,  o  PLN  também  aborda  a geração de texto e fala. Isso pode envolver a criação de respostas coerentes em uma conversa, a geração de textos escritos em diferentes estilos, ou a tradução automática entre idiomas.
- **Análise  de  Sentimento**: O  PLN  pode  ser  usado  para  analisar  opiniões  e  sentimentos  em textos, como avaliar se um comentário é positivo, negativo ou neutro.
- **Extração  de  Informações**: Essa  área  do  PLN  foca  em  extrair  informações  específicas  de textos, como nomes, locais, datas ou outros dados relevantes.
- **Processamento de Fala**: O PLN também se estende ao reconhecimento e síntese de fala, permitindo que os sistemas de IA entendam e produzam linguagem falada.
- **Tradução  Automática**: Traduzir  texto  ou  fala  de  um  idioma  para  outro  é  outra  aplicação importante do PLN, embora seja um desafio devido às complexidades e nuances dos idiomas.
- **Resposta  a  Perguntas**: Sistemas  de  PLN  podem  ser  programados  para  responder  a perguntas feitas em linguagem natural, encontrando e fornecendo a informação relevante.
- **Assistentes  Virtuais  e  Chatbots**: Muitos  assistentes  virtuais  e  chatbots  usam  PLN  para entender e responder a comandos ou perguntas dos usuários.

PLN é uma área de pesquisa e desenvolvimento ativa e em rápida evolução, impulsionada pelo  aumento  da  quantidade  de  dados  de  texto  e  fala  disponíveis,  avanços  em  algoritmos  de aprendizado de máquina e maior capacidade de processamento computacional. As aplicações do PLN estão se tornando cada vez mais comuns em nosso dia a dia, desde ferramentas simples de autocorreção até sofisticados sistemas de interação homem-máquina

---

## LLMs (Large Language Models) e a Revolução em NLP

Os Large Language Models (LLMs) representam uma das inovações mais significativas no campo   do   Processamento   de   Linguagem   Natural   (PLN).   Esses   modelos   são   sistemas   de Inteligência Artificial   treinados   em   vastos   conjuntos   de   dados   textuais,   permitindo-lhes compreender e gerar linguagem humana de maneira surpreendentemente coerente e relevante.

O   desenvolvimento   dos   LLMs   marca   uma   revolução   no   PLN   por   várias   razões. Primeiramente, sua capacidade de gerar texto que parece natural e humano é impressionante. Eles podem escrever redações, criar poesia, programar em diversas linguagens de computador, e  até  mesmo  emular  estilos  de  escrita  específicos.  Isso  abre  um  leque  de  aplicações  práticas, desde a automação de tarefas de redação até o suporte a sistemas de ensino e aprendizagem.

Além disso, os LLMs têm a habilidade de entender contexto e realizar tarefas complexas de compreensão e resposta a perguntas, o que é fundamental em áreas como assistentes virtuais, chatbots  e  sistemas  de  informação  automatizados.  Eles  podem  processar  informações,  extrair conhecimentos relevantes de grandes volumes de texto e até mesmo realizar algumas formas de raciocínio.

Outro aspecto revolucionário dos LLMs é sua flexibilidade. Eles podem ser adaptados para diferentes línguas e dialetos, tornando-os ferramentas valiosas em contextos multilíngues. Além disso,  podem  ser  treinados  ou  ajustados  para  tarefas  específicas,  melhorando  sua  eficiência  e eficácia em áreas especializadas, como medicina, direito e finanças.

Contudo, existem desafios e limitações. Um deles é o viés, que pode ser inerente aos dados de  treinamento.  Isso  requer  atenção  cuidadosa  para  garantir  que  os  outputs  não  reforcem estereótipos ou preconceitos. Além disso, embora  sejam avançados em termos linguísticos, os LLMs  não  possuem  compreensão  do  mundo  real  ou  consciência,  limitando  sua  capacidade  de entender contextos complexos ou nuances éticas.

Os LLMs representam um salto significativo em PLN, oferecendo potencial para inúmeras aplicações  práticas  e  criativas.  No  entanto,  seu  uso  responsável  e  a  superação  de  desafios técnicos e éticos continuam sendo áreas de intensa pesquisa e desenvolvimento.

---

## LLMs (Large Language Models) e a Revolução em NLP

Os Large Language Models (LLMs) representam uma das inovações mais significativas no campo   do   Processamento   de   Linguagem   Natural   (PLN).   Esses   modelos   são   sistemas   de Inteligência Artificial   treinados   em   vastos   conjuntos   de   dados   textuais,   permitindo-lhes compreender e gerar linguagem humana de maneira surpreendentemente coerente e relevante.

O   desenvolvimento   dos   LLMs   marca   uma   revolução   no   PLN   por   várias   razões. Primeiramente, sua capacidade de gerar texto que parece natural e humano é impressionante. Eles podem escrever redações, criar poesia, programar em diversas linguagens de computador, e  até  mesmo  emular  estilos  de  escrita  específicos.  Isso  abre  um  leque  de  aplicações  práticas, desde a automação de tarefas de redação até o suporte a sistemas de ensino e aprendizagem.

Além disso, os LLMs têm a habilidade de entender contexto e realizar tarefas complexas de compreensão e resposta a perguntas, o que é fundamental em áreas como assistentes virtuais, chatbots  e  sistemas  de  informação  automatizados.  Eles  podem  processar  informações,  extrair conhecimentos relevantes de grandes volumes de texto e até mesmo realizar algumas formas de raciocínio.

Outro aspecto revolucionário dos LLMs é sua flexibilidade. Eles podem ser adaptados para diferentes línguas e dialetos, tornando-os ferramentas valiosas em contextos multilíngues. Além disso,  podem  ser  treinados  ou  ajustados  para  tarefas  específicas,  melhorando  sua  eficiência  e eficácia em áreas especializadas, como medicina, direito e finanças.

Contudo, existem desafios e limitações. Um deles é o viés, que pode ser inerente aos dados de  treinamento.  Isso  requer  atenção  cuidadosa  para  garantir  que  os  outputs  não  reforcem estereótipos ou preconceitos. Além disso, embora  sejam avançados em termos linguísticos, os LLMs  não  possuem  compreensão  do  mundo  real  ou  consciência,  limitando  sua  capacidade  de entender contextos complexos ou nuances éticas.

Os LLMs representam um salto significativo em PLN, oferecendo potencial para inúmeras aplicações  práticas  e  criativas.  No  entanto,  seu  uso  responsável  e  a  superação  de  desafios técnicos e éticos continuam sendo áreas de intensa pesquisa e desenvolvimento.

---

## Qual a Relação Entre Transformers e LLMs

Transformers e LLMs (Large Language Models) estão diretamente relacionados no campo da NLP e aprendizado de máquina. Vamos detalhar essa relação:

- **Arquitetura Transformer:**
    
    A arquitetura Transformer foi introduzida em um papar de pesquisa publicado por Vaswani et al. em 2017, chamado “Attention is All You Need”.
    
    Esta arquitetura apresentou uma nova forma de lidar com sequências, usando o que é conhecido como “mecanismo de atenção autorregressiva”, que permite ao modelo dar atenção a diferentes partes de uma sequência dependendo do contexto. Isso tornou os Transformers especialmente poderosos para tarefas de sequência-a-sequência, como tradução automática.
    
- **LLMs (Large Language Models):**
    
    Estes são modelos de linguagem treinados em grandes voumes de texto. Eles têm a capacidade de gerar texto, completar frases, responder a perguntas e realizar uma variedade de outras tarefas relacionadas ao Processamento de Linguagem Natural.
    
    O que faz de um modelo de linguagem um “LLM” é, em grande parte, sua escala - estes modelos são treinados com bilhões ou até milhões de parâmetros.
    

A arquitetura Transformer é espinha dorsal dos LLMs mais populares e poderosos. Modelos como o BERT, GPT, T5 e outros baseados na arquitetura Transformer. Quando dizemos “GPT é um Transformer”, estamos nos referindo ao fato de que o GPT usa a arquitetura Transformer para processar e gerar texto.

**Por que os Transformers são populares para LLMs?**

A capacidade dos Transformers de lidar com dependências de longo alcance em texto e sua eficiência em paralelização tornam esses modelos ideias para treinar LLMs. Além disso, seu mecanismo de atenção permite que eles captem nuances e padrões em grandes volumes de dados, o que é essencial para o desempenho superior em tarefas de PLN.

---

## Arquitetura BERT e sua Relação com os LLMs

O **BERT (Bidirectional Encoder Representations from Transformers)** é uma das arquiteturas mais influentes no campo do Processamento de Linguagem Natural (PLN) e um marco no desenvolvimento de Modelos de Linguagem Grande (LLMs). Criado pelo Google AI em 2018, o BERT é baseado na arquitetura Transformer e introduziu o conceito de aprendizado bidirecional para modelagem de linguagem. Isso significa que ele analisa o contexto de palavras olhando simultaneamente para os tokens à esquerda e à direita de cada palavra, o que lhe permite capturar relações semânticas profundas. Essa característica o diferencia de modelos unidirecionais, como o GPT da época, que processavam o texto em apenas uma direção (da esquerda para a direita).  

Historicamente, o BERT é fruto do avanço iniciado pelo Transformer, apresentado em 2017 no artigo *"Attention is All You Need"*. Enquanto o Transformer foi projetado para várias aplicações, o BERT focou exclusivamente na parte de *encoders*, ideal para tarefas de compreensão de texto. Seu impacto foi imediato: redefiniu benchmarks como SQuAD e GLUE e se tornou a base para muitos modelos subsequentes em PLN.  

O treinamento do BERT é realizado em duas tarefas principais: *Masked Language Modeling (MLM)* e *Next Sentence Prediction (NSP)*. No MLM, algumas palavras são mascaradas no texto de entrada, e o modelo aprende a prever essas palavras com base no contexto. Já no NSP, o modelo aprende a determinar se uma sentença segue outra de forma lógica, o que melhora sua capacidade de entender relações entre frases. Além disso, o BERT utiliza um método de tokenização chamado *WordPiece*, que divide palavras em subpalavras, permitindo maior flexibilidade no tratamento de palavras raras ou desconhecidas.  

**Vantagens**<br/>

Entre as vantagens do BERT, destaca-se sua capacidade de entender profundamente o contexto das palavras, o que o torna especialmente eficaz em tarefas como classificação de texto, extração de entidades e respostas a perguntas. Ele também popularizou o conceito de transferência de aprendizado no PLN, onde um modelo pré-treinado em grandes conjuntos de dados pode ser ajustado (finetunado) para tarefas específicas com menos dados. Essa abordagem economiza tempo e recursos computacionais.  

**Desvantagens**<br/>

No entanto, o BERT apresenta algumas limitações. Seu custo computacional é elevado, tanto para treinamento quanto para inferência, devido ao grande número de parâmetros. Isso o torna pouco adequado para dispositivos com recursos limitados, como smartphones. Além disso, como é baseado apenas em *encoders*, o BERT não é ideal para tarefas de geração de texto, como as realizadas por modelos baseados em *decoders*, como GPT.  <br/><br/>

Em resumo, o BERT é um dos alicerces dos LLMs modernos, influenciando diretamente modelos e técnicas subsequentes. Ele estabeleceu um novo padrão no PLN ao oferecer um entendimento contextual robusto e soluções altamente eficazes para tarefas de compreensão de texto, mesmo que com algumas limitações práticas.


---

## Métricas de Avaliação de Performance dos LLMs

A avaliação da performance de LLMs (Large Language Models) em tarefas de Processamento de Linguagem Natural (PLN) envolve várias métricas que ajudam a medir a precisão, a coerência e a relevância dos textos gerados ou das previsões feitas. As métricas variam dependendo da tarefa específica, mas aqui estão algumas das mais comuns:

**1. Perplexidade**

- **Definição**: Perplexidade mede o quão bem o modelo prevê a próxima palavra em uma sequência de texto. Uma baixa perplexidade indica que o modelo está prevendo com mais confiança e precisão.
- **Aplicação**: Muito usada para avaliar modelos de linguagem em tarefas de geração de texto, como resposta a perguntas ou tradução automática.
- **Limitações**: Embora seja uma métrica útil para medir a "confiança" de um modelo, ela nem sempre se correlaciona com a qualidade percebida do texto gerado.

**2. BLEU (Bilingual Evaluation Understudy)**

- **Definição**: BLEU é uma métrica que compara o texto gerado pelo modelo com referências (ou textos de referência) usando a sobreposição de n-gramas (sequências de palavras). A pontuação BLEU vai de 0 a 1 (ou 0 a 100%) e indica quão próximo o texto gerado está da referência.
- **Aplicação**: Comumente usada em tradução automática, mas também aplicável em tarefas como resumo de texto.
- **Limitações**: BLEU não leva em conta a qualidade semântica e muitas vezes penaliza injustamente variações válidas que não estão nas referências.

**3. ROUGE (Recall-Oriented Understudy for Gisting Evaluation)**

- **Definição**: ROUGE mede a similaridade entre o texto gerado e o de referência com base em contagens de sobreposição de n-gramas, palavras e subsequências de palavras. As variantes mais comuns são ROUGE-N, ROUGE-L, e ROUGE-S.
- **Aplicação**: Utilizada principalmente em tarefas de resumo de texto e geração de respostas.
- **Limitações**: ROUGE também pode ser insensível a variações semânticas válidas, além de ser uma métrica baseada apenas em similaridade de superfície.

**4.** **METEOR (Metric for Evaluation of Translation with Explicit ORdering)**

- **Definição**: A métrica METEOR foca na correspondência entre sinônimos, inflexões e ordem das palavras, oferecendo uma análise mais detalhada em comparação ao BLEU e ROUGE.
- **Aplicação**: Utilizada em tradução automática e outras tarefas de geração de texto, como resumo, pois leva em conta tanto a correspondência exata quanto a ordem.
- **Limitações**: Como é mais complexa, METEOR é mais custosa computacionalmente e pode não se aplicar bem em textos mais longos.

**5.** **F1-Score**

- **Definição**: O F1-Score é a média harmônica entre precisão e recall. A precisão mede a porcentagem de previsões corretas em relação às previsões totais, enquanto o recall mede a porcentagem de previsões corretas em relação aos dados corretos.
- **Aplicação**: Usada em tarefas de classificação, como análise de sentimentos, classificação de perguntas e respostas e detecção de entidades nomeadas.
- **Limitações**: Pode não capturar a complexidade das respostas geradas em tarefas de geração de texto.

**6.** **Exact Match (EM)**

- **Definição**: EM mede a proporção de respostas exatas (idênticas) entre a resposta do modelo e a resposta correta esperada.
- **Aplicação**: Comum em tarefas de resposta a perguntas, especialmente para perguntas onde há uma única resposta correta.
- **Limitações**: Não captura variações linguísticas válidas e é rígida, sendo mais adequada para perguntas com respostas curtas e objetivas.

**7. CIDEr (Consensus-based Image Description Evaluation)**

- **Definição**: CIDEr mede a similaridade entre a descrição gerada e as descrições de referência usando o consenso entre várias descrições de referência.
- **Aplicação**: Embora seja mais popular em geração de descrições de imagens, pode ser usada em tarefas de resumo de texto ou em tarefas multimodais, onde o modelo gera descrições a partir de dados de entrada variados.
- **Limitações**: Depende de múltiplas descrições de referência para um bom desempenho, o que nem sempre é viável.

**8. Métrica de Coerência e Fluência**

- **Definição**: São métricas qualitativas que avaliam se o texto gerado é coerente e fluente, ou seja, se faz sentido e é bem estruturado. Em geral, são medidas subjetivas, às vezes usando avaliações humanas, ou calculadas com base na probabilidade de um texto conforme modelos de linguagem como BERT.
- **Aplicação**: Úteis para modelos de geração de texto onde a coerência narrativa é essencial, como em diálogos e redação criativa.
- **Limitações**: Avaliações qualitativas dependem da percepção humana, o que torna difícil padronizar e automatizar.

**9. Human Evaluation (Avaliação Humana)**

- **Definição**: Avaliação humana envolve pessoas que julgam a qualidade dos textos gerados, classificando critérios como relevância, coerência, fluência e adequação.
- **Aplicação**: Fundamental para tarefas onde as métricas automáticas não capturam bem a qualidade, como em geração criativa de conteúdo.
- **Limitações**: É uma avaliação subjetiva, custosa e demorada, além de difícil de reproduzir.

**Resumo das Métricas de Avaliação de LLMs**

As métricas de avaliação de LLMs são diversas e variam de acordo com a tarefa. Métricas baseadas em n-gramas (como BLEU, ROUGE e METEOR) são úteis, mas muitas vezes limitadas, enquanto métricas mais complexas, como CIDEr e avaliações humanas, são necessárias para entender o desempenho em tarefas que exigem criatividade e flexibilidade. Em última análise, o uso combinado de várias métricas fornece uma visão mais abrangente e robusta da performance dos LLMs.
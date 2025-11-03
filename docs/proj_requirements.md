Este desafio tem como objetivo desenvolver uma solução de Engenharia de Dados, que deverá abranger os seguintes tópicos: 
- extração de dados,
- ingestão de dados, 
- armazenamento de dados,
- observabilidade, 
- segurança de dados,
- mascaramento de dados, 
- arquitetura de dados e
- escalabilidade.
Seu desafio é projetar e implementar uma solução que possa lidar com o grande volume de dados. Procure abranger todos os tópicos mencionados nos requisitos.

No dia da apresentação, garanta o completo funcionamento do case (end-to-end) para banca, explique a arquitetura proposta, justificando suas escolhas tecnológicas e fornecendo exemplos práticos de como cada aspecto da solução seria implementado. Você pode utilizar como guia uma apresentação detalhada, incluindo diagramas, documentação e explicação de cada componente da solução. Forneça um plano de implementação e considere desafios e melhorias futuras. Lembre-se de que a solução deve ser escalável, segura e eficiente.

O tema abordado pelo case, no que diz respeito aos dados utilizados, é de livre escolha do candidato, por exemplo saúde pública, mercado de ações, estudos demográficos e/ou sociais, mercado de comodities, etc.

# Requisitos:
1. **Extração de Dados:**
- Utilize fontes de dados confiáveis, como dados abertos de órgãos públicos, bolsa de valores ou datasets exploratórios. Você também pode trabalhar com geração de dados simulados.
- Considere diferentes formatos de dados, como arquivos CSV, APIs públicas, bancos de dados, etc.
2. **Ingestão de Dados:**
- Implemente um mecanismo eficiente para a ingestão em lote e/ou contínua e em tempo real dos dados provenientes das diferentes fontes.
- Considere diferentes formas de ingestão, como streaming de dados, ETL (Extract, Transform,
Load) e arquiteturas (Kappa, Lambda).
3. **Armazenamento de Dados:**
- Escolha uma ferramenta de armazenamento adequada e eficiente para seu case. Saiba diferenciar e justificar o uso de outras possíveis ferramentas ou tecnologias para o armazenamento dos dados, levando em consideração aspectos como volume, velocidade e variedade.
- Avalie opções de armazenamento na nuvem (cloud) ou on-premises, considerando aspectos de segurança e escalabilidade.
4. **Observabilidade:**
- Desenvolva uma estratégia de monitoramento e observabilidade da solução, garantindo a capacidade de rastrear o fluxo de dados, detectar falhas e identificar possíveis gargalos de desempenho entre as ferramentas que compõem o(s) pipeline(s) de ingestão.
5. **Segurança de Dados:**
- Garanta a segurança e confidencialidade dos dados sensíveis dos pacientes, adotando práticas de criptografia, controle de acesso e cumprindo regulamentações de proteção de dados, como a Lei Geral de Proteção de Dados (LGPD).
6. **Mascaramento de Dados:**
- Proponha técnicas e exemplos de como mascarar dados sensíveis, garantindo a privacidade e anonimização das informações utilizadas na análise.
7. **Arquitetura de Dados:**
- Projete uma arquitetura de dados escalável que permita o processamento eficiente e uma estrutura de dados adequada para análise.
- Considere o uso de tecnologias como data lakes, data warehouse e sistemas de processamento distribuído para lidar com o grande volume e variedade de dados.
8. **Escalabilidade**:
- Garanta que (ou descreva como) a solução proposta seja capaz de lidar com o aumento contínuo do volume de dados e a crescente demanda por análises em tempo real.
- Sugira estratégias de escalabilidade horizontal e vertical, como a distribuição de carga em clusters de servidores ou o provisionamento de recursos adicionais na nuvem.

# Entregáveis:
A seguir são listados os entregáveis mínimos obrigatórios.
1. **Repositório GIT**: Deve ser entregue um repositório público no Github contendo o projeto do case desenvolvido.
O repositório deve possuir um arquivo README com a descrição do case (ver item 2. Relatório)
1. **Relatório**: deve ser entregue um relatório em formato README (Markdown) e deve possuir os seguintes tópicos:
        1. Objetivo do Case
        2. Arquitetura de Solução e Arquitetura técnica
        3. Explicação sobre o case desenvolvido
        4. Melhorias e Considerações Finais
O relatório será avaliado de acordo com a CLAREZA das informações e dos DIAGRAMAS DE SOLUÇÃO, CORRETUDE TÉCNICA e APLICAÇÃO ADEQUADA DA LÍNGUA PORTUGUESA.

# Reprodutibilidade da arquitetura:
- O candidato deve garantir que a solução implementada possa ser reproduzida em outra máquina ou ambiente;
- Todos os scripts de configuração, instalação e execução devem estar incluídos no repositório Git;
- O candidato deve incluir instruções claras para a configuração e execução do projeto em outra máquina ou ambiente.

# Apresentação do Case:
Durante a apresentação é esperado que o candidato demonstre a solução em funcionamento, apresentando cada uma das partes da arquitetura desenvolvida. O candidato terá 1hr30m (uma hora e trinta minutos) para apresentar o case e responder as perguntas dos avaliadores.
Boa sorte e esperamos que sua solução demonstre um domínio completo dos tópicos de Engenharia de Dados mencionados!
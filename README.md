# Sistema de Gestão de Telemetria e Disponibilidade de Frota (Minitrucks)

Este projeto consiste em um microsserviço de missão crítica voltado para o monitoramento contínuo, análise preditiva de telemetria e gestão de estado de frotas de mineração autônomas/tripuladas.

O sistema intercepta dados agregados de telemetria em tempo real, filtra ruídos espúrios de sensores e processa regras de negócios complexas para antecipar alertas críticos (**Don't Go**), traduzindo o risco em ações operacionais imediatas.

### 🛠️ Tecnologias Principais
* **Backend:** Python 3.11+ / FastAPI
* **Conteinerização:** Docker & Docker Compose
* **Banco de Dados:** PostgreSQL (TimescaleDB para Séries Temporais)
* **Processamento de Estado:** Redis (Cache e Rolling Windows de 4h/8h)

### 🚀 Como Executar o Projeto
*(Instruções de inicialização com Docker Compose serão adicionadas em breve, acompanhem...)*

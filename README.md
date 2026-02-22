# 🛡️ Sistema de Inventário do Bunker

Este é um sistema de linha de comando (CLI) desenvolvido para gerenciar recursos em um cenário de sobrevivência. O projeto foi criado como parte de um desafio prático para aplicar conceitos de **Lógica de Programação**, **Banco de Dados**, **Estrutura de Dados** e **Versionamento**.

---

## 🧠 Aprendizados e Fundamentos

De acordo com a metodologia de desenvolvedores sêniores, este projeto não é apenas um "exercício", mas sim a construção de uma **base sólida** de engenharia de software:

### ⚙️ Habilidades Técnicas de Base
* **Lógica de Programação:** A base para resolver qualquer problema técnico em vez de apenas decorar frameworks.
* **Estrutura de Dados:** Como organizar a informação (itens do bunker) de forma eficiente para o computador processar.
* **Banco de Dados:** Entendimento de como os sistemas realmente funcionam "por baixo do capô" e como a informação é persistida via SQLite.
* **Versionamento (Git):** O controle profissional de como o código evolui ao longo do tempo.

### 🧠 Postura e Mentalidade Profissional
1. **Foco no Problema, não na Tarefa:** Entender o impacto que o sistema gera e o "porquê" de cada funcionalidade.
2. **Código Pensado na Manutenção:** Escrita de arquivos legíveis e modulares, diferenciando um profissional de um amador.
3. **Responsabilidade e Autonomia:** Investigar erros de ambiente (como terminal e permissões) e buscar soluções de forma independente.

> 💡 **"Crescimento rápido é fruto de constância e base forte."**

---

## 🚀 Funcionalidades

- **Adicionar Itens:** Registra nome, quantidade e categoria dos recursos.
- **Listar Inventário:** Exibe todos os itens armazenados no banco de dados.
- **Persistência de Dados:** Utiliza SQLite para garantir que os dados não sejam perdidos ao fechar o programa.
- **Interface CLI:** Interação direta e rápida via terminal.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** [Python](https://www.python.org/)
* **Banco de Dados:** [SQLite3](https://www.sqlite.org/index.html)
* **Versionamento:** [Git](https://git-scm.com/) & [GitHub](https://github.com/)

## 📂 Estrutura do Projeto

* `main.py`: O menu principal que integra todas as funcionalidades.
* `banco.py`: Script responsável pela criação da estrutura da tabela SQL.
* `adicionar.py`: Lógica para entrada e inserção de dados no banco.
* `listar.py`: Lógica para consulta e exibição dos dados.
* `inventario.db`: Arquivo gerado automaticamente que armazena os dados.

## 🔧 Como Executar

1. Certifique-se de ter o Python instalado.
2. Clone este repositório:
   ```bash
   git clone [https://github.com/henri-codee/projeto_inventario..git](https://github.com/henri-codee/projeto_inventario..git)

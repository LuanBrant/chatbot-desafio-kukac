# Chatbot de Questionário Kukac

Este projeto é um chatbot interativo de questionário desenvolvido com Python, utilizando a biblioteca Streamlit para a interface de usuário e LangChain para lidar com a lógica de linguagem natural e recuperação de informações. O sistema permite a realização de questionários dinâmicos com validação de respostas e download de resultados.

## Funcionalidades

- **Upload de arquivo JSON**: Permite carregar um arquivo JSON contendo as perguntas do questionário.
- **Perguntas Dinâmicas**: Apresenta perguntas uma a uma para o usuário.
- **Validação de Respostas**: Valida as respostas ignorando diferenças de maiúsculas, minúsculas e acentos.
- **Tipos de Perguntas**: Suporte para diferentes tipos de perguntas, como:
  - **Texto**: O usuário pode digitar a resposta.
  - **Múltipla Escolha**: O usuário pode selecionar uma resposta dentre várias opções.
- **Pontuação**: Exibe a pontuação final do usuário ao final do questionário.
- **Download de Resultados**: Oferece um botão para download das respostas do usuário em formato JSON.
- **Reinício do Questionário**: Permite reiniciar o questionário com um clique duplo no botão "Reiniciar".

## Estrutura do Projeto

O projeto está organizado em duas partes principais:

- **Frontend (`frontend.py`)**: Responsável pela interface e interação com o usuário. Desenvolvido com Streamlit.
- **Backend (`backend.py`)**: Contém toda a lógica de validação, manipulação de dados e integração com LangChain.

## Requisitos

Certifique-se de ter os seguintes itens instalados:

- Python 3.8 ou superior
- Bibliotecas Python necessárias (instaladas via `pip`):
  - `streamlit`
  - `langchain`
  - `openai`
  - `faiss-cpu`
  - `python-decouple`

## Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Crie um arquivo `.env` para armazenar sua chave de API da OpenAI:
   ```plaintext
   OPENAI_API_KEY=your_openai_api_key
   ```

4. Inicie o aplicativo Streamlit:
   ```bash
   streamlit run frontend.py
   ```

5. Acesse o aplicativo no navegador em: `http://localhost:8501`

## Estrutura do Arquivo JSON

O arquivo JSON deve seguir o seguinte formato:

### Para perguntas de texto:
```json
[
  {
    "question": "Qual é a capital do Brasil?",
    "tipo": "texto",
    "answer": "Brasília"
  },
  {
    "question": "Qual é o maior planeta do sistema solar?",
    "tipo": "texto",
    "answer": "Júpiter"
  }
]
```

### Para perguntas de múltipla escolha:
```json
[
  {
    "question": "Qual é a capital do Brasil?",
    "tipo": "multipla_escolha",
    "opcoes": ["Brasília", "São Paulo", "Rio de Janeiro"],
    "answer": "Brasília"
  },
  {
    "question": "Qual é o maior planeta do sistema solar?",
    "tipo": "multipla_escolha",
    "opcoes": ["Terra", "Júpiter", "Marte"],
    "answer": "Júpiter"
  }
]
```

## Contribuição

Contribuições são bem-vindas! Siga os passos abaixo para contribuir:

1. Faça um fork do repositório
2. Crie uma branch para sua feature ou correção de bug:
   ```bash
   git checkout -b minha-feature
   ```
3. Faça commit das suas alterações:
   ```bash
   git commit -m "Adiciona minha nova feature"
   ```
4. Faça push para sua branch:
   ```bash
   git push origin minha-feature
   ```
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo `LICENSE` para mais informações.

---

import json
import unicodedata
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
import os
from decouple import config

os.environ['OPENAI_API_KEY'] = config('OPENAI_API_KEY')
llm = ChatOpenAI(temperature=0, openai_api_key=os.environ['OPENAI_API_KEY'])

def load_questions_from_file(uploaded_file):
    """Carregar perguntas de um arquivo JSON."""
    try:
        questions_data = json.load(uploaded_file)
        if not all("question" in q and "tipo" in q and "answer" in q for q in questions_data):
            raise ValueError("Arquivo JSON inválido. Certifique-se de que cada pergunta tenha 'question', 'tipo' e 'answer'.")
        for q in questions_data:
            if q["tipo"] == "multipla_escolha" and "opcoes" not in q:
                raise ValueError("Perguntas de múltipla escolha devem incluir o campo 'opcoes'.")
        return questions_data
    except Exception as e:
        raise ValueError(f"Erro ao carregar o arquivo JSON: {e}")

def create_faiss_database(questions):
    """Criar banco de dados FAISS com embeddings."""
    embeddings = OpenAIEmbeddings(openai_api_key=os.environ['OPENAI_API_KEY'])
    questions_text = [q["question"] for q in questions]
    vector_store = FAISS.from_texts(questions_text, embeddings)
    return vector_store

def normalize_text(text):
    """Normalizar texto, removendo acentos e transformando para minúsculas."""
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8').lower().strip()
    return text

def validate_response(response, correct_answer):
    """Validar a resposta do usuário."""
    return normalize_text(response) == normalize_text(correct_answer)

def generate_results(score, questions, responses):
    """Gerar resultados do questionário em formato JSON."""
    results = {
        "score": score,
        "total": len(questions),
        "responses": [
            {
                "question": normalize_text(r["question"]),
                "response": normalize_text(r["response"]),
                "correct": r["correct"],
                "correct_answer": normalize_text(r["correct_answer"])
            } for r in responses
        ]
    }
    return json.dumps(results, indent=4, ensure_ascii=True)

import streamlit as st
from main import load_questions_from_file, create_faiss_database, normalize_text, validate_response, generate_results

st.title("Chatbot de Questionário Kukac")

st.write("Faça o upload de um arquivo JSON contendo as perguntas do questionário.")
uploaded_file = st.file_uploader("Upload do arquivo JSON", type=["json"])

if uploaded_file:
    try:
        questions = load_questions_from_file(uploaded_file)
        st.success("Arquivo JSON carregado com sucesso!")
        vector_store = create_faiss_database(questions)
    except ValueError as e:
        st.error(str(e))
        st.stop()
else:
    st.stop()

if "responses" not in st.session_state:
    st.session_state.responses = []
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "reset_clicks" not in st.session_state:
    st.session_state.reset_clicks = 0

st.write("Responda às perguntas a seguir:")

if st.session_state.current_question < len(questions):
    question = questions[st.session_state.current_question]
    with st.chat_message("Pergunta"):
        st.write(f"**Pergunta {st.session_state.current_question + 1}:** {question['question']}")

    with st.chat_message("Usuário"):
        response = None
        if question["tipo"] == "texto":
            response = st.text_input("Sua resposta:", key=f"response_{st.session_state.current_question}")
        elif question["tipo"] == "multipla_escolha":
            response = st.radio("Escolha uma opção:", options=question["opcoes"], key=f"response_{st.session_state.current_question}")
        else:
            st.error("Tipo de pergunta não suportado.")

    st.write("Clique em 'Enviar' para enviar sua resposta e clique novamente para avançar para próxima pergunta.")

    submit_clicked = st.button("Enviar", key=f"send_{st.session_state.current_question}")

    if submit_clicked and response:
        is_correct = validate_response(response, question["answer"])
        if is_correct:
            st.session_state.score += 1
        st.session_state.responses.append({
            "question": question["question"],
            "response": response,
            "correct": is_correct,
            "correct_answer": question["answer"]
        })
        st.session_state.current_question += 1
else:
    with st.chat_message("Sistema"):
        st.write(f"**Você finalizou o questionário! Pontuação: {st.session_state.score}/{len(questions)}**")
        st.write("Baixe suas respostas abaixo:")
    
    json_results = generate_results(st.session_state.score, questions, st.session_state.responses)
    st.download_button(label="Download Resultados", data=json_results, file_name="resultados.json", mime="application/json")

st.write("Clique em 'Reiniciar' duas vezes para confirmar o reinício do questionário.")
reset_clicked = st.button("Reiniciar")
if reset_clicked:
    st.session_state.reset_clicks += 1
    if st.session_state.reset_clicks >= 2:
        st.session_state.responses = []
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.reset_clicks = 0


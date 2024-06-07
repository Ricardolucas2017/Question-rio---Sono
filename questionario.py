import streamlit as st

# Título e introdução
st.title('Questionário de Diagnóstico do Sono')
st.write('Olá, seja bem-vindo!')

# Informações do usuário
nome = st.text_input('Qual é o seu nome?')
nome_completo = st.text_input('Qual é o seu nome completo?')
idade = st.number_input('Qual é a sua idade?', min_value=0, max_value=120, step=1)
grau_instrucao = st.selectbox('Qual é o seu grau de instrução?', ['Fundamental', 'Médio', 'Superior', 'Pós-graduação'])

st.write('Assinale com “X” as respostas afirmativas:')

# Perguntas
quest1 = st.checkbox('1. Você frequentemente, mais de três noites por semana, tem dificuldades para dormir?')
quest2 = st.checkbox('2. Você dorme em diferentes horários a cada dia?')
quest3 = st.checkbox('3. Você acorda em diferentes horários a cada dia?')
quest4 = st.checkbox('4. Você tem o hábito de acordar frequentemente mais de duas vezes durante a noite?')
quest5 = st.checkbox('5. Você tem dificuldade em adormecer novamente quando acorda à noite?')
quest6 = st.checkbox('6. Você acorda muito cedo, antes ou em torno das 5 horas da manhã?')
quest7 = st.checkbox('7. Seu trabalho ou suas tarefas domésticas exigem que você tenha períodos noturnos de atividade?')
quest8 = st.checkbox('8. Você tem o hábito de sair durante a semana à noite em eventos sociais (jantar, barzinho, reunião com amigos, festas)?')
quest9 = st.checkbox('9. O estresse tem atrapalhado seu sono?')
quest10 = st.checkbox('10. Conflitos emocionais, familiares e divergências profissionais vêm dificultando você a adormecer e permanecer no sono?')
quest11 = st.checkbox('11. Incertezas e dúvidas sobre o desenrolar dos acontecimentos recentes e futuros chegam a incomodar sua mente na hora de adormecer e em permanecer dormindo?')
quest12 = st.checkbox('12. Você dorme num ambiente tenso, ameaçador ou inseguro?')
quest13 = st.checkbox('13. No seu ambiente de dormir há luz acesa, barulho ou sensação térmica desconfortante?')
quest14 = st.checkbox('14. No seu ambiente de dormir há aparelhos eletrônicos (TV, computador, celular, tablet)?')
quest15 = st.checkbox('15. Se você não dorme sozinho, seu companheiro (ou sua companheira) incomoda você durante a noite?')
quest16 = st.checkbox('16. Você frequentemente se sente cansado e com dores no corpo quando acorda pela manhã?')
quest17 = st.checkbox('17. Tem sentido que ultimamente está ficando irritado, com memória ruim, desanimado ou tenso durante o dia?')
quest18 = st.checkbox('18. Sua percepção e sua concentração estão sendo afetadas também?')
quest19 = st.checkbox('19. Fica angustiado quando vai se aproximando o horário de dormir?')
quest20 = st.checkbox('20. Você está tomando alguma medicação (sem orientação de um médico especialista em distúrbios do sono) para dormir?')
quest21 = st.checkbox('21. Você toma regularmente (+ de uma vez por semana) álcool à noite?')
quest22 = st.checkbox('22. Faz uso de bebidas energéticas, chás ou café durante o dia?')
quest23 = st.checkbox('23. Você sente que seu sono piorou nos últimos meses?')
quest24 = st.checkbox('24. Você acha que sempre dormiu mal?')

# Processar as respostas e gerar diagnóstico
if st.button('Ver Resultado'):
    st.write('### Resultado do Questionário')

    if quest1 or quest2 or quest3 or quest7 or quest8:
        st.write('Respostas afirmativas para 1, 2, 3, 7 e 8: indicam interferências no ritmo circadiano com horários de sono irregulares que podem provocar ou agravar quadros de insônia.')

    if quest4 or quest5:
        st.write('Respostas afirmativas para 4 e 5: indicam distúrbios ligados à manutenção do sono.')

    if quest9 or quest10 or quest11 or quest12 or quest19:
        st.write('Respostas afirmativas para 9, 10, 11, 12 e 19: indicam transtorno de ansiedade generalizada.')

    if quest13 or quest14 or quest15:
        st.write('Respostas afirmativas para 13, 14 e 15: indicam estágios leves de sono provocados por interferências do ambiente que podem provocar ou agravar quadros de insônia.')

    if quest20 or quest21 or quest22:
        st.write('Respostas afirmativas para 20, 21 e 22: indicam uso de medicação (sem orientação por profissional médico especialista em distúrbios do sono) ou outras substâncias que prejudicam a manutenção e qualidade do sono.')

    if quest23 or quest24:
        st.write('Respostas afirmativas para 23 e 24: indicam distúrbios ligados à má percepção do sono.')

    st.write('Os resultados indicam a necessidade de uma avaliação mais detalhada com um profissional especializado para um diagnóstico preciso.')

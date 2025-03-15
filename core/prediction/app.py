from joblib import load
from pandas import DataFrame

# Carregar o pipeline salvo
pipeline_carregado = load('core/prediction/pipeline_completo.pkl')


def fazer_previsao(questionario, participante):
    # Criar um dicionário com os dados do questionário
    dados_entrada = {
        'Age': [participante.idade()],  # Supondo que você tenha um campo 'idade' no modelo
        'Gender': ['F' if participante.genero == 'F' else 'M'],  # Supondo que você tenha um campo 'genero'
        'Discomfort Eye-strain': ['Y' if questionario.fadiga_ocular else 'N'],
        'Redness in eye': ['Y' if questionario.vermelhidao_ocular else 'N'],
        'Itchiness/Irritation in eye': ['Y' if questionario.irritacao_ocular else 'N'],
        'Average screen time': [questionario.tempo_medio_tela],
        'Blue-light filter': ['Y' if questionario.filtro_luz_azul else 'N'],
        'Smart device before bed': ['Y' if questionario.uso_smartphone else 'N'],
        'Sleep duration': [questionario.duracao_sono],
        'Sleep quality': [questionario.qualidade_sono],
        'Stress level': [questionario.nivel_estresse],
        'Medical issue': ['Y' if questionario.problema_medico else 'N'],
        'Ongoing medication': ['Y' if questionario.tomando_medicacao else 'N'],
        'Caffeine consumption': ['Y' if questionario.consumo_cafeina else 'N'],
        'Alcohol consumption': ['Y' if questionario.consumo_alcool else 'N'],
        'Smoking': ['Y' if questionario.tabagismo else 'N'],
        'Physical activity': [questionario.atividade_fisica],
        'Heart rate': [questionario.frequencia_cardiaca],
        'Blood pressure': [questionario.pressao_arterial]
    }

    # Converter o dicionário em um DataFrame
    df_entrada = DataFrame(dados_entrada)

    # Fazer a previsão
    probabilidades = pipeline_carregado.predict_proba(df_entrada)

    # Retornar a probabilidade de ter a doença (classe 1) em porcentagem
    return probabilidades[0][1]

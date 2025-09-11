**Projeto de Machine Learning – Previsão de Sucesso de Livros (Fictício)**

**Objetivo**
Criar um modelo de classificação binária para prever se um livro será bem-sucedido com base em características como ano, número de páginas, autor, gênero e número de reviews.

**Estrutura do Projeto**

1. **Abordar o problema e analisar**

* Problema: prever se um livro será bem-sucedido (nota >= 4.0).
* Tipo: classificação binária (0 = não sucesso, 1 = sucesso).
* Desafios: dataset fictício com diferentes autores, gêneros e avaliações.

2. **Obter os dados**

* Fonte: dataset fictício criado diretamente em Python com pandas.
* Contém colunas como: título, ano, páginas, autor, gênero, reviews, nota.

3. **Explorar os dados**

* Verificação do tamanho (`df.shape`) e tipos (`df.info()`).
* Estatísticas descritivas (`df.describe()`).
* Frequência de autores, gêneros e distribuição de notas.
* Identificação de valores ausentes.

4. **Tratamento dos dados**

* Criação da variável alvo: `sucesso` (nota >= 4.0).
* Separação de features numéricas (`ano`, `paginas`, `reviews`) e categóricas (`autor`, `genero`).
* Pré-processamento:

  * Numéricos → imputação com mediana + padronização (`StandardScaler`).
  * Categóricos → imputação com valor mais frequente + one-hot encoding.
  * Implementado com `ColumnTransformer` e `Pipeline`.

5. **Separar Base em Arrays**

* Features: `['ano','paginas','autor','genero','reviews']`.
* Target: `sucesso`.
* Definição:

```python
X = df[features]
y = df['sucesso']
```

6. **Divisão Treino/Teste**

* Separação em treino (70%) e teste (30%) estratificando pelo target:

```python
train_test_split(X, y, test_size=0.3, stratify=y, random_state=42)
```

7. **Definição de Modelos**

* Foram treinados 3 modelos do scikit-learn:

  * Logistic Regression (`LogisticRegression(max_iter=500)`)
  * Random Forest (`RandomForestClassifier(n_estimators=200, max_depth=5)`)
  * KNN (`KNeighborsClassifier(n_neighbors=3)`)
* Cada modelo foi integrado a um pipeline com pré-processamento.

8. **Validação dos Modelos**

* Métricas: Acurácia, Precision, Recall, F1-score.
* Validação cruzada com 5 folds estratificados (`cross_val_score`).
* Comparação entre resultados de treino/teste e CV.

Exemplo esperado de saída:

```
RandomForest - Acurácia: 0.83
LogisticRegression - Acurácia: 0.77
KNN - Acurácia: 0.80
```

9. **Salvar a Solução**

* O melhor modelo é salvo com `joblib` para uso futuro:

```python
import joblib
joblib.dump(best_model, "best_model_livros.pkl")
```

**Resultados**

* O RandomForestClassifier apresentou o melhor desempenho (\~83% de acurácia média).
* O modelo foi salvo em `best_model_livros.pkl`.
* O critério de sucesso (`nota >= 4.0`) pode ser ajustado para modificar o target e a distribuição das classes.

**Como Usar**

* Execute o código no Python ou Google Colab.
* Ajuste o threshold de sucesso alterando a condição:

```python
df['sucesso'] = (df['nota'] >= 4.0).astype(int)
```

* Rode os modelos e compare os resultados.
* O modelo final será salvo como `best_model_livros.pkl`.
* Pode fazer previsões para novos livros usando:

```python
previsoes = best_model.predict(novos_livros)
```

**Resumo:**
Este projeto mostra o ciclo completo de Machine Learning supervisionado: desde a análise e limpeza dos dados até o treinamento, avaliação e salvamento do modelo final. O dataset fictício de livros foi usado para prever se cada livro será bem-sucedido com base em suas características principais.

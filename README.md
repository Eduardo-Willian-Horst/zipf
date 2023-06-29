# Análise de Frequência de Palavras usando a Lei de Zipf

Este código em Python realiza uma análise de frequência de palavras em um texto, utilizando a conhecida Lei de Zipf. A Lei de Zipf é um fenômeno linguístico que descreve a distribuição de frequência das palavras em um determinado texto, onde a frequência de uma palavra é inversamente proporcional ao seu ranking.

## Funcionamento

O código começa lendo o conteúdo de um arquivo de texto chamado "Texto.txt" e o armazena na variável `texto`. Em seguida, o texto é convertido para letras maiúsculas utilizando o método `upper()`.

A próxima etapa envolve a limpeza do texto, removendo todos os caracteres especiais e pontuações utilizando uma expressão regular. A função `re.sub()` substitui tudo o que não for letra, número ou espaço por uma string vazia, resultando em `texto_limpo`.

A variável `words` é um dicionário que armazena as palavras encontradas no texto e sua contagem de ocorrências. O código itera por cada caractere do texto limpo, construindo cada palavra. Quando um espaço em branco é encontrado, a palavra é adicionada ao dicionário `words` com sua respectiva contagem de ocorrências.

Após o loop, é feita uma verificação adicional para garantir que a última palavra seja contabilizada corretamente, caso o texto não termine com um espaço em branco.

A lista `words_sorted` é criada a partir do dicionário `words`, ordenada em ordem decrescente de ocorrências, utilizando a função `sorted()`.

Finalmente, o código exibe as palavras e suas ocorrências em ordem decrescente de frequência.

## Uso

Para utilizar este código, certifique-se de ter um arquivo de texto chamado "Texto.txt" no mesmo diretório do script Python. O arquivo deve conter o texto que você deseja analisar.

Execute o código e a saída será a lista de palavras encontradas no texto, juntamente com suas contagens de ocorrências, exibidas em ordem decrescente de frequência.

## Aviso

Este código é um exemplo simplificado para realizar uma análise básica de frequência de palavras com base na Lei de Zipf. Para análises mais complexas e precisas, considere utilizar bibliotecas e técnicas adicionais, levando em conta o pré-processamento de texto, remoção de stopwords, análise de n-gramas, entre outros.

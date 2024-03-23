# Substituir a tecla Aplicações


## Informações
* Author: Rui Fontes baseado no trabalho de Héctor J. Benítez Corredera
* actualizado em 22/03/2024
* Descarregar a [versão estável][1]
* Compatibilidade: NVDA versão 2019.3 e seguintes


## Apresentação
Este é um extra simples para aqueles computadores que não possuam a tecla Aplicações, ou cuja tecla Aplicações não funciona.
Também é útil no Explorador de ficheiros do Windows 11 compilação  22621 e mais recentes, uma vez que permite atribuir uma tecla à combinação Shift+tecla de aplicações, utilizada para apresentar o menu de contexto completo, uma vez que a partir desta versão do Windows, a tecla de aplicações mostra apenas uma versão reduzida do menu de contexto.
É necessário associar a tecla, ou combinação de teclas, que desejamos para substituir a tecla Aplicações.
No diálogo Definir comandos, secção Substituir a tecla Aplicações, podemos associar a combinação que desejamos.


## Observações
Ao associar uma combinação de teclas, ou uma única tecla, temos de ter em conta que essa combinação ou tecla não seja usada em nenhuma aplicação.
Por exemplo, Alt + Seta abaixo poderia funcionar na maior parte do sistema, mas não resultaria em muitas ocasiões.
Por exemplo, eu costumo usar as teclas  à direita da barra de espaços, ou seja, na maior parte dos portáteis, a tecla Alt+Control e a tecla Control da direita.
É possível saber em que tecla carregamos usando a ajuda de entrada do NVDA. Para isso, pressionamos NVDA + 1 e começamos a explorar as teclas no teclado. Para sair da ajuda de entrada do NVDA basta pressionar novamente NVDA + 1.


## Tradutores e colaboradores:
* Francês: Rémy Ruiz
* Russo: Valentin Kupriyanov
* Ucraniano: VovaMobile
* Turco: Umut Korkmaz


## Registo de alterações



### Versão 2023.09.30
* Na versão 2023.09.02 a compatibilidade com o NVDA foi estendida para a versão 2024.1;
* Agora também é possível atribuir um comando a Shift+tecla de aplicações;
* Desta forma, se atribuir a tecla de aplicações a Shift+tecla de aplicações, o menu de contexto completo será sempre aberto.


### Versão 2023.09.02
* Passou a ser mantido por Rui Fontes e equipa portuguesa do NVDA
* O código passou a estar totalmente em inglês.


### Versão 0.4
* Adicionados idiomas Russo, Ucraniano e Turco.
* Adicionada compatibilidade com NVDA 2023.1


### Versão 0.3
* Mudado o modo de invocar a tecla de aplicações nativa do NVDA para nativa do Windows, por ser um método mais fiável e mais direto.
* Adicionada a possibilidade de clique esquerdo e direito do rato no foco.
  É necessário atribuir as correspondentes combinações de teclas no diálogo Gestos de Entrada.
  Ao executarmos a acção, o rato será movido para o foco e executado o clique correspondente, é emitido um som para indicar que o clique foi executado.


### Versão 0.2
* Compatibilidade com NVDA 2022


### Versão 0.1.5
* Resolvido problema em complementos do NVDA.
* Adicionado idioma Francês.


###Versão 0.1
* Versão inicial.


[1]: https://github.com/ruifontes/RemapKeyAplication-para-NVDA/releases/download/2024.03.22/remapApplicationsKey-2024.03.22.nvda-addon

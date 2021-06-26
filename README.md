<h1 align="center"> Bot para disparo de mensagens no Whatsapp</h1>
<h5 align="center" font-weigth="bold">  Desenvolvido em Python, o ZapBot tem por finalidade fazer o dísparo de mensagens automáticas para uma determinada lista de contatos fornecida previamente por uma planilha.</h5>
<p align="justify"> Quando criei essa automação, tinha por objetivo aprender python de uma forma diferente (uma vez que nunca tinha programado nessa linguagem antes) e satisfazer a necessidade da empresa em que eu trabalhava de: enviar avisos, dar parabéns aos aniversariantes e lembrar ao prospect sobre sua aula experimental ou avaliação marcada. </p>
<p align="center">
  <img  height='600px' src="https://github.com/nanotecnologista/botZapLivre/blob/e41a802b13669235019d3e14c028e117576b7161/Demo.gif" alt="Demonstração">
  <h6 align="center">Screens on Desktop</h6>

### Instruções:
  <p> 
    
- Planilhas - São, ao todo, 3 planilhas (aniversariantes, aulasExperimentais, mensagemPersonalizada).
  Os dados solicitados para a planilha aniversariantes são: Data do Aniversário, Número, Nome, Se é Adulto (1) ou não (0).
  Em aulasExperimentais as informações necessárias são: Data da aula, Número, Serviço (se for natação, informar o nome da criança), Nome.
  Ambos já vem com script nativo pronto, uma vez que, essas funções foram criadas para resolver um problema específico da empresa.
  
  Já em mensagemPersonalizada, basta informar o Número e o Nome.


- Mensagem Personalizada - Dentro da pasta dist, há um arquivo mensagem.txt, basta abri-lo, inserir o texto desejado e salvar o arquivo.
                                                  
                                                 Exemplo: Olá, [nome]!
  
  Para que o nome da pessoa seja inserido, é necessário que o texto contenha [nome] em seu escopo, caso contrário, o programa entederá que você não deseja colocar o nome da pessoa e enviará o texto sem a mudança.

  
  Caso queira apenas fazer um dísparo de mensagens, sem a necessidade de inserir o nome da pessoa, também é possível. Basta não inserir no texto [nome].
                                                  
                                                 Exemplo: Olá, boa noite!

- IMPORTANTE - Ao inserir o número do contato na planilha, verifique se o número está com o 9 a mais, caso esteja RETIRE-O. O Whatsapp trabalha apenas com 8 números após o DD.
                                                 
                                                 Segue um Exemplo CORRETO: 7499990520
                                                 
                                                 Exemplo ERRADO:74999990520
                                                 Outro exemplo ERRADO: 74 9999 0520
                                                
       É DE EXTREMA IMPORTÂNCIA QUE O CONTATO JÁ ESTEJA SALVO OU (SE NÃO ESTIVER SALVO) VOCÊ JÁ TENHA CONVERSADO COM ELE.

</p>

### Iniciando o dísparo de mensagens:
- Para iniciar, basta clicar no executavel whatsappbot.exe, ele abrirá o navegador que será redirecionado para o site do WhatsApp, só é necessário fazer o login uma vez.
Aparecerá a caixa com o menu, é só escolher. Após finalizada a operação, aparecerá ou caixa, esta é para perguntar se deseja realizar outra operação. Basta clicar na opção desejada. 


### Chegamos ao fim

Bom, é isso!
Gostaria de deixar claro que sou apenas uma iniciante, mas que me diverti bastante aprendendo um pouco sobre automação.

## Esse projeto está publicado aqui graças aos incentivos dos meus amigos. Agradeço, primeiramente a Deus, depois a todos eles. Galera, Obrigada!!
Gerssivaldo, Gabriel, Felype, Ruvian e Vicktor. Obrigada! Cada um de vocês tiveram um papel muito importante nesse projeto. Além disso, me aguentaram fazendo tantas perguntas kkk.

O Gabriel foi a minha maior companhia durante o desenvolvimento, acho que foi o que mais teve que ter paciência kkk Obrigada Gaell! Você é TOP!!!

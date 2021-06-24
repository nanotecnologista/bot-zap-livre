def InserindoNome(nomeAdulto, nomeCrianca, servico):
      
      if (servico == 'Natação'):
            texto_aula = f"""Olá, *{nomeAdulto}*, tudo bem?
Eu sou a Camila, da Hidrofisio 😊
Passando para te lembrar, conforme combinado, que amanhã é o dia da aula inaugural de Natação do(a) _{nomeCrianca}_. 🥰
Nos sentimos honrados por contribuir para a *segurança aquática e bem estar* do seu filho.

*Podemos contar com a presença dele?* """

      elif (servico == 'Avaliação Gratuita' or servico == 'Avaliação gratuita' or servico == 'avaliação gratuita'):
            texto_aula= f"""Olá, *{nomeAdulto}*, tudo bem?
Eu sou a Camila, da Hidrofisio 😊
Passando para te lembrar, conforme combinado, que amanhã é o dia da sua _{servico}_. 🥰
Nos sentimos honrados por contribuir para a melhora da sua *saúde e bem estar*.

*Podemos contar com a sua presença?* """         

      else:
            texto_aula= f"""Olá, *{nomeAdulto}*, tudo bem?
Eu sou a Camila, da Hidrofisio 😊
Passando para te lembrar, conforme combinado, que amanhã é o dia da sua aula inaugural de _{servico}_. 🥰
Nos sentimos honrados por contribuir para a melhora da sua *saúde e bem estar*.

*Podemos contar com a sua presença?* """

      return texto_aula




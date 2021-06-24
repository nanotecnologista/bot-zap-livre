def InserindoNome(nomeAdulto, nomeCrianca, data_vencimento, servico):

      if (servico == 'Natação'):
            texto_cobranca = f"""Olá, *{nomeAdulto}*!
Passando para te lembrar que a mensalidade da Natação de _{nomeCrianca}_ já pode ser renovada.😃
Vencimento: {data_vencimento} 

Desconsidere esse aviso, caso você já tenha renovado."""

      elif (servico == 'Pilates' or servico == 'Yoga'):
            texto_cobranca= f"""Olá, *{nomeAdulto}*!
Passando para te lembrar que a mensalidade do _{servico}_ já pode ser renovada.😃
Vencimento: {data_vencimento} 

Desconsidere esse aviso, caso você já tenha renovado."""

      else: 
            texto_cobranca= f"""Olá, *{nomeAdulto}*!
Passando para te lembrar que a mensalidade da _{servico}_ já pode ser renovada.😃
Vencimento: {data_vencimento} 

Desconsidere esse aviso, caso você já tenha renovado."""

      return texto_cobranca




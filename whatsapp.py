import pandas as pd
from twilio.rest import Client
# Your Account SID from twilio.com/console
account_sid = 'AC77740cfe24f58bef257ce9a2af45f1c0'
# Your Auth Token from twilio.com/console
auth_token  = '50e1d27862a51f999c77f58bb807b758'
client = Client(account_sid, auth_token)

#passo a passo solução
 
#abrir os 6 arquivos do excel
listas_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in listas_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No meês {mes} alguém bateu a meta. Vendedor: {vendedor} , Vendas: {vendas}')
        message = client.messages.create(
            to = "+5581996062966", 
            from_ = "+19292961902",
            body = f'No meês {mes} alguém bateu a meta. Vendedor: {vendedor} , Vendas: {vendas}')
        print(message.sid)

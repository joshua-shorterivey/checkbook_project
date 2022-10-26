
import os
from datetime import date
ledger = {'balance': 0, 'transactions':{}}
prompt = 1

def prep_ledger(input, ledger):

    transactions  = input.split(',', maxsplit=1)[1].strip().split(':', maxsplit=1)[1].strip(' {}').split(':')
    description = transactions[0].strip('\'')
    amount = float(transactions[3].strip().split(',')[0])
    trans_type = transactions[-1].strip().strip('\'')

    ledger['balance'] = input.split(',', maxsplit=1)[0].split(':')[-1].strip()
    ledger['transactions'][f"{description}"] = {}
    ledger['transactions'][f'{description}']['amount'] = amount
    ledger['transactions'][f'{description}']['type'] = trans_type

if not os.path.exists('checkbook.txt'):
    with open('checkbook.txt', 'w') as f:
        f.write(str(ledger['balance']))
else:
    with open('checkbook.txt', 'r') as f:
        ledger['balance'] = float(f.read())



print('--- Welcome to your terminal checkbook! ---')

def trans_description():
    description = input('Enter description or press enter for none: ')

    if len(description) == 0:
        description = 'no_label'

    return description

def transaction(ledger, prompt):
    description = trans_description()

    ledger['transactions'][f'{description}'] = {}
    ledger['transactions'][f'{description}']['date'] = date.today()
    amount = float(input('How much is the amount? '))

    ledger['transactions'][f'{description}']['amount'] = amount

    if prompt == 2:
        ledger['transactions'][f'{description}']['type'] = 'debit'
    elif prompt == 3:
        ledger['transactions'][f'{description}']['type'] = 'credit'
    
    return amount

def view_transactions(ledger):
    print('Transactions\n----')
    print(ledger['transactions'])
    return

while prompt != 0:
    print(ledger)
    print('-----\n\n')
    prompt = float(input('''What would you like to do?

                                1) view current balance
                                2) record a debit (withdrawal)
                                3) record a credit (deposit)
                                4) view transactions
                                5) exit
                                
                                *** Enter 1-5 (numeric values only ***
                                ? '''))
                                
    if prompt == 1:
        print(f'Current Balance is {ledger["balance"]}')
    elif prompt == 2 :
        ledger['balance'] += transaction(ledger, prompt)
        print(f'Current Balance is {ledger["balance"]}')
    elif prompt == 3:
        ledger['balance'] -= transaction(ledger, prompt)
        print(f'Current Balance is {ledger["balance"]}')
    elif prompt == 4:
        view_transactions(ledger)
    else:
        print('Have a Good Day!')
        break
with open('checkbook.txt', 'w') as f:
    f.write(str(ledger['balance']))
with open('test.txt', 'w') as f:
    f.write(str(ledger)) 
exit()




from truecallerjs import search_phonenumber

def log_database(data):
    with open('file path','+a') as db:
        db.write(data)

while True:
    phonenumber = input('Enter Phone Number: ')
    phone_number = phonenumber

    id = 'a1i0T--hsIIDIF2kug0866zEjMOXKBeJzQvNp4lDdGqLrdRt8OK5ncpo16xejdaQ'
    response = (search_phonenumber (phone_number, "BD", id))
    data= response["data"][0]
    print('Name:',data['name'])
    log_database(f'Name: {data["name"]}\n')
    log_database(f'Number: {phone_number}\n')

    phones = data['phones']
    for phone in phones:
        print('SIM:',phone['carrier'])
        log_database(f'SIM: {phone["carrier"]}\n')

    addresses = data['addresses']
    for address in addresses:
        print('Address:',address['countryCode'], address['city'])
        log_database(f'Address: {address["countryCode"]}\n')

    internetAddresses = data['internetAddresses']
    for address in internetAddresses:
        print('Gmail:',address['id'])
        log_database(f'Gmail: {address["id"]}\n')

    print('--------------------------')
    log_database('--------------------------\n')

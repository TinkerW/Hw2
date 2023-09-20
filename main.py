# contacts = ['Moscow', 'Paris', 'Phoenix', 'Tokyo', 'Stockholm', '']


contacts = ['Newt', 'Tomas', 'Minho', 'Teresa', 2, 3, 4, 5]
print(contacts)
change_name = contacts.index('Minho')





admin = input("add, change or delete contact?")
if admin == "add":
    new_contact = input('Write your new contact:')
    contacts.append(new_contact)
    print('Done!')
elif admin == 'delete':
    print(contacts)
    user_delete = input('кого хотите удалить?')
    contacts.remove(user_delete)
    print(contacts)
elif admin == 'change':
    print(contacts)
    user_change = input('какое имя вы хотите изменить:')
    change_name = contacts.index(user_change)
    new_name = input('новое имя:')
    contacts[change_name] = new_name
    print(contacts)

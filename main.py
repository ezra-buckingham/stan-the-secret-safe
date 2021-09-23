from lookup_plugins.bitwarden import Bitwarden

bw = Bitwarden('bw')

#template = bw.get_bw_template('item.login')

template = bw.create_login_item_entry('TEST', 'QUAID', 'QUAIDWUZHERW', '', ['https://msn.com'])

print(template)

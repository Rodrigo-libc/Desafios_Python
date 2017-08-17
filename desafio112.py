users ={
'rodrigo:':{
'primeiro':'rodrigo',
'ultimo':'freitas',
'localização':'recife',
},
'rafa:':{
'primeiro':'rafael',
'ultimo':'silva',
'localização':'rio de janeiro',
},
}

for username, info_user in users.items():
    print('\nNome '+username)
    nome_completo = info_user['primeiro']+' '+info_user['ultimo']
    local = info_user['localização']
    print('\t Nome completo:'+nome_completo.title())
    print('\t Localização:'+local.title())


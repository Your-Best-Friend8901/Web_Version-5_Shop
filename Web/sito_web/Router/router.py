from django.shortcuts import render
################
#Роутер для доступа 
################
def Router(request):
    Page = request.session.get('Page','Main')
    try:
        Access = request.session['Access']
    except KeyError:
        Access = None
    return Handler(request,Page,Access)

def setting_dict_and_start_render(request,dicts,Page,Access):

    #берем из словаря нашим словари для страницы 
    exp =dicts.get(Page)

    # создаем 3 переменый папка страницы само имя страницы и доступ
    Page_dict = exp.get('Page')
    Access_dict= exp.get(Page)
    Folder_dict = exp.get('Folder')

    #Проверки
    if Access in Access_dict:
        return render(request,f'{Folder_dict}/{Page_dict}')
    else:
        request.session['Access'] = None
        return render(request,'Main_Page/Main.html')

def Handler(request,Page,Access):
    dicts= {'Main':{'Main': [None,True],
            'Page': 'Main.html',
            'Folder': 'Main_Page'},

            'Login1':{'Login1': [None],
            'Page': 'phase=1.html',
            'Folder': 'Main_Page'},

            'Login2':{'Login2': [False],
            'Page': 'phase=2.html',
            'Folder': 'Main_Page'},

            'Success':{'Success': [False],
            'Page': 'succes.html',
            'Folder': 'Main_Page'},

            'Registration':{'Registration': [None],
            'Page': 'Registration.html',
            'Folder': 'Main_Page'},

            'Profil': {'Profile': [False],
            'Page': 'Profile.html',
            'Folder': 'Main_Page'}}
    
    return setting_dict_and_start_render(request,dicts,Page,Access)  

################
#Роутер для проверки Get на данные
################
def Router_GET(request,form):
    #######################################
    try:
        #######################################
        uscita = request.GET.get('uscita',None)
        if uscita is None:
            return render(request,'Login_Page/phase=2.html',context={'form':form}) 
        ####################################### #Сдеси можно  добавить проверку uscita данные будут разные и будет проверять данные которые пришли если данные такие та то срабатывать хендлер какойто
        else:
            return Handler_GET(request,form)
        #######################################
    except:
        return render(request,'Login_Page/phase=2.html') # <=========== Проблема с безопасностью ##change
#######################################
#Готовые хендлеры для работы с Роутерами
#######################################
def Handler_GET(request,form):
    username = request.session['username']
#    code = Code_Create(username) # <===========  Проблема с безопасностью
    #######################################
#    if code is not None:
#        request.session['code'] = code
#        return render(request,'Login_Page/phase=2.html',context={'form': form})
    #######################################
#    else:
#        return render(request,'Login_Page/phase=2.html',context={'function': code})

#Роутер машрутизитаор проверяет запрос HTTP 

def Router_Get(request):

    def Verification_Get(request):
        check_data = request.GET.get('Teleport',None)
        print("Все GET параметры:", dict(request.GET))
        
        if check_data is None:
            
            return render(request,'Main/Main.html',context={'check_data': check_data})
        
        return Search_in_dicts(request,value=check_data)


    def Search_in_dicts(request,value):
        dicts = {'category':{'context':{'category'}},
                 'Cart':{'template':'Cart/Cart.html'},
                 'Account':{'template':'Profile/Profile.html'},
                 'Menu_auth':{'template':'Main_auth/Main_auth.html'}}

        Position_dict = dicts.get(value)
        if value == 'category':
            Position_object = Position_dict.get('context')
        else:
            Position_object = Position_dict.get('template')

        return Render_Page(request,keys= Position_object)
        

    def Render_Page(request,keys):

        if type(keys) == dict:
            return render(request,'Main/Main.html',context=keys)
        
        return render(request,keys)
       
    return Verification_Get(request)
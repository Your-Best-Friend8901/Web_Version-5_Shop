from django.shortcuts import render

def Router_Get(request):
    check_data = request.GET.get('Телепорт',None)
    
    if check_data is None:
        return render(request,'Main.html',context={'check_data': check_data})

    dicts = {'category':{'Молочное':'Dairy products',
                        'Мясо':'Meat'}}
    
    abc = str(check_data).split()
    Position_dict = abc[0]
    Position_object = abc[1]

    Find_dict = dicts.get(Position_dict)
    Find_object = Find_dict.get(Position_object)

    return render(request,'Main.html',context={'check_data': Find_object})

# {'head':{'Корзина':'Cart',
#                     'Аккаунт':'Account',
#                     'Гость':'Guest'},
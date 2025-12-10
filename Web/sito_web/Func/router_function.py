from .Manager import Manager
from .router_cache import router_cache

def router_function(request,*args,**kwargs):
    path = request.path

    router_cache(path,request)

    if router_cache is None:

        function_dict = {'': Manager.get_random_products,
                         'profile/': Manager}

        function = function_dict.keys(path)

        router_cache(path,request,data=function)

        return function
from universal_manager import Universal_Manager
from .router_cache import router_cache

def router_function(request,*args,**kwargs):
    path = request.resolver_match.url_name

    cache = router_cache(path,request)

    if cache is None:

        function_dict = {#FBV
                            'main': Universal_Manager.FBV.get_random_products,
                            'category_products': Universal_Manager.FBV.category_filter,
                        #CBV
                            'profile': Universal_Manager.CBV}

        function = function_dict.get(path)

        data = function(*args,**kwargs)

        router_cache(path,request,data=data)

        return function
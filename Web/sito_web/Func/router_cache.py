import random
import func
from django.core.cache import cache

def router_cache(path,request,category_name=None,data=None):

    SESSION_ID = request.session.session_key

    dict_keys_cache = {
        'profile':
        {
            'KEY' : f'profile:{request.user.id}',
            'TIMEOUT' : 60000 + random.randint(1,1000)
        },

        'main':
        {
            'KEY':'get_random_products',
            'TIMEOUT': 300
        },

        'login2':
        {
            'KEY': f'code:{SESSION_ID}',
            'TIMEOUT': 180 + random.randint(-20,20),
            'CONTINUE': {'KEY': f'cache_user_id:{request.session.session_key}',
                        'TIMEOUT': 160 + random.randint(0,20)}
        },

        'login':

        {
            'KEY': f'cache_user_id:{request.session.session_key}',
            'TIMEOUT': 160 + random.randint(0,20)
        },

        'category':

        {
            'KEY': f'{str(category_name)}',
            'TIMEOUT': 300 + random.randint(1,100)
        },
        
        'products_of_category' :

        {
            'KEY': 'count_product_category',
            'TIMEOUT': 600
        }}
        

    result = dict_keys_cache[f'{path}']


    try:
        if result['CONTINUE']:
            KEY = result['KEY']
            TIMEOUT = result['TIMEOUT']

            data_cache =cache.get(KEY,None)

        if data_cache is None:


            cache2 = result['CONTINUE']
            # Понял сдеси проблема в самой проверки я кеширую даже не зная если они есть либо нет и это не допустимо меня это злит но я это оставлю на завтра
            # Сейчас отдохну чтобы набрать силы на завтра ото сегодня я уже много чего сделал  например Router_fuction уже есть идея он будет возращать не только None но также и True 
            
            cache_data = check_cache(result,data)
            cache2_data = check_cache(cache2,data)

            return cache,cache2
    except KeyError:
        return check_cache(result,data)
                


def check_cache(result,data):
    KEY = result['KEY']
    TIMEOUT = result['TIMEOUT']

    cache_data = cache.get(KEY,None)

    if data is None:

        if cache_data is None :
            return None
            
        else:
            return cache_data
        
    else:

        cache.set(KEY,data,TIMEOUT)
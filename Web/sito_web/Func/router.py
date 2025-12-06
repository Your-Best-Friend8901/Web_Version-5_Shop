import random
from sito_web.admin import keys_randint_timeout
import func
from django.core.cache import cache

def router_cache(Page,request,category_name=None,data=None):

    randint_number = keys_randint_timeout.keys(Page)
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
        [{
            'KEY': f'code:{SESSION_ID}',
            'TIMEOUT': 180 + random.randint(-20,20)
        }
        ,
        {
            'KEY': f'cache_user_id:{request.session.session_key}',
            'TIMEOUT': 160 + random.randint(0,20)
        }],

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
        
    result = dict_keys_cache[f'{Page}']

    if result is list :
        pass

    else:
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


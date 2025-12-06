import random
from sito_web.admin import keys_randint_timeout

def router_cache(Page,request,category_name=None):

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
        

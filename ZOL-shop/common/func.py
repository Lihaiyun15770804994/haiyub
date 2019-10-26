import json

from django_redis import get_redis_connection


def cookie_to_redis(request,response):
    '''
    取出cookie里面的数据, 判断cookie中的数据是否在redis里面
    如果存在就覆盖
    如果不存在就添加
    cookie  gid 1 count 2
    redis gis 1 count 3
    :return:
    '''
    #取cookie中的数据
    cookie_data = request.COOKIES.get('cookie_data')

    #取redis中的数据
    username = request.session.get('username')
    redis_cli = get_redis_connection('cart')
    redis_data = redis_cli.get(f'cart-{username}')

    if cookie_data:
        #如果redis里面没哟数据
        if not redis_data:
            redis_data = cookie_data
        else:
            cookie_data = json.loads(cookie_data)
            redis_data = json.loads(redis_data)
            print(type(redis_data))

            for cookie in cookie_data:
                redis_data[cookie] = cookie_data[cookie]

            redis_data = json.dumps(redis_data)
        redis_cli.set(f'cart-{username}',redis_data)

        response.delete_cookie('cookie_data')
        return response




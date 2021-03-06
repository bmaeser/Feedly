import redis
from feedly import settings

connection_pool = None


def get_redis_connection(server_name='default'):
    '''
    Gets the specified redis connection
    '''
    global connection_pool

    if connection_pool is None:
        connection_pool = setup_redis()

    pool = connection_pool[server_name]

    return redis.StrictRedis(connection_pool=pool)


def setup_redis():
    '''
    Starts the connection pool for all configured redis servers
    '''
    pools = {}
    for name, config in settings.FEEDLY_REDIS_CONFIG.items():
        pool = redis.ConnectionPool(
            host=config['host'],
            port=config['port'],
            db=config['db']
        )
        pools[name] = pool
    return pools

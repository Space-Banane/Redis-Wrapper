import redis
global debug
debug = False

def set_debug(value:bool=True):
    global debug
    debug = value

def connect(auth,db:int=0):
    """
    Returns a new connection (conn) with provided auth and db
    \n 
    (db default is 0) \n
    (Debug is available)
    """
    if debug == True:
        print("Debug : Connecting to Redis server")
    conn = redis.Redis(host=auth["host"], port=auth["port"],password=auth["password"], db=db)
    if debug == True:
        print("Debug : Connected to Redis server")
    return conn

def close(conn):
    """
    Destroy a provided connection \n
    (Debug is available)
    """
    if debug == True:
        print("Debug : Destroying Connection!")
    return conn.close()
    

def set(conn:redis.Redis,key,value):
    """
    Set a key and value in specified connection
    """
    result = conn.set(key,value)
    if result is not True:
        print("Redis didnt return True!!!")
    return result

def get(conn:redis.Redis,key):
    """
    Get a value from specified key and connection
    """
    result = conn.get(key)
    return result.decode('utf-8')

def delete(conn:redis.Redis,key):
    """
    Delete a key with specified key and connection
    """
    conn.delete(key)
    return "Deleted :)"
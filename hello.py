#test app

#def wsgi_app(env,resp):
def app(env,start_response):
    status = '200 OK'
    headers = [('Content-Type','text/html')]
    #body = 'hello'
    #env = {}
    env['QUERY_STRING'] = 'a=1&a=2&b=3'
    body = env['QUERY_STRING'].split('&')
    res = [i+'\r\n' for i in body]
    #res
    #print body
    start_response(status, headers)
    #return[body]
    return[res]
    #return [bytes(data, 'utf-8')]
    #return [body.encode('utf-8')]
    #return 'hi'

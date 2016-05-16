#test app

#def wsgi_app(env,resp):
def app(env,start_response):
    status = '200 OK'
    headers = [('Content-Type','text/html')]
    #body = 'hello'
    body = env['QUERY_STRING'].split('&')
    print body
    start_response(status, headers)
    #return[body]
    #return [bytes(data, 'utf-8')]
    #return [body.encode('utf-8')]
    return 'hi'

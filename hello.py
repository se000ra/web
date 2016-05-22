#test app
from cgi import parse_qs

#def wsgi_app(env,resp):
def app(env,start_response):
    query = parse_qs(env['QUERY_STRING'], keep_blank_values=1)
    print query
    res = [i+'\r\n' for i in query]
    res = ''.join(res)

    status = '200 OK'
    headers = [('Content-Type','text/plain')]
    start_response(status, headers)
    # return[body]
    return[res]

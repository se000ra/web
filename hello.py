#test app
from cgi import parse_qs

#def wsgi_app(env,resp):
# just test of atomic-packge
def app(env,start_response):
    query = parse_qs(env['QUERY_STRING'], keep_blank_values=1)
    res = [k+v+'\r\n' for  in query]
    res = ''.join(res)
    body = []
    for key, values in query.items():
        for item in values:
            body.append(key + "=" + item + "\r\n")

    status = '200 OK'
    headers = [('Content-Type','text/plain')]
    start_response(status, headers)
    return[body]
    # return[res]

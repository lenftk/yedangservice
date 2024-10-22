from flask import Flask, request, make_response

app = Flask(__name__)

visit_count = 0

@app.route('/')
def index():
    global visit_count
    user_visited = request.cookies.get('visited')

    if not user_visited:
        visit_count += 1 
        resp = make_response(f"Total Visitors: {visit_count}")
        resp.set_cookie('visited', 'true', max_age=60*60*24*30) 
        return resp
    else:
        return f"Total Visitors: {visit_count}" 

if __name__ == '__main__':
    app.run(debug=True, port=5134)

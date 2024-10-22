from flask import Flask, request, make_response

app = Flask(__name__)

# 조회수 저장
visit_count = 0

@app.route('/')
def index():
    global visit_count
    
    # Ping 서비스의 User-Agent를 필터링하여 카운트하지 않음
    user_agent = request.headers.get('User-Agent')
    if 'UptimeRobot' in user_agent or 'Freshping' in user_agent:
        return f"Monitoring request - Visitors: {visit_count}"

    # 사용자의 방문 여부를 쿠키로 확인
    user_visited = request.cookies.get('visited')

    if not user_visited:  # 쿠키가 없으면 방문한 적 없는 사용자
        visit_count += 1  # 조회수 증가
        resp = make_response(f"Total Visitors: {visit_count}")
        resp.set_cookie('visited', 'true', max_age=60*60*24*7)  # 쿠키 설정 (24시간 유지)
        return resp
    else:
        return f"Total Visitors: {visit_count}"  # 이미 방문한 사용자면 조회수 증가 안함

if __name__ == '__main__':
    app.run(debug=True)

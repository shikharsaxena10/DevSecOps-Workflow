from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def show_ip():
    ip = request.remote_addr
    reversed_ip = '.'.join(ip.split('.')[::-1])
    return render_template('index.html', ip=ip, rev_ip=reversed_ip)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
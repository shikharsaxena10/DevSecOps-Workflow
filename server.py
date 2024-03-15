from flask import Flask, request
 
app = Flask(__name__)
 
@app.route('/')
def show_ip():
    ip = request.remote_addr
    reversed_ip = '.'.join(ip.split('.')[::-1])
    original = f"The original ip is: {ip}\n"
    reversed = f"\nThe reversed ip is: {reversed_ip}"
    final = original + reversed
    return final

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
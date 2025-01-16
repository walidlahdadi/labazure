from flask import Flask, request, jsonify
import math

app = Flask(__name__)

def numerical_integration(lower, upper, N):
    dx = (upper - lower) / N
    total_area = 0.0
    for i in range(N):
        x = lower + i * dx
        height = abs(math.sin(x))
        area = height * dx
        total_area += area
    return total_area

@app.route('/integral/<float:lower>/<float:upper>', methods=['GET'])
def compute_integral(lower, upper):
    N_values = [10, 100, 1000, 10000, 100000, 1000000]
    results = {}
    for N in N_values:
        results[N] = numerical_integration(lower, upper, N)
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
from flask import Flask, jsonify
from subprocess import Popen, PIPE
import os

app = Flask(__name__)

@app.route('/run-tests', methods=['GET'])
def run_tests():
    process = Popen(['python', '-m', 'teste.run_all_tests'], stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()

    results = stdout.decode('utf-8').split('\n')
    if stderr:
        results.append(stderr.decode('utf-8'))

    return jsonify(results=results)

if __name__ == "__main__":
    app.run(debug=True)

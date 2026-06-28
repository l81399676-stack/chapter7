#!/usr/bin/env python3
"""
Flask API Module
A simple Flask API class for handling HTTP requests
"""

from flask import Flask, jsonify, request

class FlaskAPI:
    """A simple Flask API class"""
    
    def __init__(self, app_name="FlaskAPI"):
        """
        Initialize the Flask API
        
        Args:
            app_name (str): The name of the Flask application
        """
        self.app = Flask(app_name)
        self._register_routes()
    
    def _register_routes(self):
        """Register all API routes"""
        
        @self.app.route('/api/hello', methods=['GET'])
        def hello():
            """Hello endpoint"""
            return jsonify({"message": "Hello from Flask API"})
        
        @self.app.route('/api/status', methods=['GET'])
        def status():
            """Status endpoint"""
            return jsonify({"status": "API is running"}), 200
        
        @self.app.route('/api/echo', methods=['POST'])
        def echo():
            """Echo endpoint - returns the data sent"""
            data = request.get_json()
            return jsonify({"echo": data}), 200
    
    def run(self, host="127.0.0.1", port=5000, debug=False):
        """
        Run the Flask application
        
        Args:
            host (str): The host to bind to
            port (int): The port to bind to
            debug (bool): Whether to run in debug mode
        """
        self.app.run(host=host, port=port, debug=debug)


if __name__ == "__main__":
    api = FlaskAPI("MyAPI")
    api.run(debug=True)

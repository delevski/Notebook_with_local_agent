"""
Or Delbsky Representative Agent Server
סרבר שמפעיל את הסוכן הייצוגי של אור דלבסקי עם REST API endpoint
"""

from flask import Flask, request, jsonify, send_from_directory
from google import genai
from google.genai import types
import os
import yaml
from dotenv import load_dotenv
from flask_swagger_ui import get_swaggerui_blueprint

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Swagger UI Configuration
SWAGGER_URL = '/docs'
API_URL = '/spec'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Or Delbsky Representative Agent"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/spec')
def spec():
    return send_from_directory('.', 'openapi.yaml')

# Load agent configuration
def load_agent_config():
    """טוען את קובץ ההגדרות של הסוכן"""
    with open('agent_config.yaml', 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

# Initialize the Gemini client
def init_client():
    """מאתחל את ה-client של Gemini"""
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        raise ValueError("GOOGLE_API_KEY environment variable is required")
    
    client = genai.Client(api_key=api_key)
    return client

# Global variables
config = load_agent_config()
client = init_client()

# Load resources (PDF files)
def load_resources():
    """טוען את משאבי ה-PDF לסוכן"""
    resources = []
    for resource in config.get('resources', []):
        if resource['type'] == 'file':
            file_path = resource['path']
            if os.path.exists(file_path):
                with open(file_path, 'rb') as f:
                    file_content = f.read()
                resources.append({
                    'path': file_path,
                    'content': file_content,
                    'description': resource.get('description', '')
                })
    return resources

@app.route('/health', methods=['GET'])
def health_check():
    """בדיקת תקינות השרת"""
    return jsonify({
        'status': 'healthy',
        'agent': config.get('display_name'),
        'version': '1.0.0'
    })

@app.route('/agent/chat', methods=['POST'])
def chat_with_agent():
    """
    Endpoint לשיחה עם הסוכן
    
    Body:
    {
        "message": "השאלה או ההודעה למגייס",
        "context": "קונטקסט נוסף (אופציונלי)"
    }
    
    Response:
    {
        "response": "תשובת הסוכן",
        "status": "success"
    }
    """
    try:
        data = request.get_json()
        
        if not data or 'message' not in data:
            return jsonify({
                'error': 'Missing required field: message',
                'status': 'error'
            }), 400
        
        user_message = data['message']
        context = data.get('context', '')
        
        # Build the prompt with context
        full_prompt = user_message
        if context:
            full_prompt = f"קונטקסט: {context}\n\nשאלה: {user_message}"
        
        # Create chat session with system instruction
        system_instruction = config.get('system_instruction', '')
        
        # Note: For production, you'd want to upload PDFs to Gemini Files API
        # and reference them in the context. For now, we'll work with text-based context.
        
        response = client.models.generate_content(
            model=config['model']['name'],
            contents=full_prompt,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=config['model'].get('temperature', 0.7),
                top_p=config['model'].get('top_p', 0.95),
                max_output_tokens=config['model'].get('max_output_tokens', 2048),
            )
        )
        
        return jsonify({
            'response': response.text,
            'status': 'success'
        })
        
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500

@app.route('/agent/info', methods=['GET'])
def agent_info():
    """מחזיר מידע על הסוכן"""
    return jsonify({
        'name': config.get('name'),
        'display_name': config.get('display_name'),
        'description': config.get('description'),
        'model': config['model']['name'],
        'resources': [r['description'] for r in config.get('resources', [])]
    })

if __name__ == '__main__':
    print(f"🚀 Starting {config.get('display_name')}...")
    print(f"📋 Resources loaded: {len(config.get('resources', []))}")
    print(f"🤖 Model: {config['model']['name']}")
    print(f"\n✅ Server is running on http://localhost:5000")
    print(f"\nEndpoints:")
    print(f"  - POST /agent/chat - שיחה עם הסוכן")
    print(f"  - GET  /docs       - תיעוד API (Swagger UI)")
    print(f"  - GET  /agent/info - מידע על הסוכן")
    print(f"  - GET  /health     - בדיקת תקינות")
    
    app.run(host='0.0.0.0', port=5000, debug=True)

"""
Test client for Or Delbsky Representative Agent
סקריפט לבדיקת הסוכן
"""

import requests
import json

# Server URL
BASE_URL = "http://localhost:5000"

def test_health():
    """בדיקת תקינות השרת"""
    print("🔍 Testing health endpoint...")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2, ensure_ascii=False)}\n")

def test_agent_info():
    """בדיקת מידע על הסוכן"""
    print("📋 Testing agent info endpoint...")
    response = requests.get(f"{BASE_URL}/agent/info")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2, ensure_ascii=False)}\n")

def test_chat(message, context=""):
    """בדיקת שיחה עם הסוכן"""
    print(f"💬 Testing chat endpoint...")
    print(f"Message: {message}")
    if context:
        print(f"Context: {context}")
    
    response = requests.post(
        f"{BASE_URL}/agent/chat",
        json={
            "message": message,
            "context": context
        }
    )
    
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print(f"\n🤖 Agent Response:\n{data['response']}\n")
    else:
        print(f"Error: {response.json()}\n")

def main():
    """הרצת כל הבדיקות"""
    print("=" * 60)
    print("Or Delbsky Representative Agent - Test Suite")
    print("=" * 60 + "\n")
    
    try:
        # Test 1: Health check
        test_health()
        
        # Test 2: Agent info
        test_agent_info()
        
        # Test 3: Chat examples
        print("=" * 60)
        print("Chat Examples")
        print("=" * 60 + "\n")
        
        # Example 1
        test_chat(
            message="ספר לי על הניסיון המקצועי של אור",
            context="אנחנו מחפשים מפתח פולסטאק לסטארטאפ"
        )
        
        # Example 2
        test_chat(
            message="מה החוזקות המקצועיות של אור?",
            context="תהליך גיוס למשרת Senior Developer"
        )
        
        # Example 3
        test_chat(
            message="האם אור זמין לעבודה?",
            context=""
        )
        
        print("=" * 60)
        print("✅ All tests completed!")
        print("=" * 60)
        
    except requests.exceptions.ConnectionError:
        print("❌ Error: Could not connect to server.")
        print("Make sure the server is running: python agent_server.py")
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    main()

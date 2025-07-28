from flask import Flask,jsonify,request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os

def get_ip():
    # Get the first IP in X-Forwarded-For, if present; else fallback to remote_addr
    return request.headers.get('X-Forwarded-For', request.remote_addr)


app=Flask(__name__)


limiter = Limiter(
    app,
    key_func=get_ip,  # Use the function above
    storage_uri="redis:https://free-jokes-api.onrender.com",  # Or your Render Redis URL
    default_limits=["100 per hour"]
)

sample_data={"jokes": [
        {
            "id": "J001",
            "setup": "Why do programmers prefer dark mode?",
            "punchline": "Because light attracts bugs!"
        },
        {
            "id": "J002",
            "setup": "What do you call a fake noodle?",
            "punchline": "An impasta!"
        },
        {
            "id": "J003",
            "setup": "I'm reading a book about anti-gravity.",
            "punchline": "It's impossible to put down!"
        },
        {
            "id": "J004",
            "setup": None,
            "punchline": "My computer's only fear is a power outage. It makes it unstable."
        },
        {
            "id": "J005",
            "setup": "Knock, knock. \nWho's there?",
            "punchline": "Lettuce. \nLettuce who? \nLettuce in, it's cold out here!"
        },
        {
            "id": "J006",
            "setup": "Why don't scientists trust atoms?",
            "punchline": "Because they make up everything!"
        },
        {
            "id": "J007",
            "setup": "What do you call a boomerang that won't come back?",
            "punchline": "A stick."
        },
        {
            "id": "J008",
            "setup": None,
            "punchline": "Why do they call it 'beauty sleep' when you wake up looking like a drowned rat?"
        },
        {
            "id": "J009",
            "setup": "What has an eye, but cannot see?",
            "punchline": "A needle."
        }
    ]
}

@app.route('/',methods = ["POST","GET"])
@limiter.limit("10 requests per minute")
def sample_get_items():
    if request.method=="GET":
        return jsonify(sample_data)
    elif request.method=="POST":
        data=request.get_json()

        if not data or "punchline" not in data:
            return jsonify({"error": "Missing punchline"}), 400

        
        setup =data.get("setup",None)
        punchline = data["punchline"]

        new_joke = {
            "id" : f"J{len(sample_data['jokes']) + 1:03d}",
            "setup" : setup,
            "punchline" : punchline

        }

        sample_data.get("jokes").append(new_joke)

        return jsonify({"message": "New joke added"}), 201





if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)



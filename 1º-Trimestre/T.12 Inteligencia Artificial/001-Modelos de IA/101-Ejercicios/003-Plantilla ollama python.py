import json
import urllib.request

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen2.5:3b-instruct"

prompt = "Explica qué es PHP."

data = {
    "model": MODEL,
    "prompt": prompt,
    "stream": False # False = a que te responda de una sola vez, despues de ponerse a pensar, mientras que True = a que te responda palabra a palabra
}

req = urllib.request.Request(
    OLLAMA_URL,
    data=json.dumps(data).encode("utf-8"),
    headers={"Content-Type": "application/json"}
)

with urllib.request.urlopen(req) as response:
    result = json.loads(response.read().decode("utf-8"))
    print(result["response"])
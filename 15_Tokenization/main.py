import tiktoken

enc = tiktoken.encoding_for_model("gpt-3.5-turbo")

text = "There is a bright future ahead of you!"
tokens = enc.encode(text)

# Tokens [3947, 374, 264, 10107, 3938, 8469, 315, 499, 0]
print("Tokens", tokens)

decoded = enc.decode([3947, 374, 264, 10107, 3938, 8469, 315, 499, 0])
print("Decoded", decoded)

#pip freeze > requirements.txt  -> To save the dependencies in a file
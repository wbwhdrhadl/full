import tiktoken

ecn = tiktoken.get_encoding("cl100k_base")

tokens = ecn.encode("hello world")
print(len(tokens))
print(tokens)

print(ecn.decode(tokens))
print(ecn.decode_tokens_bytes(tokens))
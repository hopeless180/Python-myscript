import hashlib

def hash_text(plain_text):
    hash_algorithms = [
        "md5",
        "sha1",
        "sha224",
        "sha3_224",
        "sha256",
        "sha3_256",
        "sha384",
        "sha3_384",
        "sha512",
        "sha3_512"
    ]

    results = {}
    
    for algo in hash_algorithms:
        hasher = hashlib.new(algo)
        hasher.update(plain_text.encode())
        hash_value = hasher.hexdigest()
        results[algo] = hash_value

    result = "\n".join([f"{algo}: {results[algo]}" for algo in hash_algorithms])

    return result

# 例子用法
input_text = input("请输入明文: ")
hashed_text = hash_text(input_text)
print(hashed_text)

## 答案是无法通过逆向工程返回原文

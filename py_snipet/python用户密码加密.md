# 存储用户密码时加密的方法
> 密码安全观点：不要存储明文密码，而是存储密码的哈希值。

## 使用[bcrypt](https://github.com/pyca/bcrypt) python包

```python
import bcrypt
import hmac

# Calculating a hash
password = b"correct horse battery staple"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
# Validating a hash (don't use ==)
if (hmac.compare_digest(bcrypt.hashpw(password, hashed), hashed)):
    # Login successful
```

## 使用passlib

```python
from psslib.hash import bcrypt


# Calculating a hash
hash = bcrypt.encrypt(userPassword, rounds=12)

# Validating a hash
if bcrypt.verify(userPassword, hash):
    # Login succesful
```

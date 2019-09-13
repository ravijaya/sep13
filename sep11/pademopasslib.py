from passlib.context import CryptContext

hashes = ["pbkdf2_sha256", "md5_crypt", "des_crypt"]
deprecated = ["md5_crypt", "des_crypt"]
ctx = CryptContext(schemes=hashes, deprecated=deprecated)

serialized = ctx.to_string()
new_ctx = CryptContext.from_string(serialized)

res = ctx.hash("good password")
print(ctx.verify_and_update("good password", res))

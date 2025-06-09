from passlib.context import CryptContext
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_hashed_password(password: str) -> str:
    return password_context.hash(password)

def verify_password(password: str, hashed_pass: str) -> bool:
    return password_context.verify(password, hashed_pass)

## Testing the password hashing and verification
if __name__ == "__main__":
    # Example usage
    password = "Th1sIsASecure#9145!"
    hashedPass = get_hashed_password(password)
    print(f"The Hashed Password is: {hashedPass}")

    is_verified = verify_password(password, hashedPass)
    print(f"Password Verified: {is_verified}")

    # Testing with an incorrect password
    is_verified_wrong = verify_password("wrong_password", hashedPass)
    print(f"Wrong Password Verified: {is_verified_wrong}")
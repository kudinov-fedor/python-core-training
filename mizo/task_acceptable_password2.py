def is_acceptable_password(password: str) -> bool:
    cond1 = len(password) > 6
    cond2 = any(map(str.isdigit,
                    password))
    cond3 = any(map(str.isalpha, password))
    return all([cond1, cond2,
                cond3])

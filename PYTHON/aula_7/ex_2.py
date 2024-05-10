def eh_palindromo(entrada: str) -> bool:
    if entrada.lower() == entrada[::-1].lower:
        return True
    else:
         return False
print(eh_palindromo('madam'))
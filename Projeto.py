email = input("Digite seu email: ")

if (
    "@" in email
    and "." in email
    and email.count("@") == 1
    and not email.startswith("@")
    and not email.startswith(".")
):
    print ("\n ✅ Email válido!")
else:
    print ("\n ❌ Email inválido!")
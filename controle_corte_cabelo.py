from datetime import datetime, timedelta

# Solicita a data do último corte
data_str = input("Digite a data do último corte de cabelo (formato: DD/MM/AAAA): ")

# Converte a string para objeto de data
data_corte = datetime.strptime(data_str, "%d/%m/%Y")

# Soma 15 dias
proximo_corte = data_corte + timedelta(days=15)

# Exibe a próxima data
print(f"Você poderá cortar o cabelo novamente em: {proximo_corte.strftime('%d/%m/%Y')}")

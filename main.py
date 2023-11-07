def text_to_binary_with_custom_chars(text):
    binary_text = ' '.join(format(ord(char), '08b') for char in text)
    binary_text = binary_text.replace('0', 'ř').replace('1', 'ů')
    return binary_text

def binary_with_custom_chars_to_text(binary):
    binary = binary.replace('ř', '0').replace('ů', '1')
    binary_values = binary.split(' ')
    text = ''.join(chr(int(char, 2)) for char in binary_values)
    return text

rezim = input("Chcete přeložit text do binární soustavy (A) nebo binární řetězec zpět na text (B)? Vyberte A nebo B: ")

if rezim.upper() == 'A':
    print("Zadejte text pro překlad do asociálního písma:")
    user_text=input()
    binary_representation = text_to_binary_with_custom_chars(user_text)
    print(f"Text v asociálním písmu: {binary_representation}")
elif rezim.upper() == 'B':
    print("Zadej text v asociálním písmu pro překlad na text")
    user_text=input()
    original_text = binary_with_custom_chars_to_text(user_text)
    print(f"Překlad z asociálního písma na text: {original_text}")
else:
    print("Chyba mezi klávesnicí a židlí.")

input("Stiskněte Enter pro ukončení programu")
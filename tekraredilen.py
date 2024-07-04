print("S --> ", end="")
S = input().split("|")
print("X --> ", end="")
X = input().split("|")

üretilen = set()
tekrar = set()
for i in S:
    kelimeler = [i]

    while any('X' in kelime for kelime in kelimeler):
        yeni_kelimeler = [
            kelime.replace('X', X_kelime, 1) for kelime in kelimeler for X_kelime in X
        ]

        kelimeler = yeni_kelimeler  # kelimeler listesi güncelleniyor

    üretilen.update(kelime for kelime in kelimeler if kelime not in üretilen)

tekrar.update(kelime for kelime in kelimeler if kelime in üretilen)

print("\nÜretilen Kelimeler:")
print(", ".join(sorted(üretilen)))
print("\nTekrar Eden Kelimeler:")
print(", ".join(sorted(tekrar)))




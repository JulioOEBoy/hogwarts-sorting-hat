import time

grifinoria = 0
corvinal = 0
lufa_lufa = 0
sonserina = 0

print("✨ Bem-vindo ao Chapéu Seletor de Hogwarts! ✨")
time.sleep(1)
print("Responda às perguntas abaixo e descubra sua casa...")
time.sleep(2)

print("\n1) Você prefere:")
print("  1) Amanhecer 🌅")
print("  2) Entardecer 🌇")
p1 = int(input("Sua resposta: "))
if p1 == 1:
    grifinoria += 1
    corvinal += 1
elif p1 == 2:
    lufa_lufa += 1
    sonserina += 1

print("\n2) Quando eu morrer, quero ser lembrado como:")
print("  1) O Bondoso 💛")
print("  2) O Grande 💪")
print("  3) O Sábio 🧠")
print("  4) O Corajoso 🔥")
p2 = int(input("Sua resposta: "))
if p2 == 1:
    lufa_lufa += 2
elif p2 == 2:
    sonserina += 2
elif p2 == 3:
    corvinal += 2
elif p2 == 4:
    grifinoria += 2

print("\n3) Qual instrumento mais agrada seu ouvido?")
print("  1) Violino 🎻")
print("  2) Trompete 🎺")
print("  3) Piano 🎹")
print("  4) Tambor 🥁")
p3 = int(input("Sua resposta: "))
if p3 == 1:
    sonserina += 4
elif p3 == 2:
    lufa_lufa += 4
elif p3 == 3:
    corvinal += 4
elif p3 == 4:
    grifinoria += 4

print("\n4) Qual dessas qualidades você mais valoriza?")
print("  1) Coragem")
print("  2) Inteligência")
print("  3) Justiça")
print("  4) Ambição")
p4 = int(input("Sua resposta: "))
if p4 == 1:
    grifinoria += 3
elif p4 == 2:
    corvinal += 3
elif p4 == 3:
    lufa_lufa += 3
elif p4 == 4:
    sonserina += 3

print("\n5) Com quem você prefere fazer amizade?")
print("  1) Os corajosos e destemidos")
print("  2) Os estudiosos e criativos")
print("  3) Os justos e trabalhadores")
print("  4) Os influentes e estratégicos")
p5 = int(input("Sua resposta: "))
if p5 == 1:
    grifinoria += 2
elif p5 == 2:
    corvinal += 2
elif p5 == 3:
    lufa_lufa += 2
elif p5 == 4:
    sonserina += 2

time.sleep(2)
print("\n🔮 Calculando seu destino mágico...")
time.sleep(2)

print(f"\n🦁 Grifinória: {grifinoria}")
print(f"🦅 Corvinal: {corvinal}")
print(f"🦡 Lufa-Lufa: {lufa_lufa}")
print(f"🐍 Sonserina: {sonserina}")

casas = {
    "Grifinória": grifinoria,
    "Corvinal": corvinal,
    "Lufa-Lufa": lufa_lufa,
    "Sonserina": sonserina
}

max_pontuacao = max(casas.values())
finalistas = [casa for casa, pontos in casas.items() if pontos == max_pontuacao]

if len(finalistas) == 1:
    casa_escolhida = finalistas[0]
else:
    print("\n🧠 O Chapéu Seletor está indeciso entre:", ", ".join(finalistas))
    print("Pergunta de desempate!")
    print("Qual dessas palavras te atrai mais?")
    print("  1) Liderança")
    print("  2) Conhecimento")
    print("  3) Lealdade")
    print("  4) Poder")
    desempate = int(input("Sua resposta: "))
    if desempate == 1 and "Grifinória" in finalistas:
        casa_escolhida = "Grifinória"
    elif desempate == 2 and "Corvinal" in finalistas:
        casa_escolhida = "Corvinal"
    elif desempate == 3 and "Lufa-Lufa" in finalistas:
        casa_escolhida = "Lufa-Lufa"
    elif desempate == 4 and "Sonserina" in finalistas:
        casa_escolhida = "Sonserina"
    else:
        casa_escolhida = finalistas[0]

print(f"\n🎉 O Chapéu Seletor decidiu... {casa_escolhida.upper()}!")
print("🏰 Que sua jornada em Hogwarts seja mágica!")

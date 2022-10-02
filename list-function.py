def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism] = int(baho)
    return baholar

talabalar = ['ali', 'vali', 'omon', 'nosir', 'akmal']
marks = bahola(talabalar[:])
print(marks)
print(talabalar)
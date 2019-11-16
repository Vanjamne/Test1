f = open(f"C:\\Users\\Vanja\\Desktop\\Programiranje\\Test1\\igrice.txt", "a+",newline='')
Genre = ('SciFi', 'Adventure', 'FPS', 'Action', 'Racing')
for i in range(5):
    q1 = input("Unesite naziv igrice:")
    if len(q1) > 2 and len(q1) < 50:
        pass
    else:
        print("Nepravilan unos! Naziv mora biti veci od 2 a manji od 50 slova!")
        break
    q2 = float(input("Unesite ocjenu igrice:"))
    if q2 < 11.0:
        pass
    else:
        print("Ocjena mora biti od 1 do 10!")
        break
    q3 = input("Unesite godinu izlaska igrice:")
    if int(q3) > 1950 and int(q3) < 2019:
        pass
    else:
        print("Godina mora biti od 1950-te do danas!")
        break
    q4 = input("Koliko zanrova ima igrica?:")
    if int(q4) > 5:
        print("Igrica moze sadrzati maksimalno 3 zanra!")
        break
    else:
        pass
    q5 = input("Unesite neki od zanrova igrice('SciFi', 'Adventure', 'FPS', 'Action', 'Racing'):")
    if q5 in Genre:
        pass
    else:
        print("Ne mozete unijeti broj, ili vise od tri zanra!")
        break
    f.write(f"{q1};{q2};{q3};{q5} \r\n")
f.close()

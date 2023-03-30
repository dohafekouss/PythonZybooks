e_string = "e|-"
B_string = "B|-"
G_string = "G|-"
D_string = "D|-"
A_string = "A|-"
E_string = "E|-"
num_chords = int(input())

for i in range(num_chords):
    user_chord = input()
    if user_chord == "G":
        e_string += "3-"
        B_string += "0-"
        G_string += "0-"
        D_string += "0-"
        A_string += "2-"
        E_string += "3-"
    elif user_chord == "C":
        e_string += "0-"
        B_string += "1-"
        G_string += "0-"
        D_string += "2-"
        A_string += "3-"
        E_string += "--"
    elif user_chord == "D":
        e_string += "2-"
        B_string += "3-"
        G_string += "2-"
        D_string += "0-"
        A_string += "--"
        E_string += "--"
print(e_string)
print(B_string)
print(G_string)
print(D_string)
print(A_string)
print(E_string)
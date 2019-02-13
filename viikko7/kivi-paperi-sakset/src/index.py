from pelimuoto import Pelimuoto

def main():
    get_pelimuoto = {'a': Pelimuoto.luo_kaksinpeli(), 
                     'b': Pelimuoto.luo_helppo_tekoalypeli(), 
                     'c': Pelimuoto.luo_vaikea_tekooalypeli()}
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()
        if vastaus in get_pelimuoto:
            pelimuoto = get_pelimuoto[vastaus]
        else:
            break
        print("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s")
        pelimuoto.pelaa()

if __name__ == "__main__":
    print("lol")
    main()

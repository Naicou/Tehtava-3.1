import random
import time

class Peikko:
    """Luokka, joka kuvaa Peikon.

    :ivar nimi: peikon nimi, arvotaan
    :type nimi: str
    :ivar rohkeus: peikon rohkeus, arvotaan
    :type rohkeus: int
    :ivar katseen_voima: peikon katseen voimakkuus, arvotaan
    :type katseen_voima: int

    Julkiset metodit
        arvo_hurraus()
    """

    NIMITAVUT = ("Ur", "Gar", "Grah", "Gur", "Kan", "moii", "Bar", "Bazh", "Ragh", "Rudz")
    RIEMUTAVUT = ("Agh", "Ugh", "Ourgh", "Drar", "Brar", "Dza", "Gra", "Gur", "Rah", "Urgh", "Ra")
    TYYPIT = ("Peikko", "Vuorenpeikko", "Luolapeikko")

    def __init__(self):
        """Konstruktori."""
        self.nimi = self._arvo_sanat(self.NIMITAVUT, 3, "-")
        self.rohkeus = random.randint(4, 8)
        self.katseen_voima = random.randint(2, 4)
        self.tyyppi = random.choice(self.TYYPIT)

    def _arvo_sanat(self, tavut, n, erotin, p=0.5):
        """Muodostaa satunnaisen tekstin annetuista tavuista.

        :param tavut: ne tavut, joita palautettava teksti voi sisältää
        :type tavut: Union[list[str], tuple[str]]
        :param n: mukaan poimittavien tavujen maksimimäärä
        :type n: int
        :param erotin: tavujen väliin satunnaisesti laitettava merkki
        :type erotin: str
        :param p: todennäköisyys lisätä erotin tavujen väliin (oletus 0.5)
        :type p: float
        :return: satunnainen teksti
        :rtype: str
        """
        osat = random.choices(tavut, k=random.randint(2, n))
        sanat = osat[0]
        for osa in osat[1:]:
            if random.random() < p:
                sanat += erotin + osa
            else:
                sanat += osa.lower()
        return sanat

    def arvo_hurraus(self):
        """Palauttaa satunnaisen hurraushuudahduksen.

        :return: hurraava huudahdus
        :rtype: str
        """
        return self._arvo_sanat(self.RIEMUTAVUT, 8, " ", 0.7)


### Kirjoita luokka Sankari tähän.
class Sankari(Peikko):
    """Luokka, joka kuvaa sankaria.

    :ivar nimi: sankarin nimi, annetaan parametrina
    :type nimi: str
    :ivar rohkeus: sankarin rohkeus, arvotaan
    :type rohkeus: int
    :ivar katseen_voima: sankarin katseen voimakkuus, arvotaan
    :type katseen_voima: int
    :ivar hurraukset: lista mahdollisista hurraushuudoista
    :type hurraukset: list[str]
    """
    
    HURRAUKSET = ("Eläköön!", "Hurraa!", "Voittoon!", "Sankarillisesti eteenpäin!", "Jee!")

    def __init__(self, nimi):
        """Konstruktori.

        :param nimi: sankarin nimi
        :type nimi: str
        """
        super().__init__()  # Kutsutaan yliluokan konstruktoria
        self.nimi = nimi
        self.hurraukset = self.HURRAUKSET

    def arvo_hurraus(self):
        """Palauttaa satunnaisen hurraushuudahduksen.

        :return: hurraava huudahdus
        :rtype: str
        """
        return random.choice(self.hurraukset)

class Olento:
    """Luokka, joka toimii kantaluokkana Peikko- ja Sankari-luokille."""

    def __init__(self, nimi, rohkeus, katseen_voima):
        """Konstruktori.

        :param nimi: olennon nimi
        :type nimi: str
        :param rohkeus: olennon rohkeus
        :type rohkeus: int
        :param katseen_voima: olennon katseen voima
        :type katseen_voima: int
        """
        self.nimi = nimi
        self.rohkeus = rohkeus
        self.katseen_voima = katseen_voima

    def arvo_hurraus(self):
        """Palauttaa satunnaisen hurraushuudahduksen.

        :return: hurraava huudahdus
        :rtype: str
        """
        raise NotImplementedError("Metodia 'arvo_hurraus' ei ole toteutettu.")

class Vuorenpeikko:
    """Luokka, joka kuvaa Vuorenpeikkoa."""

    NIMITAVUT = ("moi", "moi", "moi", "moi", "moi", "moi", "moi", "moi", "moi", "moi", "moi")

    def __init__(self):
        """Konstruktori."""
        self.nimi = self._arvo_sanat(self.NIMITAVUT, 2, "-")
        self.rohkeus = random.randint(6, 10)
        self.katseen_voima = random.randint(3, 6)

    def _arvo_sanat(self, tavut, n, erotin, p=0.5):
        """Muodostaa satunnaisen tekstin annetuista tavuista.

        :param tavut: ne tavut, joita palautettava teksti voi sisältää
        :type tavut: Union[list[str], tuple[str]]
        :param n: mukaan poimittavien tavujen maksimimäärä
        :type n: int
        :param erotin: tavujen väliin satunnaisesti laitettava merkki
        :type erotin: str
        :param p: todennäköisyys lisätä erotin tavujen väliin (oletus 0.5)
        :type p: float
        :return: satunnainen teksti
        :rtype: str
        """
        osat = random.choices(tavut, k=random.randint(2, n))
        sanat = osat[0]
        for osa in osat[1:]:
            if random.random() < p:
                sanat += erotin + osa
            else:
                sanat += osa.lower()
        return sanat

    def arvo_hurraus(self):
        """Palauttaa satunnaisen hurraushuudahduksen.

        :return: hurraava huudahdus
        :rtype: str
        """
        return "Vuorenpeikko huutaa: " + self._arvo_sanat(("Gruu!", "Graah!", "Vuori-voittoon!", "Voitokkaasti eteenpäin!"), 1, " ")

class Luolapeikko:
     """Luokka, joka kuvaa Vuorenpeikkoa."""

     NIMITAVUT = ("moi", "moi", "moi", "moi", "moi", "moi", "moi", "moi", "moi", "moi", "moi")

def __init__(self):
        """Konstruktori."""
        self.nimi = self._arvo_sanat(self.NIMITAVUT, 2, "-")
        self.rohkeus = random.randint(6, 10)
        self.katseen_voima = random.randint(3, 6)

def _arvo_sanat(self, tavut, n, erotin, p=0.5):
        """Muodostaa satunnaisen tekstin annetuista tavuista.

        :param tavut: ne tavut, joita palautettava teksti voi sisältää
        :type tavut: Union[list[str], tuple[str]]
        :param n: mukaan poimittavien tavujen maksimimäärä
        :type n: int
        :param erotin: tavujen väliin satunnaisesti laitettava merkki
        :type erotin: str
        :param p: todennäköisyys lisätä erotin tavujen väliin (oletus 0.5)
        :type p: float
        :return: satunnainen teksti
        :rtype: str
        """
        osat = random.choices(tavut, k=random.randint(2, n))
        sanat = osat[0]
        for osa in osat[1:]:
            if random.random() < p:
                sanat += erotin + osa
            else:
                sanat += osa.lower()
        return sanat

def arvo_hurraus(self):
        """Palauttaa satunnaisen hurraushuudahduksen.

        :return: hurraava huudahdus
        :rtype: str
        """
        return "Vuorenpeikko huutaa: " + self._arvo_sanat(("Gruu!", "Graah!", "Vuori-voittoon!", "Voitokkaasti eteenpäin!"), 1, " ")




def hurraa(olio):
    """Tulostaa satunnaisen hurrauksen annetulle oliolle.

    :param olio: hurraava olio
    """
    print(f'{olio.nimi}: "{olio.arvo_hurraus()}!"')


def tulosta_rapaytys(rapayttaja):
    """Tulostaa sopivan tekstin räpäyttävälle oliolle.

    :param rapayttaja: silmiään räpäyttävä olio
    """
    if rapayttaja:
        if rapayttaja.rohkeus > 0:
            print(f"ja {rapayttaja.nimi} räpäyttää!")
        else:
            print(f"ja {rapayttaja.nimi} karkaa!")
    else:
        print("eikä kummankaan silmä rävähdä!")


def tuijota(olio1, olio2):
    """Asettaa annetut oliot taistelemaan keskenään yhden kierroksen.

    :param vasen: ensimmäinen taisteleva olio
    :type vasen: Union[Sankari, Peikko]
    :param oikea: toinen taisteleva olio
    :type oikea: Union[Sankari, Peikko]
    :return: hävinnyt olio
    :rtype: Union[Sankari, Peikko]
    """
    print("He tuijottavat toisiaan...", end='')
    time.sleep(1)
    # Arvotaan kummankin olion tämän kierroksen vahvuus.
    katse1 = random.randint(0, olio1.katseen_voima)
    katse2 = random.randint(0, olio2.katseen_voima)
    rapayttaja = None

    # heikomman vahvuuden saanut olio menettää rohkeutta
    if katse1 > katse2:
        rapayttaja = olio2
        rapayttaja.rohkeus -= katse1
    elif katse1 < katse2:
        rapayttaja = olio1
        rapayttaja.rohkeus -= katse2
    return rapayttaja


def taistele(vasen, oikea):
    """Asettaa annetut oliot taistelemaan keskenään, kunnes toinen voittaa.

    :param vasen: ensimmäinen taisteleva olio
    :type vasen: Union[Sankari, Peikko]
    :param oikea: toinen taisteleva olio
    :type oikea: Union[Sankari, Peikko]
    :return: voittanut olio
    :rtype: Union[Sankari, Peikko]
    """
    while vasen.rohkeus > 0 and oikea.rohkeus > 0:
        haviaja = tuijota(vasen, oikea)
        tulosta_rapaytys(haviaja)
        time.sleep(0.5)
    if vasen.rohkeus > 0:
        return vasen
    else:
        return oikea




sankari = Sankari(input("Mikä on sankarimme nimi? "))
pelastetut = 0
# Käydään tuijotuskisoja peikkoja vastaan, kunnes sankari karkaa
while sankari.rohkeus > 0:
    # Tulostetaan kierroksen alkutiedot.
    sankarin_tiedot = sankari.nimi + " [" + str(sankari.rohkeus) + "]"
    print(f"Sankarimme {sankarin_tiedot} kävelee kohti seikkailua.")
    time.sleep(0.7)

    # Tulostetaan vastaan tulevan peikon tiedot.
    peikko = Peikko()   
    peikko.tyyppi = random.choice(Peikko.TYYPIT) 
    tyyppi = Peikko.TYYPIT
    peikon_tiedot = peikko.tyyppi +' '+  peikko.nimi + " [" + str(peikko.rohkeus) + "]"
    print(f"Vastaan tulee hurja {peikon_tiedot}!")
    time.sleep(1)

    # Käydään tuijotuskisa peikkoa vastaan.
    voittaja = taistele(peikko, sankari)
    hurraa(voittaja)
    print()
    time.sleep(1.5)

time.sleep(1.5)
print(f"{sankari.nimi} herää sängystään hikisenä - onneksi se oli vain unta!")





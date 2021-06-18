from warp import Warp


class Localisation:

    def __init__(self, warp, map, name):
        self.exit = {}
        self.warp = warp
        self.map = map
        self.name = name

    def set_exit(self, direction, voisin: object) -> None:
        self.exit[direction] = voisin

    def get_exit(self, option) -> None:
        return self.exit[option]


class Localisations:

    def __init__(self, game):
        self.game = game
        self.create()

    def create(self):
        # create all warps with good tuple of coordinate
        warp_route_2 = {'North': (10, 5)}
        warp_foret_maudite = {'South': (16, 37), 'North': (15, 6)}
        warp_VILLE1 = {'North': (20, 10)}
        warp_VILLE2 = {'North': (20, 10), 'South': (20, 6), 'West': (6, 18), 'East': (33, 22)}
        warp_ville3 = {'East': (51, 15)}
        warp_VILLE4 = {"West": (6, 16)}
        warp_VILLE5 = {}
        warp_route1 = {}
        warp_route_2 = {'North': (10, 5), 'East': (43, 13)}
        warp_route3 = {'South': (72, 12), 'West': (4, 10)}
        warp_desert = {"West": (7, 9), 'East': (30, 136)}

        grotte2_warp = {"North", (4, 1), "South", (8, 30)}
        grotte3_warp = {"North", (4, 1), "South", (27, 16)}








        # create all the different localisation and set the relation between another
        # VILLE1 = Localisation(warp_VILLE1, self.game.maps['Ville1'], "Bourg-en-vol")
        # VILLE2 = Localisation("Ville2")
        # VILLE3 = Localisation("Ville3")
        # VILLE4 = Localisation("Ville4")
        # VILLE5 = Localisation("Ville5")

        # ROUTE1 = Localisation("Route1")
        ROUTE2 = Localisation(warp_route_2, self.game.maps['Route2'], "route2")
        # ROUTE3 = Localisation("Route3")
        # ROUTE4 = Localisation("Route4")
        # ROUTE5 = Localisation("Route5")

        FORET_MAUDITE = Localisation(warp_foret_maudite, self.game.maps['ForetMaudite'], "foret_maudite")
        # DESERT_DELASSANT = Localisation("Desert Delassant")
        # MANOIR = Localisation("Manoir")
        # GROTTE = Localisation("Grotte Hivernale")

        # VILLE1.set_exit('North', ROUTE1)

        # ROUTE1.set_exit('South', VILLE1)
        # ROUTE1.set_exit('North', VILLE2)

        # VILLE2.set_exit('South', ROUTE1)
        # VILLE2.set_exit('West', ROUTE2)
        # VILLE2.set_exit('East', DESERT_DELASSANT)
        # VILLE2.set_exit('North', ROUTE5)

        # ROUTE2.set_exit('East', VILLE2)
        ROUTE2.set_exit('North', FORET_MAUDITE)

        FORET_MAUDITE.set_exit('South', ROUTE2)
        # FORET_MAUDITE.set_exit('North', ROUTE3)

        # ROUTE3.set_exit('South', FORET_MAUDITE)
        # ROUTE3.set_exit('West', VILLE3)

        # DESERT_DELASSANT.set_exit('West', VILLE2)
        # DESERT_DELASSANT.set_exit('South', ROUTE4)

        # ROUTE4.set_exit('North', DESERT_DELASSANT)
        # ROUTE4.set_exit('East', VILLE4)

        # ROUTE5.set_exit('South', VILLE2)
        # ROUTE5.set_exit('North', GROTTE)

        # GROTTE.set_exit('South', ROUTE5)
        # GROTTE.set_exit('West', VILLE5)

        # VILLE5.set_exit('South', GROTTE)

        # MANOIR.set_exit('South', FORET_MAUDITE)

        self.game.localisation_list['ForetMaudite'] = FORET_MAUDITE
        self.game.localisation_list['Route2'] = ROUTE2














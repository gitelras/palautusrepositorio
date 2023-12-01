from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or
from query_builder import QueryBuilder


def testeja():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)
    matcher = And(
        HasAtLeast(5, "goals"),
        HasAtLeast(20, "assists"),
        PlaysIn("PHI")
    )

    #matcher = All()
    matcher = Not(HasAtLeast(5, "assists"))
    matcher = HasFewerThan(5, "goals")
    matcher = And(Not(HasAtLeast(2, "goals")),PlaysIn("NYR"))
    matcher = And(
        HasFewerThan(2, "goals"),
        PlaysIn("NYR")
    )
    filtered_with_all = stats.matches(All())
    print(len(filtered_with_all))   

    matcher = Or(
        HasAtLeast(45, "goals"),
        HasAtLeast(70, "assists")
    )
    matcher = And(
        HasAtLeast(70, "points"),
        Or(
            PlaysIn("NYR"),
            PlaysIn("FLA"),
            PlaysIn("BOS")
        )
    )
    for player in stats.matches(matcher):
        print(player)



def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder() #rakentaja jonka sisöllä All() matcher-olio
    matcher = query.build()
    matcher = query.playsIn("NYR").build()

    query2 = query.playsIn("NYR") #rakentaja, jonka sisällä on AND-matcher, jonka sisällä on ALL ja PLAYisIN mathcerit
    query3 = query2.playsIn("KKK") # rakentaja 

    matcher = query.playsIn("NYR").hasAtLeast(5, "goals").hasAtLeast(2, "assists").build()
    matcher = (
        query
        .playsIn("NYR")
        .hasAtLeast(10, "goals")
        .hasFewerThan(20, "goals") 
        .build()
    )
    m1 = (
    query
    .playsIn("PHI")
    .hasAtLeast(10, "assists")
    .hasFewerThan(5, "goals")
    .build()
    )

    m2 = (
    query
    .playsIn("EDM")
    .hasAtLeast(50, "points")
    .build()
    )

    matcher = query.oneOf(m1, m2).build()



    for player in stats.matches(matcher):
        print(player)

if __name__ == "__main__":
    main()

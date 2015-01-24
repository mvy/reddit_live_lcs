# Format lines for outputting comments
# 
# Each action have it's own format, try to be careful if you add some
# Sentence are meant to be selected at random
# Do not over format information. Let each element format itself (e.g. there is
# a format for players and for kills. Kills will use player and its format)

kill = [
    "{0} has killed {1}",
    "{1} has been killed by {0}",
    "{0} scored a kill on {1}",
    "A kill has been scored by {0} on {1}"
]

dragon = [
    "Dragon ({stack}) has been taken by {team}",
    "{team} takes dragon ({stack})",
]

baron = [
    "Baron Nashor has been taken by {team}",
    "{team} has slain the baron",
    "{team} has slain baron Nashor",
]

player = "{name} ({team}/{position}/{champion})"

team = "**{team}**"

ban = "{team} banned {champion}"

pick_single = "{team} picks {champion}"
pick_double = "{team} picks {champion[0]} and {champion[1]}"

tower_down = [
    "{team} has taken {lane} {level}-tower"
]

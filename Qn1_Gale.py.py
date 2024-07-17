def stable_matches(men_prefs,women_prefs):
    free_men=list(men_prefs.keys())
    engagements={}

    while free_men:
        man=free_men.pop(0)
        man_prefs=men_prefs[man]

        woman=man_prefs.pop(0)
        fiance=engagements.get(woman)

        if not fiance:
            engagements[woman]=man
        else:
            if women_prefs[woman].index(man) < women_prefs[woman].index(fiance):
                engagements[woman]=man
                free_men.append(fiance)
            else:
                free_men.append(man)
    return engagements
men_prefs = {
    'a': ['v', 'w', 'x'],
    'b': ['w', 'v', 'x'],
    'c': ['v', 'w', 'x']
}

women_prefs = {
    'v': ['a', 'b', 'c'],
    'w': ['b', 'c', 'a'],
    'x': ['c', 'a' 'b']
}
stableMatches=stable_matches(men_prefs,women_prefs)
for man,woman in stableMatches.items():
    print(f"{man} is engaged to {woman}")
            
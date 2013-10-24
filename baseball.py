# Calculates statistics of baseball player
# by inputting stats for each game


def main():


    num_games = integer_check("How many games?")
    
    tot_hits = 0
    tot_plate_apps = 0
    tot_walks = 0
    tot_tb = 0
    tot_runs = 0
    tot_rbi = 0
    tot_sb = 0
    tot_hr = 0
    tot_tr = 0
    tot_do = 0
    tot_sc = 0

    # Acquires each game's stats and stores data in a set of variables
    for x in range(num_games):
    
        h, pa, bb, sc, ru, rb, st = one_game()
        
        tbb, nd, nt, nh = the_total_bases(h)
        
        tot_hits += h
        tot_walks += bb
        tot_plate_apps += pa
        tot_tb += tbb
        tot_runs += ru
        tot_rbi += rb
        tot_sb += st
        tot_hr += nh
        tot_tr += nt
        tot_do += nd
        tot_sc += sc
        
        ob, a, s, op = percentages(tot_tb, tot_walks, tot_hits, tot_plate_apps, tot_sc)
        
        print("\nAfter Game {}:".format(x + 1))
        print("{0:.3f}/{1:.3f}/{2:.3f}".format(a, ob, s))

    # Season Stats
    print("\nSeason stats:")
    print("{0:.3f}/{1:.3f}/{2:.3f}".format(a, ob, s))
    print("{0} doubles, {1} triples, {2} home runs".format(tot_do, tot_tr, tot_hr))
    print("{0} SBs, {1} runs scored, {2} RBIs".format(tot_sb, tot_runs, tot_rbi))



# Gathers stats from one game
def one_game():


    # Plate appearances
    plate_apps = integer_check("PAs:")

    # Hits
    hits = integer_check("Hits:")
    while hits > plate_apps:
        print("Error: too many hits")
        hits = integer_check("Hits:")

    # Walks, Intentinal Walks, and Hit by Pitches
    walks = integer_check("BB/HBP/IBB")
    while walks > (hits + plate_apps):
        print("Error: too many walks")
        walks = integer_check("BB/HBP/IBB")

    # Sacrifices
    sacs = integer_check("Sacrifices:")
    while sacs > (hits + walks + plate_apps):
        print("Error: too many sacrifices")
        sacs = integer_check("Sacrifices:")

    # Runs
    runs = integer_check("Runs scored:")
    while runs > plate_apps:
        print("Error: too many runs")
        runs = integer_check("Runs scored:")

    # RBIs
    rbis = integer_check("Runs batted in:")
    while rbis > (plate_apps * 4):
        print("Error: too many RBIs")
        rbis = integer_check("Runs batted in:")
    
    # Stolen Bases
    stba = integer_check("Stolen bases:")
    while stba > (plate_apps * 3):
        print("Error: too many stolen bases")
        stba = integer_check("Stolen bases:")

    return hits, plate_apps, walks, sacs, runs, rbis, stba


# Calculates total bases using singles and extra base hits
def the_total_bases(hi):

    if hi == 0:

        total_bases = 0

    if hi > 0:
    
        ans = integer_check("Any extra base hits? (Y/N)")
        
        if ans == 'N':
        
            num_doubles = 0
            num_triples = 0
            num_homers = 0
            total_bases = hi

        if ans == 'Y':
        
            num_xbh = integer_check("How many?")
            
            while num_xbh > hi:
                print("Can't have more extra base hits than hits.")
                num_xbh = integer_check("How many?")
            
            num_singles = hi - num_xbh

            num_doubles = 0
            num_triples = 0
            num_homers = 0

            for x in range(num_xbh):

                type_ans = input("At bat {0}: Double (2), Triple (3), or Home Run (4)?".format(x + 1))

                if type_ans == '2':
                    num_doubles += 1
                elif type_ans == '3':
                    num_triples += 1
                else:
                    num_homers += 1

            total_bases = (1 * num_singles) + (2 * num_doubles) + (3 * num_triples) + (4 * num_homers)

    return total_bases, num_doubles, num_triples, num_homers



# Calculates the average, on base, slugging,
# and on base plus slugging percentages
def percentages(tob, bbs, hh, papp, ss):
    ab = papp - bbs - ss

    obp = float((hh + bbs) / (papp))
    avg = float(hh / ab)
    slg = float(tob / ab)
    ops = float(obp + slg)

    return obp, avg, slg, ops
    

# Try to change value inputted into an int
# If not a valid integer, asks again
# Uses a try except while loop
def integer_check(theString):

    while True:
        try:
            x = int(input(theString))
            break
        except:
            print("Not a valid integer")
    
    return x
    
    


# Exercises
# ---------
# Create a while loop that will print:
#     1. from 396 to 506 by 5.
#     2. from -477 to 3 by 16.
#     3. from -75 to 23 by 7.
#     4. from -168 to -72 by 4.
#     5. from -250 to 326 by 12.
#     6. from -401 to 124 by 15.
#     7. from 357 to 389 by 1.
#     8. from 356 to 896 by 18.
#     9. from 404 to 638 by 9.
#     10. from -327 to -285 by 3.

def run_loop (start,end,inc):
    print(f"From {start} to {end} by {inc}.")
    print("------------------------------")
    i = start
    while (i <= end):
        print(i) 
        i = i+inc
    print()


#--------------------------------
#SORRY SIR I AM LAZY :/
#--------------------------------


run_loop(396,506,5)
run_loop(-477,3,16)
run_loop(-75,23,7)
run_loop(-168,-72,4)
run_loop(-250,326,12)
run_loop(-401,124,15)
run_loop(-357,389,1)
run_loop(356,896,18)
run_loop(404,638,9)
run_loop(-327,-285,3)

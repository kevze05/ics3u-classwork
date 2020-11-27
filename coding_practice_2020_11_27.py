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

start_array = [396, -477, -75, -168, -250, -401, 357, 356, 404, -327]
end_array = [506, 3, 23, -72, 326, 124, 389, 896, 638, -285]
inc_array = [5, 16, 7, 4, 12, 15, 1, 18, 9, 3]

for i in range(10):
    run_loop(start_array[i],end_array[i],inc_array[i])

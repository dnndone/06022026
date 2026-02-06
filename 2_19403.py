print("w x y z")

for w in (0, 1):
    for x in (0, 1):
        for y in (0, 1):
            for z in (0, 1):
                if not (not (not (x or y) or w) or not (z and not (y and w))):
                    print(w, x, y, z)

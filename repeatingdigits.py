d = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
done = 0;
never = True;
firstrun = 0;
r = 10;
saven = 0;
while never:
    n = input("Enter number");
    if n == "l":
        if firstrun == 1:
            r = 25;
            n = saven;
            print("\nLoading " + str(r) + " more comments...\n");
        else:
            print("Cannot load 25 more on first script run. Please try again.");
    print(n + " <= Initial Number")
    for p in range(0, r):
        done = 0;
        temp = int(n);
        temp += 1;
        n = str(temp);
        while done is not 1:
            invalid = 0;
            l = list(n);
            for x in range(0, len(l)):
                l[x] = int(l[x]);
                for y in range(0, 10):
                    if y == l[x]:
                        d[y] += 1;
            for x in range(0, 10):
                if d[x] == 1:
                    invalid = 1;

            if invalid == 1:
                temp = int(n);
                temp += 1;
                n = str(temp);
            else:
                done = 1;
                print(n)
            d = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    firstrun = 1;
    r = 10;
    saven = n;

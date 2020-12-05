def run_05():
    with open("inputs/d05.txt") as f:
        boarding_passes = [
            line.strip()
                .replace("F", "0")
                .replace("B", "1")
                .replace("L", "0")
                .replace("R", "1")
            for line in f.readlines()]
        ids = sorted({
            int(b_pass, 2) for b_pass in boarding_passes
        })
        print(ids[-1])
        for id in range(ids[0], ids[-1]):
            if id not in ids:
                print(id)

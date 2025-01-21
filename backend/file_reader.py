def read_menu(filename):
    with open("Backend/" + filename) as f:
        return [line.strip() for line in f.readlines()]

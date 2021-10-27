from collections import defaultdict


if __name__ == "__main__":

    words = ["jury", "lineage", "invasion", "pick", "shaft", "virus", "preach", "reluctance", "devote", "tumble",
             "employee", "city", "pin", "priority", "east", "efflux", "fail", "fist", "woman", "current", "straight",
             "ivory", "despair", "audience", "remind", "paradox", "in", "Koran", "fisherman", "offense", "tap",
             "qualify", "deserve", "stick", "choke", "arena", "find", "sum", "plaintiff", "platform", "narrow",
             "confusion", "volume", "look", "steam", "gloom", "product", "deprive", "social", "lounge"]

    # round robin
    x = defaultdict(list)
    for index, i in enumerate(words):
        x[index % 10].append(i)

    # based on  1 letter
    x = defaultdict(list)
    for i in words:
        x[i[0]].append(i)

    # using hash
    def get_hash(w, groups=10):
        return sum(ord(i) for i in w) % groups

    x = defaultdict(list)
    for i in words:
        x[get_hash(i)].append(i)

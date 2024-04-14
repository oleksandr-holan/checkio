# def safe_pawns(pawns: set) -> int:
#     res = set()
#     for i in pawns:
#         for j in pawns:
#             if abs(ord(i[0]) - ord(j[0])) == 1 and int(i[1]) - int(j[1]) == 1:
#                 res.add(i)
#                 break
#     return len(res)

# return len(list(filter(lambda x: any([abs(ord(i[0]) - ord(x[0])) == 1 and int(i[1]) - int(x[1]) == 1 for i in pawns]), pawns)))

# o, safe_pawns = lambda l, d=-1: chr(ord(l) + d), lambda P: sum(bool({o(f) + o(r), o(f, 1) + o(r)} & P) for f, r in P)

def safe_pawns(pawns):
    return sum((any(chr(ord(l) + i) + str(int(d) - 1) in pawns for i in [-1, 1])) for l, d in pawns)

print("Example:")
print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))

assert safe_pawns({"d2", "f4", "d4", "b4", "e3", "g5", "c3"}) == 6
assert safe_pawns({"f4", "g4", "d4", "b4", "e4", "e5", "c4"}) == 1

print("The mission is done! Click 'Check Solution' to earn rewards!")

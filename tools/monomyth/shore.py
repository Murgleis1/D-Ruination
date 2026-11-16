"""Ragged beach waterline from the Old Bay Island sandbank pieces (+ their hflipped twins).

Per column x: s[x] = surf row (171 = sand above, surf line), wet sand (173) below it,
w[x] = first water row: 175 (the water's soft edge under wet sand), then 162. Neighbouring columns may differ by ONE row. As in the source
sandbank, a step is drawn in the first column of the LOWER side: falling to the right ->
172 over 174 in column x; rising to the right -> the hflipped pair in column x-1. Water
steps likewise: 176 (falling) / hflipped 176 (rising).
"""

def shore_columns(s, w, y0, y1, F172, F174, F176):
    n = len(s)
    col = []
    for x in range(n):
        c = {}
        for y in range(y0, y1 + 1):
            c[y] = 163 if y < s[x] else (171 if y == s[x] else (173 if y < w[x] else (175 if y == w[x] else 162)))
        col.append(c)
    for x in range(1, n):
        if s[x] == s[x - 1] + 1:                       # falls to the right: step in column x
            col[x][s[x] - 1], col[x][s[x]] = 172, 174
        elif s[x] == s[x - 1] - 1:                     # rises to the right: step in column x-1
            col[x - 1][s[x]], col[x - 1][s[x - 1]] = F172, F174
        if w[x] == w[x - 1] + 1:
            col[x][w[x] - 1] = 176
        elif w[x] == w[x - 1] - 1:
            col[x - 1][w[x]] = F176                    # (its own water row below stays 175)
    return col

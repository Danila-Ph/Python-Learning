letters = list("""Hours after President Trump assailed guidelines issued by the Centers for Disease Control and Prevention for reopening schools, Vice President Mike Pence, appearing with the White House coronavirus task force, announced the agency would issue new recommendations next week, saying administration officials don’t want the guidance to be a reason schools don’t open.

“Well, the president said today, we just don’t want the guidance to be too tough,” Mr. Pence said. “That’s the reason why next week, the C.D.C. is going to be issuing a new set of tools, five different documents that will be giving even more clarity on the guidance going forward.”

Mr. Trump openly rebuffed the C.D.C. on Twitter Wednesday morning, assailing current guidelines issued by the agency recommending a slew of preventive measures necessary to bring the nation’s children back to class. And he threatened to cut off federal aid to schools that refuse to fully reopen this fall.""")
letters_copy = letters.copy()
res = []
b = 'b'
i = 0
while letters.count(b) != 0:
    res.append(letters.index(b) + i)
    letters.remove(b)
    i += 1
print(res)
i = 0
while i < len(res):
    letters_copy[res[i]] = letters_copy[res[i]].upper()
    i += 1
print(str(letters_copy))

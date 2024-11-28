singers = {"Alice", "Charlie", "Eve", "Grace", "Ivy"}
dancers = {"Bob", "Charlie", "David", "Eve", "Henry"}
print("All artists:",singers|dancers)
print("Allrounders:",singers&dancers)
print("Dancers but not singers:",dancers-singers)
print("Singers but not dancers:",singers-dancers)
print("Dancers but not singers cum singers but not dancers:",(dancers-singers)|(singers-dancers))
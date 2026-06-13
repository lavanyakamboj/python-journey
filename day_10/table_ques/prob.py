def generate_table(i, f):
    for j in range(1, 11):
        f.write(f"{i} * {j} = {i*j}\n")

for k in range(1, 21):
    with open(f"table_ques/table{k}.txt", "w") as f:
        f.write(f"table of: {k}\n\n")
        generate_table(k, f)
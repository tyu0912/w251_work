fh = open("cleaned_logs.txt", "r").read().splitlines()

total_run_time = 0

for l in fh:
    if "completed" in l:
        total_run_time += float(l.split(" ")[5])

print(total_run_time)

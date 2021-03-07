import csv

def save_to_file(jobs, job_name):
    f = open(job_name + ".csv", mode="w", encoding="utf-8")
    writer = csv.writer(f)
    writer.writerow(["title", "company", "link"])
    for job in jobs:
        writer.writerow(list(job.values()))
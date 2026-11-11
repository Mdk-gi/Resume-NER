
import json
import os

files = [
    "data/dotin_resume_ner_converted_310.json",
    "data/indian_resume_ner_synthetic_600.json"
]

for file in files:
    if not os.path.exists(file):
        print("File not found:", file)
        continue

    print("\n\n==========", file, "==========")

    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)

    count = 0

    for record in data:
        text = record["text"]

        for entity in record["entities"]:
            if entity["label"] == "NAME":
                name = text[entity["start"]:entity["end"]]

                print("Text:", text[:150].replace("\n", " "))
                print("NAME:", name)

                count += 1
                if count == 10:
                    break

        if count == 10:
            break

    print("NAME examples checked:", count)
from collections import Counter

for file in files:
    if not os.path.exists(file):
        continue

    with open(file, "r", encoding="utf-8") as f:
        records = json.load(f)

    print("\nDATASET:", file)

    counter = Counter()

    for record in records:
        for entity in record["entities"]:
            counter[entity["label"]] += 1

    print(counter)
for file in files:
    if not os.path.exists(file):
        continue

    with open(file, "r", encoding="utf-8") as f:
        records = json.load(f)

    print("\nDATASET:", file)

    for record in records:
        text = record["text"]
        entities = record["entities"]

        names = [
            text[e["start"]:e["end"]]
            for e in entities if e["label"] == "NAME"
        ]

        designations = [
            text[e["start"]:e["end"]]
            for e in entities if e["label"] == "DESIGNATION"
        ]

        if names and designations:
            print("NAME:", names[:2])
            print("DESIGNATION:", designations[:2])
            print("TEXT:", text[:200].replace("\n", " "))
            print("-" * 50)

            if file.endswith("indian_resume_ner_synthetic_600.json"):
                if names:
                    break
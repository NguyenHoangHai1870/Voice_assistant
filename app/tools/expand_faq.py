import json
import random

INPUT = "data/faq_knowledge.json"
OUTPUT = "data/faq_expanded.json"

TEMPLATES = [
    "{} là gì",
    "{} dùng để làm gì",
    "{} hoạt động như thế nào",
    "{} có tác dụng gì",
    "{} có quan trọng không",
    "giải thích {}",
    "cho tôi biết về {}",
]

def normalize(q: str) -> str:
    return q.strip().lower()

with open(INPUT, "r", encoding="utf-8") as f:
    data = json.load(f)

expanded = []
seen = set()

for item in data:
    base_q = item["question"]
    answer = item["answer"]

    # lấy keyword thô (đơn giản: bỏ "là gì")
    key = base_q.replace("là gì", "").strip()

    variants = [base_q]

    for tpl in TEMPLATES:
        variants.append(tpl.format(key))

    for q in variants:
        nq = normalize(q)
        if nq not in seen:
            seen.add(nq)
            expanded.append({
                "question": q,
                "answer": answer
            })

with open(OUTPUT, "w", encoding="utf-8") as f:
    json.dump(expanded, f, ensure_ascii=False, indent=2)

print("Saved:", OUTPUT, "Total:", len(expanded))
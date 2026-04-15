courses = [
   "bsc cs",
   "bsc CS",
   "Bsc CS",
   "BSC CS",
   "BSc CS",
   "BSC cs",
   "Bsc cs",
]

patterns = [
  "{} Admission Eligibility",
  "{} Admission Criteria",
  "{} Admission Requirements",
  "{} Admission process",
  "{} Admission Eligibility Criteria",
  "{} admission Eligibility",
  "{} admission Criteria",
  "{} admission Requirements",
  "{} admission process",
  "{} admission Eligibility Criteria",
  "{} Admission eligibility",
  "{} Admission criteria",
  "{} Admission requirements",
  "{} Admission process",
  "{} Admission eligibility Criteria",
  "{} admission eligibility",
  "{} admission criteria",
  "{} admission requirements",
  "{} admission process",
  "{} admission eligibility Criteria",
]

data = []

for course in courses:
    for p in patterns:
        q = p.format(course)
        ans = f"For {course}, the eligibility criteria typically include a high school diploma or equivalent qualification with specific subject requirements depending on the course. For detailed information, please contact the admissions office."
        tag = course.lower().replace(" ", "_") + "_Admission"
        data.append([q, ans, tag])

# Save to CSV
import csv
with open("college_faqnew.csv", "a", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("Dataset created with", len(data), "rows")
import json
import base64
import os

print("Updating database with newly uploaded official brochure cards & portraits...")

with open("conference_database.json", "r", encoding="utf-8") as f:
    db = json.load(f)

# Base64 portraits
def get_b64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return "data:image/jpeg;base64," + base64.b64encode(f.read()).decode("utf-8")
    return ""

img_rangaswamy = get_b64("assets_dignitaries/rangaswamy_sq.jpg")
img_harish = get_b64("assets_dignitaries/harish_hande_sq.jpg")
img_pashim = get_b64("assets_dignitaries/pashim_tewari_sq.jpg")
img_ramesh = get_b64("assets_dignitaries/ramesh_b_sq.jpg")

# 1. Update Inauguration & Keynote Dignitaries
inaugural_dignitaries = [
    {
        "name": "Prof. B. E. Rangaswamy",
        "title": "Hon’ble Vice-Chancellor",
        "org": "Davangere University, Shivagangotri, Davanagere",
        "role": "Presidential Address (Inauguration & Valedictory)",
        "tag": "Presided By",
        "photo": img_rangaswamy
    },
    {
        "name": "Dr. Harish Hande",
        "title": "Renowned Social Entrepreneur & Ramon Magsaysay Awardee",
        "org": "CEO & Founder, SELCO-India, Bengaluru",
        "role": "Inauguration of the Annual National Conference (Day 1: 11:00 am)",
        "tag": "Inauguration By",
        "photo": img_harish
    },
    {
        "name": "Shri. Pashim Tewari",
        "title": "Technical Director",
        "org": "All India Institute of Local Self Government (AIILSG), New Delhi",
        "role": "Keynote Address: Innovative Technologies for Social Work Practice",
        "tag": "Keynote Speaker",
        "photo": img_pashim
    },
    {
        "name": "Prof. Ramesh B.",
        "title": "Hon’ble Vice-Chancellor & President, ISPSW",
        "org": "Dr. Manmohan Singh Bengaluru City University & ISPSW",
        "role": "Chief Guest (Inauguration) & Guest of Honour",
        "tag": "Chief Guest & President ISPSW",
        "photo": img_ramesh
    },
    {
        "name": "Ms. Sahitya M. Aladakatti I.A.S",
        "title": "Chief Executive Officer (CEO)",
        "org": "Zilla Panchayath, Davanagere District",
        "role": "Chief Guest & Valedictory Address (Day 3: 1:15 pm – 2:00 pm)",
        "tag": "Valedictory Chief Guest",
        "photo": ""
    },
    {
        "name": "Prof. R. Dhanasekara Pandian",
        "title": "Professor, Dept. of Psychiatric Social Work",
        "org": "National Institute of Mental Health & Neurosciences (NIMHANS), Bengaluru",
        "role": "General Secretary, ISPSW (Vote of Thanks)",
        "tag": "General Secretary ISPSW",
        "photo": ""
    }
]

# 2. Update Valedictory specific details
valedictory_info = {
    "date": "9th October, 2026",
    "time": "1:15 pm to 2:00 pm",
    "venue": "MBA Auditorium, Davangere University",
    "presided_by": "Prof. B E Rangaswamy, Hon'ble Vice-Chancellor, Davangere University",
    "chief_guest": "Ms. Sahitya M. Aladakatti I.A.S, Chief Executive Officer (CEO), Zilla Panchayath, Davanagere District",
    "guests_of_honour": [
        {"name": "Prof. Ramesh B", "desig": "Hon’ble Vice-Chancellor, Dr. Manmohan Singh Bengaluru City University, & President, ISPSW"},
        {"name": "Mr. Manjunatha Rangaraju", "desig": "Dean, PSSEMR School & PU College, Davanagere"},
        {"name": "Prof. I.A. Shariff", "desig": "Professor (Rtd.), Dept. of Psychiatric Social Work, NIMHANS, Bengaluru"},
        {"name": "Col. Prof. Y.S. Siddegowda", "desig": "Former Vice Chancellor, Tumkur University & Former Vice Chairman, KSHEC, GOK"}
    ],
    "presence": [
        {"name": "Prof. Parashurama K.G", "desig": "Vice President, ISPSW & Senior Professor of Social Work, Tumkur University"},
        {"name": "Prof. R Shivappa", "desig": "Vice President, ISPSW & Registrar (Evl.), Bangalore University"},
        {"name": "Prof. R. Dhanasekara Pandian", "desig": "General Secretary, ISPSW & Professor, Dept. PSW, NIMHANS"},
        {"name": "Sri. S B Ganti", "desig": "Registrar, Davangere University (K.A.S Super Time Scale)"},
        {"name": "Prof. C K Ramesh", "desig": "Registrar (Evl.), Davangere University"},
        {"name": "Prof. Shashidhar R", "desig": "Finance Officer, Davangere University"}
    ]
}

# 3. National Presence / Advisory Luminaries
national_presence = [
    {"name": "Prof. M. Ranganathan", "desig": "Professor of PSW (Retd.), NIMHANS & Founder President of Family Fellowship Society"},
    {"name": "Prof. D. Muralidhar", "desig": "Professor and Head of PSW (Retd.), NIMHANS & Former President of ISPSW"},
    {"name": "Prof. S.A. Kazi", "desig": "Former Registrar and Vice-Chancellor (I/c), KSWU, Vijayapura"},
    {"name": "Prof. B.S. Gunjal", "desig": "Professor & Chairman, Dept. of Studies in Social Work, KSOU, Mysuru"},
    {"name": "Prof. Kodandarama", "desig": "Prof. (Retd.) & Former Head, Dept. of Social Work, Bangalore University"},
    {"name": "Dr. Kanmani T.R", "desig": "Joint Secretary ISPSW; Additional Professor, Dept. of Psychiatric Social Work, NIMHANS"},
    {"name": "Dr. Sojan Antony", "desig": "Treasurer ISPSW; Additional Professor, Dept. of Psychiatric Social Work, NIMHANS"},
    {"name": "Prof. Sanjoy Roy", "desig": "Prof. & Head, Delhi School of Social Work, New Delhi"},
    {"name": "Dr. L. Ponnuchamy", "desig": "Associate Professor, Dept. of Psychiatric Social Work, NIMHANS"},
    {"name": "Prof. Sangeetha R. Mane", "desig": "Professor & Chairman, Dept. of Social Work, Karnatak University, Dharwad"},
    {"name": "Dr. R. Mangaleswaran", "desig": "Professor, Dept. of Social Work, Bharathidasan University, Coimbatore"},
    {"name": "Prof. Ashok Antony D’Souza", "desig": "Professor, Dept. of Social Work, Rani Channamma University, Belagavi"},
    {"name": "Dr. R. Bhaskar", "desig": "Associate Professor & Head, Dept. of Social Work, Bharathiar University, Coimbatore"},
    {"name": "Dr. Noor Mudasheer C. A", "desig": "Assistant Professor, Dept. of Social Work, St. Philomena College, Mysuru"},
    {"name": "Dr. M. P. Somashekar", "desig": "Associate Professor & Head, Dept. of Social Work, J.S.S College, Mysuru"},
    {"name": "Dr. Veda C.V", "desig": "Assistant Professor & Coordinator, Dept. of Social Work, Bangalore University"},
    {"name": "Dr. Srinivasa D", "desig": "Assistant Professor, Dept. of Social Work, Central University of Karnataka, Kalaburagi"}
]

# 4. Conference Organizing Committee
organizing_committee = [
    {"name": "Dr. Thippesh K", "role": "Organizing Secretary & Assistant Professor", "dept": "DoS in Social Work, Davangere University"},
    {"name": "Dr. Shivalingappa B.P", "role": "Convener & Professor", "dept": "Chairman, DoS in Social Work, Davangere University"},
    {"name": "Dr. Lokesh M U", "role": "Conference Advisor", "dept": "Professor, DoS in Social Work and Dean, Faculty of Arts, Davangere University"},
    {"name": "Dr. Pradeep B S", "role": "Conference Advisor", "dept": "Professor, DoS in Social Work, Davangere University"},
    {"name": "Dr. Patwardhan Rathod", "role": "Co-Organizing Secretary", "dept": "Assistant Professor, DoS in Social Work, Davangere University"}
]

# Update DB
db["dignitaries"] = inaugural_dignitaries
db["valedictory_info"] = valedictory_info
db["national_presence"] = national_presence
db["organizing_committee"] = organizing_committee

# Also update Day 1 Keynote in Programme Schedule to match Shri Pashim Tewari
day1_events = db["programme_schedule"]["day1"]["events"]
for ev in day1_events:
    if "keynote" in ev["event"].lower():
        ev["event"] = "Keynote Address: Innovative Technologies for Social Work Practice"
        ev["details"] = "Keynote Speaker: Shri. Pashim Tewari, Technical Director, All India Institute of Local Self Government (AIILSG), New Delhi"
    if "inauguration" in ev["event"].lower():
        ev["details"] = "Inaugurated by Dr. Harish Hande (CEO SELCO India, Ramon Magsaysay Awardee); Presided by Prof. B.E. Rangaswamy (Hon'ble VC); Chief Guest: Prof. Ramesh B (VC BCU & President ISPSW)"

# Update Day 3 Valedictory in Programme Schedule
day3_events = db["programme_schedule"]["day3"]["events"]
for ev in day3_events:
    if "valedictory" in ev["event"].lower():
        ev["details"] = "Presided by Prof. B E Rangaswamy, Hon'ble VC; Chief Guest & Valedictory Address: Ms. Sahitya M. Aladakatti I.A.S, CEO Zilla Panchayath, Davanagere; Guests of Honour: Prof. Ramesh B, Mr. Manjunatha Rangaraju, Prof. I.A. Shariff, Col. Prof. Y.S. Siddegowda"

with open("conference_database.json", "w", encoding="utf-8") as f:
    json.dump(db, f, ensure_ascii=False, indent=2)

print("Updated conference_database.json successfully!")

import json

print("Updating database with complete exhaustive dignitaries list from invitations...")

with open("conference_database.json", "r", encoding="utf-8") as f:
    db = json.load(f)

# Complete all names from invitations
all_invitation_dignitaries = {
    "inauguration": [
        {
            "name": "Prof. B. E. Rangaswamy",
            "title": "Hon’ble Vice-Chancellor",
            "org": "Davangere University, Davangere",
            "role": "Presided by (Inauguration & Valedictory)",
            "category": "Inaugural Leadership",
            "photo_key": "rangaswamy"
        },
        {
            "name": "Dr. Harish Hande",
            "title": "Renowned Social Entrepreneur & Ramon Magsaysay Awardee",
            "org": "CEO, SELCO-India, Karnataka",
            "role": "Inauguration by (Day 1: 11:00 am)",
            "category": "Inaugural Leadership",
            "photo_key": "harish_hande"
        },
        {
            "name": "Shri. Pashim Tewari",
            "title": "Technical Director",
            "org": "All India Institute of Local Self Government (AIILSG), New Delhi",
            "role": "Keynote Address: Innovative Technologies for Social Work Practice",
            "category": "Inaugural Leadership",
            "photo_key": "pashim_tewari"
        },
        {
            "name": "Prof. Ramesh B.",
            "title": "Hon’ble Vice-Chancellor & President, ISPSW",
            "org": "Dr. Manmohan Singh Bengaluru City University & ISPSW",
            "role": "Chief Guest (Inauguration) & Guest of Honour",
            "category": "Inaugural Leadership",
            "photo_key": "ramesh_b"
        }
    ],
    "valedictory": [
        {
            "name": "Prof. B. E. Rangaswamy",
            "title": "Hon’ble Vice-Chancellor",
            "org": "Davangere University, Davangere",
            "role": "Presided by (Valedictory Ceremony)",
            "category": "Valedictory Ceremony"
        },
        {
            "name": "Ms. Sahitya M. Aladakatti I.A.S",
            "title": "Chief Executive Officer (CEO)",
            "org": "Zilla Panchayath, Davanagere District",
            "role": "Chief Guest & Valedictory Address (9th Oct, 1:15 pm)",
            "category": "Valedictory Ceremony"
        },
        {
            "name": "Prof. Ramesh B.",
            "title": "Hon’ble Vice-Chancellor",
            "org": "Dr. Manmohan Singh Bengaluru City University & President, ISPSW",
            "role": "Guest of Honour (Valedictory)",
            "category": "Valedictory Ceremony"
        },
        {
            "name": "Mr. Manjunatha Rangaraju",
            "title": "Dean",
            "org": "PSSEMR School & PU College, Davanagere",
            "role": "Guest of Honour (Valedictory)",
            "category": "Valedictory Ceremony"
        },
        {
            "name": "Prof. I. A. Shariff",
            "title": "Professor (Rtd.)",
            "org": "Department of Psychiatric Social Work, NIMHANS, Bengaluru",
            "role": "Guest of Honour (Valedictory) & Special Address Speaker",
            "category": "Valedictory Ceremony"
        },
        {
            "name": "Col. Prof. Y. S. Siddegowda",
            "title": "Former Vice Chancellor & Former Vice Chairman",
            "org": "Tumkur University & KSHEC, Government of Karnataka",
            "role": "Guest of Honour (Valedictory)",
            "category": "Valedictory Ceremony"
        }
    ],
    "presence_officers": [
        {
            "name": "Prof. Parashurama K. G.",
            "title": "Vice President, ISPSW & Senior Professor of Social Work",
            "org": "Tumkur University, Tumakuru",
            "role": "Eminent Presence (Valedictory)",
            "category": "Executive Presence"
        },
        {
            "name": "Prof. R. Shivappa",
            "title": "Vice President, ISPSW & Registrar (Evl.)",
            "org": "Bangalore University, Bengaluru",
            "role": "Eminent Presence (Valedictory)",
            "category": "Executive Presence"
        },
        {
            "name": "Prof. R. Dhanasekara Pandian",
            "title": "General Secretary, ISPSW & Professor",
            "org": "Dept. of Psychiatric Social Work, NIMHANS, Bengaluru",
            "role": "Eminent Presence & Vote of Thanks",
            "category": "Executive Presence"
        },
        {
            "name": "Sri. S. B. Ganti",
            "title": "Registrar (K.A.S Super Time Scale)",
            "org": "Davangere University, Davangere",
            "role": "Eminent Presence (Valedictory)",
            "category": "Executive Presence"
        },
        {
            "name": "Prof. C. K. Ramesh",
            "title": "Registrar (Evl.)",
            "org": "Davangere University, Davangere",
            "role": "Eminent Presence (Valedictory)",
            "category": "Executive Presence"
        },
        {
            "name": "Prof. Shashidhar R.",
            "title": "Finance Officer",
            "org": "Davangere University, Davangere",
            "role": "Eminent Presence (Valedictory)",
            "category": "Executive Presence"
        }
    ],
    "national_council": [
        {
            "name": "Prof. M. Ranganathan",
            "title": "Professor of PSW (Retd.), NIMHANS",
            "org": "Founder President, Family Fellowship Society for Psychosocial Rehabilitation Services, India",
            "role": "National Presence",
            "category": "National Academic Presence"
        },
        {
            "name": "Prof. D. Muralidhar",
            "title": "Professor and Head of PSW (Retd.), NIMHANS",
            "org": "Former President of ISPSW",
            "role": "National Presence",
            "category": "National Academic Presence"
        },
        {
            "name": "Prof. S. A. Kazi",
            "title": "Former Registrar and Vice-Chancellor (I/c)",
            "org": "Karnataka State Akkamahadevi Women's University, Vijayapura",
            "role": "National Presence",
            "category": "National Academic Presence"
        },
        {
            "name": "Prof. B. S. Gunjal",
            "title": "Professor & Chairman, Dept. of Studies in Social Work",
            "org": "Karnataka State Open University (KSOU), Mysuru",
            "role": "National Presence",
            "category": "National Academic Presence"
        },
        {
            "name": "Prof. Kodandarama",
            "title": "Prof. (Retd.) & Former Head, Dept. of Social Work",
            "org": "Bangalore University, Bengaluru",
            "role": "National Presence & Poster Session Judge",
            "category": "National Academic Presence"
        },
        {
            "name": "Dr. Kanmani T. R.",
            "title": "Joint Secretary, ISPSW & Additional Professor",
            "org": "Dept. of Psychiatric Social Work, NIMHANS, Bengaluru",
            "role": "National Presence & Executive Council",
            "category": "National Academic Presence"
        },
        {
            "name": "Dr. Sojan Antony",
            "title": "Treasurer, ISPSW & Additional Professor",
            "org": "Dept. of Psychiatric Social Work, NIMHANS, Bengaluru",
            "role": "National Presence & Plenary II Speaker",
            "category": "National Academic Presence"
        },
        {
            "name": "Prof. Sanjoy Roy",
            "title": "Prof. & Head",
            "org": "Delhi School of Social Work, University of Delhi, New Delhi",
            "role": "National Presence",
            "category": "National Academic Presence"
        },
        {
            "name": "Dr. L. Ponnuchamy",
            "title": "Associate Professor",
            "org": "Dept. of Psychiatric Social Work, NIMHANS, Bengaluru",
            "role": "National Presence",
            "category": "National Academic Presence"
        },
        {
            "name": "Prof. Sangeetha R. Mane",
            "title": "Professor & Chairman, Dept. of Social Work",
            "org": "Karnatak University, Dharwad",
            "role": "National Presence & Panel Discussion I Chairperson",
            "category": "National Academic Presence"
        },
        {
            "name": "Dr. R. Mangaleswaran",
            "title": "Professor, Dept. of Social Work",
            "org": "Bharathidasan University, Tiruchirappalli / Coimbatore",
            "role": "National Presence",
            "category": "National Academic Presence"
        },
        {
            "name": "Prof. Ashok Antony D’Souza",
            "title": "Professor, Dept. of Social Work",
            "org": "Rani Channamma University, Belagavi",
            "role": "National Presence & Plenary I Chairperson",
            "category": "National Academic Presence"
        },
        {
            "name": "Dr. R. Bhaskar",
            "title": "Associate Professor & Head, Dept. of Social Work",
            "org": "Bharathiar University, Coimbatore",
            "role": "National Presence & Technical Session I Track 1 Chairperson",
            "category": "National Academic Presence"
        },
        {
            "name": "Dr. Noor Mudasheer C. A.",
            "title": "Assistant Professor, Dept. of Social Work",
            "org": "St. Philomena’s College (Autonomous), Mysuru",
            "role": "National Presence & Panel Discussion II Speaker",
            "category": "National Academic Presence"
        },
        {
            "name": "Dr. M. P. Somashekar",
            "title": "Associate Professor & Head, Dept. of Social Work",
            "org": "J.S.S. College, Mysuru",
            "role": "National Presence & Technical Session III Track 1 Chairperson",
            "category": "National Academic Presence"
        },
        {
            "name": "Dr. Veda C. V.",
            "title": "Assistant Professor & Coordinator, Dept. of Social Work",
            "org": "Bangalore University, Bengaluru",
            "role": "National Presence & Technical Session II Track 3 Chairperson",
            "category": "National Academic Presence"
        },
        {
            "name": "Dr. Srinivasa D.",
            "title": "Assistant Professor, Dept. of Social Work",
            "org": "Central University of Karnataka, Kalaburagi",
            "role": "National Presence & Technical Session III Track 3 Discussant",
            "category": "National Academic Presence"
        }
    ],
    "organizing_committee": [
        {
            "name": "Dr. Thippesh K.",
            "title": "Organizing Secretary & Assistant Professor",
            "org": "DoS in Social Work, Davangere University",
            "role": "Organizing Secretary",
            "category": "Organizing Committee"
        },
        {
            "name": "Dr. Shivalingappa B. P.",
            "title": "Convener and Professor & Chairman",
            "org": "DoS in Social Work, Davangere University",
            "role": "Conference Convener",
            "category": "Organizing Committee"
        },
        {
            "name": "Dr. Lokesh M. U.",
            "title": "Conference Advisor, Professor & Dean",
            "org": "Faculty of Arts & DoS in Social Work, Davangere University",
            "role": "Conference Advisor",
            "category": "Organizing Committee"
        },
        {
            "name": "Dr. Pradeep B. S.",
            "title": "Conference Advisor & Professor",
            "org": "DoS in Social Work, Davangere University",
            "role": "Conference Advisor",
            "category": "Organizing Committee"
        },
        {
            "name": "Dr. Patwardhan Rathod",
            "title": "Co-Organizing Secretary & Assistant Professor",
            "org": "DoS in Social Work, Davangere University",
            "role": "Co-Organizing Secretary",
            "category": "Organizing Committee"
        }
    ]
}

db["all_invitation_dignitaries"] = all_invitation_dignitaries

with open("conference_database.json", "w", encoding="utf-8") as f:
    json.dump(db, f, ensure_ascii=False, indent=2)

print("Saved all invitation dignitaries into conference_database.json!")

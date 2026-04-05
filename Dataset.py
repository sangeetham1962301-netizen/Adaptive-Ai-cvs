import csv
data=[
["question","answer","tag"],
["what courses are offered?","BSC.CS(Computer Science),BCA,BCom,Bio chemistry,bio maths,BBA","courses"],
["what is the admission process?","The admission is based on 12th marks.","admission"],
["what is the fee structure?","The fee structure is as follows: BSC.CS:17500/sem,BCA:17500/sem","fee structure"],
["what are the facilities available?","The college provides various facilities such as library, sports, hostel, and cafeteria.","facilities"],
["what is the location of the college?","The college is located in Thirukazhukundram,chengalpauttu District,Tamil Nadu, India.","location",],
["what are the extracurricular activities?","The college offers a range of extracurricular activities including sports, cultural events, and clubs.","extracurricular activities"],
["what is the contact information?","You can contact the college at tel:6380544088 or email us at:office@atasctkm.com","contact information"],
["what is the college's vision and mission?","Committed to maintain the quality of higher education, so that the rural students will come out as citizen of Eminence and Excellence to serve the Society and the Nation.","vision","mission"],["what are the career opportunities after graduation?","Graduates from our college have a wide range of career opportunities in various fields such as IT, finance, management, and education.","career opportunities"],["what is the student to faculty ratio?","The student to faculty ratio is 20:1.","student to faculty ratio"],["Academic calendar?","The academic calendar includes the 1	Regular Class time	Monday to Saturday	9.00 a.m to 2.00 p.m 2.Add on courses	Monday to Friday	01.10 p.m to 2.00 p.m","academic calendar"],["what are admisson process?","Procedure1.Candidate with a pass in the Higher Secondary Examination (+2) conducted by the Government of Tamilnadu or its equivalent as fixed by the University of Madras are eligible to join the degree courses."
"2	Minimum age 17 as on July and upper age limit is 21 year (5 years relaxed for SC/ST and Women Students). Candidates who have passed the Examination other than Higher Secondary Examination of Tamilnadu state should produce the Provisonal eligibility certificate obtained from the University of Madras before the admission."
"3	Director of Collegiate Education and University of Madras admission eligibility rules should be followed for choosing of candidates."
"4	Admission will be made through the College Committee for admission based on the Government of reservation policies, rules and regulations. Spot admission will be made for vacancy seats in first come first served basis."
"5	Mode of Admission: Candidate when called for Interview must produce the following original certificates."
"i	H.S.C Mark Statements"
"ii	Transfer Certificate"
"iii	Community certificate from a competent authority in case of BC/MBC/DCN/SC/ST only"
"iv	Students from other state should produce the following certificatei	Provisional Eligibility obtained from University of Madras (before Admission)"
"iv	Recognization Certificate from University of Madras (before Admission)v	Aadhar Card & Address Proof"
"vi	Bank Account detail for SC/ST only. To remit the scholarship.vii	All relevant document should be submitted at the time of admission6	The Certificate will be retained in the college office and will not be returned under any circumstance till the student leaves the institution. Therefore the students are advised to take sufficient photo copies of all the certificate before submitting the originals to the college."
"7	Admission will be confirmed only after the interview and completepayment of admission and tuition fee."
"8	Selected candidates should pay the fees immediately after the interview. Fees once paid will not be refunded."
"9	Admission of the students to any course will be provisional and will be subject to the approval of the University of Madras. Students must satisfy themselves that they are eligible for admission. After admission if they are found not eligible the college cannot be held responsible for it. They will lose their seats and also the fees paid.","admission process"],["What are the elegiblity criteria for admission?","B.Sc., Computer Science.,9.00 a.m to 2.00 p.m.	Passed in Hr Sec Examination should have to studied Mathematics (or) Computer Science2	B.Sc., Chemistry	9.00 a.m. to 2.00 p.m.	Passed in Hr. Sec. Examination with Chemistry / Physics / Mathematics3	B.Sc., Biochemistry	9.00 a.m. to 2.00 p.m.	Passed in Hr. Sec. Examination with Chemistry / Physics / Biology / Zoology / Botany4	B.C.A	9.00 a.m. to 2.00 p.m.	Passed in Hr. Sec. Examination with Mathematics(or) Computer Science (or) Computer Applications5	B.Com (General)	9.00 a.m. to 2.00 p.m.	Passed in Hr. Sec. Examination with Commerce / Accountancy / Economics (or) Business Mathematics6	B.Com (Computer Application)	9.00 a.m. to 2.00 p.m.	Passed in Hr. Sec. Examination with Commerce / Accountancy / Computer Science7	B.B.A	"
"9.00 a.m. to 2.00 p.m.	Passed in Hr. Sec. Examination with Commerce / Accountancy / Economics (or) Business Mathematics","eligibility criteria"
],["how about transportation facilities?","The college provides transportation facilities for students and staff. There are buses that operate on various routes to and from the college.","transportation facilities"],["What are the bus routes and timings?","The bus routes and timings are as follows: Route 1: Main Gate to City Center, Route 2: Main Gate to Suburb, Route 3: Main Gate to Railway Station. The buses operate from 7:00 AM to 10:00 PM with a frequency of every 30 minutes.","bus routes and timings"]
]
with open("college_faq.csv","w",newline="") as f:
    writer=csv.writer(f)
    writer.writerows(data)
    print("csv file created successfully.")
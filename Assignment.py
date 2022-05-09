def my_details(S):
  for key in S:
    print(key, ":", S[key])

# S = {"Name" : "Aritta Sinha", "Roll Number" : "VU21CSEN0100997", "Branch" : "CSE", "Specialization" : "Core", "Email Id" : "asinha2@gitam.in", "Moodle Id" : "Aritta Sinha 210061751", "Github Id" : "arittASinha2003", "Replit Id" : "arittASinha2003", "Semester" : "2", "Year" : "1"}
S = {"Name" : {"First Name" : "Aritta", "Last Name" : "Sinha"}, "Roll Number" : "VU21CSEN0100997", "Branch" : "CSE", "Specialization" : "Core", "Email Id" : "asinha2@gitam.in", "Moodle Id" : "Aritta Sinha 210061751", "Github Id" : "arittASinha2003", "Replit Id" : "arittASinha2003", "Semester" : "2", "Year" : "1"}

# dt = my_details(S)
# print(dt)
my_details(S)
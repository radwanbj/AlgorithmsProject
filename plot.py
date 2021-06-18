from analysis import Analysis

analysis = Analysis(debug=True)
d = analysis.run_analysis()

# Print the contents of dictionary to a txt file
output = open("pos_neg.txt", "w")

for key in list(d.keys()):
    output.write(key + ":" + str(d[key]) + "\n")






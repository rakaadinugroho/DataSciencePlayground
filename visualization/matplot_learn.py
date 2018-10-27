from matplotlib import pyplot as plt

# Sample create visualization with MatPlot Library
# medium.com/@rakaadinugroho
# Data source from World Bank Statistik Pertumbuhan Domestik Bruto (PDB) Indonesia

years = [2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016]
pdb = [432.2, 510.2, 539.6, 755.0, 893.0, 918.0, 915.0, 891.0, 861.0, 933.0]

#create a line chart, x-axis for years and y-axis for pdb
plt.plot(years, pdb, color='blue', marker='o', linestyle='solid')
plt.title("Statistik Pertumbuhan Domestik Bruto")
plt.xlabel("Pertahun")
plt.ylabel("Nilai dalam USD $")
plt.show()
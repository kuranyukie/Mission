# -*- coding: utf-8 -*- 
from util import *

class Calculator :
    
    def __init__(self) :
        self.data  = []
        self.data2 = []

    def add(self, number) :
        self.data.append(number)

    def add_tuple(self, new_tuple) :
        self.data2.append(new_tuple)

    def find_tuple(self) :
        return self.data2

    def calc_median(self) :
        self.data = sorted(self.data)
        mid = len(self.data) / 2
        if len(self.data) % 2 == 0 :
            return 1.0 * (self.data[mid - 1] + self.data[mid]) / 2
        else :
            return self.data[mid]

    def calc_mean(self) :
        if len(self.data) == 0 : # working with data2
            self.data = self.data2
        return sum(self.data) / len(self.data)

    def ratio_per_SG(self) : 
        remaining = sorted(self.data2, key = lambda _ : float(_[0]))[:-1] # sort by PA and delete the highest
        same_PA = 0
        for pair in remaining :
            PA, PAA, PAB = pair[0], pair[1], pair[2]
            if abs(PA - PAA) < 0.001 or abs(PA - PAB) < 0.001 :
                same_PA += 1
        return same_PA / 3.0

class parser :

    filename_data = '20150508-2.txt'

    fields = ['150505_1345', '2', 'subjects', 'Period', 'Subject', 'Group', 'Profit', 'Participate', 'PAP', 'PageSlider', 'Z1', 'PA', 'PAA3D', 'PPA3D', 'PAB3D', 'PPB3D', 'PAU3D', 'PPU3D', 'SG', 'rank2', 'LL']

    data = []

    calculators = {}

    result = []

    def __init__(self) :
        pass
    
    def import_data(self) : 
        for line in open(self.filename_data):
            fields_data = line.strip('\n').split('\t')
            datum = dict(zip(self.fields, fields_data)) # mapping from field to data
            if datum['LL'] not in ['', 'LL'] : # filter data really needed
                self.data.append(datum)
                Period = datum['Period']
                Group  = datum['Group']
                SG     = datum['SG']
                PA     = float(datum['PA'])
                PAA3D  = float(datum['PAA3D'])
                PAB3D  = float(datum['PAB3D'])
                if not self.calculators.has_key(Period) :
                    self.calculators[Period] = {'Overall' : Calculator()}
                if not self.calculators[Period].has_key(Group) :
                    self.calculators[Period][Group] = {}
                if not self.calculators[Period][Group].has_key(SG) :
                    self.calculators[Period][Group][SG] =  Calculator()
                # self.calculators[Period][Group][SG].add(PA) # mission_1
                self.calculators[Period][Group][SG].add_tuple((PA, PAA3D, PAB3D)) # mission_2

    def mission_1(self) :
        for Period in self.calculators.keys() :
            for Group in self.calculators[Period].keys() :
                if Group != 'Overall' :
                    for SG in self.calculators[Period][Group].keys() :
                        median = self.calculators[Period][Group][SG].calc_median()
                        # print Period, Group, SG, median
                        self.calculators[Period]['Overall'].add(median)
            self.result.append((Period, self.calculators[Period]['Overall'].calc_mean()))

    def mission_2(self) :
        for Period in self.calculators.keys() :
            for Group in self.calculators[Period].keys() :
                if Group != 'Overall' :
                    for SG in self.calculators[Period][Group].keys() :
                        ratio = self.calculators[Period][Group][SG].ratio_per_SG()
                        self.calculators[Period]['Overall'].add(ratio)
            self.result.append((Period, self.calculators[Period]['Overall'].calc_mean()))

    def export_data(self, filename) :
        filename = open('%s.txt' %filename, 'w')
        for item in sorted(self.result, key = lambda _ : int(_[0])) :
            filename.write('%s\t%s\n' %(item[0], item[1]))
        filename.close()

if __name__ == '__main__':
    p = parser()
    p.import_data()
    # p.mission_1()
    p.mission_2()
    p.export_data('ratio')
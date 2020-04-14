# -*- coding: utf-8 -*- 

class parser :

    filename_data = 'raw_time_log.txt'

    fields = ['Date', 'Name', 'Time', 'Type']

    data        = []
    calculators = {}
    result      = []

    def __init__(self) :
        pass

    def import_data(self) : 
        for line in open(self.filename_data):
            fields_data = line.strip('\n').split('\t')
            datum = dict(zip(self.fields, fields_data)) # mapping from field to data
            self.data.append(datum)
        # print self.data

    def calc_time_sum(self) : # calculate every member's overall working time
        for datum in self.data :
            Date       = datum['Date']
            Name       = datum['Name']
            Type       = datum['Type']
            if datum['Time'] :
                Time       = int(datum['Time'])
            # Assessment = int(datum['Assessment'])
            if not self.calculators.has_key(Name) :
                self.calculators[Name] = []
            self.calculators[Name].append(Time)
        for (person, time) in self.calculators.items() :
            working_time = sum(time)
            self.result.append((person, working_time))

    def sort_working_time(self, filename) :
        r = open(filename, 'w')
        r.write('Name\tTime\n')
        for (person, time) in sorted(self.result, key = lambda _ : float(_[1]), reverse = True) :
            r.write('%s\t%d\n' %(person, time))

if __name__ == '__main__':
    p = parser()
    p.import_data()
    p.calc_time_sum()
    p.sort_working_time('time_log_summary.txt')
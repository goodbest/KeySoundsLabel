#!/usr/bin/env python
#encoding: utf8

import json
import csv
import sys


def json2csv(infile, outfile):
    with open(infile) as datafile:
        data = json.load(datafile)
        dates = data['timeline']['date']
        dates.sort(key = lambda x: (x['asset']['caption']))
    
    with open(outfile, 'w') as output:
        output.write('caption\tstartdate\theadline\ttext\tmedia\tthumbnail\tcredit\n')
        for row in dates:
            output.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\n' %(row['asset']['caption'].encode('utf-8'), row['startDate'].encode('utf-8'), 
            row['headline'].encode('utf-8'), row['text'].encode('utf-8'),row['asset']['media'].encode('utf-8'), 
            row['asset']['thumbnail'].encode('utf-8'), row['asset']['credit'].encode('utf-8')))



def csv2json(infile, outfile):
    nolist=["KSLA-0056","KSLA-0113~0115","KSLA-0116","KSLA-0117","KSLA-0118","KSLC-0006~0007","KSLC-0009","KSLC-0010~0011","KSLC-0013","KSLV-0001~0003"]
    dates = []
    with open(infile) as datafile:
        for row in csv.DictReader(datafile, delimiter='\t'):
            
            if row['caption'] not in nolist:
                dates.append({
                    'headline': row['headline'],
                    'text':     row['text'],
                    'startDate':row['startdate'],
                    'asset':    {
                        'caption':   '<a target=\"_blank\" title=\"Listen\" href=\"http://kslm.oldcat.me/?album=' + row['caption'] + '\">' + row['caption'] + '</a>',
                        'credit':    row['credit'],
                        'thumbnail': row['thumbnail'],
                        'media':     row['media']
                    }
                })
            else:
                dates.append({
                    'headline': row['headline'],
                    'text':     row['text'],
                    'startDate':row['startdate'],
                    'asset':    {
                        'caption':   row['caption'],
                        'credit':    row['credit'],
                        'thumbnail': row['thumbnail'],
                        'media':     row['media']
                    }
                })
    
    data = {}
    data['headline'] = 'Key Sounds Label Timeline'
    data['text'] = '<p><a href=\"https://github.com/goodbest/KeySoundsLabel\">Click here to contribute</a><br/><br/>' \
        'Last update: 2016/12<br/>webpage made by <a href=\"https://twitter.com/lovegoodbest\">goodbest</a><br/>' \
        'Special Thanks to KSLU group</p><br/>*All dates are album\'s first release date'
    data['type'] = 'default'
    data['asset'] = {}
    data['asset']['media'] = 'img/ksl_logo.png'
    data['date'] = dates
    
    with open (outfile, 'w') as output:
        json.dump({'timeline': data}, output)


#json2csv('ksl.json', 'ksl.csv')
csv2json('ksl.csv', 'ksl.json')







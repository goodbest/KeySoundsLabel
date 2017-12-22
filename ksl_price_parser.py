import collections
import urllib2
import json

ksls={}
ksls['KSLA-0001']=('806304536', 'Album')
ksls['KSLA-0002']=('818353982', 'Single')
ksls['KSLA-0003']=('818391612', 'Album')
ksls['KSLA-0004~0005']=('818439884', 'O.S.T')
ksls['KSLA-0006']=('813627592', 'O.S.T')
ksls['KSLA-0007']=('818498765', 'Single')
ksls['KSLA-0008']=('818369305', 'Single')
ksls['KSLA-0009']=('823459551', 'Album')
ksls['KSLA-0010']=('813701606', 'Album')
ksls['KSLA-0011']=('823471549', 'Album')
ksls['KSLA-0012~0014']=('823583025', 'O.S.T')
ksls['KSLA-0015']=('827603884', 'Album')
ksls['KSLA-0016~0017']=('827606781', 'Album')
ksls['KSLA-0018']=('823514303', 'Album')
ksls['KSLA-0019']=('870404014', 'Album')
ksls['KSLA-0020']=('828841767', 'O.S.T')
ksls['KSLA-0021']=('852744542', 'Album')
ksls['KSLA-0023~0024']=('813688318', 'Album')
ksls['KSLA-0025']=('835602145', 'O.S.T')
ksls['KSLA-0026']=('814159510', 'Single')
ksls['KSLA-0027']=('835492997', 'Drama')
ksls['KSLA-0028']=('778654390', 'Single')
ksls['KSLA-0029']=('835571900', 'Drama')
ksls['KSLA-0030~0031']=('835538686', 'Drama')
ksls['KSLA-0032']=('778636985', 'Album')
ksls['KSLA-0033~0035']=('784286860', 'O.S.T')
ksls['KSLA-0036']=('827628707', 'Single')
ksls['KSLA-0037']=('784387003', 'Album')
ksls['KSLA-0038']=('778548057', 'Single')
ksls['KSLA-0039~0040']=('794374323', 'Album')
ksls['KSLA-0042']=('784244764', 'Album')
ksls['KSLA-0043']=('784306182', 'O.S.T')
ksls['KSLA-0044']=('827630593', 'Single')
ksls['KSLA-0045~0046']=('806512967', 'Album')
ksls['KSLA-0047']=('778674781', 'Single')
ksls['KSLA-0048']=('797441697', 'Album')
ksls['KSLA-0049']=('778664886', 'Single')
ksls['KSLA-0050']=('778564623', 'Single')
ksls['KSLA-0051']=('838212890', 'Single')
ksls['KSLA-0052']=('838604626', 'Single')
ksls['KSLA-0053~0054']=('838213287', 'Single')
ksls['KSLA-0055']=('838212719', 'Single')
ksls['KSLA-0056']=('793021394', 'Single')
ksls['KSLA-0058']=('845149880', 'Album')
ksls['KSLA-0059~60']=('842476044', 'O.S.T')
ksls['KSLA-0061~0063']=('806473128', 'Album')
ksls['KSLA-0064']=('842370459', 'Single')
ksls['KSLA-0065']=('842374279', 'Single')
ksls['KSLA-0067']=('848603194', 'Single')
ksls['KSLA-0068']=('784226790', 'Album')
ksls['KSLA-0069']=('848137969', 'Single')
ksls['KSLA-0070']=('852132345', 'Album')
ksls['KSLA-0073~0075']=('848264194', 'O.S.T')
ksls['KSLA-0076']=('852115269', 'Album')
ksls['KSLA-0077']=('797458538', 'O.S.T')
ksls['KSLA-0078']=('806234962', 'Album')
ksls['KSLA-0079']=('797420170', 'Album')
ksls['KSLA-0080']=('852763774', 'Single')
ksls['KSLA-0081']=('852515337', 'O.S.T')
ksls['KSLA-0082~0083']=('903785943', 'Album')
ksls['KSLA-0084']=('794348046', 'Album')
ksls['KSLA-0087~0088']=('784236185', 'Single')
ksls['KSLA-0089']=('793020107', 'Album')
ksls['KSLA-0090']=('852237934', 'Album')
ksls['KSLA-0091']=('852153344', 'Album')
ksls['KSLA-0092']=('784399896', 'Single')
ksls['KSLA-0093']=('784318302', 'Single')
ksls['KSLM-0097']=('903878095', 'Album')
ksls['KSLA-0103~104']=('1047176678', 'Single')
ksls['KSLA-0105']=('1137562282', 'Single')
ksls['KSLA-0106']=('1137567006', 'Single')
ksls['KSLA-0108']=('1137585749', 'Album')
ksls['KSLA-0109']=('1137599218', 'Album')
ksls['KSLA-0110~111']=('1137602263', 'O.S.T')
ksls['KSLA-0117']=('1146701512', 'Single')
ksls['KSLA-0118']=('1146776232', 'Single')
ksls['KSLA-0119']=('1154353902', 'Single')
ksls['KSLA-0120']=('1167346271', 'Single')
ksls['KSLA-0121']=('1167345782', 'Single')
ksls['KSLA-0122~0123']=('1168996332', 'O.S.T')



ksl_od=collections.OrderedDict(sorted(ksls.items()))

queryID=''
first_flag=True
for key in ksl_od.keys():
    if(first_flag):
        queryID=ksl_od[key][0]
        first_flag=False
    else:
        queryID+=','+ksl_od[key][0]
        
        
countryList=['JP','HK','TW','US','RU']
totalPrice=[]
trackCount=[]

for country in countryList:
    url='https://itunes.apple.com/lookup?id='+queryID+'&country='+country+'&media=music'
    request=urllib2.Request(url)
    webpage=urllib2.urlopen(request).read()
    data=json.loads(webpage)
    
    i=0
    priceSum=0
    trackCnt=0
    for key in ksl_od.keys():
       ksl_od[key]+=(str(data['results'][i]['collectionPrice']),)
       priceSum+=data['results'][i]['collectionPrice']
       trackCnt+=data['results'][i]['trackCount']
       i+=1
    totalPrice.append(str(priceSum))
    trackCount.append(str(trackCnt))

print 'KSL Albums\t'+'\t'.join(countryList)
for key in ksl_od.keys():
    print key+'\t'+'\t'.join(ksl_od[key][2:])
print "==================="
print 'Total Price\t'+'\t'.join(totalPrice)
print 'Track Count\t'+'\t'.join(trackCount)

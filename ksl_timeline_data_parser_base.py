import urllib2
import json
import time
import csv
from bs4 import BeautifulSoup

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

countryCode='jp'
iTunesLookupURL='https://itunes.apple.com/'+countryCode+'/lookup?id='
iTunesTrackURL='https://itunes.apple.com/'+countryCode+'/album/id'

#TO keep SN order, do some trick when albums are having same release date (add 1 hour)
patch={}
patch['KSLA-0002']=('startDate','2001,8,10,1')
patch['KSLA-0003']=('startDate','2001,12,29')
patch['KSLA-0009']=('startDate','2003,12,28')
patch['KSLA-0010']=('startDate','2003,12,28,1')
patch['KSLA-0011']=('startDate','2004,4,28')
patch['KSLA-0012~0014']=('startDate','2004,8,13')
patch['KSLA-0015']=('startDate','2004,12,28')
patch['KSLA-0016~0017']=('startDate','2004,12,28,1')
patch['KSLA-0018']=('startDate','2005,8,12')
patch['KSLA-0020']=('startDate','2005,11,25')
patch['KSLA-0021']=('startDate','2005,12,29')
patch['KSLA-0025']=('startDate','2006,8,11')
patch['KSLA-0028']=('startDate','2007,5,25,1')
patch['KSLA-0030~0031']=('startDate','2007,7,27,1')
patch['KSLA-0032']=('startDate','2007,7,27,2')
patch['KSLA-0037']=('startDate','2007,12,29')
patch['KSLA-0038']=('startDate','2007,12,29,1')
patch['KSLA-0043']=('startDate','2008,8,15')
patch['KSLA-0047']=('startDate','2009,2,28')
patch['KSLA-0048']=('startDate','2009,2,28,1')
patch['KSLA-0049']=('startDate','2009,12,29')
patch['KSLA-0050']=('startDate','2009,12,29,1')
patch['KSLA-0056']=('startDate','2010,4,23,1')
patch['KSLA-0065']=('startDate','2010,12,08,1')
patch['KSLA-0069']=('startDate','2011,5,27,1')
patch['KSLA-0071']=('startDate','2011,6,24,1')
patch['KSLA-0073~0075']=('startDate','2011,8,12')
patch['KSLA-0076']=('startDate','2011,12,29')
patch['KSLA-0077']=('startDate','2011,12,29,1')
patch['KSLA-0078']=('startDate','2011,12,29,2')
patch['KSLA-0084']=('startDate','2012,07,29')
patch['KSLA-0090']=('startDate','2012,12,29')
patch['KSLA-0091']=('startDate','2012,12,29')

patch['KSLC-0004~0005']=('startDate','2009,2,28,2')
patch['KSLC-0006~0007']=('startDate','2009,2,28,3')

#To keep credit year right, replace patch
patch_cr={}
patch_cr['KSLA-0011']=('credit','2014','2004')
patch_cr['KSLA-0049']=('credit','2013','2009')
patch_cr['KSLA-0050']=('credit','2010','2009')
patch_cr['KSLA-0090']=('credit','2014','2012')
patch_cr['KSLA-0091']=('credit','2014','2012')

def lookupAlbumBasic(id):
    url=iTunesLookupURL+str(id)
    request=urllib2.Request(url)
    webpage=urllib2.urlopen(request).read()
    data=json.loads(webpage)
    return data

def parseTrackInfo(id):
    url=iTunesTrackURL+str(id)
    request=urllib2.Request(url)
    webpage=urllib2.urlopen(request).read()
    wp=BeautifulSoup(webpage)
    tracktable=wp.find_all("div", class_="track-list album music")[0]
    titles=tracktable.find_all("td", class_="name")
    artists=tracktable.find_all("td", class_="artist")
    times=tracktable.find_all("td", class_="time")
    tracks=[]
    for i in range(0, len(titles)):
        track={}
        track['index']=i+1
        track['title']=titles[i].span.text
        track['artist']=artists[i].span.text
        track['time']=times[i].span.text
        tracks.append(track)
    return tracks

def outputAlbum(SN, basic, tracks):
    albumdata={}
    basic=basic['results'][0]
    
    parsed_time=time.strptime(basic['releaseDate'], "%Y-%m-%dT%H:%M:%SZ")
    albumdata['startDate']=str(parsed_time.tm_year)+','+str(parsed_time.tm_mon)+','+str(parsed_time.tm_mday)
    albumdata['headline']=basic['collectionName']
    #albumdata['tag']=ksls[SN][1]
    asset={}
    asset['media']=basic['artworkUrl100'].replace('100x100-75','1200x1200-75')
    asset['thumbnail']=basic['artworkUrl60']
    asset['credit']='<a href=\''+basic['collectionViewUrl']+'\' target="_blank">'+basic['copyright']+'</a>'
    asset['caption']=SN
    albumdata['asset']=asset
    
    text=''
    artists=set()
    for track in tracks:
        text=text+'{:02}'.format(track['index'])+'. '+track['title']+'<br/>'
        for art in track['artist'].replace(' & ',', ').split(', '):
            if art!='VisualArt\'s / Key Sounds Label':
                artists.add(art)
                
    if len(artists)>0:
        artists=list(artists)
        if len(artists)==1:
            text=text+'<br/>Artist: '+artists[0]
        else:
            text=text+'<br/>Artists: '+artists[0]
            for i in range(1, len(artists)):
                text=text+', '+artists[i]
    
    albumdata['text']=text
    return albumdata
    

def outputCSV2JSON(csvfile):
    csvfile = open(csvfile, 'r')
    reader = csv.DictReader( csvfile )
    data=[ row for row in reader ]
    newdata=[]
    for row in data:
        parsed_time=time.strptime(row['Start Date'], "%m/%d/%Y %H:%M:%S")
    
        newrow={}
        newrow['startDate']=str(parsed_time.tm_year)+','+str(parsed_time.tm_mon)+','+str(parsed_time.tm_mday)
        newrow['headline']=row['Headline']
        newrow['text']=row['Text'].replace('\n','')
        #newrow['tag']=row['Tag']
    
        asset={}
        asset['media']=row['Media']
        asset['thumbnail']=row['Media Thumbnail']
        asset['credit']=row['Media Credit']
        asset['caption']=row['Media Caption']
        newrow['asset']=asset
    
        newdata.append(newrow)
    return newdata

def patchData(data):
    for album in data:
        SN=album['asset']['caption']
        if SN in patch.keys():
            key=patch[SN][0]
            value=patch[SN][1]
            album[key]=value
        if SN in patch_cr.keys():
            key=patch_cr[SN][0]
            album['asset'][key]=album['asset'][key].replace(patch_cr[SN][1],patch_cr[SN][2])
    return data


jsonfile = open('ksl.json', 'w')
ksl={}
ksl['headline']='Key Sounds Label Timeline'
ksl['text']='<p>Last update: 2014/8<br/>webpage made by <a href=\'http://about.me/goodbest\'>goodbest</a><br/>Special Thanks to KSLU group</p><br/>*All dates are album\'s first release date'
ksl['asset']={"media":"img/ksl_logo.png"}
ksl['type']='default'

dates=[]
for i in ksls.keys():
    albumID=ksls[i][0]
    dates.append(outputAlbum(i, lookupAlbumBasic(albumID), parseTrackInfo(albumID)))
    time.sleep(5)
    
csvdata=outputCSV2JSON('ksl_not_in_itunes.csv')
for i in csvdata:
    dates.append(i)

dates=patchData(dates)

ksl['date']=dates

out = json.dumps({'timeline': ksl})
jsonfile.write(out)
    
# Import frameworks
import os
import music_tag
import logging

#Init
def f_init():
    # global vDirectory = "/Volumes/Muziek/Muzieklijsten/Zomer Top50 kopie"
    global vDirectory 
    global vForce
    global vTotalTracks
    global vAlbum
    global vDiscnumber
    global vTotaldiscs
    global vComment
    vDirectory = "/Volumes/Muziek/Muzieklijsten/ArrowRock/2022/Top 500"
    vForce = 1
    vTotalTracks = 500
    vAlbum = "ArrowRock Top 500 - 2022 - The Long Versions"
    vDiscnumber = 1
    vTotaldiscs = 1
    vComment = "Compiled by Jan"

def f_init_logging():
    #Set logging level and output
    # Gets or creates a logger
    global logger
    logger = logging.getLogger(__name__)  

    # set log level
    logger.setLevel(logging.INFO)

    # define file handler and set formatter
    file_handler = logging.FileHandler('Readmusictags.log')
    formatter    = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
    file_handler.setFormatter(formatter)

    # add file handler to logger
    logger.addHandler(file_handler)

def f_process():
    for filename in os.listdir(vDirectory):
        if filename.endswith(".aiff") or filename.endswith(".flac") or filename.endswith(".wav") or filename.endswith(".aif"): 
            f = music_tag.load_file(os.path.join(vDirectory, filename))
            vNumber = filename[0:3]
            #print(type(vNumber))
            #print(type(f['tracknumber']))
            #print(int(vNumber))
            #print(int(f['tracknumber']))
            try:
                if int(vNumber) != int(f['tracknumber']) or vForce == 1:
                    vLoginfo = str(f['tracknumber']) + " - " + os.path.join(vDirectory, filename) + " - " + str(vNumber)
                    logger.info(vLoginfo)
                    f['tracknumber'] = int(vNumber)
                    f['totaltracks'] = vTotalTracks
                    f['album'] = vAlbum
                    f['discnumber'] = vDiscnumber
                    f['totaldiscs'] = vTotaldiscs
                    f['comment'] = vComment
                    f['album artist'] = ""
                    f.save()
            except:
                template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                message = template.format(type(ex).__name__, ex.args)
                print(message)

# Main body

f_init()
f_init_logging()
f_process()

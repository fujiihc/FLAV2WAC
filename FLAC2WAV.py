import os
import soundfile as sf
import taglib

#test virtual environment
from mutagen.wave import WAVE


def FLAV2WAC(path, boolean):   
    if os.path.exists(path):    
        for dirpath, dirs, files in os.walk(path):
            for file in files:
                fileName = os.path.splitext(file)
                masterPath = dirpath + '\\' + fileName[0]
                if boolean:
                    swap('.flac', '.wav', fileName, masterPath)
                else:
                    swap('.wav', '.flac', fileName, masterPath)             
        return True               
    return False


def swap(start, end, fileName, masterPath):

    if fileName[1] == start:
        if start == '.flac':
            data, sampleRate = sf.read(masterPath + start)
            sf.write(masterPath + end, data, sampleRate, 'PCM_16')
            #use something that isnt pytaglib
            #create second virual envionment
            #mutagen for wav tags

            sav = taglib.File(masterPath + end)

            #sav.tags = taglib.File(masterPath + start).tags

            #sav.save()
            sav.close()

            wav = WAVE(masterPath + end)
            print(wav.tags)
            wav.add_tags()

            #https://from-locals.com/python-mutagen-mp3-id3/

            os.remove(masterPath + start)
        else:
            data, sampleRate = sf.read(masterPath + start)
            sf.write(masterPath + end, data, sampleRate, 'PCM_16')
            sav = taglib.File(masterPath + end)
            sav.tags = taglib.File(masterPath + start).tags
            sav.save()
            sav.close()
            os.remove(masterPath + start)


print('Please Make Sure To Backup Your FLAC/WAV Files Elsewhere As This Program Will Convert Them.')
print('----------------------------------------------------------------------------------------------')
cont = True
while cont:
    path = input('Enter File Path Where FLAC/WAV Files Exist: ')
    convType = ''
    convBool = True

    while True:
        convert = input('Converting From FLAC -> WAV Or WAV -> FLAC? (F/W): ')
        if convert == 'F' or convert == 'f':
            convType = 'FLAC -> WAV'
            break
        elif convert == 'W' or convert == 'w':
            convType = 'WAV -> FLAC'
            convBool = False
            break
        else:
            print('>> Invalid Input.')
    
    while True:
        conf = input('Confirm Conversion Of ' + convType + ' At Path "' + path + '"? (Y/N): ')
        if (conf == 'Y' or conf == 'y') and convType != '':
            if FLAV2WAC(path, convBool):
                if convBool:
                    print('>> FLAC Files Converted To WAV.')
                else:
                    print('>> WAV Files Converted To FLAC.')
            else:      
                print('>> Path Not Found.')
            break
        elif conf == 'N' or conf == 'n':
            print('>> Conversion Terminated.')
            break
        else:
            print('>> Invalid Input.')
    
    while True:
        ans = input('Continue? (Y/N): ')
        if ans == 'N' or ans == 'n':
            cont = False
            break
        elif ans == 'Y' or ans == 'y':
            print('>> Continuing...')
            break
        else:
            print('>> Invalid Input.')
input('>> Hit Any Key To Close Program.')
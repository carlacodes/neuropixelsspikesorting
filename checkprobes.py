from pathlib import Path
from tqdm import tqdm
import matplotlib.pyplot as plt
import spikeinterface.extractors as se
from probeinterface.plotting import plot_probe
import glob
from glob import glob
import os
from spikesorting_scripts.helpers import get_channelmap_names
##Author - Jules

def main():
    savedir = Path('D:/Data/probefiguresneuropixels/AM')
    datadir = Path('E:/Electrophysiological_Data')
    ferret = 'F2103_Fettucini'
    subfolder ='/'
    fulldir = datadir / ferret


    #get all the folder namesD
    print([f.name for f in fulldir.glob('*g0')])
    list_subfolders_with_paths = [f.path for f in os.scandir(fulldir) if f.is_dir()]
    session_list = list(fulldir.glob('*_g0'))

    for session in tqdm(session_list):
        recording = se.read_spikeglx(session, stream_id='imec0.ap')
        probe = recording.get_probe()
        fig, ax = plt.subplots(1,1,figsize=(10, 10), dpi=300)
        plot_probe(probe, ax=ax)

        fig.savefig(savedir / f'probe_{session.name}.png', dpi=300)



def getchanmapnames():
    datadir = Path('E:/Electrophysiological_Data')
    ferret='F2103_Fettucini'
    subfolder ='/'
    fulldir = datadir / ferret
    print([f.name for f in fulldir.glob('*g0')])
    list_subfolders_with_paths = [f.path for f in os.scandir(fulldir) if f.is_dir()]
    session_list = list(fulldir.glob('*_g0'))
    bigdict = {}
    for session in tqdm(session_list):

        chanmapdict = get_channelmap_names(session)
        print(chanmapdict)
        #
        # print(chanmapdict)
        #append chan map dict to big dict
        bigdict[session] =chanmapdict
    return chanmapdict

    #get the channel map name

if __name__ == '__main__':
    chanmapdict = getchanmapnames()
    #main()
def load_eeg(filename):
    # CONVERT BACK TO ASCII OR WHAT?
    # import eeg_pyload
    #raw = eeg_pyload.load_eeg('C:/Users/OMISTAJA/Desktop/sample_eeg/20170809_MREG_FA5_20170809_043827_end_bin_ica.dat')
    
    
    filename_eeg = str(filename)
    filename_eeg = filename_eeg.split('.')  
    filename_eeg = filename_eeg[0]
    
    with open(filename_eeg + '.vhdr') as f:
        lines = f.readlines()
    
    dataformat = [s for s in lines if 'DataFormat' in s]
    dataformat=dataformat[0]
    dataformat = dataformat.split('DataFormat=')
    dataformat = dataformat[1]
    
    
    if dataformat == "BINARY\n":
 
        chan_lkm = [s for s in lines if 'NumberOfChannels=' in s]
        sample_lkm = [s for s in lines if 'DataPoints=' in s]
        orientation = [s for s in lines if 'DataOrientation=' in s]
        samplinginter = [s for s in lines if 'SamplingInterval=' in s]

        chan_lkm = chan_lkm[0]; chan_lkm = chan_lkm.split('NumberOfChannels=')
        chan_lkm = chan_lkm[1]
        sample_lkm = sample_lkm[0]; sample_lkm = sample_lkm.split('DataPoints=')
        sample_lkm = sample_lkm[1]
        orientation = orientation[0]; orientation = orientation.split('DataOrientation=')
        orientation = orientation[1]
        samplinginter = samplinginter[0]; samplinginter = samplinginter.split('SamplingInterval=')
        samplinginter = samplinginter[1]
        srate = int(1000000 / int(samplinginter))
        

        if orientation == 'MULTIPLEXED\n':
         
            import numpy as np
            dtype = np.dtype('i4') # 32-bit signed integrer
            with open(filename_eeg + '.dat') as fid:
                raw = np.fromfile(fid,dtype).reshape(int(chan_lkm),int(sample_lkm))
    
        elif orientation == 'VECTORIZED\n':

            import numpy as np
            dtype = np.dtype('i4') # 32-bit signed integrer
            with open(filename_eeg + '.dat') as fid:
                raw = np.fromfile(fid,dtype).reshape(int(sample_lkm),int(chan_lkm)).T

        else:
             print('Data orientation not recognized')
             
      
    else:
            pass
            #with open(filename_eeg + '.dat', 'r') as fid:
            #   raw = fid.read()
    return raw
            
if __name__ == '__main__':
    globals()[sys.argv[1]]()
    
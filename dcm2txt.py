import pydicom

read_file = 'ttfm.dcm' # or 'ttfm.dcm'

ds = pydicom.read_file(read_file)
tag_names = ds.dir()

write_file = 'display_TTFM.txt' # or 'display_TTFM.txt'

with open(write_file,'w') as f:
    for tag in tag_names:
        f.write(tag+" : ")
        data_element = ds.data_element(tag)
        vr = data_element.VR
        
        # if the value is a sequence we have to show the inner tags also
        if vr=="SQ":
            f.write("\n")
            seq = data_element.value
            for i in range(0,len(seq)):
                inner_tags = seq[i].dir()
                for t in inner_tags:
                    f.write(t+" - ") 
                    delement = seq[i].data_element(t)
                    f.write(str(delement.value))
                    f.write("\n")
                    
        # if the value representation format is not pixel data 
        # then we show the value       
        elif vr!="OW" :
            f.write(str(data_element.value))
            f.write("\n")
            
        # if pixel data we dont show anything   
        else : f.write("\n")  
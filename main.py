from rembg import remove

input_path = "sincap.jpeg"
output_path = "output.png"
#arka tarafı transparan olan resimleri png destekler.

#rb read binary , wb write binary

with open(input_path,'rb') as i:
    with open (output_path,'wb') as o:
        input_file = i.read()
        output_file = remove(input_file)
        o.write(output_file)
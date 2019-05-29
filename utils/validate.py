FILE_TYPE='csv'

def check_file(filename):
    return filename.rsplit(".",1)[1].lower()==FILE_TYPE
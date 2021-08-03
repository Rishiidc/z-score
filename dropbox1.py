import dropbox

class transfer:
    def __init__(self,accesstoken):
        self.accesstoken = accesstoken
    def uploadfile(self,sourcefile,destinationfile):
        """Hello, we are going to upload a file to dropbox"""
        connection = dropbox.Dropbox(self.accesstoken)
        with open(sourcefile,"rb")as f:
            connection.files_upload(f.read(),destinationfile)
    
def main():
    accesstoken = "sl.Ay-9VWXIk8lVDj09I8wmPZiIM-V1KhxW6Q5WZosKIsijz5wZBnvnE0kjcRqQmbjXmyIBCTG12SVlVu4kR1hHahFQpzR8yjGmvSn3Hv_u8aE9TZ2qTU3fAWyZvABt5uvmKc9PGWYzAaM"
    transferdata = transfer(accesstoken)
    source = input("Enter the name of the file")
    destination = input("Enter the destination")
    transferdata.uploadfile(source,destination)

if __name__ == "__main__":
    main()
 

    
       

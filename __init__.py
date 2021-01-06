import subprocess

mode = input('Enter the function you want to use: ').lower()
dirName = input('Enter the directory of the files: ')

if mode == 'encrypt':
    imageName = input('Enter the file name of the image: ')
    folderName = input('Enter the file name of the file/folder: ')

    imageRename = input('Enter the new name of the image: ')

    commands = \
        f'cd ~/"{dirName}" &&' \ # go to the directory where the file to be encoded is located at
        f'ditto -c -k --sequesterRsrc "{folderName}" archive.zip &&' \ # first zip the folder/file so that it can later be merged with the image file 
        f'cat "{imageName}" archive.zip > "{imageRename}" &&' \ # concatenate the image and the zip file to form a another new image
        f'rm archive.zip' # finally remove the zip file, as it only acts as an intermediate
elif mode == 'decrypt':
    imageName = input('Enter the file name of the image to be decomposed: ')

    commands = \
        f'cd ~/"{dirName}" &&' \
        f'unzip "{imageName}"'

p = subprocess.Popen([commands], shell=True) # to execute the commands

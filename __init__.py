import subprocess

mode = input('Enter the function you want to use: ').lower()
dirName = input('Enter the directory of the files: ')

if mode == 'encrypt':
    imageName = input('Enter the file name of the image: ')
    folderName = input('Enter the file name of the folder: ')

    imageRename = input('Enter the new name of the image: ')

    commands = \
        f'cd ~/"{dirName}" &&' \
        f'ditto -c -k --sequesterRsrc "{folderName}" archive.zip &&' \
        f'cat "{imageName}" archive.zip > "{imageRename}" &&' \
        f'rm archive.zip'
elif mode == 'decrypt':
    imageName = input('Enter the file name of the image to be decomposed: ')

    commands = \
        f'cd ~/"{dirName}" &&' \
        f'unzip "{imageName}"'

p = subprocess.Popen([commands], shell=True)

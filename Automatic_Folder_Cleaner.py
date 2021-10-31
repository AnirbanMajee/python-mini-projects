import os


def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


def move(folderName, files):
    for file in files:
        os.replace(file, f"{folderName}/{file}")


if __name__ == '__main__':

    files = os.listdir()
    files.remove("file.py")

    createIfNotExist('Images')
    createIfNotExist('Docs')
    createIfNotExist('Media')
    createIfNotExist('Others')

    imgExts = [".png", ".svg", ".jpg", ".jpeg"]
    images = [file for file in files if os.path.splitext(file)[
        1].lower() in imgExts]

    docExts = [".txt", ".doc", ".docx", ".pdf"]
    docs = [file for file in files if os.path.splitext(file)[
        1].lower() in docExts]

    mediaExts = [".mp4", ".mp3", ".flv", ".mp5", ".song"]
    medias = [file for file in files if os.path.splitext(file)[
        1].lower() in mediaExts]

    others = []
    for file in files:
        ext = os.psth.splitext(file)[1].lower()
        if (ext not in mediaExts) and (ext not in docExts) and (ext not in imgExts) and os.path.isfile(file):
            others.append(file)

move("Images", images)
move("Docs", docs)
move("Media", medias)
move("Others", others)

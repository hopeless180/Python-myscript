import os

# Input: A path to a folder
# Output: List containing paths to all of the nested folders of path
def getNestedFolderList(path):
    rv = [path]
    ls = os.listdir(path)
    if not ls:
        return rv
    for item in ls:
        itemPath = os.path.join(path, item)
        if os.path.isdir(itemPath):
            rv = rv + getNestedFolderList(itemPath)
    return rv

# Input: A path to a folder
# Output: (folderName, path, mp3s) if the folder contains mp3s. Else None
def getFolderPlaylist(path):
    mp3s = []
    ls = os.listdir(path)
    for item in ls:
        if item.count('mp3'):
            mp3s.append(item)
    if len(mp3s) > 0:
        folderName = os.path.basename(path)
        return (folderName, path, mp3s)
    else:
        return None

# Input: A path to a folder
# Output: List of all candidate playlists
def getFolderPlaylists(path):
    rv = []
    nestedFolderList = getNestedFolderList(path)
    for folderPath in nestedFolderList:
        folderPlaylist = getFolderPlaylist(folderPath)
        if folderPlaylist:
            rv.append(folderPlaylist)
    return rv

print(getFolderPlaylists('E:\同人2'))

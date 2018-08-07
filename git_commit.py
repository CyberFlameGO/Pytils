import subprocess as sp
from datetime import date


def getDate():
    currentDate = date.today()
    return format('{currDate.year}-{currDate.month}-{currDate.day}')


def movePosts():
    lsProcess = sp.run('ls ./_drafts', shell=True)
    fileList = lsProcess.stdout.decode('utf-8').strip().split('\n')
    newPost = len(fileList)

    if newPost == 1:
        print('A new post has been detected')
        srcName = './_drafts/' + fileList[0]
        destName = './_post/' + getDate() + '-' + fileList[0]
        cmd = 'mv ' + srcName + destName
        sp.run(cmd, shell=True)

        return [destName, fileList[0]]

    elif newPost == 0:
        print('No new posts detected!')
    else:
        print('Too many posts have been found, unable continue process')


def runGit(fullPath, fileName, message):
        cmd1 = 'git add ' + fullPath
        cmd2 = 'git commit -m ' + message
        cmds = [cmd1, cmd2]

        for cmd in cmds:
            cp = sp.run(cmd, shell=True)

        if __name__ == '__main__':
            path_post, file_name = movePosts()
            runGit(path_post, file_name, 'Adds in new blog post')
            print('Running git commands completed!')
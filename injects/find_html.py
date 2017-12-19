import os


def locate(pattern, root=os.curdir):
    html_files = []
    for path, dirs, files in os.walk(os.path.abspath(root)):
        for f in files:
            if f.endswith(".html"):
                html_files.append("%s\%s" % (path, f))

    print html_files


locate("", "..")

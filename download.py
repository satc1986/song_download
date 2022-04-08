from pytube import YouTube
import os
#where to save
SAVE_PATH = "./assets" #to_do

#link of the video to be downloaded
# link=["https://www.youtube.com/watch?v=xWOoBJUqlbI",
#     "https://www.youtube.com/watch?v=xWOoBJUqlbI"
#     ]

link = ["https://www.youtube.com/watch?v=ApXoWvfEYVU", "https://www.youtube.com/watch?v=fWt3mLPUs7g", "https://www.youtube.com/watch?v=UlyIKdSmq0Y", "https://www.youtube.com/watch?v=u35SoCPkMf0", "https://www.youtube.com/watch?v=2hL1aiKotGQ", "https://www.youtube.com/watch?v=KP_XkN2v7OM", "https://www.youtube.com/watch?v=l9PxOanFjxQ", "https://www.youtube.com/watch?v=mWRsgZuwf_8"]

for i in link:
    try:

        # object creation using YouTube
        # which was imported in the beginning
        yt = YouTube(i)
    except:

        #to handle exception
        print("Connection Error")

    #filters out all the files with "mp4" extension
    mp4file = yt.streams.filter(only_audio=True)
    print(mp4file[0])
    # get the video with the extension and
    # resolution passed in the get() function

    try:
        # downloading the video
        out = mp4file[0].download(SAVE_PATH)
        base, ext = os.path.splitext(out)
        new_file = base + ".mp3"
        os.rename(out, new_file)

    except:
        print("Some Error!")


print('Task Completed!')

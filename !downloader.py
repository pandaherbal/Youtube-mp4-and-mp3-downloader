from __future__ import unicode_literals
import youtube_dl


def repeat():
    print (".__       ___.          .__   ")
    print ("|__| _____\_ |__ _____  |  |  ")
    print ("|  |/ ____/| __ \\__  \ |  |  ")
    print ("|  < <_|  || \_\ \/ __ \|  |__")
    print ("|__|\__   ||___  (____  /____/")
    print ("       |__|    \/     \/      ")

    print ("selamat datang")
    print("halo, mau download video atau lagu?")
    print("[1] untuk video")
    print("[2] untuk lagu")

    opsi = int(input (" jawaban anda : "))
    if opsi == 1 :
        from pytube import YouTube

        link = input("MASUKKAN LINK YOUTUBE : ")
        yt = YouTube(link)

        print("mohon tunggu...")
        video = yt.streams.get_highest_resolution()
        video.download()
        print("video anda sudah didownload")

    if opsi == 2 :
        import youtube_dl
        def run():
            video_url = input("MASUKKAN LINK YOUTUBE:")
            video_info = youtube_dl.YoutubeDL().extract_info(
                url = video_url,download=False
            )
            filename = f"{video_info['title']}.mp3"
            options={
                'format':'bestaudio/best',
                'keepvideo':False,
                'outtmpl':filename,
            }

            with youtube_dl.YoutubeDL(options) as ydl:
                ydl.download([video_info['webpage_url']])

            print("Download selesai... {}".format(filename))

        if __name__=='__main__':
            run()

while True :
    repeat()

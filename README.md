# you_tube_downloader
If you are facing problem with current pytube version, it's recommended to uninstall current version and install pytube3. Just do pip uninstall pytube and then pip install pytube3 --upgrade
# Also with recent pytube update, we are only allowed to download videos that are by default allowed by creators or copyright free for usage. It's recommended to search "copyright free music".

#Here this itag is important, itag 22 means (720p at 30fps). Now each video has different resolution and you need to check their itag before downloading or you can simply use .first() instead of .get_by_itag() method. Here .first() download video in the highest possible resolution, selected automatically.

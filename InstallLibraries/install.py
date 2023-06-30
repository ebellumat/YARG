import requests, zipfile, io, os, shutil

PATH = os.path.dirname(os.path.realpath(__file__))
DEST_PATH = f"{PATH}/../Assets/Plugins/BassNative"
URL = "https://www.un4seen.com/files/"

def download(name, prefix=""):
    req = requests.get(f"{URL}/{prefix}{name}")
    zip = zipfile.ZipFile(io.BytesIO(req.content))
    zip.extractall(f"{PATH}/{name}")

def move(start, to):
    os.makedirs(os.path.dirname(f"{DEST_PATH}/{to}"), exist_ok=True)
    shutil.copy(f"{PATH}/{start}", f"{DEST_PATH}/{to}")

# Check if we are in the repo
if not os.path.exists(DEST_PATH):
    print("You are not in the YARG repo. Make sure you keep the script in the `InstallLibraries` folder.")
    exit()

# Delete old stuff
if os.path.exists(f"{PATH}/../Assets/Libraries"):
    shutil.rmtree(f"{PATH}/../Assets/Libraries")

# Install BASS
download("bass24.zip")
move("bass24.zip/bass.dll", "Windows/x86/bass.dll")
move("bass24.zip/x64/bass.dll", "Windows/x86_64/bass.dll")

download("bass24-linux.zip")
move("bass24-linux.zip/libs/x86_64/libbass.so", "Linux/x86_64/libbass.so")

download("bass24-osx.zip")
move("bass24-osx.zip/libbass.dylib", "Mac/libbass.dylib")

download("bass24-android.zip")
move("bass24-android.zip/libs/arm64-v8a/libbass.so", "Android/arm64-v8a/libbass.so")
move("bass24-android.zip/libs/armeabi-v7a/libbass.so", "Android/armeabi-v7a/libbass.so")
move("bass24-android.zip/libs/x86/libbass.so", "Android/x86/libbass.so")
move("bass24-android.zip/libs/x86_64/libbass.so", "Android/x86_64/libbass.so")

# Install BASSOPUS
download("bassopus24.zip")
move("bassopus24.zip/bassopus.dll", "Windows/x86/bassopus.dll")
move("bassopus24.zip/x64/bassopus.dll", "Windows/x86_64/bassopus.dll")

download("bassopus24-linux.zip")
move("bassopus24-linux.zip/libs/x86_64/libbassopus.so", "Linux/x86_64/libbassopus.so")

download("bassopus24-osx.zip")
move("bassopus24-osx.zip/libbassopus.dylib", "Mac/libbassopus.dylib")

download("bassopus24-android.zip")
move("bassopus24-android.zip/libs/arm64-v8a/libbassopus.so", "Android/arm64-v8a/libbassopus.so")
move("bassopus24-android.zip/libs/armeabi-v7a/libbassopus.so", "Android/armeabi-v7a/libbassopus.so")
move("bassopus24-android.zip/libs/x86/libbassopus.so", "Android/x86/libbassopus.so")
move("bassopus24-android.zip/libs/x86_64/libbassopus.so", "Android/x86_64/libbassopus.so")

# Install BASSmix
download("bassmix24.zip")
move("bassmix24.zip/bassmix.dll", "Windows/x86/bassmix.dll")
move("bassmix24.zip/x64/bassmix.dll", "Windows/x86_64/bassmix.dll")

download("bassmix24-linux.zip")
move("bassmix24-linux.zip/libs/x86_64/libbassmix.so", "Linux/x86_64/libbassmix.so")

download("bassmix24-osx.zip")
move("bassmix24-osx.zip/libbassmix.dylib", "Mac/libbassmix.dylib")

download("bassmix24-android.zip")
move("bassmix24-android.zip/libs/arm64-v8a/libbassmix.so", "Android/arm64-v8a/libbassmix.so")
move("bassmix24-android.zip/libs/armeabi-v7a/libbassmix.so", "Android/armeabi-v7a/libbassmix.so")
move("bassmix24-android.zip/libs/x86/libbassmix.so", "Android/x86/libbassmix.so")
move("bassmix24-android.zip/libs/x86_64/libbassmix.so", "Android/x86_64/libbassmix.so")

# Install BASS FX
download("bass_fx24.zip", "z/0/")
move("bass_fx24.zip/bass_fx.dll", "Windows/x86/bass_fx.dll")
move("bass_fx24.zip/x64/bass_fx.dll", "Windows/x86_64/bass_fx.dll")

download("bass_fx24-linux.zip", "z/0/")
move("bass_fx24-linux.zip/libs/x86_64/libbass_fx.so", "Linux/x86_64/libbass_fx.so")

download("bass_fx24-osx.zip", "z/0/")
move("bass_fx24-osx.zip/libbass_fx.dylib", "Mac/libbass_fx.dylib")

download("bass_fx24-android.zip", "z/0/")
move("bass_fx24-android.zip/libs/arm64-v8a/libbass_fx.so", "Android/arm64-v8a/libbass_fx.so")
move("bass_fx24-android.zip/libs/armeabi-v7a/libbass_fx.so", "Android/armeabi-v7a/libbass_fx.so")
move("bass_fx24-android.zip/libs/x86/libbass_fx.so", "Android/x86/libbass_fx.so")
move("bass_fx24-android.zip/libs/x86_64/libbass_fx.so", "Android/x86_64/libbass_fx.so")

# Clean up
shutil.rmtree(f"{PATH}/bass24.zip")
shutil.rmtree(f"{PATH}/bass24-linux.zip")
shutil.rmtree(f"{PATH}/bass24-osx.zip")
shutil.rmtree(f"{PATH}/bass24-android.zip")

shutil.rmtree(f"{PATH}/bassopus24.zip")
shutil.rmtree(f"{PATH}/bassopus24-linux.zip")
shutil.rmtree(f"{PATH}/bassopus24-osx.zip")
shutil.rmtree(f"{PATH}/bassopus24-android.zip")

shutil.rmtree(f"{PATH}/bassmix24.zip")
shutil.rmtree(f"{PATH}/bassmix24-linux.zip")
shutil.rmtree(f"{PATH}/bassmix24-osx.zip")
shutil.rmtree(f"{PATH}/bassmix24-android.zip")

shutil.rmtree(f"{PATH}/bass_fx24.zip")
shutil.rmtree(f"{PATH}/bass_fx24-linux.zip")
shutil.rmtree(f"{PATH}/bass_fx24-osx.zip")
shutil.rmtree(f"{PATH}/bass_fx24-android.zip")

print("Done!")

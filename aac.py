#!/usr/bin/python3

import os

version = "1.0_061115"
print("\nWelcome on ACC " + version)
print("\nYou need to launch this program where you want to see your sources.")
print("\n\nFolder name for the sources : ")
name_of_folder = input()

#Init
os.system("mkdir -p " + name_of_folder)
os.chdir(name_of_folder)
print("\nThat's good, now just wait, we're gonna download things you need to build.")

#Download java
os.system("sudo apt-add-repository ppa:webupd8team/java && sudo apt-get update && sudo apt-get install oracle-java7-installer")
print("Okay, java is ready to work !")

#Download other things
os.system("sudo apt-get install git-core gnupg flex bison gperf build-essential \
  zip curl zlib1g-dev gcc-multilib g++-multilib libc6-dev-i386 \
  lib32ncurses5-dev x11proto-core-dev libx11-dev lib32z-dev ccache \
  libgl1-mesa-dev libxml2-utils xsltproc unzip lzop")
print("Done !")

#Init sources
print("Okay, you have to tell wich sources you want to build.\n")
print("1.CyanogenMod\n2.AOSP (in work)")

choose = input()

if choose == "1":
    print("So, you chose CyanogenMod, but wich branch ?\n")
    print("1.CM-12.0\n2.CM-12.1\n3.CM-13.0 (Not ready at all)")
    b = input()
    if b == "1":
        b = "cm-12.0"
    if b == "2":
        b = "cm-12.1"
    if b == "3":
        b = "cm-13.0"

    os.system("repo init -u https://www.github.com/CyanogenMod/android -b " + b)

if choose == "2":
    print("So, you chose AOSP but wich version ?\n")
    print("1.Android 5.1.1\n2.Android 6.0.0")
    v = input()
    if v == "1":
        version = "android-5.1.1_r9"
    if v == "2":
        version = "android-6.0.0_r26"
    os.system("repo init -u https://www.android.googlesource.com/platform/manifest/ -b " + version)

print("Repo is successfully initialized.\n")

# Time to download all that s***
print("Download the sources ? (Yes/No)\n")

answer = input()

if answer == "Yes":
    os.system("repo sync")
    print("Repo successfully downloaded.\n")

if answer == "No":
    os.system("exit")

# Time to build
print("Now we can build our ROM.\n")
print("... but for wich device ? (Depending of the disponibility of your device at CM)\n")
your_device = input()
os.system("source build/envsetup.sh && brunch " + your_device)

print("If you had no errors, your ROM is ready to use.\nYou can find it at \out\ target\product\your_device\nDon't forget to share your build !")

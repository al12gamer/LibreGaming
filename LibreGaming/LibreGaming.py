import os, subprocess
import argparse

global distro
distro = ["apt","yay", "paru", "pacman", "dnf"]
global found 
dir = os.path.dirname(__file__)
script = os.path.join(dir, 'getPackageManager.sh') # get the path to the package manager script
found = subprocess.getoutput("sh "+script)      # run the script 
#print (found)

def installPkgs():
    if found == distro[0]:  #packages for Ubuntu and Ubuntu based distros
        print("\nNow installing Ubuntu Gaming Packages")
        Ubuntu = [
            "wget -nc https://dl.winehq.org/wine-builds/winehq.key",
            "sudo apt-key add winehq.key",
            "sudo add-apt-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ focal main' -y",
            "sudo add-apt-repository ppa:lutris-team/lutris -y",
            "sudo add-apt-repository multiverse -y",
            "sudo add-apt-repository ppa:flexiondotorg/mangohud -y",
            "sudo apt update",
            "sudo apt-get install --install-recommends winehq-staging -y",
            "sudo apt-get install libgnutls30:i386 libldap-2.4-2:i386 libgpg-error0:i386 libxml2:i386 libasound2-plugins:i386 libsdl2-2.0-0:i386 libfreetype6:i386 libdbus-1-3:i386 libsqlite3-0:i386 -y",
            "sudo apt-get install lutris python3-pip meson libsystemd-dev pkg-config ninja-build git libdbus-1-dev libinih-dev dbus-user-session steam goverlay -y"
            ]  
        for i in Ubuntu:
            os.system(i) #running each element in Ubuntu array 

    elif found == distro[1] or found == distro[2]:    #packages for Arch and Arch based distros
        print("\nNow installing Arch Gaming Packages")   #for those who have AUR enabled
        Arch = found+" -S goverlay-bin python-pip wine-staging giflib lib32-giflib libpng lib32-libpng libldap lib32-libldap gnutls lib32-gnutls mpg123 lib32-mpg123 openal lib32-openal v4l-utils lib32-v4l-utils libpulse lib32-libpulse libgpg-error lib32-libgpg-error alsa-plugins lib32-alsa-plugins alsa-lib lib32-alsa-lib libjpeg-turbo lib32-libjpeg-turbo sqlite lib32-sqlite libxcomposite lib32-libxcomposite libxinerama lib32-libgcrypt libgcrypt lib32-libxinerama ncurses lib32-ncurses opencl-icd-loader lib32-opencl-icd-loader libxslt lib32-libxslt libva lib32-libva gtk3 lib32-gtk3 gst-plugins-base-libs lib32-gst-plugins-base-libs vulkan-icd-loader lib32-vulkan-icd-loader lutris steam gamemode --needed --noconfirm"
        os.system(Arch)
    elif found == distro[3]:    
        print("\nNow installing Arch Gaming Packages")
        Arch = "sudo pacman -S python-pip wine-staging giflib lib32-giflib libpng lib32-libpng libldap lib32-libldap gnutls lib32-gnutls mpg123 lib32-mpg123 openal lib32-openal v4l-utils lib32-v4l-utils libpulse lib32-libpulse libgpg-error lib32-libgpg-error alsa-plugins lib32-alsa-plugins alsa-lib lib32-alsa-lib libjpeg-turbo lib32-libjpeg-turbo sqlite lib32-sqlite libxcomposite lib32-libxcomposite libxinerama lib32-libgcrypt libgcrypt lib32-libxinerama ncurses lib32-ncurses opencl-icd-loader lib32-opencl-icd-loader libxslt lib32-libxslt libva lib32-libva gtk3 lib32-gtk3 gst-plugins-base-libs lib32-gst-plugins-base-libs vulkan-icd-loader lib32-vulkan-icd-loader lutris steam gamemode --needed --noconfirm"
        os.system(Arch)
    elif found == distro[4]:    #packages for Fedora
        print("\nNow installing Fedora Gaming Packages")
        Fedora = "sudo dnf install python3-pip wine lutris gamemode goverlay steam -y"
        os.system(Fedora)
    else:
        print("Your distro was not found :(")
        exit()
           
def parse_arguments():
    #Parse commandline arguments
    parser = argparse.ArgumentParser(usage="%(prog)s", description="Install Gaming Packages with ease",
                                     epilog="GPLv3 - Repo : https://github.com/Ahmed-Al-Balochi/LibreGaming.git")
    parser.add_argument('-a', '--all', action='store_true', help='Install both ProtonGE and Gaming Packages')
    parser.add_argument('-p', '--proton', action='store_true', help='Install/Update ProtonGE')
    parser.add_argument('-g', '--gaming', action='store_true', help='Install Gaming Packages only')
    return parser.parse_args()

def main():
    args = parse_arguments()
    if args.proton:
        os.system("protonup")
    if args.gaming:
        installPkgs()
    if args.all:
        installPkgs()
        os.system("protonup")

if __name__ == "__main__":
    main()

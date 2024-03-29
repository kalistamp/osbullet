# Chrome Extensions for new OS Setup
# author = Автор: калистамп 

import webbrowser
import time
x = ' '

print(x*2)
print(' [ Kalistamp | https://github.com/kalistamp ] ')
print(x*2)
print('TABLE OF CONTENTS:')
print(x)
print('All (a): Open all the Extensions ')
print('Basics (b): Just the basic Extensions ')
print('OSINT (o): Osint Extentions ')
print('Print (p): Print out Extensions List & Guides ')
print(x*2)

extension = [
    'https://therecap.org/chrome-ex/',
        'https://chrome.google.com/webstore/detail/google-translate/aapbdbdomjkkjkaonfhkkikfgjllcleb?hl=en',
        'https://chrome.google.com/webstore/detail/trufflepiggy-context-sear/chffnhocnckigoapjdienmaphjnljpmo?hl=en',
        'https://chrome.google.com/webstore/detail/quillbot-for-chrome/iidnbdjijdkbmajdffnidomddglmieko',
        'https://chrome.google.com/webstore/detail/grammarly-grammar-checker/kbfnbcaeplbcioakkpcpgfkobkghlhen',
        'https://translate.yandex.com/',
        'https://chrome.google.com/webstore/detail/dark-reader/eimadpbcbfnmbkopoojfekhnkhdbieeh?hl=sv',
        'https://chrome.google.com/webstore/detail/photosint/gonhdjmkgfkokhkflfhkbiagbmoolhcd/related?hl=nl',
        'https://chrome.google.com/webstore/detail/violentmonkey/jinjaccalgkegednnccohejagnlnfdag?hl=en',
        'https://chrome.google.com/webstore/detail/onetab/chphlpgkkbolifaimnlloiipkdnihall?hl=en',
        'https://chrome.google.com/webstore/detail/url-render/flhclpkhoiajoikkabbfbinnjapaflog?hl=en',
        'https://chrome.google.com/webstore/detail/singlefile/mpiodijhokgodhhofbcjdecpffjipkle?hl=en',
        'https://chrome.google.com/webstore/detail/youtube-booster/dajnidicmkknmmbapmmmlemjdfolgjnf/related',
        'https://chrome.google.com/webstore/detail/youtube-actual-top-commen/hbdmelobmfcompinikjdaiphhonbgfpn/related',
        'https://chrome.google.com/webstore/detail/quick-source-viewer/cfmcghennfbpmhemnnfjhkdmnbidpanb?hl=en-US',
        'https://chrome.google.com/webstore/detail/umatrix/ogfcmafjalglgifnmanfmnieipoejdcf/related',
        'https://chrome.google.com/webstore/detail/ublacklist/pncfbmialoiaghdehhbnbhkkgmjanfhe?hl=en',
        'https://chrome.google.com/webstore/detail/stethoscope/gdkkpjagibimlpgmcbaajccgahfbojec',
        'https://chrome.google.com/webstore/detail/momentum/laookkfknpbbblfpciffpaejjkokdgca?hl=en',
        'https://chrome.google.com/webstore/detail/github-repository-size/apnjnioapinblneaedefcnopcjepgkci'
]

basic = [
    
    'https://chrome.google.com/webstore/detail/google-translate/aapbdbdomjkkjkaonfhkkikfgjllcleb?hl=en',
    'https://chrome.google.com/webstore/detail/trufflepiggy-context-sear/chffnhocnckigoapjdienmaphjnljpmo?hl=en',
    'https://translate.yandex.com/',
    'https://chrome.google.com/webstore/detail/onetab/chphlpgkkbolifaimnlloiipkdnihall?hl=en',
    'https://chrome.google.com/webstore/detail/singlefile/mpiodijhokgodhhofbcjdecpffjipkle?hl=en',
    'https://chrome.google.com/webstore/detail/quick-source-viewer/cfmcghennfbpmhemnnfjhkdmnbidpanbhl=en-US',
    'https://chrome.google.com/webstore/detail/violentmonkey/jinjaccalgkegednnccohejagnlnfdag?hl=en',
    'https://chrome.google.com/webstore/detail/momentum/laookkfknpbbblfpciffpaejjkokdgca?hl=en',
    'https://chrome.google.com/webstore/detail/github-repository-size/apnjnioapinblneaedefcnopcjepgkci'
]

OSINT = [

'https://chrome.google.com/webstore/detail/vortimo-osint-tool/mnakbpdnkedaegeiaoakkjafhoidklnf',
'https://chrome.google.com/webstore/detail/gotanda/jbmdcdfnnpenkgliplbglfpninigbiml',
'https://chrome.google.com/webstore/detail/fast-advanced-google-sear/idijdjdcncjcgmeiipcnkpjedhgepalk',
'https://chrome.google.com/webstore/detail/treeverse/aahmjdadniahaicebomlagekkcnlcila?hl=en',
'https://chrome.google.com/webstore/detail/exif-viewer-pro/mmbhfeiddhndihdjeganjggkmjapkffm',
'https://chrome.google.com/webstore/detail/fake-news-debunker-by-inv/mhccpoafgdgbhnjfhkcmgknndkeenfhe?hl=en',
'https://chrome.google.com/webstore/detail/tineye-reverse-image-sear/haebnnbpedcbhciplfhjjkbafijpncjl',
'https://chrome.google.com/webstore/detail/search-by-image/cnojnbdhbhnkbcieeekonklommdnndci',
'https://chrome.google.com/webstore/detail/distill-web-monitor/inlikjemeeknofckkjolnjbpehgadgge?hl=en-US',
'https://chrome.google.com/webstore/detail/take-webpage-screenshots/mcbpblocgmgfnpjjppndjkmgjaogfceg?hl=en-US',
'https://chrome.google.com/webstore/detail/nimbus-screenshot-screen/bpconcjcammlapcogcnnelfmaeghhagj',
'https://chrome.google.com/webstore/detail/go-back-in-time/hgdahcpipmgehmaaankiglanlgljlakj',
'https://chrome.google.com/webstore/detail/wayback-machine/fpnmgdkabkmnadcjpehmlllkndpkmiak',
'https://chrome.google.com/webstore/detail/instant-data-scraper/ofaokhiedipichpaobibbnahnkdoiiah',
'https://chrome.google.com/webstore/detail/email-extract/ejecpjcajdpbjbmlcojcohgenjngflac',
'https://chrome.google.com/webstore/detail/hunter-email-finder-exten/hgmhmanijnjhaffoampdlllchpolkdnj',
'https://chrome.google.com/webstore/detail/osiris-osint-reputation-i/jjdjccppehnjdennppcnlnaadcdlffdf',
'https://chrome.google.com/webstore/detail/sputnik/manapjdamopgbpimgojkccikaabhmocd',
'https://github.com/mitchmoser/sputnik'

]

sources = [
    '- - - SOURCES:',
    'https://github.com/kalistamp',
    'https://www.google.com/chrome/',
    'https://www.torproject.org/download/',
    'https://mullvad.net/en/download',
    'https://www.qbittorrent.org/download.php',
    'https://www.win-rar.com/download.html?&L=0',
    'https://desktop.telegram.org/',
    'https://libgen.onl/library-genesis/',
    'https://twitter.com/1800otrack',
    'https://wallpaperbat.com/img/430531-usa-lake-mountains-stones-scenery-lake-tahoe-nevada-nature-407420.jpg'
]

methods = """

                        Disable Windows Auto Update:

Fire up the Run command (Win + R). Type in “services.msc” and hit Enter.

Select the Windows Update service from the Services list
(Right above Windows Update Service Media...)

Click on the “General” tab and change the “Startup Type” to “Disabled”

[Restart Machine]

                        Browser Uninstall Guides:

Microsoft edge windows 10 (Settings | Apps | Edge Version) -

cd %PROGRAMFILES(X86)%\Microsoft\Edge\Application\<EDGE_Version_#>\Installer 

setup.exe --uninstall --system-level --verbose-logging --force-uninstall

                        KAZAM - Linux Screen Recorder:
                        
sudo apt update

sudo apt install kazam

sudo apt install python3-cairo python3-xlib

Exit and run - kazam

Drop Filesize: Files -> Preferences - Screencast | Record with: VP8(Webm) or MP4

                        FISH - Command Line Shell (https://fishshell.com/):

                        [Enter command "fish" to activate Command Shell]

Step 1: Install fish repository in ubuntu - 

sudo apt-add-repository ppa:fish-shell/release-3 

Step 2: Update and upgrade repository - 

sudo apt-get update && sudo apt-get upgrade

Step 3: Install fish shell - 

sudo apt-get install fish

Step 4: Make fish shell as default shell - 

sudo chsh -s /usr/local/bin/fish

[ Restart Machine and test new Command Line shell]

                        OHMYZSHELL (2 Methods):

apt install zsh

apt install git

curl -

sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

wget -

sh -c "$(wget https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"

                        YOUTUBE-DL (Linux):

sudo wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl

sudo chmod a+rx /usr/local/bin/youtube-dl

sudo pip install --upgrade youtube_dl

"""


vscode = """

                        VS_CODE Download / Extensions :


https://code.visualstudio.com/download

cd Downloads
sudo apt install ./<code_amd64.deb> 

cobalt2 theme
codestackr theme
fluent icons
tabnine
vscode-icons
python


[+] Unzip and Download a Deb File:

sudo apt install </.deb> 

"""

KITCHEN_TABLE = extension + OSINT 

def Chrome():
    choice = input(f'What Section of would you like to open? \n [Enter the Letter]: ')
    print(x*2)
    if choice == 'a':
        for url in KITCHEN_TABLE:
            time.sleep(3)
            webbrowser.open_new_tab(url)
    elif choice == 'b':
        for url in basic:
            time.sleep(3)
            webbrowser.open_new_tab(url)
    elif choice == 'o':
        for url in OSINT:
            time.sleep(3)
            webbrowser.open_new_tab(url)
    elif choice == 'p':
        for number, links in enumerate(sources):
            print(number, links)
        print(x*2)
        for number, links in enumerate(KITCHEN_TABLE):
            print(number, links)
        print(x*2)       
        print(methods)
        print(vscode)
    else:
        print(' [!] It seems you made a typo, that option does not exist')

Chrome()

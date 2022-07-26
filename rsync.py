import subprocess

home = subprocess.run("whoami",stdout=subprocess.PIPE).stdout.decode("utf-8").strip().replace("\n","")
print(home)

with open("./sync","w") as f:
    f.write("#!/usr/bin/bash\n")

paths = {
    "config":[
        f"/home/{home}/.config/bspwm/",
        f"/home/{home}/.config/cava/",
        f"/home/{home}/.config/dunst/",
        f"/home/{home}/.config/eww/",
        f"/home/{home}/.config/jgmenu/",
        f"/home/{home}/.config/polybar/",
        f"/home/{home}/.config/sxhkd/",
        f"/home/{home}/.config/zathura/",
        f"/home/{home}/.config/fish/",
        f"/home/{home}/.config/gtk-3.0/",
        f"/home/{home}/.config/gtk-4.0/",
        f"/home/{home}/.config/neofetch/",
        f"/home/{home}/.config/rofi/",
        f"/home/{home}/.config/picom.conf",
    ],
    "usr":[
        "/usr/bin/color-picker"
    ],
    "fonts":{
        "dest":"/usr/share/fonts/",
        "from":f"/home/{home}/Documents/fonts/"
    }
}
def rsync(path:str,dest:str):
    if path[-1]=="/":
        cmd = ["rsync","-a","-r",path,dest]
    else:
        cmd = ["rsync","-a",path,dest]
    with open("./sync","a") as f:
        f.write(" ".join(cmd)+"\n")

def sync_here():
    for path in paths["config"]:
        rsync(path,(f"config/"+path.split('/')[-2]) if path[-1] == "/" else "config/")
    for path in paths["usr"]:
        rsync(path,(f"usr/"+path.split('/')[-2]) if path[-1] == "/" else "usr/")
    rsync(paths["fonts"]["from"],"./fonts")
    subprocess.run("./sync")

sync_here()





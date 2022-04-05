pkgname = "xwayland"
pkgver = "22.1.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dipv6=true", "-Dxcsecurity=true", "-Ddri3=true", "-Dglamor=true",
    "-Dxvfb=false", "-Dxdmcp=false", "-Dxwayland_eglstream=false",
    "-Dxkb_dir=/usr/share/X11/xkb", "-Dxkb_output_dir=/var/lib/xkb",
]
hostmakedepends = ["meson", "pkgconf", "wayland-progs"]
makedepends = [
    "libxfont2-devel", "libxkbfile-devel", "libxshmfence-devel",
    "libxcb-devel", "libxcvt-devel", "wayland-devel", "wayland-protocols",
    "libtirpc-devel", "mesa-devel", "libepoxy-devel", "pixman-devel",
    "nettle-devel", "dbus-devel", "font-util-devel", "xorgproto", "xtrans",
]
# check if this needs to be updated when updating
depends = ["xserver-xorg-protocol>=20180227"]
pkgdesc = "Xwayland X server"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"https://gitlab.freedesktop.org/xorg/xserver/-/archive/{pkgname}-{pkgver}/xserver-{pkgname}-{pkgver}.tar.gz"
sha256 = "42837e7b90e0d92aff4d7846f0609f8d3c0c6641bdd6add6e4e0c5c214371149"
# needs xtest repository
options = ["!check"]

def post_install(self):
    self.install_license("COPYING")
    self.rm(self.destdir / "usr/share/man/man1/Xserver.1")
    # provided by xserver-xorg-protocol
    self.rm(self.destdir / "usr/lib/xorg/protocol.txt")

subarch: amd64
version_stamp: plasma-@TIMESTAMP@
target: livecd-stage1
rel_type: default
profile: default/linux/amd64/17.1/desktop/plasma
snapshot: @TIMESTAMP@
source_subpath: default/stage3-amd64-openrc-@TIMESTAMP@.tar.xz
compression_mode: pixz
portage_confdir: @REPO_DIR@/releases/portage/livegui

livecd/use:
	-aac
	compile-locales
	fbcon
	jpeg2k
	livecd
	modules
	networkmanager
	openexr
	opus
	postproc
	portaudio
	pulseaudio
	python
	theora
	vpx
	xetex

livecd/packages:
	app-accessibility/brltty
	app-accessibility/espeakup
	app-admin/hddtemp
	app-admin/sudo
	app-admin/syslog-ng
	app-admin/sysstat
	app-admin/testdisk
	app-arch/bzip2
	app-arch/cpio
	app-arch/dpkg
	app-arch/deb2targz
	app-arch/gzip
	app-arch/mt-st
	app-arch/p7zip
	app-arch/pbzip2
	app-arch/rpm
	app-arch/tar
	app-arch/zip
	app-arch/unrar
	app-backup/fsarchiver
	app-benchmarks/bonnie
	app-benchmarks/bonnie++
	app-benchmarks/dbench
	app-benchmarks/iozone
	app-benchmarks/stress
	app-benchmarks/tiobench
	app-cdr/dvd+rw-tools
	app-cdr/cdrtools
	app-crypt/chntpw
	app-crypt/gnupg
	app-crypt/pinentry
	app-editors/emacs
	app-editors/ghex
	app-editors/hexedit
	app-editors/joe
	app-editors/kile
	app-editors/mg
	app-editors/nano
	app-editors/vim
	app-emacs/ebuild-mode
	app-emulation/cloud-init
	app-emulation/xen-tools
	app-eselect/eselect-repository
	app-misc/colordiff
	app-misc/livecd-tools
	app-misc/mc
	app-misc/pax-utils
	app-misc/screen
	app-misc/tmux
	app-misc/wipe
	app-office/libreoffice
	app-office/lyx
	app-office/texstudio
	app-officeext/texmaths
	app-portage/eix
	app-portage/genlop
	app-portage/gentoolkit
	app-portage/mirrorselect
	app-portage/portage-utils
	app-portage/pram
	app-portage/repoman
	app-portage/ufed
	app-shells/bash-completion
	app-shells/gentoo-bashcomp
	app-text/bibutils
	app-text/dos2unix
	app-text/ghostscript-gpl
	app-text/pdftk
	app-text/recode
	app-text/texlive
	app-text/tree
	app-text/wgetpaste
	app-text/xournalpp
	app-vim/gentoo-syntax
	dev-lang/perl
	dev-lang/python
	dev-util/kdevelop
	dev-util/kdevelop-python
	dev-vcs/git
	dev-vcs/kdesvn
	dev-vcs/subversion
	kde-apps/k3b
	kde-apps/kde-apps-meta
	kde-apps/kdenlive
	kde-apps/kipi-plugins
	kde-apps/kompare
	kde-misc/kdiff3
	kde-plasma/plasma-meta
	media-gfx/digikam
	media-gfx/engauge
	media-gfx/fbgrab
	media-gfx/gimp
	media-gfx/graphviz
	media-gfx/hugin
	media-gfx/inkscape
	media-gfx/jhead
	media-gfx/pngcrush
	media-gfx/pngquant
	media-gfx/povray
	media-sound/alsa-utils
	media-video/mpv
	net-analyzer/iptraf-ng
	net-analyzer/nmap
	net-analyzer/openbsd-netcat
	net-analyzer/tcpdump
	net-analyzer/tcptraceroute
	net-analyzer/traceroute
	net-analyzer/traceroute-nanog
	net-dialup/minicom
	net-dialup/mingetty
	net-dialup/pptpclient
	net-dialup/rp-pppoe
	net-dns/bind-tools
	net-fs/cifs-utils
	net-fs/nfs-utils
	net-ftp/ftp
	net-ftp/ncftp
	net-irc/irssi
	net-irc/weechat
	net-misc/chrony
	net-misc/dhcpcd
	net-misc/iputils
	net-misc/ndisc6
	net-misc/ntp
	net-misc/openssh
	net-misc/rdate
	net-misc/rdesktop
	net-misc/rsync
	net-misc/telnet-bsd
	net-misc/vconfig
	net-misc/wget
	net-misc/whois
	net-proxy/dante
	net-proxy/tsocks
	net-vpn/networkmanager-openvpn
	net-vpn/networkmanager-pptp
	net-vpn/openfortivpn
	net-vpn/openvpn
	net-wireless/b43-fwcutter
	net-wireless/iw
	net-wireless/wireless-tools
	net-wireless/wpa_supplicant
	sys-apps/arrayprobe
	sys-apps/acl
	sys-apps/attr
	sys-apps/busybox
	sys-apps/cciss_vol_status
	sys-apps/chname
	sys-apps/coreutils
	sys-apps/dcfldd
	sys-apps/diffutils
	sys-apps/dmidecode
	sys-apps/dstat
	sys-apps/ethtool
	sys-apps/file
	sys-apps/findutils
	sys-apps/flashrom
	sys-apps/fxload
	sys-apps/gawk
	sys-apps/gptfdisk
	sys-apps/hdparm
	sys-apps/hwinfo
	sys-apps/ipmitool
	sys-apps/iproute2
	sys-apps/inxi
	sys-apps/less
	sys-apps/man-db
	sys-apps/man-pages
	sys-apps/man-pages-posix
	sys-apps/memtester
	sys-apps/mlocate
	sys-apps/netplug
	sys-apps/nvme-cli
	sys-apps/pciutils
	sys-apps/pcmciautils
	sys-apps/sdparm
	sys-apps/sed
	sys-apps/setserial
	sys-apps/sg3_utils
	sys-apps/smartmontools
	sys-apps/which
	sys-apps/usbutils
	sys-apps/util-linux
	sys-block/aoetools
	sys-block/fio
	sys-block/gparted
	sys-block/mtx
	sys-block/open-iscsi
	sys-block/parted
	sys-block/partimage
	sys-block/tw_cli
	sys-block/whdd
	sys-boot/grub
	sys-firmware/ipw2100-firmware
	sys-firmware/ipw2200-firmware
	sys-fs/bcache-tools
	sys-fs/btrfs-progs
	sys-fs/cryptsetup
	sys-fs/ddrescue
	sys-fs/dmraid
	sys-fs/dosfstools
	sys-fs/e2fsprogs
	sys-fs/exfat-utils
	sys-fs/extundelete
	sys-fs/fuse-exfat
	sys-fs/f2fs-tools
	sys-fs/growpart
	sys-fs/jfsutils
	sys-fs/lsscsi
	sys-fs/lvm2
	sys-fs/mac-fdisk
	sys-fs/mdadm
	sys-fs/multipath-tools
	sys-fs/ntfs3g
	sys-fs/reiserfsprogs
	sys-fs/xfsprogs
	sys-kernel/linux-firmware
	sys-libs/gpm
	sys-power/acpid
	sys-process/htop
	sys-process/lsof
	sys-process/iotop
	sys-process/procps
	sys-process/psmisc
	www-client/chromium
	www-client/firefox
	www-client/links
	x11-misc/sddm

